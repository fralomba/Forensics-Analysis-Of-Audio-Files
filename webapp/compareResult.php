<!DOCTYPE html>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>

<meta charset="utf-8">
<link rel="stylesheet" type="text/css" href="css/style.css">
<?php
define("UPLOAD_DIR", "uploads/");
if(isset($_POST['action']) and $_POST['action'] == 'upload')
{
    if(isset($_FILES['user_file1']) and isset($_FILES['user_file1']))
    {
        $file1 = $_FILES['user_file1'];
        $file2 = $_FILES['user_file2'];

        echo "<h2>".$file1['name']."</h2>";
        echo "<h2>".$file2['name']."</h2>";

        if($file1['error'] == UPLOAD_ERR_OK and is_uploaded_file($file1['tmp_name']))
        {
            move_uploaded_file($file1['tmp_name'], UPLOAD_DIR.$file1['name']);
            move_uploaded_file($file2['tmp_name'], UPLOAD_DIR.$file2['name']);
        }
    }
}

$command = 'export LC_ALL=en_US.UTF-8
		 export LANG=en_US.UTF-8
         python ../compare.py '.UPLOAD_DIR.$file1['name'].' '.UPLOAD_DIR.$file2['name'];

$output = shell_exec($command);

if($output != NULL)
echo "<script type='text/javascript'>".$output."</script>";
/*SE TUTTO VA BENE HO 2 VARIABILI: qData e gData*/
else{
	echo "<h1>Something Wrong<h1>";
	exit;}

?>
<div id="qContainer" class="container"></div>
<div id="gContainer" class="container"></div>

<script type="text/javascript">
    var qContainer = $('#qContainer');
    for(i = 0; i < qData.length; i++){
        console.log(qData[i].value);
    }
    var gContainer = $('#qContainer');
    for(i = 0; i < gData.length; i++){
        console.log(gData[i].value);
    }
</script>
