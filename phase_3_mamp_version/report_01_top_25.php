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
						<div class="subtitle">Top 25 Manufactures</div>
						<table>
							<tr>
								<th class="heading">Manufacturer</th>
								<th class="heading">Appliance No.</th>
								<th class="heading">Details</th>
							</tr>

							<?php
							// SQL Query						
							$query = "SELECT manufacturer_name, COUNT(*) AS appliances_number FROM Appliance GROUP BY manufacturer_name ORDER BY appliances_number DESC LIMIT 25";

							// Error Check
							$result = mysqli_query($db, $query);
							if (!empty($result) && (mysqli_num_rows($result) == 0)) {
								array_push($error_msg,  "SELECT ERROR: find Manufacturer <br>" . __FILE__ . " line:" . __LINE__);
							}

							// Display with HTML code
							while ($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
								print "<tr>";
								print "<td>{$row['manufacturer_name']} </td>";
								print "<td>{$row['appliances_number']}</td>";
								print "<td><a href='report_01_manufacturer_detail.php?manufacturer_name={$row['manufacturer_name']}'>View Details</a></td>";
								print "</tr>";
							}
							?>
						</table>

					</div>
				</div>
			</div>

			<?php include("lib/error.php"); ?>

			<div class="clear"></div>
		</div>

	</div>
	<br>
	<button type="button" onclick="location.href='report_list.php'"class="button">Back</button>
	<br><br>
</body>

</html>


<!-- The content of the footer.php page goes here -->
<?php include("lib/footer.php"); ?>