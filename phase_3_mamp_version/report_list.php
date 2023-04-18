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
		<div class="title">View Reports</div>
			<p>Please choose what you'd like view</p>
			<ul>
				<li><a href="report_01_top_25.php">Top 25 popular manufacturers</a></li>
				<li><a href="report_02_search_mm.php">Manufacturer/model search</a></li>
				<li><a href="report_03_heating_cooling.php">Heating/cooling method details</a></li>
				<li><a href="report_04_water_heater_stats.php">Water heater statistics by state</a></li>
				<li><a href="report_05_off_grid.php">Off-the-grid household dashboard</a></li>
				<li><a href="report_06_radius.php">Household averages by radius</a></li>
			</ul>

			<br>
			<button type="button" onclick="location.href='index.php'" class="button">Back</button>
			<br><br>
		</div>
	</div>
</body>

</html>

<!-- The content of the footer.php page goes here -->
<?php include("lib/footer.php"); ?>