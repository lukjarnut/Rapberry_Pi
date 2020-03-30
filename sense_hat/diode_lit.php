<?php

if(empty($_GET))
{
	echo shell_exec("./led_clear.py 2>&1");
}
for ($i = 0; $i <= 7; $i++) 
{
    for ($j = 0; $j <= 7; $j++) 
	{
		if($_GET["$i$j"])
		{
			echo shell_exec("./led.py -x $i -y $j 2>&1");
		}
	}
}
header("Location: /sensehat/diode.html");
?>