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
						<div class="h2">Household List</div>
						<div class="subtitle">List of All the household</div>
						<table>
							<tr>
								<td class="heading">Email</td>
								<td class="heading">Square Footage</td>
								<td class="heading">Type</td>
								<td class="heading">Postal Code</td>
								<td class="heading"> </td>
							</tr>
							<br><br>

							<?php
					
							// SQL query
							$query = "SELECT email,square_footage, household_types, postal_code
									FROM Household ";

							// Error Check
							$result = mysqli_query($db, $query);
							if (!empty($result) && (mysqli_num_rows($result) == 0)) {
								array_push($error_msg, "SELECT ERROR: find Manufacturer <br>" . __FILE__ . " line:" . __LINE__);
							}

							// Display
							while ($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
								print "<tr>";
								print "<td>{$row['email']}</td>";
								print "<td>{$row['square_footage']}</td>";
								print "<td>{$row['household_types']}</td>";
								print "<td>{$row['postal_code']}</td>";
								print "</tr>";
							}
					


							?>
						</table>

					</div>
				</div>
			</div>

			<?php include("lib/error.php"); ?>

			<div class="clear"></div>

			<br><br>
		</div>



	</div>
</body>

</html>