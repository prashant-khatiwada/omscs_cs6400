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
						<div class="subtitle">Manufacturer/Model Search</div>


						<form method="POST" action="">
							<input type="text" name="search_string" placeholder="Enter Search string" required>
							<input type="submit" value="Search">
						</form>

						<br>

						<?php

						if (isset($_POST['search_string'])) {

							$search_string = strtolower($_POST['search_string']);
							$query = "SELECT manufacturer_name, model_name 
										FROM Appliance 
										WHERE manufacturer_name
										LIKE '%{$search_string}%' 
										OR model_name LIKE '%{$search_string}%' 
										ORDER BY manufacturer_name ASC, model_name ASC";

							$result = mysqli_query($db, $query);

							if (mysqli_num_rows($result) > 0) {

								echo "<div class=\"subtitle\">Search String: $search_string </div>";
								echo "<br>";
								echo "<table>";
								echo "<tr><th>Manufacturer</th><th>Model</th></tr>";



								while ($row = mysqli_fetch_assoc($result)) {
									$manufacturer_name = $row['manufacturer_name'];
									$model_name = $row['model_name'];

									// Highlight the matching portions of the manufacturer name
									$manufacturer_name = preg_replace('/(' . preg_quote($search_string, '/') . ')/i', '<span class="highlight">$1</span>', $manufacturer_name);

									// Highlight the matching portions of the model name
									$model_name = preg_replace('/(' . preg_quote($search_string, '/') . ')/i', '<span class="highlight">$1</span>', $model_name);


									echo "<tr>
									<td>{$manufacturer_name}</td>
									<td>{$model_name}</td>
									</tr>";
								}


								echo "</table>";
							} else {
								echo "No Results Found.";
							}
						}
						?>

					</div>
				</div>
			</div>

			<?php include("lib/error.php"); ?>

			<br>
			<button type="button" onclick="location.href='report_list.php'" class="button">Back</button>
			<br>
		</div>

	</div>

	<style>
		.highlight {
			background-color: lightgreen;
		}
	</style>

</body>

</html>


<!-- The content of the footer.php page goes here -->
<?php include("lib/footer.php"); ?>