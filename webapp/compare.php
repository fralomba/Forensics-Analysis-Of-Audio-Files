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

        echo"
            <div class='headbar'>
                <div>
                    <a target='_blank' href='macro.php?object=".UPLOAD_DIR.$file1['name']."'>
                        <h2 id='file1' class=' filename left'>".$file1['name']."</h2>
                    </a>
                    <h7 id='evidenceSize'>9<h7>
                </div>
                <div>
                    <h2 id='file2' class=' filename'>Different Tags</h2><h7 id='differentSize'>9<h7></div>
                <div>
                    <a target='_blank' href='macro.php?object=".UPLOAD_DIR.$file2['name']."'>
                        <h2 id='file3' class=' filename right'>".$file2['name']."</h2>
                    </a>
                    <h7 id='referenceSize'>9<h7>
                </div>
            </div>
            <br><br><br><br><br>
        ";

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

// $filesToDelete = glob('uploads/*'); // get all file names
// foreach($filesToDelete as $del){ // iterate files
//   if(is_file($del))
//     unlink($del); // delete file
// }

?>

<body id="compareResultPage">
    <div id = "container" min-height:10%;"></div>
    
<script type="text/javascript">
    $(document).ready(function(){
        var container = document.getElementById("container");
        for(var i = 0; i < data.length; i++){
            //alert(data[i].label);

            if(String(data[i].label).localeCompare("LUNGHEZZA") == 0){
                document.getElementById("evidenceSize").innerHTML = 'available '+data[i].value1;
                document.getElementById("differentSize").innerHTML = 'shown '+(data.length-1);
                document.getElementById("referenceSize").innerHTML = 'available '+data[i].value2;
            }else{
                var mainRow = document.createElement("DIV");
                mainRow.setAttribute('class','flex-row');
                
                var leftDiv = document.createElement("DIV");
                leftDiv.setAttribute('class','evidence column');
                leftDiv.innerHTML = data[i].value1;
                var centralDiv = document.createElement("DIV");
                
                ((data[i].alert) != 0)? 
                    centralDiv.setAttribute('class','tags alert'):
                    centralDiv.setAttribute('class','tags');

                centralDiv.innerHTML = data[i].label;
                var rightDiv = document.createElement("DIV");
                rightDiv.setAttribute('class','reference column');
                rightDiv.innerHTML = data[i].value2;
                                 // Create a <li> node
                
                mainRow.appendChild(leftDiv);                             // Append the text to <li>
                mainRow.appendChild(centralDiv);                             // Append the text to <li>
                mainRow.appendChild(rightDiv);

                container.appendChild(mainRow);
            }
        }
    });
</script>

</body>

