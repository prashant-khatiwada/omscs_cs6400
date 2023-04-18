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
						<div class="subtitle">Manufacturer: <?php echo $_GET['manufacturer_name']; ?></div>
						<table>
							<tr>
								<th class="heading">Type</th>
								<th class="heading">Count</th>
							</tr>

							<?php
							// fetch the name from page
							$manufacturer_name = $_GET['manufacturer_name'];

							// SQL query
							$query = "SELECT appliance_type, COUNT(*) AS appliance_count 
									FROM Appliance
									WHERE manufacturer_name = '{$manufacturer_name}'
									GROUP BY appliance_type";

							// Error Check
							$result = mysqli_query($db, $query);
							if (!empty($result) && (mysqli_num_rows($result) == 0)) {
								array_push($error_msg,  "SELECT ERROR: find Manufacturer <br>" . __FILE__ . " line:" . __LINE__);
							}

							// Display
							while ($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
								print "<tr>";
								print "<td>{$row['appliance_type']}</td>";
								print "<td>{$row['appliance_count']}</td>";
								print "</tr>";
							}

							?>
						</table>

					</div>
				</div>
			</div>
			<?php include("lib/error.php"); ?>
			<br>
			<button type="button" onclick="location.href='report_01_top_25.php'" class="button">Back</button>
			<br>
		</div>
	</div>
</body>



</html>

<!-- The content of the footer.php page goes here -->
<?php include("lib/footer.php"); ?>