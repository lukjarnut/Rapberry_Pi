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

if(isset($_GET['r']))
{
	$r_flag = "-r";
}
?>