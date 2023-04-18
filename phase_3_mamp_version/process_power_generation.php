<?php
// Open up the database
include('lib/common.php');
include('lib/show_queries.php');

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  ////////////////////////
  // Get stuff from previous page
  $email = $_POST['email'];
  $generation_type = $_POST['energy_source'];
  $monthly_power_generated = $_POST['monthly_kwh'];
  $battery_storage_capacity = $_POST['storage_kwh'];


/////////////////////////
// Prepartion for INSERT
// Table Powergeneration
// Prepare the query to insert into Appliance table
$query = "INSERT INTO PowerGeneration (email, power_generation_number, generation_type, monthly_power_generated,  battery_storage_capacity) 
SELECT ?, COALESCE(MAX(P.power_generation_number), 0) + 1, ?, ?, ?
FROM PowerGeneration P
WHERE P.email = ?";
  // prepare statement
  $stmt = mysqli_prepare($db, $query);

 // bind the parameters
 mysqli_stmt_bind_param($stmt, "sssss", $email, $generation_type, $monthly_power_generated, $battery_storage_capacity, $email);

// execure bind
mysqli_stmt_execute($stmt);

// Check for errors
if(mysqli_stmt_error($stmt)) {
  echo "Error: " . mysqli_stmt_error($stmt);
  exit();
}

  ////////////////////////
  // check for errors
if(mysqli_stmt_error($stmt)) {
  echo "Error: " . mysqli_stmt_error($stmt);
} else {
  // Redirect the user to the next page
  header("Location: info_power_generation_list.php?email=" . urlencode($email));
  exit();
}

}
