<?php

$period=0;

if(isset($_GET['period'])){
	echo "Changing period of blnking diode... <br>";
	$period=$_GET['period'];
	$command = './zapis.py ' . '-w' . ' ' . $period;
	$cos = passthru($command);
	echo($cos);
}
else {
	echo "Readind period of blnking diode... <br>";
	$comman = './zapis.py ' . '-r';
	$co = passthru($comman);
	echo($co);
}
?>