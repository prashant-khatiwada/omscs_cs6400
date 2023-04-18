<?php
// Open up the database
include('lib/common.php');
include('lib/show_queries.php');

if ($_SERVER["REQUEST_METHOD"] == "POST") {

  // 01 - Email -  Sanitize and validate form data
  $email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);
  if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    die("Invalid email address format");
  } 

  // Check if the email already exists in the database
$stmt = mysqli_prepare($db, "SELECT email FROM HouseHold WHERE email = ?");
mysqli_stmt_bind_param($stmt, "s", $email);
mysqli_stmt_execute($stmt);
mysqli_stmt_bind_result($stmt, $result);
mysqli_stmt_fetch($stmt);


if ($result == $email) {
  echo "Error: Email Already in Database";
} else {

  // 02 Postal Code - Sanitize and validate form data
  // Get the postal code from the form input
  $postal_code = filter_var($_POST['postal_code'], FILTER_SANITIZE_STRING);
  // Check if the postal code is valid (5 digits for US system)
  if (preg_match("/^\d{5}$/", $postal_code)) {
    // Postal code is valid, continue processing the form from in the database
    $query = "SELECT * FROM Address WHERE postal_code='$postal_code'";
    $result = mysqli_query($db, $query);
    if ($result->num_rows == 0) {
      // No matching records found in the database
      //echo "Error: Postal code not found in database.";
      echo "<script>alert('Error: Postal code not found in database.');</script>";
    } else {
      // Matching records found in the database
      echo "Postal code validated successfully.";
  }

  } else {
    // Postal code is invalid, display an error message
    echo "Error: Invalid Postal code. Please enter a valid 5-digit postal code.";
  }

  // 03 Household Types - Sanitize and validate form data
  $household_types = $_POST['household_types'];

  // 04 Square footage - Sanitize and validate form data
  $square_footage = filter_var($_POST['square_footage'], FILTER_SANITIZE_NUMBER_INT);

  // 05 Public Utility - Sanitize and validate form data
  $public_utility = '';
  if (isset($_POST['public_utility'])) {
    $public_utility = implode(',', $_POST['public_utility']);
  } else {
    $public_utility = 'Off-The-Grid';
  }


  /////////////////////////
  // Prepartion for INSERT
  // Table Household
  $query = "INSERT INTO HouseHold (email, square_footage, household_types, postal_code)  
          VALUES ('$email', '$square_footage', '$household_types', '$postal_code')";
  $queryID = mysqli_query($db, $query);

  if ($queryID == False) { //INSERT, UPDATE, DELETE, DROP return True on Success  / False on Error
    array_push($error_msg, "INSERT ERROR: Household: " . $email . " " . $square_footage . " (" . $household_types . ") error in processing <br>" . __FILE__ . " line:" . __LINE__);
  }

  // Table Temperature - Cooling
  if (isset($_POST['cooling_thermostat'])) {
    // Checkbox is checked, insert NULL
    $query = "INSERT INTO Cooling (email, temperature) VALUES ('$email', NULL)";
    $queryID = mysqli_query($db, $query);
    if ($queryID == False) {
      array_push($error_msg, "INSERT ERROR: Temperature: " . $email . " " . $cooling_value . " <br>" . __FILE__ . " line:" . __LINE__);
      echo "Error: Cooling Temp = NULL, Not able to process in Database <br>";
    }
  } else {
    // Checkbox is not checked, insert the integer value
    $cooling_value = $_POST['cooling_temp'];
    $query = "INSERT INTO Cooling (email, temperature) VALUES ('$email', '$cooling_value')";
    $queryID = mysqli_query($db, $query);
    if ($queryID == False) {
      array_push($error_msg, "INSERT ERROR: Temperature: " . $email . " " . $cooling_value . " <br>" . __FILE__ . " line:" . __LINE__);
      echo "Error: Cooling Temp - Integer, Not able to process in Database<br>";
      echo $error_msg;
    }
  }


  // Table Temperature - Heating
  if (isset($_POST['heating_thermostat'])) {
    // Checkbox is checked, insert NULL
    // $heating_value = NULL;
    $query = "INSERT INTO Heating (email, temperature) VALUES ('$email', NULL)";
    $queryID = mysqli_query($db, $query);
    if ($queryID == False) {
      echo "Error: Heating = NULL, Not able to process in Database<br>";
    }
  } else {
    // Checkbox is not checked, insert the integer value
    $heating_value = $_POST['heating_temp'];
    $query = "INSERT INTO Heating (email, temperature) VALUES ('$email', '$heating_value')";
    $queryID = mysqli_query($db, $query);
    if ($queryID == False) {
      echo "Error: Heating Temp - Integer - Not able to process in Database<br>";
    }
  }

  // Table Public Utility
  $query = "INSERT INTO PublicUtility (email, public_utility)  
          VALUES ('$email', '$public_utility')";
  $queryID = mysqli_query($db, $query);
  if ($queryID == False) {
    array_push($error_msg, "INSERT ERROR: PublicUtility: " . $email . " " . $public_utility . " error in processing <br>" . __FILE__ . " line:" . __LINE__);
  }


  // Check if the insertion was successful
  if ($queryID) {
    // Redirect the user to the next page
    header("Location: info_appliance_initial.php?email=" . urlencode($email));
    exit();
  } else {
    // Display an error message
    echo "Error: Failed to insert into the database.";
  }

}

}

?>