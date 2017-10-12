<link rel="stylesheet" type="text/css" href="css/style.css">

<html>
    <head>
        <title>File upload</title>
    </head>
    <body class="general">
        <center>
            <h1>1 vs 1</h1> 
            <h3>Compare</h3>
            <div class="container">
                <form method="post" action="compareResult.php" enctype="multipart/form-data">
                    <input type="hidden" name="action" value="upload" />
                    <input type="file" id = "user_file1" class = "myButton"  name="user_file1" />
                    <label for="user_file1">Carica il primo file!</label>

                    <input type="file" id = "user_file2" class = "myButton"  name="user_file2" />
                    <label for="user_file2">Carica il secondo file!</label>
                    <br />

                    <input type="submit" id = "compareFiles" class = "myButton" />
                    <label for="compareFiles">Compara</label>
                </form>
            </div>
        </center>
    </body>
</html>