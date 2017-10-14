<link rel="stylesheet" type="text/css" href="css/style.css">

<html>
    <head>
        <title>File upload</title>
    </head>
    <body class="general">
        <center>
            <h1>Classification</h1> 
            <h3>From here you can upload and have a forensic analysis of your audio files.</h3>
            <div class="container">
                <form method="post" action="dbCompareResult.php" enctype="multipart/form-data">
                    <input type="hidden" name="action" value="upload" />
                    <input type="file" id = "getFile" class = "myButton" name="user_file" />
                    <label for="getFile">Carica il tuo file!</label>
                    <br />
                    <input type="submit" id = "compareFile" class = "myButton" name="user_file" />
                    <label for="compareFile">Compara</label>
                </form>
            </div>
        </center>
    </body>
</html>