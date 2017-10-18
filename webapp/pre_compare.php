<link rel="stylesheet" type="text/css" href="css/style.css">

<html>
    <head>
        <title>File upload</title>
    </head>
    <body class="general">
        <center>
            <h1>Identification</h1> 
            <div class="container">
                <form method="post" action="compare.php" enctype="multipart/form-data">
                    <input type="hidden" name="action" value="upload" />
                    
                    <input type="file" id = "user_file1" class = "myButton"  name="user_file1" />
                    <label for="user_file1">Load Evidence</label>

                    <input type="file" id = "user_file2" class = "myButton"  name="user_file2" />
                    <label for="user_file2">Load Reference</label>
                    <br />

                    <input type="submit" id = "compareFiles" class = "myButton" />
                    <label for="compareFiles">Compare</label>
                </form>
            </div>
        </center>
    </body>
</html>