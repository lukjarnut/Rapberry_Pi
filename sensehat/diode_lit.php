<?php

shell_exec("./python/led_clear.py 2>&1"); #clear the screen

# $_POST is matrix with coordinates in one argument $_POST[xy] so we need two loops
for ($i = 0; $i <= 7; $i++) #first axis
{
    for ($j = 0; $j <= 7; $j++) #second axis
	{
		if($_POST["$i$j"] == "r" || $_POST["$i$j"] == "g" || $_POST["$i$j"] == "b") #if we know the color
		{
			$color = $_POST["$i$j"];
			shell_exec("./python/led.py -x $i -y $j -c $color 2>&1"); #setting pixel with python script at given coordinates ($i $j)
		}
	}
} 
header("Location: /sensehat/diode.html"); #return to previus page (choosing pixel to light)

?>