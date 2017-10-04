<!DOCTYPE html>
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
echo "<script>var datas;datas =".$output.";</script>";
else{
	echo "<h1>Something Wrong<h1>";
	exit;}

?>

<button class="container" onmouseover="printDatas()"><a href="/webapp/index.php">BACK</a></button>

<script type="text/javascript">
    function printDatas(){
        alert(datas);
    }
</script>
