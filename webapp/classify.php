<!DOCTYPE html>
<meta charset="utf-8">
<link rel="stylesheet" type="text/css" href="css/style.css">
<script src="js/jquery.min.js"></script>

<?php

define("UPLOAD_DIR", "uploads/");
if(isset($_POST['action']) and $_POST['action'] == 'upload')
{
    if(isset($_FILES['user_file']))
    {
        $file = $_FILES['user_file'];
        echo "<a target='_blank' href='macro.php?object=".UPLOAD_DIR.$file['name']."'>
                <h2 id='file1' class=' filename left'>".$file['name']."</h2>
            </a>";
        if($file['error'] == UPLOAD_ERR_OK and is_uploaded_file($file['tmp_name']))
        {
            if ( !move_uploaded_file($file['tmp_name'], UPLOAD_DIR.$file['name']) )
                echo 'file non caricato';
        }
    }
}


$command = 'export LC_ALL=en_US.UTF-8
		 export LANG=en_US.UTF-8
		 python ../classify.py '.UPLOAD_DIR.$file['name'];

$output = shell_exec($command);

if($output != NULL)
    echo "<script>var datas =".$output.";</script>";
else{
	echo "<h1>Something Wrong<h1>";
}

// $filesToDelete = glob('uploads/*'); // get all file names
// foreach($filesToDelete as $del){ // iterate files
//   if(is_file($del))
//     unlink($del); // delete file
// }

?>


<div>
    Threshold:
    <input type="range" id="select_treshold" name="select_treshold" min="0" max="1000" oninput="updateTreshold()">
</div>
<br>
<script src="http://d3js.org/d3.v3.min.js"></script>
<script src="js/chartPlotter.js"></script>

