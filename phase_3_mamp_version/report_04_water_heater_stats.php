<!-- This connects the database and result -->
<?php
// This 2 lines below, help in opening up database connection and showing the result.
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
						<div class="subtitle">Water Heater Statistics by State</div>
						<table>
							<tr>
								<th class="heading">State</th>
								<th class="heading">Avg. Capacity</th>
								<th class="heading">Avg. BTU</th>
								<th class="heading">Avg. Temp</th>
								<th class="heading">Temp Set</th>
								<th class="heading">Temp Not Set</th>
							</tr>

							<?php
							// SQL Query						
							$query = "SELECT
							Address.state AS state,
							IFNULL(ROUND(AVG(WaterHeater.capacity)), 0) AS avg_capacity,
							IFNULL(ROUND(AVG(Appliance.btu_rating)), 0) AS avg_btu,
							IFNULL(ROUND(AVG(WaterHeater.temperature), 1), 0) AS avg_temp,
							IFNULL(COUNT(CASE WHEN WaterHeater.temperature IS NOT NULL THEN 1 END), 0) AS temp_set,
							IFNULL(COUNT(CASE WHEN WaterHeater.temperature IS NULL THEN 1 END), 0) AS temp_no_set
						FROM
							Household
							LEFT JOIN Address ON Household.postal_code = Address.postal_code
							LEFT JOIN WaterHeater ON Household.email = WaterHeater.email
							LEFT JOIN Appliance ON WaterHeater.email = Appliance.email AND WaterHeater.appliance_number = Appliance.appliance_number
						GROUP BY 
							Address.state
						ORDER BY 
							Address.state ASC";

							// Error Check
							$result = mysqli_query($db, $query);
							if (!empty($result) && (mysqli_num_rows($result) == 0)) {
								array_push($error_msg, "SELECT ERROR: find Manufacturer <br>" . __FILE__ . " line:" . __LINE__);
							}

							// Display with HTML code
							while ($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
								print "<tr>";
								print "<td>{$row['state']} </td>";
								print "<td>{$row['avg_capacity']}</td>";
								print "<td>{$row['avg_btu']}</td>";
								print "<td>{$row['avg_temp']}</td>";
								print "<td>{$row['temp_set']}</td>";
								print "<td>{$row['temp_no_set']}</td>";
								print "<td><a href='report_04_water_heater_detail.php?state={$row['state']}'>View Details</a></td>";
								print "</tr>";
							}
							?>
						</table>
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