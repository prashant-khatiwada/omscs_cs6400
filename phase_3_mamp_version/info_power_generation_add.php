<!-- The content of the header.php page goes here -->
<?php include("lib/header.php"); ?>

<!-- The content of the index.php page goes here -->
<!DOCTYPE html>
<html>

<head>
	<title>Alternakraft</title>
</head>

<body>
	<div id="main_container">
		<div class="center_content">
			<div class="title">Add Power Generation</div>
			<div class="subtitle">Please provide power generation details.</div>
			<div class="subtitle">User:
				<?php echo $_GET['email']; ?></div>
			<br>
			<form method="post" action="process_power_generation.php">
				<input type="email" id="email" name="email" value="<?php echo $_GET['email']; ?>" style="display: none;">
				<label for="energy_source">Type</label>
				<select id="energy_source" name="energy_source">
					<option value="">--Please choose an option--</option>
					<option value="solar-electric">Solar Electric</option>
					<option value="wind">Wind</option>
				</select><br><br>

				<label for="monthly_kwh">Monthly kWh</label>
				<input type="number" id="monthly_kwh" name="monthly_kwh" min="0" step="0.1" required><br><br>

				<label for="storage_kwh">Storage kWh</label>
				<input type="number" id="storage_kwh" name="storage_kwh" min="0" step="0.1"><br><br>

				<input type="submit" name="add_button" value="Add" class="button">
			</form>
			<br>
			<?php
			include('lib/common.php');
			$email = $_GET['email'];
			$query = "SELECT EXISTS ( SELECT * FROM PublicUtility WHERE email = '{$email}' AND public_utility = 'off-the-grid' ) AS is_off_the_grid";
			$result = mysqli_query($db, $query);
			$row = mysqli_fetch_assoc($result);
			$energy_status = $row['is_off_the_grid'];

			// Display the Add button if the user is not off the grid
			if ($energy_status == 1) {
				// Button
				echo '<form action="submission_complete.php" method="get">';
				echo '<input type="hidden" name="email" value="' . $email . '" id="email-input">';
				echo '<button type="submit" name="skip_button" value="Skip"class="button" >Skip</button>';
				echo '</form>';
			} else {
			}
			?>
			<br>

		</div>
	</div>
</body>

</html>

<!-- The content of the footer.php page goes here -->
<?php include("lib/footer.php"); ?>