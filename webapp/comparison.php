<link rel="stylesheet" type="text/css" href="css/style.css">

<html>
    <head>
        <title>File upload</title>
    </head>
    <body>
        <center>
            <h1>1 vs 1</h1> 
            <h3>Compare</h3>
            <div class="container">
                <form method="post" action="compareResult.php" enctype="multipart/form-data">
                    <input type="hidden" name="action" value="upload" />
                    <label>Carica il tuo file1:</label>
                    <input type="file" name="user_file1" />
                    <label>Carica il tuo file2:</label>
                    <input type="file" name="user_file2" />
                    <br />
                    <input type="submit" value="Compare" />
                </form>
            </div>
        </center>
    </body>
</html>