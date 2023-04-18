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
			<div class="title">Add Appliance</div>
			<div class="subtitle">User:
				<?php echo $_GET['email']; ?>
				<br>
			</div>
			<div class="subtitle">Please provide the details for the appliance.</div>
			<br><br>
			<form method="POST" action="process_appliance.php">

				<input type="email" id="email" name="email" value="<?php echo $_GET['email']; ?>" style="display: none;">

				<!-- Appliance Type -->
				<label for="appliance_type">Appliance Type:</label>
				<select id="appliance_type" name="appliance_type" onchange="showApplianceTypeForm()">
					<option value="">Select Appliance Type</option>
					<option value="Air Handler">Air Handler</option>
					<option value="Water Heater">Water Heater</option>
				</select><br><br>
				<!-- Manufacturer -->
				<label for="manufacturer">Manufacturer:</label>
				<input type="text" id="manufacturer" name="manufacturer" required><br><br>
				<!-- Model Name -->
				<label for="model_name">Model Name:</label>
				<input type="text" id="model_name" name="model_name"><br><br>
				<!-- BTU Rating -->
				<label for="btu_rating">BTU Rating:</label>
				<input type="number" id="btu_rating" name="btu_rating" min="0" step="0.1" required><br>
				<br><br>


				<!-- AIR HANDLER -->
				<div id="air_handler_form" style="display:none;">

					<label for="heating_method">Heating Method:</label>
					<input type="checkbox" id="heater_method" name="heater_method" value="Heater"> Heater
					<input type="checkbox" id="air_conditioner_method" name="air_conditioner_method" value="Air Conditioner"> Air Conditioner
					<input type="checkbox" id="heatpump_method" name="heatpump_method" value="Heat Pump"> Heat Pump
					<br><br>

					<div id="energy_source_entry" style="display:none;">
						<label for="energy_source">Energy Source:</label>
						<select id="energy_source" name="energy_source">
							<option value="electric">Electricity</option>
							<option value="gas">Natural Gas</option>
							<option value="thermosolar">Propane</option>
							<option value="heat pump">Oil</option>
						</select><br><br>
					</div>

					<div id="eer_entry" style="display:none;">
						<label for="eer">Energy Efficiency Ratio:</label>
						<input type="number" id="eer" name="eer" min="0" step="0.1"><br><br>
					</div>

					<div id="hspf_entry" style="display:none;">
						<label for="hspf">Heating Seasonal Performance Factor:</label>
						<input type="number" id="hspf" name="hspf" min="0" step="0.1"><br><br>
					</div>

					<div id="seer_entry" style="display:none;">
						<label for="seer">Seasonal Efficiency Ratio:</label>
						<input type="number" id="seer" name="seer" min="0" step="0.1"><br><br>
					</div>

				</div>

				<!-- WATER HEATER -->
				<div id="water_heater_form" style="display:none;">

					<label for="energy_source">Energy Source:</label>
					<select id="energy_source" name="energy_source">
						<option value="">Choose an Option</option>
						<option value="electric">Electricity</option>
						<option value="gas">Natural Gas</option>
						<option value="thermosolar">Propane</option>
						<option value="heat-pump">Oil</option>
					</select><br><br>

					<label for="capacity">Capacity (in gallons):</label>
					<input type="number" id="capacity" name="capacity" min="0" step="0.1"><br><br>

					<label for="temperature">Temperature:</label>
					<input type="number" id="temperature" name="temperature" min="0" step="0.1"><br><br>

				</div>
				<br>
				<input type="submit" value="Next" class="button">
				<br>
			</form>

			<!-- Script file for showing either of the Appliance Type -->
			<script src="js/appliance_info.js"></script>
		</div>
	</div>
</body>

</html>

<!-- The content of the footer.php page goes here -->
<?php include("lib/footer.php"); ?>