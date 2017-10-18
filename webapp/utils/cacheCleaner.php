
<?php

define("UPLOAD_DIR", "../uploads/");
$filesToDelete = glob('uploads/*'); // get all file names
foreach($filesToDelete as $del){ // iterate files
  if(is_file($del))
    unlink($del); // delete file
}

?><link rel="stylesheet" type="text/css" href="../css/style.css">

<html>
    <head>
        <title>Cache Cleaner</title>
    </head>
    <body class="general">
        <center>
            <h1>ALL DONE</h1> 
            <h3>All files you uploaded are deleted.</h3>
            <div class="container">
                <form method="post" action="../index.html" enctype="multipart/form-data">
                    <input type="submit" id = "compareFile" class = "myButton" name="user_file" />
                    <label for="compareFile">Back</label>
                </form>
            </div>
        </center>
    </body>
</html>