<!-- This connects the database and result -->
<?php
include('lib/common.php');
include('lib/show_queries.php');
?>

<!-- The content of the header.php page goes here -->
<?php include("lib/header.php"); ?>

<!-- The content of the body code goes here -->
<!DOCTYPE html>
<html lang="en">
<html>

<head>
	<title>Alternakraft</title>
</head>

<body>
	<div id="main_container">
		<div class="center_content">
			<div class="center_left">
				<div class="features">
					<div class="profile_section">
						<div class="title">List Appliance</div>
						<div class="subtitle">You have following appliances to your household</div>
						<table>
							<tr>
								<th class="heading">Appliance Number</th>
								<th class="heading">Type</th>
								<th class="heading">Manufacturer</th>
								<th class="heading">Model</th>
								<th class="heading"> </th>
							</tr>
							<br><br>

							<?php
							// fetch the name from page
							$email = $_GET['email'];


							// SQL query
							$query = "SELECT appliance_number,appliance_type, manufacturer_name, model_name
									FROM Appliance 
									WHERE Appliance.email = '{$email}' ";

							// Error Check
							$result = mysqli_query($db, $query);
							if (!empty($result) && (mysqli_num_rows($result) == 0)) {
							}

							// Display
							while ($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
								print "<tr>";
								print "<td>{$row['appliance_number']}</td>";
								print "<td>" . ($row['appliance_type'] == 'air_handler' ? "Water Heater" : "Air Handler") . "</td>";
								print "<td>{$row['manufacturer_name']}</td>";
								print "<td>{$row['model_name']}</td>";
								print "<td><form method='POST'><button type='submit' name='delete' value='{$row['appliance_number']}'>Delete</button></form></td>";
								print "</tr>";
							}


							// Handle delete request
							if (isset($_POST['delete'])) {
								$appliance_number = mysqli_real_escape_string($db, $_POST['delete']);
								$email = $_GET['email'];

								//  Heater table
								$query = "DELETE FROM Heater WHERE email = ? AND appliance_number = ?";
								$stmt = mysqli_prepare($db, $query);
								mysqli_stmt_bind_param($stmt, 'si', $email, $appliance_number);
								mysqli_stmt_execute($stmt);

								// // Water Heater table
								$query = "DELETE FROM WaterHeater WHERE email = ? AND appliance_number = ?";
								$stmt = mysqli_prepare($db, $query);
								mysqli_stmt_bind_param($stmt, 'si', $email, $appliance_number);
								mysqli_stmt_execute($stmt);

								//  AC table
								$query = "DELETE FROM AirConditioner WHERE email = ? AND appliance_number = ?";
								$stmt = mysqli_prepare($db, $query);
								mysqli_stmt_bind_param($stmt, 'si', $email, $appliance_number);
								mysqli_stmt_execute($stmt);

								//  Heate Pump table
								$query = "DELETE FROM HeatPump WHERE email = ? AND appliance_number = ?";
								$stmt = mysqli_prepare($db, $query);
								mysqli_stmt_bind_param($stmt, 'si', $email, $appliance_number);
								mysqli_stmt_execute($stmt);

								// Finally, delete the Appliance
								$query = "DELETE FROM Appliance WHERE email = ? AND appliance_number = ?";
								$stmt = mysqli_prepare($db, $query);
								mysqli_stmt_bind_param($stmt, 'si', $email, $appliance_number);
								mysqli_stmt_execute($stmt);

								header("Location: info_appliance_list.php?email=" . urlencode($_GET['email']));
							}

							?>
						</table>

					</div>
				</div>
			</div>

			<?php include("lib/error.php"); ?>

			<div class="clear"></div>

			<br>

			<!-- Set the email address -->
			<input type="hidden" id="email" value="<?php echo $email; ?>">

			<!-- Link 1 redirects to info_appliance_add.php with email parameter -->
			<form action="info_appliance_add.php" method="get">
				<input type="hidden" name="email" value="" id="email-input">
				<a href="#" onclick="document.getElementById('email-input').value = document.getElementById('email').value; this.parentNode.submit();"> + Add another appliance</a>
			</form>
			<br>
			<!-- Set the email input value to the email address -->
			<script>
				document.getElementById("email-input").value = document.getElementById("email").value;
			</script>

			<?php
			// Check if the button has been clicked before displaying it
			if (!isset($_POST['power_gen_initial'])) {
				echo '<form method="POST">';
				echo '<button type="submit" name="power_gen_initial" class="button">Next</button>';
				echo '</form>';
			} else {
				header("Location: info_power_generation_initial.php?email=" . urlencode($_GET['email']));
			}
			?>


		</div>



	</div>
	<br>

</body>

</html>

<!-- The content of the footer.php page goes here -->
<?php include("lib/footer.php"); ?>