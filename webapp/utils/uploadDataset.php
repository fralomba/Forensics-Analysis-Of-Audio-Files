<link rel="stylesheet" type="text/css" href="../css/style.css">
<?php

if( isset($_POST['action']) )
{

    $command = 'export LC_ALL=en_US.UTF-8
		 export LANG=en_US.UTF-8
		 python ../../addDAtasetToDB.py '.$_POST['DatasetFolder'];

    $output = shell_exec($command);
    if($output)
        echo $output;
    else
        echo "Something Wrong!";
}
?>

<html>
    <head>
        <title>Cache Cleaner</title>
    </head>
    <body class="general">
        <center>
            <h1>ALL DONE</h1> 
            <h3>All files below was uploaded</h3>
            <div class="container">
                <form method="post" action="../index.html" enctype="multipart/form-data">
                    <input type="submit" id = "compareFile" class = "myButton" name="user_file" />
                    <label for="compareFile">Back</label>
                </form>
            </div>
        </center>
    </body>
</html>