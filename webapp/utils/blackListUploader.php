<link rel="stylesheet" type="text/css" href="../css/style.css">

<html>
    <head>
        <title>List upload</title>
    </head>
    <body class="general">
        <center>
            <h1>List Uploader</h1>
            <div>
                <h3>Guidelines:</h3>
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lobortis nibh. Nulla facilisi. Cras volutpat nulla sit amet dui mollis congue. Mauris nisl velit, suscipit vel consequat eu, fermentum vel arcu. Pellentesque ultrices tortor sit amet nisi mollis, sit amet blandit eros aliquam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus a risus vitae est luctus feugiat id non nisl. Aliquam maximus, diam id posuere vehicula, dolor turpis suscipit lacus, sit amet tempor tortor magna tincidunt lorem. Proin blandit volutpat arcu vitae commodo. Pellentesque metus urna, fringilla ut ligula nec, tincidunt posuere libero. Aliquam aliquet nisl quis cursus pellentesque. Sed mauris sem, commodo nec lobortis eu, viverra eget sem. Phasellus at nulla consectetur, fermentum arcu ut, vestibulum ex. Morbi rutrum, justo nec varius fermentum, tellus justo ornare orci, et accumsan orci eros sed purus. Nullam vel lorem id nunc malesuada volutpat.


                </p>
            </div> 
            <div class="container">
                <form method="post" action="uploadLists.php" enctype="multipart/form-data">
                    <input type="hidden" name="action" value="upload" />
                    
                    <input type="file" id = "user_file1" class = "myButton"  name="blackList" />
                    <label for="user_file1">Load Black List</label>

                    <input type="file" id = "user_file2" class = "myButton"  name="ignoredList" />
                    <label for="user_file2">Load Ignored List</label>
                    <br />

                    <input type="submit" id = "compareFiles" class = "myButton" />
                    <label for="compareFiles">Upload</label>
                </form>
            </div>
        </center>
    </body>
</html>