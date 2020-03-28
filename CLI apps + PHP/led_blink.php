<?php

$period=0;

if(isset($_GET['period'])){
	echo "Changing period of blinking diode... <br>";
	$period=$_GET['period'];
	$command = './zapis.py ' . '-w' . ' ' . $period;
	$cos = passthru($command);
	echo($cos);
}
else {
	echo "Reading period of blinking diode... <br>";
	$comman = './zapis.py ' . '-r';
	$co = passthru($comman);
	echo($co);
}
?>