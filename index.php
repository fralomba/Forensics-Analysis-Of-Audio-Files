<?php
echo "ciao";
//$command = escapeshellcmd('python /Users/francesco/Desktop/testPHP/echo.py');
$command = escapeshellcmd('python compare.py');
$output = shell_exec($command);
echo $output;

//echo "test";

// $output = shell_exec('python /Users/francesco/Desktop/echo.py');
// echo $output;

?>