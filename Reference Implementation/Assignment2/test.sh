


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
name = ${array[$i]} | tail -c +3
echo ${array[$i]}
python3 150070001-150070018.py ${name};
./Assignment2 name;
 diff Parser_ast_${name}.txt Parser_ast_${name}.txt 
 echo "\n"
let i++
done


