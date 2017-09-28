<h2> ciao </h2>
<br>

<?php

$command = 'python /Users/adel/Desktop/FAOAF/compare.py';
$output = system($command);
if($output != NULL)
	echo $output;	
else
	echo "<h1>DIO CANE<h1>";


?>