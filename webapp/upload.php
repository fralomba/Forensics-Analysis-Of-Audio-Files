<link rel="stylesheet" type="text/css" href="css/style.css">

<html>
    <head>
        <title>File upload</title>
    </head>
    <body>
        <center>
            <h1>Welcome on Hector Tool</h1> 
            <h3>From here you can upload and have a forensics analysis of your audio files.</h3>
            <div class="container">
                <form method="post" action="dbCompareResult.php" enctype="multipart/form-data">
                    <input type="hidden" name="action" value="upload" />
                    <label>Carica il tuo file:</label>
                    <input type="file" name="user_file" />
                    <br />
                    <input type="submit" value="Compare" />
                </form>
            </div>
        </center>
    </body>
</html>