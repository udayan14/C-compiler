./test.sh $1
python3 Parser.py $1
diff -bB $1".s" $1".s1" 