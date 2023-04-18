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
						<div class="subtitle">Heating/cooling method details</div>
						<br><br>
						<div class="subtitle">Air Conditioner</div>
						<table>
							<tr>
								<th class="heading">Types</th>
								<th class="heading">Count</th>
								<th class="heading">avg BTU</th>
								<th class="heading">EER</th>
							</tr>

							<?php
							// SQL Query						
							$query = "SELECT
							household_types,
							COUNT(AirConditioner.appliance_number) AS count,
							ROUND(AVG(Appliance.btu_rating)) AS average_btu,
							ROUND(AVG(AirConditioner.eer),1) AS average_eer
						FROM
							AirConditioner
						INNER JOIN Appliance ON AirConditioner.email = Appliance.email
						INNER JOIN Household ON AirConditioner.email = Household.email
						GROUP BY
							Household.household_types
						ORDER BY
							household_types";

							// Error Check
							$result = mysqli_query($db, $query);
							if (!empty($result) && (mysqli_num_rows($result) == 0)) {
								array_push($error_msg, "SELECT ERROR: find Manufacturer <br>" . __FILE__ . " line:" . __LINE__);
							}

							// Display with HTML code
							while ($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
								print "<tr>";
								print "<td>{$row['household_types']} </td>";
								print "<td>{$row['count']}</td>";
								print "<td>{$row['average_btu']}</td>";
								print "<td>{$row['average_eer']}</td>";
								print "</tr>";
							}
							?>
						</table>

						<br><br>
						<div class="subtitle">Heater</div>
						<table>
							<tr>
								<th class="heading">Types</th>
								<th class="heading">Count</th>
								<th class="heading">avg BTU</th>
								<th class="heading">Common Source</th>
								<th class="heading"> </th>
							</tr>

							<?php
							// SQL Query						
							$query = "SELECT
							household_types,
							COUNT(Heater.appliance_number) AS count,
							ROUND(AVG(Appliance.btu_rating)) AS average_btu,
							(SELECT energy_source FROM Heater RIGHT JOIN Household ON Heater.email = Household.email
							GROUP BY energy_source ORDER BY COUNT(*) DESC LIMIT 1 ) AS common_source
						FROM
							Heater
						INNER JOIN Appliance ON Heater.email = Appliance.email
						INNER JOIN Household ON Heater.email = Household.email
						GROUP BY
							Household.household_types
						ORDER BY
							household_types";

							// Error Check
							$result = mysqli_query($db, $query);
							if (!empty($result) && (mysqli_num_rows($result) == 0)) {
								array_push($error_msg, "SELECT ERROR: find Manufacturer <br>" . __FILE__ . " line:" . __LINE__);
							}

							// Display with HTML code
							while ($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
								print "<tr>";
								print "<td>{$row['household_types']} </td>";
								print "<td>{$row['count']}</td>";
								print "<td>{$row['average_btu']}</td>";
								print "<td>{$row['common_source']}</td>";
								print "</tr>";
							}

							?>
						</table>


						<br><br>
						<div class="subtitle">Heat Pump</div>
						<table>
							<tr>
								<th class="heading">Types</th>
								<th class="heading">Count</th>
								<th class="heading">avg BTU</th>
								<th class="heading">SEER</th>
								<th class="heading">HSPF</th>
							</tr>

							<?php
							// SQL Query						
							$query = "SELECT
							Household.household_types,
							COUNT(HeatPump.appliance_number) AS count,  -- THIS DISPLAYS A VERY LARGE NUMBER
							ROUND(AVG(Appliance.btu_rating)) AS average_btu,
							ROUND(AVG(HeatPump.seer), 1) AS average_seer, 
							ROUND(AVG(HeatPump.hspf), 1) AS average_hspf
						FROM
							HeatPump 
							INNER JOIN Appliance ON HeatPump.email = Appliance.email
							INNER JOIN Household ON HeatPump.email = Household.email
						GROUP BY
							Household.household_types
						ORDER BY
							household_types";

							// Error Check
							$result = mysqli_query($db, $query);
							if (!empty($result) && (mysqli_num_rows($result) == 0)) {
								array_push($error_msg, "SELECT ERROR: find Manufacturer <br>" . __FILE__ . " line:" . __LINE__);
							}

							// Display with HTML code
							while ($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
								print "<tr>";
								print "<td>{$row['household_types']} </td>";
								print "<td>{$row['count']}</td>";
								print "<td>{$row['average_btu']}</td>";
								print "<td>{$row['average_seer']}</td>";
								print "<td>{$row['average_hspf']}</td>";
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