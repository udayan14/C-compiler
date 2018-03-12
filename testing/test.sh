find . -name '*.c' | while read line; do
	NAME="$(echo $line | tail -c +3)"
	echo ${NAME}
	 python3 better.py ${NAME};
	./Parser ${NAME};
	 diff -bB ${NAME}.cfg ${NAME}.cfg1 
	 echo   

done



