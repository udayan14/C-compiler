import os
import sys

filename = str(sys.argv[1])

os.system("python3 150070001-150070018.py "+filename)
os.system("./Assignment2 "+filename)
os.system("diff Parser_ast_"+filename+".txt Parser_ast_"+filename+".txt1")