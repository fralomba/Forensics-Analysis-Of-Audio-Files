<?php
define("LISTS_DIR", "../helpFiles/");
if(isset($_POST['action']) and $_POST['action'] == 'upload')
{
    if(isset($_FILES['blackList']) or isset($_FILES['ignoredList']))
    {
        $file1 = $_FILES['blackList'];
        $file2 = $_FILES['ignoredList'];

        if($file1['error'] == UPLOAD_ERR_OK and is_uploaded_file($file1['tmp_name']))
            move_uploaded_file($file1['tmp_name'], LISTS_DIR.'tagsBlackList.txt');
            
        if($file2['error'] == UPLOAD_ERR_OK and is_uploaded_file($file2['tmp_name']))
            move_uploaded_file($file2['tmp_name'], LISTS_DIR.'tagsIgnoredList.txt');
        
    }
}
header("location: ../index.html");