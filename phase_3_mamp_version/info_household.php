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
			<div class="title">Enter household info</div>

			<!-- FORM 01 - Household Info -->
			<!-- process_household.php file handles the validation stuff -->
			<form action="process_household.php" method="POST">
				<!-- Email -->
				<label for="email">Please enter your email address:</label><br>
				<input type="email" name="email" required><br><br>
				<!-- Postal code -->
				<label for="postal_code">Please enter your five digit postal code:</label>
				<input type="text" name="postal_code" required pattern="[0-9]{3,5}"><br><br>

				<p>Please enter following details for your household:</p>
				<!-- Houshold Types -->
				<label for="household_types">Household Types:</label>
				<select name="household_types" required>
					<option value="">--Please choose an option--</option>
					<option value="House">House</option>
					<option value="Apartment">Apartment</option>
					<option value="Townhome">Townhome</option>
					<option value="Condominium">Condominium</option>
					<option value="Mobile-Home">Mobile Home</option>
				</select><br><br>
				<!-- Square Footage -->
				<label for="square_footage">Square Footage:</label>
				<input type="number" name="square_footage" required min="500" max="10000"><br><br>
				<!-- Thermostat - Heat -->
				<label for="heating_thermostat">Heating Thermostat:</label>
				<input type="number" id="heating_temp" name="heating_temp" required min="-999" max="999">
				<input type="checkbox" id="heating_checkbox" name="heating_thermostat" value="yes" onchange="handleHeatingCheckbox()">No Heat<br><br>
				<!-- Thermostat - Cool -->
				<label for="cooling_thermostat">Cooling Thermostat:</label>
				<input type="number" id="cooling_temp" name="cooling_temp" required min="-999" max="999">
				<input type="checkbox" id="cooling_checkbox" name="cooling_thermostat" value="yes" onchange="handleCoolingCheckbox()">No Cool<br><br>
				<div class="thin_box">
					<!-- Public Utility -->
					<label for="public_utility">Public Utility: (if none, leave unchecked)</label><br>
					<input type="checkbox" id="electric" name="public_utility[]" value="Electric">
					<label for="electric">Electric</label><br>
					<input type="checkbox" id="gas" name="public_utility[]" value="Gas">
					<label for="gas">Gas</label><br>
					<input type="checkbox" id="steam" name="public_utility[]" value="Steam">
					<label for="steam">Steam</label><br>
					<input type="checkbox" id="fuel_oil" name="public_utility[]" value="Fuel Oil">
					<label for="fuel_oil">Fuel Oil</label>
				</div>
				<br>
				<br>
				<input type="submit" value="Next" class="button">
				<!-- Script file for heating and cooling input disabling if checkbox is clicked -->
				<script src="js/household_info.js"></script>
			</form>
			<br><br>
		</div>
	</div>
</body>

</html>

<!-- The content of the footer.php page goes here -->
<?php include("lib/footer.php"); ?>