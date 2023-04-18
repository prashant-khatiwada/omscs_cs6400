<?php


// Check if the file was uploaded without errors
if (isset($_FILES["file"]) && $_FILES["file"]["error"] == 0) {



	// Set the file name and directory
	$target_dir = "uploads/";
	$target_file = $target_dir . basename($_FILES["file"]["name"]);
	$file_type = pathinfo($target_file, PATHINFO_EXTENSION);

	// Check if the file type is csv
	if ($file_type == "csv") {

		// Move the uploaded file to the target directory
		if (move_uploaded_file($_FILES["file"]["tmp_name"], $target_file)) {

			// Connect to the database
			$servername = "localhost";
			$username = "username";
			$password = "password";
			 $dbname = "cs6400_household_team92";
			$conn = new mysqli($servername, $username, $password, $dbname);

		  // Open up the database
include('lib/common.php');
include('lib/show_queries.php');

			// Open the uploaded file
			$file = fopen($target_file, "r");  

			// Loop through each line in the file
			while (($data = fgetcsv($file, 0, "\t")) !== FALSE) {

				// Get the values from the line
				$postal_code = $data[0];
				$city = $data[1];
				$state = $data[2];
				$latitude = $data[3];
				$longitude = $data[4];

				// Insert the values into the Address table
				$sql = "INSERT INTO Address (postal_code, latitude, longitude, city, state)
						VALUES ('$postal_code', '$latitude', '$longitude', '$city', '$state')";

				if ($conn->query($sql) === FALSE) {
					echo "Error: " . $sql . "<br>" . $conn->error;
				}

			}

			echo "File uploaded and data imported successfully.";

		} else {
			echo "Sorry, there was an error uploading your file.";
		}

	} else {
		echo "Sorry, only TSV files are allowed.";
	}

} else {
	echo "Sorry, there was an error uploading your file.";
}




?>