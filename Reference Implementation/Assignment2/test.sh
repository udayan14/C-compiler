


array=()
find . -name "*.c" -print0 >tmpfile
while IFS=  read -r -d $'\0'; do
    array+=("$REPLY")
done <tmpfile
rm -f tmpfile

len=${#array[*]}
echo "found : ${len}"

i=0

while [ $i -lt $len ]
do
echo ${array[$i]}
python3 150070001-150070018.py ${array[$i]};
./Assignment2 ${array[$i]};
 diff Parser_ast_${array[$i]}.txt Parser_ast_${array[$i]}.txt
 echo "\n"
let i++
done


