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
						<div class="title">Off-The-Grid Household Information</div>
						<div class="subtitle">The state with the most off-the-grid households </div>
						<!-- PART ONE -->
						<table>
							<tr>
								<th class="heading">State</th>
								<th class="heading">Count</th>
							</tr>

							<?php
							// SQL Query						
							$query = "SELECT Address.state, COUNT(*) AS count
									FROM Household
									  JOIN Address ON Household.postal_code = Address.postal_code
									  LEFT JOIN PublicUtility ON Household.email = PublicUtility.email
									WHERE PublicUtility.public_utility = 'Off-The-Grid'
									GROUP BY Address.state
									-- if max count in more than 1 state
									HAVING count = (
									  SELECT MAX(count)
									FROM (
										SELECT COUNT(*) AS count
									  FROM Household
										JOIN Address ON Household.postal_code = Address.postal_code
										LEFT JOIN PublicUtility ON Household.email = PublicUtility.email
									  WHERE PublicUtility.public_utility = 'Off-The-Grid'
									  GROUP BY Address.state
									  ) AS t
									)
									ORDER BY count";

							// Error Check
							$result = mysqli_query($db, $query);
							if (!empty($result) && (mysqli_num_rows($result) == 0)) {
								array_push($error_msg,  "SELECT ERROR: find Manufacturer <br>" . __FILE__ . " line:" . __LINE__);
							}

							// Display with HTML code
							while ($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
								print "<tr>";
								print "<td>{$row['state']} </td>";
								print "<td>{$row['count']}</td>";
								print "</tr>";
							}
							?>
						</table> <br>

						<div class="subtitle">All State Average BTU</div>
						<!-- PART TWO -->
						<table>
							<tr>
								<th class="heading">Total Count</th>
								<th class="heading">Percentage</th>
							</tr>

							<?php
							// SQL Query						
							$query = "SELECT
									COUNT(*) AS total_count,
									ROUND(COUNT(*) / (SELECT COUNT(*) FROM PowerGeneration WHERE generation_type IN ('solar-electric', 'wind')) * 100, 1) as percentage
								  FROM PowerGeneration
									JOIN Household ON Household.email = PowerGeneration.email
									JOIN PublicUtility ON Household.email = PublicUtility.email
								  WHERE  PublicUtility.public_utility = 'Off-The-Grid'";

							// Error Check
							$result = mysqli_query($db, $query);
							if (!empty($result) && (mysqli_num_rows($result) == 0)) {
								array_push($error_msg,  "SELECT ERROR: find Manufacturer <br>" . __FILE__ . " line:" . __LINE__);
							}

							// Display with HTML code
							while ($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
								print "<tr>";
								print "<td>{$row['total_count']} </td>";
								print "<td>{$row['percentage']} </td>";
								print "</tr>";
							}
							?>
						</table> <br>

						<div class="subtitle">Average Off-Grid BTU - by generation_type</div>
						<!-- PART TWO -->
						<table>
							<tr>
								<th class="heading">Off-Grid-Count</th>
								<th class="heading">Average Capacity</th>
							</tr>

							<?php
							// SQL Query						
							$query = "SELECT
									generation_type,
									COUNT(*) AS total_count
									FROM PowerGeneration
									JOIN Household ON Household.email = PowerGeneration.email
									JOIN PublicUtility ON Household.email = PublicUtility.email
								  WHERE  PublicUtility.public_utility = 'Off-The-Grid'
								  GROUP BY PowerGeneration.generation_type";

							// Error Check
							$result = mysqli_query($db, $query);
							if (!empty($result) && (mysqli_num_rows($result) == 0)) {
								array_push($error_msg,  "SELECT ERROR: find Manufacturer <br>" . __FILE__ . " line:" . __LINE__);
							}

							// Display with HTML code
							while ($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
								print "<tr>";
								print "<td>{$row['generation_type']} </td>";
								print "<td>{$row['total_count']} </td>";
								print "<td>{$row['percentage']} </td>";
								print "</tr>";
							}
							?>
						</table> <br>

						<!-- PART TWO -->
						<div class="subtitle">All State with Average BTU </div>
						<table>
							<tr>
								<th class="heading">State</th>
								<th class="heading">Avg Battery</th>
							</tr>

							<?php
							// SQL Query						
							$query = "SELECT 
									Address.state AS state,
									ROUND(AVG(PowerGeneration.battery_storage_capacity)) AS average_battery_capacity
								  FROM Household
									LEFT JOIN Address ON Household.postal_code = Address.postal_code
									LEFT JOIN PowerGeneration ON Household.email = PowerGeneration.email
									LEFT JOIN PublicUtility ON Household.email = PublicUtility.email
								  WHERE PublicUtility.public_utility = 'Off-The-Grid'
								  GROUP BY state";

							// Error Check
							$result = mysqli_query($db, $query);
							if (!empty($result) && (mysqli_num_rows($result) == 0)) {
								array_push($error_msg,  "SELECT ERROR: find Manufacturer <br>" . __FILE__ . " line:" . __LINE__);
							}

							// Display with HTML code
							while ($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
								print "<tr>";
								print "<td>{$row['state']} </td>";
								print "<td>{$row['average_battery_capacity']}</td>";
								print "</tr>";
							}
							?>
						</table> <br>

						<!-- PART THREE -->
						<div class="subtitle">All State Average BTU - with power generation type in percentage</div>
						<table>
							<tr>
								<th class="heading">Mixed Type</th>
								<th class="heading">Solar Electric</th>
								<th class="heading">Wind</th>
							</tr>

							<?php
							// SQL Query						
							$query = "SELECT 
									CONCAT(ROUND(((SELECT COUNT(*) AS total_count
										FROM PowerGeneration
										WHERE PowerGeneration.email IN (
											SELECT email
											FROM PowerGeneration
											GROUP BY email
											HAVING COUNT(DISTINCT generation_type) > 1
										)
									) / COUNT(*)) * 100, 1), '%') AS mixed_percentage,
									
									CONCAT(ROUND((SUM(CASE WHEN generation_type = 'solar-electric' THEN 1 ELSE 0 END) / COUNT(*)) * 100, 1), '%') AS solar_electric_percentage,
									
									CONCAT(ROUND(( (SUM(CASE WHEN generation_type = 'wind' THEN 1 ELSE 0 END)) / COUNT(*)) * 100, 1), '%') AS wind_percentage
									
								FROM PowerGeneration
								  JOIN Household ON Household.email = PowerGeneration.email
								  JOIN PublicUtility ON Household.email = PublicUtility.email
								WHERE PublicUtility.public_utility = 'Off-The-Grid'";

							// Error Check
							$result = mysqli_query($db, $query);
							if (!empty($result) && (mysqli_num_rows($result) == 0)) {
								array_push($error_msg,  "SELECT ERROR: find Manufacturer <br>" . __FILE__ . " line:" . __LINE__);
							}

							// Display with HTML code
							while ($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
								print "<tr>";
								print "<td>{$row['mixed_percentage']} </td>";
								print "<td>{$row['solar_electric_percentage']}</td>";
								print "<td>{$row['wind_percentage']}</td>";
								print "</tr>";
							}
							?>
						</table> <br>

						<!-- PART FOUR -->
						<div class="subtitle">Average water heater gallon capacity</div>
						<table>
							<tr>
								<th class="heading">On-Grid</th>
								<th class="heading">Off-The-Grid</th>
							</tr>

							<?php
							// SQL Query						
							$query = "SELECT
									ROUND(AVG(CASE WHEN PublicUtility.public_utility != 'Off-The-Grid' THEN WaterHeater.capacity END), 1) AS grid_avg_capacity,
									ROUND(AVG(CASE WHEN PublicUtility.public_utility = 'Off-The-Grid' THEN WaterHeater.capacity END), 1) AS off_grid_avg_capacity
								  FROM Household
									JOIN PowerGeneration ON Household.email = PowerGeneration.email
									LEFT JOIN PublicUtility ON Household.email = PublicUtility.email
									JOIN Appliance ON Household.email = Appliance.email
									LEFT JOIN WaterHeater ON Appliance.appliance_number = WaterHeater.appliance_number AND Appliance.email = WaterHeater.email";

							// Error Check
							$result = mysqli_query($db, $query);
							if (!empty($result) && (mysqli_num_rows($result) == 0)) {
								array_push($error_msg,  "SELECT ERROR: find Manufacturer <br>" . __FILE__ . " line:" . __LINE__);
							}

							// Display with HTML code
							while ($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
								print "<tr>";
								print "<td>{$row['grid_avg_capacity']} </td>";
								print "<td>{$row['off_grid_avg_capacity']}</td>";
								print "</tr>";
							}
							?>
						</table> <br>


						<!-- PART FIVE -->
						<div class="subtitle">Minimum, Average and Maximum - BTUs </div>
						<table>
							<tr>
								<th class="heading">Appliance Type</th>
								<th class="heading">Min BTU</th>
								<th class="heading">Avg BTU</th>
								<th class="heading">Max BTU</th>
							</tr>

							<?php
							// SQL Query						
							$query = "SELECT
									Appliance.appliance_type,
									ROUND(MIN(Appliance.btu_rating), 0) AS min_btu,
									ROUND(AVG(Appliance.btu_rating), 0) AS avg_btu,
									ROUND(MAX(Appliance.btu_rating), 0) AS max_btu
								  FROM Household
									JOIN PowerGeneration ON Household.email = PowerGeneration.email
									LEFT JOIN PublicUtility ON Household.email = PublicUtility.email
									JOIN Appliance ON Household.email = Appliance.email
								  WHERE PublicUtility.public_utility = 'Off-The-Grid'
								  GROUP BY Appliance.appliance_type";

							// Error Check
							$result = mysqli_query($db, $query);
							if (!empty($result) && (mysqli_num_rows($result) == 0)) {
								array_push($error_msg,  "SELECT ERROR: find Manufacturer <br>" . __FILE__ . " line:" . __LINE__);
							}

							// Display with HTML code
							while ($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
								print "<tr>";
								print "<td>" . ($row['appliance_type'] == 'air_handler' ? "Water Heater" : "Air Handler") . "</td>";
								print "<td>{$row['min_btu']}</td>";
								print "<td>{$row['avg_btu']}</td>";
								print "<td>{$row['max_btu']}</td>";
								print "</tr>";
							}
							?>
						</table> <br>
					</div>
				</div>
			</div>
			<?php include("lib/error.php"); ?>
			<br>
			<button type="button" onclick="location.href='report_list.php'" class="button">Back</button>
			<br>
		</div>
	</div>
</body>
</html>


<!-- The content of the footer.php page goes here -->
<?php include("lib/footer.php"); ?>