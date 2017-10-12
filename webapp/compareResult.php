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

        echo "<h2><p id='file1' class='fileName'>".$file1['name']."</p></h2>";
        echo "<h2><p id='file2' class='fileName'>Different Tags</p></h2>";
        echo "<h2><p id='file3' class='fileName'>".$file2['name']."</p></h2>";

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

$filesToDelete = glob('uploads/*'); // get all file names
foreach($filesToDelete as $del){ // iterate files
  if(is_file($del))
    unlink($del); // delete file
}

?>

<body id="compareResultPage">
    <div id = "container" min-height:10%;"></div>

<script type="text/javascript">
    $(document).ready(function(){
        var container = document.getElementById("container");
        for(var i = 0; i < data.length; i++){
            //alert(data[i].label);
            var leftDiv = document.createElement("DIV");
            leftDiv.setAttribute('class','left column');
            leftDiv.innerHTML = data[i].value1;
            var centralDiv = document.createElement("DIV");
            centralDiv.setAttribute('class','central column');
            centralDiv.innerHTML = data[i].label;
            var rightDiv = document.createElement("DIV");
            rightDiv.setAttribute('class','right column');
            rightDiv.innerHTML = data[i].value2;
                             // Create a <li> node
            
            container.appendChild(leftDiv);                             // Append the text to <li>
            container.appendChild(centralDiv);                             // Append the text to <li>
            container.appendChild(rightDiv); 
        }
        var qContainer = $('#left');
        // for(i = 0; i < qData.length; i++){
        //     console.log(qData[i].value);
        // }
        var gContainer = $('#right');
        // for(i = 0; i < gData.length; i++){
        //     console.log(gData[i].value);
        // }
    });
</script>

</body>

