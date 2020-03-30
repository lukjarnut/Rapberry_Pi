<?php

//print_r($_POST);

shell_exec("./led_clear.py 2>&1");

for ($i = 0; $i <= 7; $i++) 
{
    for ($j = 0; $j <= 7; $j++) 
	{
		if($_POST["$i$j"] == "r" || $_POST["$i$j"] == "g" || $_POST["$i$j"] == "b")
		{
		$color = $_POST["$i$j"];
		shell_exec("./led.py -x $i -y $j -c $color 2>&1");
		}
	}
} 
shell_exec("./screen_rot.py 2>&1");
header("Location: /sensehat/diode.html");
?>