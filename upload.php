<?php

$given_name = $_POST["title"];

$path = $_FILES["file"]["name"];
$info = pathinfo($path);

$ext = $info['extension']; // get the extension of the file

$course = $_POST["course"];

$uploadOk = 1;

// Create connection
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "reviewmycourses";
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
    $uploadOk = 0;
}

$target_dir = './documents/' . $course . "/";
$target_url = '../documents/' . $course . "/";
$target_file = $target_dir . $given_name .".". $ext;
$target_file_url = $target_url . $given_name .".". $ext;

$sql2 = "SELECT * FROM documents WHERE course='".$course."' AND title='".$given_name."'";
$result = $conn->query($sql2);

if ($result->num_rows > 0) {
    echo "Sorry, a file with this title already exists. Please try a different title.";
    $uploadOk = 0;
}

if (!file_exists($target_dir)) {
    mkdir($target_dir, 0777, true);
}

// Checking if the file size is appropriate (Raise error if bigger than 10MB)
if ($_FILES["file"]["size"] > 10000000) {
    echo "Sorry, your file is too large. Please try a different file.";
    $uploadOk = 0;
}

if ($uploadOk != 0) {
    if (move_uploaded_file($_FILES["file"]["tmp_name"], $target_file)) {
        echo "The file ". $given_name .".". $ext . " has been uploaded.";

        $lastmodified = date("Y/m/d H:i:s", filemtime($target_file));

        $sql = "INSERT INTO documents (tstamp, title, course, url) VALUES ('".$lastmodified."', '".$given_name."', '".$course."', '".$target_file_url."')";

        if ($conn->query($sql) === TRUE) {
            
        } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
    } 
    else {
        echo "Sorry, your file cannot be uploaded because of error #".$_FILES["file"]["error"].". Please try a different file.";
    }
}

$conn->close();

echo "<script>window.location = 'http://localhost/cgi-bin/coursepage.cgi?course=$course'</script>";
?>