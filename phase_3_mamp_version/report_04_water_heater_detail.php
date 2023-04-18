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
						<div class="subtitle">Water heater statistics in
							<?php echo $_GET['state']; ?>
						</div>
						<table>
							<tr>
								<th class="heading">Energy Source</th>
								<th class="heading">Min Capacity</th>
								<th class="heading">Avg Capacity</th>
								<th class="heading">Max Capacity</th>
								<th class="heading">Min Temp</th>
								<th class="heading">Avg Temp</th>
								<th class="heading">Max Temp</th>
							</tr>

							<?php
							// fetch the name from page
							$state = $_GET['state'];

							// SQL query
							$query = "SELECT 
							Address.state AS State,
    WaterHeater.energy_source AS EnergySource,
    -- capacity
    ROUND(MIN(WaterHeater.capacity),0) AS MinCapacity,
    ROUND(AVG(WaterHeater.capacity),0) AS AvgCapacity,
    ROUND(MAX(WaterHeater.capacity),0) AS MaxCapacity,
							-- temp
    ROUND(MIN(WaterHeater.temperature),1) AS MinTemp,
    ROUND(AVG(WaterHeater.temperature), 1) AS AvgTemp,
    ROUND(MAX(WaterHeater.temperature),1) AS MaxTemp
						FROM 
						WaterHeater
    INNER JOIN Appliance ON WaterHeater.email = Appliance.email 
    INNER JOIN Household ON Household.email = WaterHeater.email
    INNER JOIN Address ON Household.postal_code = Address.postal_code
						WHERE 
							Address.state = '$state'
						GROUP BY 
							Address.state, 
							WaterHeater.energy_source 
						ORDER BY 
							WaterHeater.energy_source ASC";

							// Error Check
							$result = mysqli_query($db, $query);
							if (!empty($result) && (mysqli_num_rows($result) == 0)) {
								array_push($error_msg, "SELECT ERROR: find Manufacturer <br>" . __FILE__ . " line:" . __LINE__);
							}

							// Display
							while ($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
								print "<tr>";
								print "<td>{$row['EnergySource']} </td>";
								print "<td>{$row['MinCapacity']}</td>";
								print "<td>{$row['AvgCapacity']}</td>";
								print "<td>{$row['MaxCapacity']}</td>";
								print "<td>{$row['MinTemp']}</td>";
								print "<td>{$row['AvgTemp']}</td>";
								print "<td>{$row['MaxTemp']}</td>";
								print "</tr>";
							}

							?>
						</table>

					</div>
				</div>
			</div>

			<?php include("lib/error.php"); ?>

			<br>
			<button type="button" onclick="location.href='report_04_water_heater_stats.php'" class="button">Back</button>
			<br>
		</div>

	</div>
</body>



</html>

<!-- The content of the footer.php page goes here -->
<?php include("lib/footer.php"); ?>