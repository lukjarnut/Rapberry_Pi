<?PHP
	$h_unit = ' ';
	$t_unit = ' ';
	$p_unit = ' ';

#getting readings form senshat by web page running python scirpt
	if(isset($_GET['h'])) #check humidity flag
	{
		$h_unit=$_GET['h']; #get units [ *.php?h=% => &h_unit = %]
		
		if(strcmp($h_unit, '%') == 0) #cheking units pt.1
		{
			$h_flag = "-h %"; #setting flag for python scirpt
		}
		elseif(strcmp($h_unit, 'd') == 0) #cheking units pt.2
		{
			$h_flag = "-h d"; 
		}
		elseif(strcmp($h_unit, " ") == 0) #cathing case when user didn't want to read humisity
		{
			$h_flag = " ";
		}
		else #cathing wrong units provided by user
		{
			echo "zła jednostka wilgotności! <br>";
		}
	}
	if(isset($_GET['t']))
	{
		$t_unit=$_GET['t'];
		
		if(strcmp($t_unit, 'c') == 0)
		{
			$t_flag = "-t c";
		}
		elseif(strcmp($t_unit, 'f') == 0)
		{
			$t_flag = "-t f";
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
echo shell_exec("./sensor.py $h_flag $t_flag $p_flag 2>&1"); #executing python script with given attributes
echo("<br>");
#second script reading roll, pitch, yaw from sensehat

if(isset($_GET['r']))
{
	$r_flag = "-r";
}

if(isset($_GET['pi']))
{
	$pi_flag = "-p";
}

if(isset($_GET['y']))
{
	$y_flag = "-y";
}

if(isset($_GET['u']))
{
	$u_unit = $_GET['u'];
	if(strcmp($p_unit, "r") == 0)
	{
		$u_flag = "-u r";
	}
	elseif(strcmp($u_unit, "d") == 0)
	{
		$u_flag = "-u d";
	}
	else
	{
		echo("Wrong rotation units!");
	}
}
//echo shell_exec("./rot.py $r_flag $pi_flag $y_flag $u_flag 2>&1")

?>