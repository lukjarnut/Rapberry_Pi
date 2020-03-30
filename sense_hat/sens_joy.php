<?PHP
	$h_unit = ' ';
	$t_unit = ' ';
	$p_unit = ' ';
	
	echo "odczyt ";
	
	if(isset($_GET['h']))
	{
		echo "wilgotności ";
		$h_unit=$_GET['h'];
		
		if(strcmp($h_unit, '%') == 0)
		{
			$h_flag = "-h %";
		}
		elseif(strcmp($h_unit, 'd') == 0)
		{
			$h_flag = "-h d";
		}
		elseif(strcmp($h_unit, " ") == 0)
		{
			$h_flag = " ";
		}
		else
		{
			echo "zła jednostka wilgotności! <br>";
		}
	}
	if(isset($_GET['t']))
	{
		echo "temperatury ";
		$t_unit=$_GET['t'];
		
		if(strcmp($t_unit, 'c') == 0)
		{
			$t_flag = "-p c";
		}
		elseif(strcmp($t_unit, 'f') == 0)
		{
			$t_flag = "-p f";
		}
		elseif(strcmp($t_unit, " ") == 0)
		{
			$t_flag = " ";
		}
		else
		{
			echo "zła jednostka temperatury! <br>";
		}
	}

	if(isset($_GET['p']))
	{
		echo "ciśnienia ";
		$p_unit=$_GET['p'];
		
		if(strcmp($p_unit, "hpa") == 0)
		{
			$p_flag = "-p hpa";
		}
		elseif(strcmp($p_unit, "mmhg") == 0)
		{
			$p_flag = "-p mmhg";
		}
		elseif(strcmp($p_unit, " ") == 0)
		{
			$p_flag = " ";
		}
		else
		{
			echo "zła jednostka ciśnienia! <br>";
		}
	}

		// chdir('/home/pi/server_examples/sense_hat/');
echo ("./sensor.py $h_flag $t_flag $p_flag <br>");
echo exec('./sensor.py $h_flag $t_flag $p_flag 2>&1');
?>