<!DOCTYPE html>
<meta charset="utf-8">
<link rel="stylesheet" type="text/css" href="css/style.css">
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>

<?php

define("UPLOAD_DIR", "uploads/");
if(isset($_POST['action']) and $_POST['action'] == 'upload')
{
    if(isset($_FILES['user_file']))
    {
        $file = $_FILES['user_file'];
        echo "<h2>".$file['name']."</h2>";
        if($file['error'] == UPLOAD_ERR_OK and is_uploaded_file($file['tmp_name']))
        {
            move_uploaded_file($file['tmp_name'], UPLOAD_DIR.$file['name']);
        }
    }
}


$command = 'export LC_ALL=en_US.UTF-8
		 export LANG=en_US.UTF-8
		 python ../dbCompare.py '.UPLOAD_DIR.$file['name'];

$output = shell_exec($command);

if($output != NULL)
echo "<script>var datas =".$output.";</script>";
else{
	echo "<h1>Something Wrong<h1>";
	exit;}

?>


<div>
    treshold:
    <input type="range" id="select_treshold" name="select_treshold" min="0" max="100" onchange="updateTreshold()">
</div>
<br>
<script src="http://d3js.org/d3.v3.min.js"></script>
<script src="js/chartPlotter.js"></script>

<button class="container"> BACK </button>
<button class="container"> INFO </button>
