<!DOCTYPE html>
<script src="js/jquery.min.js"></script>

<meta charset="utf-8">
<link rel="stylesheet" type="text/css" href="css/style.css">
<body id="macroPage">
<?php
define("UPLOAD_DIR", "uploads/");
if(isset($_GET['object']))
{
        $file = $_GET['object']; 
}

$command = 'export LC_ALL=en_US.UTF-8
		 export LANG=en_US.UTF-8
         python ../macro.py '.$file;

$output = shell_exec($command);

if($output != NULL)
echo "<script type='text/javascript'>".$output."</script>";
else{
	echo "<h1>Something Wrong<h1>";
	exit;}
?>

<div id = "container" min-height:10%;">
    <div class="headbar">
        <h2><?php echo $file; ?></h2>
        <br>
        <h7 id='size'>9<h7>    
        </div>
    <br><br><br><br><br>
</div>
    
<script type="text/javascript">
    $(document).ready(function(){
        var container = document.getElementById("container");
        for(var i = 0; i < data.length; i++){
            if(String(data[i].label).localeCompare("LUNGHEZZA") == 0){
                document.getElementById("size").innerHTML = 'shown '+(data.length-1);
            }else{
                var mainRow = document.createElement("DIV");
                mainRow.setAttribute('class','flex-row');
                
                var centralDiv = document.createElement("DIV");
                centralDiv.setAttribute('class','tags');
                centralDiv.innerHTML = data[i].label;

                var rightDiv = document.createElement("DIV");
                rightDiv.setAttribute('class','reference column');
                rightDiv.innerHTML = data[i].value;

                mainRow.appendChild(centralDiv);                             // Append the text to <li>
                mainRow.appendChild(rightDiv);

                container.appendChild(mainRow);
            }
        }
    });
</script>
</body>

