#!/bin/bash

flagstate=("RESET" "SET") 

t_flag=0
h_flag=0
p_flag=0
unit=" "

while getopts ":hpt:" opt; do
		case $opt in
				h)  
					h_flag=1 ;;
				p) 
					p_flag=1 ;;
				t)
					t_flag=1 
					unit=$OPTARG ;;
				\?)
					echo "option '$OPTARG' not recognised" 
					exit 1 ;;
				\:)
					echo " option '-$OPTARG ' requires argument "
					exit 1 ;;
		esac
done
shift $((OPTIND-1))

if [ $t_flag -eq 1 ]
then
	if [ "$unit" == "c" ] || [ "$unit" == "C" ]
	then
		cat /home/pi/Lab_01/temperature.dat
		echo 
	elif [ $unit == 'f' ] || [ "$unit" == "F" ]
	then
		t_C=$(cat /home/pi/Lab_01/temperature.dat)
		echo "$t_C*1.8+32"| bc -l
	else
		echo "wrong unit"
	fi
fi
if [ $h_flag -eq 1 ]
then
	cat /home/pi/Lab_01/humidity.dat
	echo
fi
if [ $p_flag -eq 1 ]
then
	cat /home/pi/Lab_01/pressure.dat
	echo
fi	