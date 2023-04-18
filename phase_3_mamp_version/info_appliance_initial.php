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
			<div class="title">Appliance</div>
			<div class="subtitle">User: <?php echo $_GET['email']; ?>
			</div>
			<br><br>
			<?php
			// Check if the button has been clicked before displaying it
			if (!isset($_POST['add_appliance'])) {
				echo '<form method="POST">';
				echo '<button type="submit" name="add_appliance" class="button">Add Appliance</button>';
				echo '</form>';
			} else {
				header("Location: info_appliance_add.php?email=" . urlencode($_GET['email']));
			}
			?> <br>
		</div>
	</div>
</body>

</html>

<!-- The content of the footer.php page goes here -->
<?php include("lib/footer.php"); ?>