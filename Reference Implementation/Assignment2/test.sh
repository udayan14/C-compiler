find . -name '*.c' | while read line; do
	NAME="$(echo $line | tail -c +3)"
	echo ${NAME}
	 python3 150070001-150070018.py ${NAME};
	./Assignment2 name;
	 diff Parser_ast_${NAME}.txt Parser_ast_${NAME}.txt 
	 echo "\n"   
done



