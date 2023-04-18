<?php
// Open up the database
include('lib/common.php');
include('lib/show_queries.php');

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  
  // Sanitize and validate form data
  $email = $_POST['email'];
  $appliance_type = null;
  if ($_POST['appliance_type'] == 'Air Handler') {
    $appliance_type = 'air_handler';
  } else if ($_POST['appliance_type'] == 'Water Heater') {
    $appliance_type = 'water_heater';
  }
  $manufacturer_name = $_POST['manufacturer'];
  $model_name = $_POST['model_name'] ?? '';
  $btu_rating = $_POST['btu_rating'];
  $energy_source = $_POST['energy_source'];
  $eer = $_POST['eer'];
  $seer = $_POST['seer'];
  $hspf = $_POST['hspf'];
  $capacity_in_gallons = $_POST['capacity'];
  $temperature = $_POST['temperature'];


// INSERT FOR APPLIANCE
// Prepare the query to insert into Appliance table
$query = "INSERT INTO Appliance (email, appliance_number, appliance_type, btu_rating,  model_name, manufacturer_name) 
SELECT ?, COALESCE(MAX(A.appliance_number), 0) + 1, ?, ?, ?, ? FROM Appliance A WHERE A.email = ?";
$stmt = mysqli_prepare($db, $query);
// Bind parameters to the prepared statement
mysqli_stmt_bind_param($stmt, "ssssss", $email, $appliance_type, $btu_rating, $model_name, $manufacturer_name, $email);
// Execute the prepared statement
mysqli_stmt_execute($stmt);

// Check for errors
if(mysqli_stmt_error($stmt)) {
  echo "Error: " . mysqli_stmt_error($stmt);
  exit();
}

 // Get the last inserted ID
 $appliance_number = mysqli_insert_id($db);

// PREPARE FOR OTHER TABLES 
  // Prepare AIR HANDLERS
  if ($_POST['appliance_type'] == 'Air Handler') {

      // Check 
      if (!isset($_POST['heater_method']) && !isset($_POST['air_conditioner_method']) && !isset($_POST['heatpump_method'])) {
        //echo "Error: Please select at least one of the air handler options.";
        echo "<script>alert('Error: Please select at least one of the air handler options.');</script>";
        exit();
      }

     // Heater table
     if (isset($_POST['heater_method'])) {
      // prepare query
      $query = "INSERT INTO Heater (email, appliance_number, energy_source)
      SELECT ?, COALESCE(MAX(W.appliance_number), 0) + 1, ? FROM Heater W WHERE W.email = ?";
      // prepare statement
      $stmt = mysqli_prepare($db, $query);
      // bind statement
      mysqli_stmt_bind_param($stmt, "sss", $email, $energy_source,  $email);
      // execure bind
      mysqli_stmt_execute($stmt);

      // Check for errors
      if(mysqli_stmt_error($stmt)) {
        echo "Error: " . mysqli_stmt_error($stmt);
        exit();
      }
      }

      // Insert into AirConditioner table
      if (isset($_POST['air_conditioner_method'])) {
      // // prepare query
      $query = "INSERT INTO AirConditioner (email, appliance_number, eer)
      SELECT ?, COALESCE(MAX(W.appliance_number), 0) + 1, ? FROM AirConditioner W WHERE W.email = ?";
      // prepare statement
      $stmt = mysqli_prepare($db, $query);
      // bind statement
      mysqli_stmt_bind_param($stmt, "sis", $email, $eer, $email);
      // execure bind
      mysqli_stmt_execute($stmt);

      // Check for errors
      if(mysqli_stmt_error($stmt)) {
        echo "Error: " . mysqli_stmt_error($stmt);
        exit();
      }
      }

       // HeatPump table
    if (isset($_POST['heatpump_method'])) {
      // INSERT
      $query = "INSERT INTO HeatPump (email, appliance_number, seer, hspf)
      SELECT ?, COALESCE(MAX(W.appliance_number), 0) + 1, ?, ? FROM HeatPump W WHERE W.email = ?";
      // bind and execute parameters
      mysqli_stmt_bind_param($stmt, "ssss", $email, $seer, $hspf, $email);
      // execure bind
      mysqli_stmt_execute($stmt);   

      // Check for errors
      if(mysqli_stmt_error($stmt)) {
        echo "Error: " . mysqli_stmt_error($stmt);
        exit();
      }
     }

  } else if ($_POST['appliance_type'] == 'Water Heater') {

    // Check
    if (!isset($_POST['energy_source']) || !isset($_POST['temperature']) || !isset($_POST['capacity'])) {
      echo "Error: Please select all the options.";
      // Display an error message in an alert dialog box
      exit();
    }

     // Prepare the query to insert into Appliance table
    $query = "INSERT INTO WaterHeater (email, appliance_number, energy_source, temperature, capacity)
    SELECT ?, COALESCE(MAX(W.appliance_number), 0) + 1, ?, ?, ? FROM WaterHeater W WHERE W.email = ?";
     // prepare statement
     $stmt = mysqli_prepare($db, $query);
     // bind statement
    mysqli_stmt_bind_param($stmt, 'sssss', $email, $energy_source, $temperature, $capacity_in_gallons, $email);
    // execure bind
    mysqli_stmt_execute($stmt);

    // Check for errors
    if(mysqli_stmt_error($stmt)) {
      echo "Error: " . mysqli_stmt_error($stmt);
      exit();
    }

  }


   ////////////////////////
  // check for errors
    if(mysqli_stmt_error($stmt)) {
        echo "Error: " . mysqli_stmt_error($stmt);
      } else {
      // Redirect the user to the next page
      header("Location: info_appliance_list.php?email=" . urlencode($email));
      exit();
    }   

}

?>