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
						<div class="title">Power Generation</div>
						<div class="subtitle">You have added these to your household</div>
						<div class="subtitle">User: <?php echo $_GET['email']; ?></div>
							<table>
								<tr>
									<th class="heading">Number</th>
									<th class="heading">Type</th>
									<th class="heading">Monthly kWh</th>
									<th class="heading">Battery kWh</th>
									<th class="heading"> </th>
								</tr>
								<br><br>

								<?php
								// fetch the name from page
								$email = $_GET['email'];

								// SQL query
								$query = "SELECT power_generation_number, generation_type, monthly_power_generated, battery_storage_capacity 
									FROM PowerGeneration WHERE PowerGeneration.email = '{$email}' ";

								// Error Check
								$result = mysqli_query($db, $query);
								if (!empty($result) && (mysqli_num_rows($result) == 0)) {
								}

								// Display
								while ($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
									print "<tr>";
									print "<td>{$row['power_generation_number']}</td>";
									print "<td>{$row['generation_type']}</td>";
									print "<td>{$row['monthly_power_generated']}</td>";
									print "<td>{$row['battery_storage_capacity']}</td>";
									print "<td><form method='POST'><button type='submit' name='delete' value='{$row['power_generation_number']}'>Delete</button></form></td>";
									print "</tr>";
								}

								// Handle delete request
								if (isset($_POST['delete'])) {

									$number = mysqli_real_escape_string($db, $_POST['delete']);
									$email = $_GET['email'];

									// DELETE
									$query = "DELETE FROM PowerGeneration WHERE email = ? AND power_generation_number = ?";
									$stmt = mysqli_prepare($db, $query);
									mysqli_stmt_bind_param($stmt, 'si', $email, $number);
									mysqli_stmt_execute($stmt);

									header("Location: info_power_generation_list.php?email=" . urlencode($_GET['email']));
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

				<!-- Button 1 redirects to info_appliance_add.php with email parameter -->
				<form action="info_power_generation_add.php" method="get">
					<input type="hidden" name="email" value="" id="email-input">
					<a href="#" onclick="document.getElementById('email-input').value = document.getElementById('email').value; this.parentNode.submit();"> + Add more power</a>
				</form>

				<!-- Set the email input value to the email address -->
				<script>
					document.getElementById("email-input").value = document.getElementById("email").value;
				</script>
				<br>
				<?php
				// Check if the button has been clicked before displaying it
				if (!isset($_POST['submit'])) {
					echo '<form method="POST">';
					echo '<button type="submit" name="submit"class="button">Finish</button>';
					echo '</form>';
				} else {
					header("Location: submission_complete.php");
				}
				?>
			</div>



		</div>
</body>

</html>