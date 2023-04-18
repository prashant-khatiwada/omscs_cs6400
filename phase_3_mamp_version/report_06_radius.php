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
						<div class="title">Search for Household Statistics</div>
						<form action="" method="post">
							<label for="postal_code">Enter a postal code:</label>
							<input type="text" id="postal_code" name="postal_code" required>
							<br><br>
							<label for="search_radius">Select a search radius:</label>
							<select id="search_radius" name="search_radius" required>
								<option value="0">Within postal code only</option>
								<option value="5">Within 5 miles</option>
								<option value="10">Within 10 miles</option>
								<option value="25">Within 25 miles</option>
								<option value="50">Within 50 miles</option>
								<option value="100">Within 100 miles</option>
								<option value="250">Within 250 miles</option>
							</select>
							<br><br>
							<input type="submit" value="Search">
						</form>
						<br><br>

						<!-- PHP Logic with output -->
						<?php
						// Retrieve search radius and postal code from form
						$search_radius = $_POST['search_radius'];
						$center_postal_code = $_POST['postal_code'];

						// Build MySQL query using $search_radius and $postal_code variables
						$query = "SELECT 
						Household.household_types,
						COUNT(*) AS household_count,
						-- Household types
						SUM(CASE WHEN household_types = 'House' THEN 1 ELSE 0 END) AS type_house,
						SUM(CASE WHEN household_types = 'Apartment' THEN 1 ELSE 0 END) AS type_apartment,
						SUM(CASE WHEN household_types = 'Townhome' THEN 1 ELSE 0 END) AS type_townhome,
						SUM(CASE WHEN household_types = 'Condominium' THEN 1 ELSE 0 END) type_condominium,
						SUM(CASE WHEN household_types = 'Mobile Home' THEN 1 ELSE 0 END) AS type_mobile_home,
						-- Temperature
						ROUND(AVG(Household.square_footage)) AS Avg_Sq_Ft, 
						COALESCE(ROUND(AVG(Heating.temperature), 1), 0.0) AS Avg_Heating_Temp, 
						COALESCE(ROUND(AVG(Cooling.temperature), 1), 0.0) AS Avg_Cooling_Temp,
						-- Public Utility
						GROUP_CONCAT(DISTINCT PublicUtility.public_utility SEPARATOR ', ') AS used_public_utilities,
						COALESCE(SUM(CASE WHEN PublicUtility.public_utility = 'Off-The-Grid' THEN 1 ELSE 0 END), 0) AS off_grid_count,
						-- Power Generation
						COALESCE(SUM(CASE WHEN PowerGeneration.generation_type IS NOT NULL THEN 1 ELSE 0 END), 0) AS power_generation_count,
						(SELECT generation_type FROM PowerGeneration
							GROUP BY PowerGeneration.generation_type
							ORDER BY COUNT(*) DESC LIMIT 1) as Most_Common_Method,
						-- Remaining
						COALESCE(ROUND(AVG(CASE WHEN PowerGeneration.monthly_power_generated IS NOT NULL THEN PowerGeneration.monthly_power_generated END)), 0) AS avg_monthly_power_generated,
						COALESCE(SUM(CASE WHEN PowerGeneration.battery_storage_capacity IS NOT NULL THEN 1 ELSE 0 END), 0) AS battery_storage_count
					FROM Household 
					JOIN Address ON Household.postal_code = Address.postal_code
					LEFT JOIN PublicUtility ON Household.email = PublicUtility.email
					LEFT JOIN Heating  ON Household.email = Heating.email
					LEFT JOIN Cooling ON Household.email = Cooling.email
					LEFT JOIN PowerGeneration ON Household.email = PowerGeneration.email
					WHERE Address.postal_code IN (
						SELECT postal_code 
				FROM Address 
				WHERE postal_code <> $center_postal_code 
					AND (3958.75 * 2 * ATAN2(
						SQRT(
							SIN(RADIANS(latitude - (SELECT latitude FROM Address WHERE postal_code = $center_postal_code))) * SIN(RADIANS(latitude - (SELECT latitude FROM Address WHERE postal_code = $center_postal_code)))
							+ COS(RADIANS(latitude)) * COS(RADIANS((SELECT latitude FROM Address WHERE postal_code = $center_postal_code))) * SIN(RADIANS(longitude - (SELECT longitude FROM Address WHERE postal_code = $center_postal_code))) * SIN(RADIANS(longitude - (SELECT longitude FROM Address WHERE postal_code = $center_postal_code)))
						),
						SQRT(
							1 - SIN(RADIANS(latitude - (SELECT latitude FROM Address WHERE postal_code = $center_postal_code))) * SIN(RADIANS(latitude - (SELECT latitude FROM Address WHERE postal_code = $center_postal_code)))
							- COS(RADIANS(latitude)) * COS(RADIANS((SELECT latitude FROM Address WHERE postal_code = $center_postal_code))) * SIN(RADIANS(longitude - (SELECT longitude FROM Address WHERE postal_code = $center_postal_code))) * SIN(RADIANS(longitude - (SELECT longitude FROM Address WHERE postal_code = $center_postal_code)))
						)
					)) <= $search_radius
				
					)
					
					GROUP BY Household.household_types";



						// Execute MySQL query and display results
						$result = mysqli_query($db, $query);

						if (mysqli_num_rows($result) > 0) {
							// fetch all rows into an array
							$rows = mysqli_fetch_all($result, MYSQLI_ASSOC);

							echo "<div class=\"subtitle\">For the Radius: $search_radius  and Postal Code: $center_postal_code  </div>";
							echo "<br>";
							// Table 01
							echo "<table>";
							echo "<tr>
								<th>Household Types</th>
								<th>Total Count</th>
								<th>House</th>
								<th>Apartment</th>
								<th>Townhome</th>
								<th>Condomunium</th>
								<th>Mobile Home</th>
							</tr>";

							foreach ($rows as $row) {
								echo "<tr>
								<td>{$row['household_types']}</td>
									<td>{$row['household_count']}</td>
									<td>{$row['type_house']}</td>
									<td>{$row['type_apartment']}</td>
									<td>{$row['type_townhome']}</td>
									<td>{$row['type_condominium']}</td>
									<td>{$row['type_mobile_home']}</td>
								</tr>";
							}
							echo "</table>";
							echo "<hr>";
							//
							// Table 2
							echo "<table>";
							echo "<tr>
								<th>Household Types</th>
								<th>Count</th>
								<th>Avg Square Feet</th>
								<th>Avg Heat Temperature</th>
								<th>Avg Cool Temperature</th>
							</tr>";

							foreach ($rows as $row) {
								echo "<tr>
									<td>{$row['household_types']}</td>
									<td>{$row['household_count']}</td>
									<td>{$row['Avg_Sq_Ft']}</td>
									<td>{$row['Avg_Heating_Temp']}</td>
									<td>{$row['Avg_Cooling_Temp']}</td>
								</tr>";
							}
							// close the table
							echo "</table>";
							echo "<hr>";
							//
							// Table 3
							echo "<table>";
							echo "<tr>
								<th>Household Types</th>
								<th>Public Utilities</th>
								<th>Off-The-Grid Count</th>
								<th>Power Generation Count</th>
								<th>Most Common Method</th>
								<th>Avg Monthly Power Generated</th>
								<th>Battery Storage Count</th>
							</tr>";

							foreach ($rows as $row) {
								echo "<tr>
									<td>{$row['household_types']}</td>
									<td>{$row['used_public_utilities']}</td>
									<td>{$row['off_grid_count']}</td>
									<td>{$row['power_generation_count']}</td>
									<td>{$row['Most_Common_Method']}</td>
									<td>{$row['avg_monthly_power_generated']}</td>
									<td>{$row['battery_storage_count']}</td>
								</tr>";
							}
							// close the table
							echo "</table>";
							echo "<hr>";
						} else {
							echo "No Results Found.";
						}

						?>

					</div>
				</div>
			</div>
			<br>
			<button type="button" onclick="location.href='report_list.php'" class="button">Back</button>
			<br>
		</div>
		<?php include("lib/error.php"); ?>
	</div>
	</div>

</body>

</html>

<!-- The content of the footer.php page goes here -->
<?php include("lib/footer.php"); ?>