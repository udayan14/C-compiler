find . -name '*.c' | while read line; do
	NAME="$(echo $line | tail -c +3)"
	echo ${NAME}
	 python3 150070001-150070018.py ${NAME};
	./Parser ${NAME};
	 diff -bB ${NAME}.cfg ${NAME}.cfg1 
	 echo   

done



