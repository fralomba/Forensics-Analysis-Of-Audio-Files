<link rel="stylesheet" type="text/css" href="../css/style.css">

<html>
    <head>
        <title>Dataset upload</title>
    </head>
    <body class="general">
        <center>
            <h1>Dataset Uploader</h1>
            <div>
                <h3>Guidelines:</h3>
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lobortis nibh. Nulla facilisi. Cras volutpat nulla sit amet dui mollis congue. Mauris nisl velit, suscipit vel consequat eu, fermentum vel arcu. 
                </p>
            </div> 
            <div class="container">
                <form method="post" action="uploadDataset.php" enctype="multipart/form-data">
                    <input type="hidden" name="action" value="upload" />
                    
                    <label for="dataset_path:"> Dataset Folder</label>
                    <input type="text" id = "dataset_path"   name="DatasetFolder" />
                    
                    <br>
                    <input type="submit" id = "compareFiles" class = "myButton" />
                    <label for="compareFiles">Upload</label>
                </form>
            </div>
        </center>
    </body>
</html>