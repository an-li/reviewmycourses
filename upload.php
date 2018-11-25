<?php

$given_name = $_POST["title"];

$path = $_FILES["file"]["name"];
$info = pathinfo($path);

$ext = $info['extension']; // get the extension of the file

$course = $_POST["course"];

$target_dir = './documents/' . $course . "/";
$target_url = '../documents/' . $course . "/";
$target_file = $target_dir . basename($_FILES["file"]["name"]);
$target_file_url = $target_url . basename($_FILES["file"]["name"]);

if (!file_exists($target_dir)) {
    mkdir($target_dir, 0777, true);
}

if ($given_name != '') {
    $basetitle = $given_name;
} 
else {
    $basetitle = basename($_FILES["file"]["name"], $ext);
}

$uploadOk = 1;

$docFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

// Checking if the file size is appropriate (Raise error if bigger than 10MB)
if ($_FILES["file"]["size"] > 10000000) {
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
        echo "The file ". basename($path). " has been uploaded. ";

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
            echo "New record created successfully.";
        } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }

        $conn->close();
    } 
    else {
        echo "Not uploaded because of error #".$_FILES["file"]["error"];
    }
}
echo "<script>window.location = 'http://localhost/cgi-bin/coursepage.py?course=$course'</script>";
?>