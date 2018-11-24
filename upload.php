<?php

$given_name = $_POST["title"];

$info = pathinfo($_FILES["file"]["name"]);

$ext = $info['extension']; // get the extension of the file

$course = $_POST["course"];

$target_dir = './documents/' . $course . "/";
$target_url = '../documents/' . $course . "/";

if (!file_exists($target_dir)) {
    mkdir($target_dir, 0777, true);
}

if ($given_name != '') {
    $basetitle = $given_name . "." . $ext;
    $target_file = $target_dir . $given_name . "." . $ext;
    $target_file_url = $target_url . $given_name . "." . $ext;
} 
else {
    $basetitle = basename($_FILES["file"]["name"]);
    $target_file = $target_dir . basename($_FILES["file"]["name"]);
    $target_file_url = $target_url . basename($_FILES["file"]["name"]);
}

$uploadOk = 1;

$docFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

// Checking if the file size is appropriate
if ($_FILES["file"]["size"] > 50000000) {
    echo "Sorry, your file is too large.";
    $uploadOk = 0;
}

// Allow certain file formats
if($docFileType != "txt" && $docFileType != "rtf" && $docFileType != "pdf" && $docFileType != "doc" && $docFileType != "docx" && $docFileType != "ppt" 
&& $docFileType != "pptx" && $docFileType != "xls" && $docFileType != "xlsx" && $docFileType != "ods" && $docFileType != "odp" && $docFileType != "odt" ) {
    echo "Sorry, you have the wrong file type";
    $uploadOk = 0;
}

// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 0) {
    echo "Sorry, your file was not uploaded.";
// if everything is ok, try to upload file
} else {
    if (move_uploaded_file($_FILES["file"]["tmp_name"], $target_file)) {
        echo "The file ". basename($_FILES["file"]["name"]). " has been uploaded.";

        $lastmodified = date("Y/m/d H:i:s", filemtime($target_file));

        $servername = "localhost";
        $username = "root";
        $password = "";
        $dbname = "reviewmycourses";

        // Create connection
        $conn = new mysqli($servername, $username, $password, $dbname);
        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        } 

        $sql = "INSERT INTO documents (tstamp, title, course, url) VALUES ('".$lastmodified."', '".$basetitle."', '".$course."', '".$target_file_url."')";

        if ($conn->query($sql) === TRUE) {
            echo "New record created successfully";
        } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }

        $conn->close();
    } 
    else {
        echo "Sorry, there was an error uploading your file.";
    }
}
?>
