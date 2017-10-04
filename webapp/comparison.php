<link rel="stylesheet" type="text/css" href="css/style.css">

<html>
    <head>
        <title>File Comparison</title>
    </head>
    <body>
        <center>
            <h1>Select the files you want to compare:</h1> 
            <div class="container" id="leftBox">
                <form method="post" action="compareResult.php" enctype="multipart/form-data">
                    <input type="hidden" name="action" value="upload" />
                    <label>Load native audio file:</label>
                    <input type="file" name="user_file" />
                </form>
            </div>
            <div class="container" id="rightBox">
                <form method="post" action="compareResult.php" enctype="multipart/form-data">
                    <input type="hidden" name="action" value="upload" />
                    <label>Load the file you want to analyse:</label>
                    <input type="file" name="user_file" />
                </form>
            </div>

            <button class="container"> COMPARE </button> 

        </center>
    </body>
</html>