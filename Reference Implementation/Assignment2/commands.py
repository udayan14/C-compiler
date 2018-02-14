import os
import sys

os.system("list = $(find .  -name \"*.c\") ")	

os.system("for i in \"$list\"; do python3 150070001-150070018.py $i; ./Assignment2 $i; diff Parser_ast_{$i}.txt Parser_ast_{$i}.txt1 ")


# os.system("python3 150070001-150070018.py "+filename)
# os.system("./Assignment2 "+filename)
# os.system("diff Parser_ast_"+filename+".txt Parser_ast_"+filename+".txt1")