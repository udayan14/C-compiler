#!/usr/bin/python3

import sys
import ply.lex as lex
import ply.yacc as yacc
import functools
from CFGclass import *
from ASTclass import *
from HelperFunctions import *
from GlobalVariables import *

condendnum=0
condfalsenum=0

class SymbolTable:

	def __init__(self):
		self.parent = None
		self.varTable = dict()
		self.funcTable = dict()
		self.size = 0
		self.paramsize = 0
		self.empty = 0
	def addEntry(self,ast):
		global declaration_error, declaration_error_string
		if(ast.Type == "DECL"):
			t = ast.l[0]
			for i in range(0,len(ast.l[1])):
				if isinstance(ast.l[1][i],str):
					if ast.l[1][i] in self.varTable:
						declaration_error = 1
						declaration_error_string = str(ast.l[1][i])+" declared more than once in same scope."
					else:
						if ast.l[0] == "int":
							self.varTable[ast.l[1][i]] = [t,0,self.size,0]
							self.size+=4

						else:
							self.varTable[ast.l[1][i]] = [t,0,self.size,0]
							self.size+=8              ##This is gonna get bad
				else:
					if ast.l[1][i][0] in self.varTable:
						declaration_error = 1
						declaration_error_string = str(ast.l[1][i])+" declared more than once in same scope."
					else:
						self.varTable[ast.l[1][i][0]] = [t,ast.l[1][i][1],self.size,0]
						self.size+=4

		elif(ast.Type == "FCALL"):
			global globalSym
			typeslist = []
			for ch in ast.l[0].l:
				retvalue, type1, level1 = Checktype(self.varTable, ch)
				if(level1<0 or not retvalue):
					print(level1,retvalue)
					declaration_error = 1
					declaration_error_string = "too much indirection"
					return

				# typestring = type1 + str(int(level1)*"*")
				typeslist.append([type1,('a',level1)])

			# print("Types : ",typeslist)
			temp = makestring1(typeslist)
			ast.funcstr = temp
			t = (ast.Name, temp)
			# print("Self.functable",globalSym.funcTable)

			if t in self.funcTable:
				# print(globalSym.funcTable[t])
				if(self.funcTable[t][0]!="void"):

					declaration_error=1
					declaration_error_string = "function is not of void type"
				pass
			elif t in globalSym.funcTable:
				if(globalSym.funcTable[t][0]!="void"):
					declaration_error=1
					declaration_error_string = "function is not of void type"
				pass
			else:
				declaration_error = 1
				declaration_error_string = "function " + ast.Name + " calling error"

		elif (ast.Type == "PROTO"):
			temp = makestring1(ast.l[1])
			t = (ast.Name,temp)
			if t in self.funcTable:
				declaration_error = 1
				declaration_error_string = "function " + ast.Name + " declared more than once"
			else:
				fTable = SymbolTable()
				fTable.empty = 1
				self.funcTable[t] = (ast.l[0],ast.l[2],fTable,getoffset(ast.l[1]))

		elif (ast.Type == "FUNC"):
			# print("ASTL1",ast.l[1])
			temp = makestring1(ast.l[1])
			# print("TEMP", temp)
			t = (ast.Name,temp)
			if t in self.funcTable:
				temp1 = self.funcTable[t]
				if(temp1[2].empty):

					temp1[2].addEntry(AST("PARAMLIST","",[ast.l[1]]))
					temp1[2].addEntry(ast.l[2])
					temp1[2].empty = 0
				else:
					declaration_error = 1
					declaration_error_string = "function " + ast.Name + " already defined more than once"
			else:
				
				fTable = SymbolTable()
				fTable.addEntry(AST("PARAMLIST","",[ast.l[1]]))
				fTable.addEntry(ast.l[2])			
				self.funcTable[t] = (ast.l[0],ast.l[3],fTable,getoffset(ast.l[1]))

			for ss in ast.l[2].l:
				if(ss.Type == "RETURN"):
					a,b,c = Checktype(self.funcTable[t][2].varTable, ss.l[0])
					if(b == "void" and ss.l[0]=="EMPTYRETURN"):
						print("Empty return statement found")
						pass
					if(self.funcTable[t][0]!=b or self.funcTable[t][1]!=c or not a):
						print("Values:::::",self.funcTable[t][0],b ,self.funcTable[t][1],c,a)
						declaration_error = 1
						declaration_error_string = "return statement not of correct type"

		elif(ast.Type == "PARAMLIST"):
			l = ast.l[0]
			for t in l:
				type1 = t[0]
				name = t[1]
				if isinstance(name,str):
					if name in self.varTable:
						declaration_error = 1
						declaration_error_string = name + " declared more than once in same scope."
					else:
						if type1 == "int":
							self.varTable[name] = (type1,0,self.paramsize,1)
							self.paramsize+=4
						else:
							self.varTable[name] = (type1,0,self.paramsize,1)
							self.paramsize+=8
				else:
					name1 = name[0]
					level = name[1]
					if name1 in self.varTable:
						declaration_error = 1
						declaration_error_string = name1 + " declared more than once in same scope."
					else:
						self.varTable[name1] = (type1,level,self.paramsize,1)
						self.paramsize+=4

		elif (ast.Type == "BODY"):
			for ast1 in ast.l:
				self.addEntry(ast1)

		elif (ast.Type == "ASGN"):
			c1,t1,l1 = Checktype(self.varTable,ast)
			if not c1:
				declaration_error = 1
				declaration_error_string = "Type error in assignment !"

		elif (ast.Type == "RETURN"):
			c1,l1,t1 = Checktype(self.varTable, ast.l[0])
			if(not c1):
				declaration_error = 1
				declaration_error_string = "return expression type mismatch"

	def printTable(self):
		print("Global Variable defined in the code are :")
		for key,value in self.varTable.items():
			print(value[0] + '*'*value[1] + " " +key +" Offset: ",value[2])
		print("Functions defined in code are :")
		for key,value in self.funcTable.items():
			print(key[0],"("+key[1]+")"+" Offset list is: "+str(value[3]))
			for key1,value1 in value[2].varTable.items():
				print(value1[0] + '*'*value1[1] + " " + key1 +" Offset: ",value1[2])
		pass

globalSym = SymbolTable() 

def Checktype(varTable, ast):
	global globalSym
	if(ast=="EMPTYRETURN"):
		return True,"void",0
	if(ast.Type in ["ASGN","LE","GE","GT","LT","EQ","NE","AND","OR"]):
		llt, type1, level1 = Checktype(varTable, ast.l[0])
		rrt, type2, level2 = Checktype(varTable, ast.l[1])
		if(not llt or not rrt):
			return False,"",-1
		if(type1 != type2):

			print("Type mismatch",type1,type2)
			return False,"",-1
			
		if (level1 != level2):
			print("Indirection level mismatch", level1, level2)
			return False, "",-1

		else:
			return True, type1, level1

	elif(ast.Type in ["PLUS","MINUS","MUL","DIV"]):
		llt, type1, level1 = Checktype(varTable, ast.l[0])
		rrt, type2, level2 = Checktype(varTable, ast.l[1])
		if(not llt or not rrt):
			return False,"",-1
		if(type1 != type2):

			print("Type mismatch",type1,type2)
			return False,"",-1
			
		if (level1 > 0 and level2 > 0):
			print("Arithmetic operations on pointers not allowed", level1, level2)
			return False, "",-1

		else:
			return True, type1, level1

	elif(ast.Type == "CONST"):
		return True,ast.Name, 0
	elif(ast.Type == "VAR"):
		# print(varTable.keys())
		if ast.Name not in varTable.keys():
			if ast.Name not in globalSym.varTable:
				# print("iauhfc iuaeohmi")
				print("",varTable)
				return False, "int",-1
			else:
				# print(globalSym.varTable[ast.Name])
				this_level = globalSym.varTable[ast.Name][1]
				return True, globalSym.varTable[ast.Name][0], this_level
		else:
			# print("yoyoyoyoyoyoy",varTable[ast.Name])
			return True, varTable[ast.Name][0],  varTable[ast.Name][1]

	elif(ast.Type == "DEREF"):
		llt, type1, level1 = Checktype(varTable, ast.l[0])
		return llt, type1, level1-1

	elif(ast.Type == "ADDR"):
		llt, type1, level1 = Checktype(varTable, ast.l[0])
		return llt, type1, level1+1

	elif(ast.Type == "UMINUS" or ast.Type == "NOT"):
		return Checktype(varTable, ast.l[0]) 

	elif(ast.Type == "FCALL"):
		typeslist = []
		for ch in ast.l[0].l:
			retvalue, type1, level1 = Checktype(varTable, ch)
			if(level1<0 or not retvalue):
				declaration_error = 1
				declaration_error_string = "Too much indirection"
				return False, "int", -1
			# typestring = type1 + str(int(level1)*"*")
			typeslist.append([type1,('a',level1)])
			# print("Types : ",typeslist)
		temp = makestring1(typeslist)
		ast.funcstr = temp
		t = (ast.Name, temp)
		if t in globalSym.funcTable:
			temp = globalSym.funcTable[t]
			# print("TEMP",temp)
			print("Returning type ",ast.l[1])
			return True, temp[0], temp[1]+ast.l[1]
			# print(globalSym.funcTable[t])
		else:
			declaration_error = 1
			declaration_error_string = "function " + ast.Name + " calling error"
			return False, "int", -1

tokens = (
	'NUMBER','FLOAT',
	'TYPE',
	'SEMICOLON', 'EQUALS', 'COMMA',
	'LPAREN', 'RPAREN','LBRACE', 'RBRACE',
	'ANDOPERATOR','OROPERATOR','ADDROF',
	'NAME',
	'PLUS','MINUS','TIMES','DIVIDE',
	'WHILE','IF','ELSE','RETURN',
	'EQUALCHECK','UNEQUAL','LESSTHAN','LESSTHANEQ','GREATERTHAN','GREATERTHANEQ','NOT',
	)

t_ignore = " \t"
t_SEMICOLON = ";"
t_COMMA = ","
t_EQUALS = "="
t_EQUALCHECK = "=="
t_UNEQUAL = "!="
t_LESSTHAN = "<"
t_LESSTHANEQ = "<="
t_GREATERTHAN = ">"
t_GREATERTHANEQ = ">="
t_NOT = "!"
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ADDROF = r'&'
t_ANDOPERATOR = "&&"
t_OROPERATOR = r'\|\|'
t_TIMES = r'\*'
t_PLUS = r'\+'
t_MINUS = r'-'
t_DIVIDE = r'/'

def t_TYPE(t):
	r'\bvoid\b | \bint\b | \bfloat\b'
	return t

def t_RETURN(t):
	r'\breturn\b'
	return t

def t_WHILE(t):
	r'\bwhile\b'
	return t

def t_IF(t):
	r'\bif\b'
	return t

def t_ELSE(t):
	r'\belse\b'
	return t

def t_newline(t):
	r'\n'
	t.lexer.lineno += len(t.value)

def t_COMMENT(t):
	r'//.*'
	pass

def t_FLOAT(t):
	r'\d+\.\d+'
	try:
		t.value = float(t.value)
		# print(t.value)
	except ValueError:
		print("Float value too large %f", t.value)
		t.value = 0
	return t

def t_NUMBER(t):
	r'\d+'
	try:
		t.value = int(t.value)
	except ValueError:
		print("Integer value too large %d", t.value)
		t.value = 0
	return t



def t_error(t): 
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

precedence = (
	('left','OROPERATOR'),
	('left','ANDOPERATOR'),
	('left','EQUALCHECK','UNEQUAL'),
	('left','LESSTHANEQ','LESSTHAN','GREATERTHANEQ','GREATERTHAN'),
	('left','PLUS','MINUS'),
	('left','TIMES','DIVIDE'),
	('right','VALOF','ADDROF'),
	('right','NOT'),
	('right','UMINUS'),
	
	)

def printCFG(ast):
	l1 = ast.l
	CFG_list = []
	num = 0
	for i in range(0,len(l1)):
		if ast.l[i].Type == "FUNC":
			cfg = CFG()
			cfg.insert(l1[i])
			cleanup(cfg.head)
			num1 = giveNumbering(cfg.head,num-1)
			s = "function " + ast.l[i].Name + "(" + makestring(ast.l[i].l[1]) + ")"
			print(s)
			printCFGhelper(cfg.head,num-1)
			CFG_list.append(cfg)
			num = num1-1
			if ast.l[i].Name == "main":
				num += 1
	return CFG_list

def printSymbolTable():
	print("Procedure table :-")
	s = "-----------------------------------------------------------------"
	print(s)
	print("Name		|	Return Type  |  Parameter List")
	for key,values in globalSym.funcTable.items():
		print(key[0]+"\t\t"+"|"+"\t"+values[0]+values[1]*"*"+"\t\t"+"|"+"\t"+key[1])
	print(s)
	print("Variable table :- ")
	print(s)
	print("Name\t\t|\tScope\t\t|\tBase Type\t\t|\tDerived Type")
	print(s)
	for key,values in globalSym.varTable.items():
		print(key+"\t\t"+"|"+"\t"+"procedure global"+"\t\t"+"|"+"\t"+values[0]+"\t\t"+"|\t"+values[1]*"*")
	for key,values in globalSym.funcTable.items():
		for key1, values1 in values[2].varTable.items():
			print(key1+"\t\t"+"|"+"\t"+"procedure "+key[0]+"\t\t"+"|"+"\t"+values1[0]+"\t\t"+"|\t"+values1[1]*"*")
	print(s)
	print(s)

def printAssembly(cfg_list):
	print("")
	printhelper(".data",1)
	for key in sorted(globalSym.varTable):
		if globalSym.varTable[key][1]==0 and globalSym.varTable[key][0]=="float":
			print("global_{0}:\t.space\t8".format(key))
		else:
			print("global_{0}:\t.word\t0".format(key))
	print("")
	for cfg in cfg_list:
		#Printing Prologue
		printhelper(".text\t# The .text assembler directive indicates",1)
		printhelper(".globl {0}\t# The following is the code".format(cfg.funcinfo[0]),1)
		print("{0}:".format(cfg.funcinfo[0]))
		print("# Prologue begins")
		printhelper("sw $ra, 0($sp)  # Save the return address",1)
		printhelper("sw $fp, -4($sp) # Save the frame pointer",1)
		printhelper("sub $fp, $sp, 8 # Update the frame pointer",1)
		t = globalSym.funcTable[cfg.funcinfo]
		table = t[2]
		printhelper("sub $sp, $sp, {0}        # Make space for the locals".format(table.size+8),1)
		print("# Prologue ends")
		#Printint function
		printAssemblyHelper(cfg.head,0,cfg.funcinfo)
		printhelper("j epilogue_{0}".format(cfg.funcinfo[0]),1)
		print("")
		#Printing Epilogue
		print("# Epilogue begins")
		print("epilogue_{0}:".format(cfg.funcinfo[0]))
		printhelper("add $sp, $sp, {0}".format(table.size+8),1)
		printhelper("lw $fp, -4($sp)",1)
		printhelper("lw $ra, 0($sp)",1)
		printhelper("jr $ra  # Jump back to the called procedure",1)
		print("# Epilogue ends")


def printAssemblyHelper(n1,nextstatenum,funcinfo):
	if n1==-1:
		return
	elif n1.Type == "Start":
		printAssemblyHelper(n1.left,nextstatenum,funcinfo)

	elif n1.Type == "End":
		print("label{0}:".format(n1.num))

	elif n1.Type == "Normal":
		print("label{0}:".format(n1.num))
		# print("{0} has child {1}".format(n1.num,n1.l))	
		for ast in n1.astList:
			ASTtoAssembly(ast,funcinfo)
		if n1.hasreturn == 1:
			pass
		elif (not (n1.left==-1 and n1.right==-1 and n1.middle==-1)):			
			printhelper("j label{0}".format(n1.num+1),1)
			print("")
			printAssemblyHelper(n1.left,nextstatenum,funcinfo)
		else:
			printhelper("j label{0}".format(nextstatenum),1)
			print("")

	elif n1.Type == "ITE":
		print("label{0}:".format(n1.num))
		reg = ASTtoAssembly(n1.astList[0],funcinfo)
		freeNormReg(reg[0])
		# if(n1.left==-1):
		# 	print("if(t{0}) goto <bb {1}>".format(n1.num1,n1.middle.num))
		# else:
		# 	print("if(t{0}) goto <bb {1}>".format(n1.num1,n1.left.num))
		# if(n1.right==-1):
		# 	print("else goto <bb {0}>".format(n1.middle.num))
		# else:
		# 	print("else goto <bb {0}>".format(n1.right.num))
		# print("")
		if n1.left!=-1 and n1.right!=-1 and n1.middle!=-1:
			printhelper("bne $s{0}, $0, label{1}".format(reg[0],n1.left.num),1)
			printhelper("j label{0}".format(n1.right.num),1)
			print("")
			printAssemblyHelper(n1.left,n1.middle.num,funcinfo)
			printAssemblyHelper(n1.right,n1.middle.num,funcinfo)
			printAssemblyHelper(n1.middle,nextstatenum,funcinfo)
		elif n1.left!=-1 and n1.middle!=-1:
			printhelper("bne $s{0}, $0, label{1}".format(reg[0],n1.left.num),1)
			printhelper("j label{0}".format(n1.middle.num),1)
			print("")
			printAssemblyHelper(n1.left,n1.middle.num,funcinfo)
			printAssemblyHelper(n1.middle,nextstatenum,funcinfo)
		elif n1.right!=-1 and n1.middle!=-1:
			printhelper("bne $s{0}, $0, label{1}".format(reg[0],n1.middle.num),1)
			printhelper("j label{0}".format(n1.right.num),1)
			print("")
			printAssemblyHelper(n1.right,n1.middle.num,funcinfo)
			printAssemblyHelper(n1.middle,nextstatenum,funcinfo)
		elif n1.left!=-1 and n1.right!=-1:
			printhelper("bne $s{0}, $0, label{1}".format(reg[0],n1.left.num),1)
			printhelper("j label{0}".format(n1.right.num),1)
			print("")
			printAssemblyHelper(n1.left,nextstatenum,funcinfo)
			printAssemblyHelper(n1.right,nextstatenum,funcinfo)
		elif n1.left!=-1:
			printhelper("bne $s{0}, $0, label{1}".format(reg[0],n1.left.num),1)
			printhelper("j label{0}".format(nextstatenum),1)
			print("")
			printAssemblyHelper(n1.left,nextstatenum,funcinfo)
		elif n1.right!=-1:
			printhelper("bne $s{0}, $0, label{1}".format(reg[0],nextstatenum),1)
			printhelper("j label{0}".format(n1.right.num),1)
			print("")
			printAssemblyHelper(n1.right,nextstatenum,funcinfo)
		elif n1.middle!=-1:
			printhelper("bne $s{0}, $0, label{1}".format(reg[0],nextstatenum),1)
			printhelper("j label{0}".format(nextstatenum),1)
			print("")
			printAssemblyHelper(n1.middle,nextstatenum,funcinfo)

	elif n1.Type == "IF":
		print("label{0}:".format(n1.num))
		reg = ASTtoAssembly(n1.astList[0],funcinfo)
		freeNormReg(reg[0])
		if (n1.left!=-1 and n1.middle!=-1):
			printhelper("bne $s{0}, $0, label{1}".format(reg[0],n1.left.num),1)
			printhelper("j label{0}".format(n1.middle.num),1)
			print("")
			printAssemblyHelper(n1.left,n1.middle.num,funcinfo)
			printAssemblyHelper(n1.middle,nextstatenum,funcinfo)
		elif n1.left!=-1:
			printhelper("bne $s{0}, $0, label{1}".format(reg[0],n1.left.num),1)
			printhelper("j label{0}".format(nextstatenum),1)
			print("")
			printAssemblyHelper(n1.left,nextstatenum,funcinfo)
		elif n1.middle!=-1:
			printhelper("bne $s{0}, $0, label{1}".format(reg[0],n1.middle.num),1)
			printhelper("j label{0}".format(n1.middle.num),1)
			print("")
			printAssemblyHelper(n1.middle,nextstatenum,funcinfo)
		else:
			printhelper("bne $s{0}, $0, label{1}".format(reg[0],nextstatenum),1)
			printhelper("j label{0}".format(nextstatenum),1)
			print("")

	elif n1.Type == "WHILE":
		print("label{0}:".format(n1.num))			
		reg = ASTtoAssembly(n1.astList[0],funcinfo)
		freeNormReg(reg[0])
		# print("")
		if (n1.left!=-1 and n1.middle!=-1):
			printhelper("bne $s{0}, $0, label{1}".format(reg[0],n1.left.num),1)
			printhelper("j label{0}".format(n1.middle.num),1)
			print("")
			printAssemblyHelper(n1.left,n1.num,funcinfo)
			printAssemblyHelper(n1.middle,nextstatenum,funcinfo)
		elif n1.left!=-1:
			printhelper("bne $s{0}, $0, label{1}".format(reg[0],n1.left.num),1)
			printhelper("j label{0}".format(nextstatenum),1)
			print("")
			printAssemblyHelper(n1.left,n1.num,funcinfo)
		elif n1.middle!=-1:
			printhelper("bne $s{0}, $0, label{1}".format(reg[0],n1.num),1)
			printhelper("j label{0}".format(n1.middle.num),1)
			print("")
			printAssemblyHelper(n1.middle,nextstatenum,funcinfo)
		else:
			printhelper("bne $s{0}, $0, label{1}".format(reg[0],nextstatenum),1)
			printhelper("j label{0}".format(nextstatenum),1)
			print("")

def ASTtoAssembly(ast,funcinfo):
	global condfalsenum, condendnum
	if ast.Type == "PLUS":
		if ast.l[0].isSimple():
			if ast.l[1].isSimple():
				r0 = ASTtoAssembly(ast.l[0],funcinfo)
				r1 = ASTtoAssembly(ast.l[1],funcinfo)
			else:
				r1 = ASTtoAssembly(ast.l[1],funcinfo)
				r0 = ASTtoAssembly(ast.l[0],funcinfo)
		else:
			r0 = ASTtoAssembly(ast.l[0],funcinfo)
			r1 = ASTtoAssembly(ast.l[1],funcinfo)
		if(r0[1]==0):
			val = getNormReg()
			printhelper("add $s{0}, $s{1}, $s{2}".format(val,r0[0],r1[0]),1)
			freeNormReg(r0[0])
			freeNormReg(r1[0])
			# printNormReg()
			val1 = getNormReg()
			printhelper("move $s{0}, $s{1}".format(val1,val),1)
			freeNormReg(val)
			# printNormReg()
			# print("Freeing reg ",val)
			return(val1,0)
		else:
			val = getFloatReg()
			printhelper("add.s $f{0}, $f{1}, $f{2}".format(val,r0[0],r1[0]),1)
			freeFloatReg(r0[0])
			freeFloatReg(r1[0])
			val1 = getFloatReg()
			printhelper("mov.s $f{0}, $f{1}".format(val1,val),1)
			freeFloatReg(val)
			return(val1,1)

	if ast.Type == "MINUS":
		if ast.l[0].isSimple():
			if ast.l[1].isSimple():
				r0 = ASTtoAssembly(ast.l[0],funcinfo)
				r1 = ASTtoAssembly(ast.l[1],funcinfo)
			else:
				r1 = ASTtoAssembly(ast.l[1],funcinfo)
				r0 = ASTtoAssembly(ast.l[0],funcinfo)
		else:
			r0 = ASTtoAssembly(ast.l[0],funcinfo)
			r1 = ASTtoAssembly(ast.l[1],funcinfo)
		if(r0[1]==0):
			val = getNormReg()
			printhelper("sub $s{0}, $s{1}, $s{2}".format(val,r0[0],r1[0]),1)
			freeNormReg(r0[0])
			freeNormReg(r1[0])
			# printNormReg()
			val1 = getNormReg()
			printhelper("move $s{0}, $s{1}".format(val1,val),1)
			freeNormReg(val)
			# printNormReg()
			# print("Freeing reg ",val)
			return(val1,0)
		else:
			val = getFloatReg()
			printhelper("sub.s $f{0}, $f{1}, $f{2}".format(val,r0[0],r1[0]),1)
			freeFloatReg(r0[0])
			freeFloatReg(r1[0])
			val1 = getFloatReg()
			printhelper("mov.s $f{0}, $f{1}".format(val1,val),1)
			freeFloatReg(val)
			return(val1,1)

	if ast.Type == "MUL":
		if ast.l[0].isSimple():
			if ast.l[1].isSimple():
				r0 = ASTtoAssembly(ast.l[0],funcinfo)
				r1 = ASTtoAssembly(ast.l[1],funcinfo)
			else:
				r1 = ASTtoAssembly(ast.l[1],funcinfo)
				r0 = ASTtoAssembly(ast.l[0],funcinfo)
		else:
			r0 = ASTtoAssembly(ast.l[0],funcinfo)
			r1 = ASTtoAssembly(ast.l[1],funcinfo)
		if(r0[1]==0):
			val = getNormReg()
			printhelper("mul $s{0}, $s{1}, $s{2}".format(val,r0[0],r1[0]),1)
			freeNormReg(r0[0])
			freeNormReg(r1[0])
			# printNormReg()
			val1 = getNormReg()
			printhelper("move $s{0}, $s{1}".format(val1,val),1)
			freeNormReg(val)
			# printNormReg()
			# print("Freeing reg ",val)
			return(val1,0)
		else:
			val = getFloatReg()
			printhelper("mul.s $f{0}, $f{1}, $f{2}".format(val,r0[0],r1[0]),1)
			freeFloatReg(r0[0])
			freeFloatReg(r1[0])
			val1 = getFloatReg()
			printhelper("mov.s $f{0}, $f{1}".format(val1,val),1)
			freeFloatReg(val)
			return(val1,1)

	if ast.Type == "DIV":
		if ast.l[0].isSimple():
			if ast.l[1].isSimple():
				r0 = ASTtoAssembly(ast.l[0],funcinfo)
				r1 = ASTtoAssembly(ast.l[1],funcinfo)
			else:
				r1 = ASTtoAssembly(ast.l[1],funcinfo)
				r0 = ASTtoAssembly(ast.l[0],funcinfo)
		else:
			r0 = ASTtoAssembly(ast.l[0],funcinfo)
			r1 = ASTtoAssembly(ast.l[1],funcinfo)
		if(r0[1]==0):
			val = getNormReg()
			printhelper("div $s{0}, $s{1}".format(r0[0],r1[0]),1)
			printhelper("mflo $s{0}".format(val),1)
			freeNormReg(r0[0])
			freeNormReg(r1[0])
			# printNormReg()
			val1 = getNormReg()
			printhelper("move $s{0}, $s{1}".format(val1,val),1)
			freeNormReg(val)
			# printNormReg()
			# print("Freeing reg ",val)
			return(val1,0)
		else:
			val = getFloatReg()
			printhelper("div.s $f{0}, $f{1}, $f{2}".format(val,r0[0],r1[0]),1)
			freeFloatReg(r0[0])
			freeFloatReg(r1[0])
			val1 = getFloatReg()
			printhelper("mov.s $f{0}, $f{1}".format(val1,val),1)
			freeFloatReg(val)
			return(val1,1)

	if ast.Type == "LE":
		if ast.l[0].isSimple():
			if ast.l[1].isSimple():
				r0 = ASTtoAssembly(ast.l[0],funcinfo)
				r1 = ASTtoAssembly(ast.l[1],funcinfo)
			else:
				r1 = ASTtoAssembly(ast.l[1],funcinfo)
				r0 = ASTtoAssembly(ast.l[0],funcinfo)
		else:
			r0 = ASTtoAssembly(ast.l[0],funcinfo)
			r1 = ASTtoAssembly(ast.l[1],funcinfo)
		if(r0[1]==0):
			val = getNormReg()
			printhelper("sle $s{0}, $s{1}, $s{2}".format(val,r0[0],r1[0]),1)
			freeNormReg(r0[0])
			freeNormReg(r1[0])
			# printNormReg()
			val1 = getNormReg()
			printhelper("move $s{0}, $s{1}".format(val1,val),1)
			freeNormReg(val)
			# printNormReg()
			# print("Freeing reg ",val)
			return(val1,0)
		else:
			# val = getFloatReg()
			printhelper("c.le.s $f{0}, $f{1}".format(r0[0],r1[0]),1)
			freeFloatReg(r0[0])
			freeFloatReg(r1[0])
			printhelper("bc1f L_CondFalse_{0}".format(condfalsenum),1)
			cond1 = getNormReg()
			printhelper("li $s{0}, 1".format(cond1),1)
			printhelper("j L_CondEnd_{0}".format(condendnum),1)
			printhelper("L_CondFalse_{0}:".format(condfalsenum),0)
			printhelper("li $s{0}, 0".format(cond1),1)
			printhelper("L_CondEnd_{0}:".format(condendnum),0)
			condfalsenum +=1
			condendnum += 1
			cond2 = getNormReg()
			printhelper("move $s{0}, $s{1}".format(cond2,cond1),1)
			freeNormReg(cond1)
			return (cond2,0)

	if ast.Type == "LT":
		if ast.l[0].isSimple():
			if ast.l[1].isSimple():
				r0 = ASTtoAssembly(ast.l[0],funcinfo)
				r1 = ASTtoAssembly(ast.l[1],funcinfo)
			else:
				r1 = ASTtoAssembly(ast.l[1],funcinfo)
				r0 = ASTtoAssembly(ast.l[0],funcinfo)
		else:
			r0 = ASTtoAssembly(ast.l[0],funcinfo)
			r1 = ASTtoAssembly(ast.l[1],funcinfo)
		if(r0[1]==0):
			val = getNormReg()
			printhelper("slt $s{0}, $s{1}, $s{2}".format(val,r0[0],r1[0]),1)
			freeNormReg(r0[0])
			freeNormReg(r1[0])
			# printNormReg()
			val1 = getNormReg()
			printhelper("move $s{0}, $s{1}".format(val1,val),1)
			freeNormReg(val)
			# printNormReg()
			# print("Freeing reg ",val)
			return(val1,0)
		else:
			# val = getFloatReg()
			printhelper("c.lt.s $f{0}, $f{1}".format(r0[0],r1[0]),1)
			freeFloatReg(r0[0])
			freeFloatReg(r1[0])
			printhelper("bc1f L_CondFalse_{0}".format(condfalsenum),1)
			cond1 = getNormReg()
			printhelper("li $s{0}, 1".format(cond1),1)
			printhelper("j L_CondEnd_{0}".format(condendnum),1)
			printhelper("L_CondFalse_{0}:".format(condfalsenum),0)
			printhelper("li $s{0}, 0".format(cond1),1)
			printhelper("L_CondEnd_{0}:".format(condendnum),0)
			condfalsenum +=1
			condendnum += 1
			cond2 = getNormReg()
			printhelper("move $s{0}, $s{1}".format(cond2,cond1),1)
			freeNormReg(cond1)
			return (cond2,0)

	if ast.Type == "EQ":
		if ast.l[0].isSimple():
			if ast.l[1].isSimple():
				r0 = ASTtoAssembly(ast.l[0],funcinfo)
				r1 = ASTtoAssembly(ast.l[1],funcinfo)
			else:
				r1 = ASTtoAssembly(ast.l[1],funcinfo)
				r0 = ASTtoAssembly(ast.l[0],funcinfo)
		else:
			r0 = ASTtoAssembly(ast.l[0],funcinfo)
			r1 = ASTtoAssembly(ast.l[1],funcinfo)
		if(r0[1]==0):
			val = getNormReg()
			printhelper("seq $s{0}, $s{1}, $s{2}".format(val,r0[0],r1[0]),1)
			freeNormReg(r0[0])
			freeNormReg(r1[0])
			# printNormReg()
			val1 = getNormReg()
			printhelper("move $s{0}, $s{1}".format(val1,val),1)
			freeNormReg(val)
			# printNormReg()
			# print("Freeing reg ",val)
			return(val1,0)
		else:
			# val = getFloatReg()
			printhelper("c.eq.s $f{0}, $f{1}".format(r0[0],r1[0]),1)
			freeFloatReg(r0[0])
			freeFloatReg(r1[0])
			printhelper("bc1f L_CondFalse_{0}".format(condfalsenum),1)
			cond1 = getNormReg()
			printhelper("li $s{0}, 1".format(cond1),1)
			printhelper("j L_CondEnd_{0}".format(condendnum),1)
			printhelper("L_CondFalse_{0}:".format(condfalsenum),0)
			printhelper("li $s{0}, 0".format(cond1),1)
			printhelper("L_CondEnd_{0}:".format(condendnum),0)
			condfalsenum +=1
			condendnum += 1
			cond2 = getNormReg()
			printhelper("move $s{0}, $s{1}".format(cond2,cond1),1)
			freeNormReg(cond1)
			return (cond2,0)

	if ast.Type == "AND":
		r0 = ASTtoAssembly(ast.l[0],funcinfo)
		r1 = ASTtoAssembly(ast.l[1],funcinfo)
		val = getNormReg()
		printhelper("and $s{0}, $s{1}, $s{2}".format(val,r0[0],r1[0]),1)
		freeNormReg(r0[0])
		freeNormReg(r1[0])
		# printNormReg()
		val1 = getNormReg()
		printhelper("move $s{0}, $s{1}".format(val1,val),1)
		freeNormReg(val)
		# printNormReg()
		# print("Freeing reg ",val)
		return(val1,0)
	if ast.Type == "OR":
		r0 = ASTtoAssembly(ast.l[0],funcinfo)
		r1 = ASTtoAssembly(ast.l[1],funcinfo)
		val = getNormReg()
		printhelper("or $s{0}, $s{1}, $s{2}".format(val,r0[0],r1[0]),1)
		freeNormReg(r0[0])
		freeNormReg(r1[0])
		# printNormReg()
		val1 = getNormReg()
		printhelper("move $s{0}, $s{1}".format(val1,val),1)
		freeNormReg(val)
		# printNormReg()
		# print("Freeing reg ",val)
		return(val1,0)

	if ast.Type == "NE":
		if ast.l[0].isSimple():
			if ast.l[1].isSimple():
				r0 = ASTtoAssembly(ast.l[0],funcinfo)
				r1 = ASTtoAssembly(ast.l[1],funcinfo)
			else:
				r1 = ASTtoAssembly(ast.l[1],funcinfo)
				r0 = ASTtoAssembly(ast.l[0],funcinfo)
		else:
			r0 = ASTtoAssembly(ast.l[0],funcinfo)
			r1 = ASTtoAssembly(ast.l[1],funcinfo)
		if(r0[1]==0):
			val = getNormReg()
			printhelper("sne $s{0}, $s{1}, $s{2}".format(val,r0[0],r1[0]),1)
			freeNormReg(r0[0])
			freeNormReg(r1[0])
			# printNormReg()
			val1 = getNormReg()
			printhelper("move $s{0}, $s{1}".format(val1,val),1)
			freeNormReg(val)
			# printNormReg()
			# print("Freeing reg ",val)
			return(val1,0)
		else:
			# val = getFloatReg()
			printhelper("c.eq.s $f{0}, $f{1}".format(r0[0],r1[0]),1)
			freeFloatReg(r0[0])
			freeFloatReg(r1[0])
			printhelper("bc1f L_CondTrue_{0}".format(condfalsenum),1)
			cond1 = getNormReg()
			printhelper("li $s{0}, 0".format(cond1),1)
			printhelper("j L_CondEnd_{0}".format(condendnum),1)
			printhelper("L_CondTrue_{0}:".format(condfalsenum),0)
			printhelper("li $s{0}, 1".format(cond1),1)
			printhelper("L_CondEnd_{0}:".format(condendnum),0)
			condfalsenum +=1
			condendnum += 1
			cond2 = getNormReg()
			printhelper("move $s{0}, $s{1}".format(cond2,cond1),1)
			freeNormReg(cond1)
			return (cond2,0)

	if ast.Type == "GE":
		if ast.l[0].isSimple():
			if ast.l[1].isSimple():
				r0 = ASTtoAssembly(ast.l[0],funcinfo)
				r1 = ASTtoAssembly(ast.l[1],funcinfo)
			else:
				r1 = ASTtoAssembly(ast.l[1],funcinfo)
				r0 = ASTtoAssembly(ast.l[0],funcinfo)
		else:
			r0 = ASTtoAssembly(ast.l[0],funcinfo)
			r1 = ASTtoAssembly(ast.l[1],funcinfo)
		if(r0[1]==0):
			val = getNormReg()
			printhelper("sle $s{0}, $s{1}, $s{2}".format(val,r1[0],r0[0]),1)
			freeNormReg(r0[0])
			freeNormReg(r1[0])
			# printNormReg()
			val1 = getNormReg()
			printhelper("move $s{0}, $s{1}".format(val1,val),1)
			freeNormReg(val)
			# printNormReg()
			# print("Freeing reg ",val)
			return(val1,0)
		else:
			# val = getFloatReg()
			printhelper("c.le.s $f{0}, $f{1}".format(r1[0],r0[0]),1)
			freeFloatReg(r0[0])
			freeFloatReg(r1[0])
			printhelper("bc1f L_CondFalse_{0}".format(condfalsenum),1)
			cond1 = getNormReg()
			printhelper("li $s{0}, 1".format(cond1),1)
			printhelper("j L_CondEnd_{0}".format(condendnum),1)
			printhelper("L_CondFalse_{0}:".format(condfalsenum),0)
			printhelper("li $s{0}, 0".format(cond1),1)
			printhelper("L_CondEnd_{0}:".format(condendnum),0)
			condfalsenum +=1
			condendnum += 1
			cond2 = getNormReg()
			printhelper("move $s{0}, $s{1}".format(cond2,cond1),1)
			freeNormReg(cond1)
			return (cond2,0)

	if ast.Type == "GT":
		if ast.l[0].isSimple():
			if ast.l[1].isSimple():
				r0 = ASTtoAssembly(ast.l[0],funcinfo)
				r1 = ASTtoAssembly(ast.l[1],funcinfo)
			else:
				r1 = ASTtoAssembly(ast.l[1],funcinfo)
				r0 = ASTtoAssembly(ast.l[0],funcinfo)
		else:
			r0 = ASTtoAssembly(ast.l[0],funcinfo)
			r1 = ASTtoAssembly(ast.l[1],funcinfo)
		if(r0[1]==0):
			val = getNormReg()
			printhelper("slt $s{0}, $s{1}, $s{2}".format(val,r1[0],r0[0]),1)
			freeNormReg(r0[0])
			freeNormReg(r1[0])
			# printNormReg()
			val1 = getNormReg()
			printhelper("move $s{0}, $s{1}".format(val1,val),1)
			freeNormReg(val)
			# printNormReg()
			# print("Freeing reg ",val)
			return(val1,0)
		else:
			# val = getFloatReg()
			printhelper("c.lt.s $f{0}, $f{1}".format(r1[0],r0[0]),1)
			freeFloatReg(r0[0])
			freeFloatReg(r1[0])
			printhelper("bc1f L_CondFalse_{0}".format(condfalsenum),1)
			cond1 = getNormReg()
			printhelper("li $s{0}, 1".format(cond1),1)
			printhelper("j L_CondEnd_{0}".format(condendnum),1)
			printhelper("L_CondFalse_{0}:".format(condfalsenum),0)
			printhelper("li $s{0}, 0".format(cond1),1)
			printhelper("L_CondEnd_{0}:".format(condendnum),0)
			condfalsenum +=1
			condendnum += 1
			cond2 = getNormReg()
			printhelper("move $s{0}, $s{1}".format(cond2,cond1),1)
			freeNormReg(cond1)
			return (cond2,0)

	if(ast.Type == "ADDR"):

		curr = ast.l[0]
		table = globalSym.funcTable[funcinfo]
		if(curr.Name in table[2].varTable):
			entry = table[2].varTable[curr.Name]
			offset = entry[2]
			newt = getNormReg()
			printhelper("addi $s{0}, $sp, {1}".format(newt,offset+4),1)
			return (newt,0)

		else:
			entry = globalSym.varTable[curr.Name]
			newt = getNormReg()
			printhelper("la $s{0}, global_{1}".format(newt,curr.Name),1)
			return (newt,0)

	if(ast.Type == "NOT"):
		child = ASTtoAssembly(ast.l[0],funcinfo)
		newt = getNormReg()
		printhelper("xori $s{0}, $s{1}, 1".format(newt,child[0]),1)
		freeNormReg(child[0])
		new2 = getNormReg()
		printhelper("move $s{0}, $s{1}".format(new2,newt),1)
		freeNormReg(newt)
		return (new2,0)

	if(ast.Type == "UMINUS"):
		child = ASTtoAssembly(ast.l[0],funcinfo)
		newt = getNormReg()
		printhelper("negu $s{0}, $s{1}".format(newt,child[0]),1)
		freeNormReg(child[0])
		new2 = getNormReg()
		printhelper("move $s{0}, $s{1}".format(new2,newt),1)
		freeNormReg(newt)
		return (new2,0)


	if(ast.Type == "ASGN"):
		r1 = ASTtoAssembly(ast.l[1],funcinfo)
		curr = ast.l[0]
		count = 0
		while(curr.Type!="VAR"):
			curr = curr.l[0]
			count+=1
		if count==0:
			table = globalSym.funcTable[funcinfo]
			if curr.Name in table[2].varTable:
				entry = table[2].varTable[curr.Name]
				offset = entry[2]
				printhelper("sw $s{0}, {1}($sp)".format(r1[0],offset+4),1)
				freeNormReg(r1[0])
			else:
				printhelper("sw $s{0}, global_{1}".format(r1[0],curr.Name),1)
				freeNormReg(r1[0])


		else:
			table = globalSym.funcTable[funcinfo]
			if curr.Name in table[2].varTable:
				entry = table[2].varTable[curr.Name]
				offset = entry[2]
				val = getNormReg()
				printhelper("lw $s{0}, {1}($sp)".format(val,offset+4),1)
				temp_reg = val
			elif curr.Name in globalSym.varTable:
				entry = globalSym.varTable[curr.Name]
				val = getNormReg()
				printhelper("lw $s{0}, global_{1}".format(val,curr.Name),1)
				temp_reg = val
			for i in range(count - 1):
				val = getNormReg()
				printhelper("lw $s{0}, 0($s{1})".format(val,temp_reg),1)
				freeNormReg(temp_reg)
				temp_reg = val
			if r1[1] == 0:
				printhelper("sw $s{0}, 0($s{1})".format(r1[0],temp_reg),1)
				freeNormReg(temp_reg)
				freeNormReg(r1[0])
				return (0,0)
			else:
				printhelper("s.s $f{0}, 0($s{1})".format(r1[0],temp_reg),1)
				freeNormReg(temp_reg)
				freeFloatReg(r1[0])
				return (0,1)

	elif(ast.Type == "DEREF"):
		curr = ast
		count = 0
		while(curr.Type!="VAR"):
			curr = curr.l[0]
			count+=1
		r0 = ASTtoAssembly(curr,funcinfo)		
		temp_reg = r0[0]
		for i in range(count - 1):
			val = getNormReg()
			printhelper("lw $s{0}, 0($s{1})".format(val,temp_reg),1)
			freeNormReg(temp_reg)
			temp_reg = val

		table = globalSym.funcTable[funcinfo]
		if curr.Name in table[2].varTable:
			entry = table[2].varTable[curr.Name]
		else:
			entry = globalSym.varTable[curr.Name]
		# print("Entry ",entry[2],count)
		if entry[0] == "int":
			val = getNormReg()
			printhelper("lw $s{0}, 0($s{1})".format(val,temp_reg),1)
			freeNormReg(temp_reg)
			return (val,0)
		elif entry[1]>count:
			val = getNormReg()
			printhelper("lw $s{0}, 0($s{1})".format(val,temp_reg),1)
			freeNormReg(temp_reg)
			return (val,1)
		else:
			val = getFloatReg()
			printhelper("l.s $f{0}, 0($s{1})".format(val,temp_reg),1)
			freeNormReg(temp_reg)
			return (val,1)


	elif(ast.Type == "CONST"):
		if ast.Name == "int":
			val = getNormReg()
			printhelper("li $s{0}, {1}".format(val,ast.l[0]),1)
			return (val,0)
		elif ast.Name == "float":
			val = getFloatReg()
			printhelper("li.s $f{0}, {1}".format(val,ast.l[0]),1)
			return (val,1)

	elif(ast.Type == "VAR"):
		table = globalSym.funcTable[funcinfo]
		if ast.Name in table[2].varTable:
			entry = table[2].varTable[ast.Name]
			offset = entry[2]
			if entry[3]==0:
				if entry[0]=="int":
					if entry[1]==0:
						val = getNormReg()
						printhelper("lw $s{0}, {1}($sp)".format(val,4+offset),1)
						return (val,0)
					else:
						val = getNormReg()
						printhelper("lw $s{0}, {1}($sp)".format(val,4+offset),1)
						return (val,0)
				else:
					if entry[1]==0:
						val = getFloatReg()
						printhelper("l.s $f{0}, {1}($sp)".format(val,4+offset),1)
						return (val,1)
					else:
						val = getNormReg()
						printhelper("lw $s{0}, {1}($sp)".format(val,4+offset),1)
						return (val,0,1)
			else:
				if entry[0]=="int":
					val = getNormReg()
					printhelper("lw $s{0}, {1}($sp)".format(val,table[2].size+12+offset),1)
					return (val,0)
				elif entry[1]>0:
					val = getNormReg()
					printhelper("lw $s{0}, {1}($sp)".format(val,table[2].size+12+offset),1)
					return (val,1)
				else:
					val = getFloatReg()
					printhelper("lw $f{0}, {1}($sp)".format(val,table[2].size+12+offset),1)
					return (val,1)
		elif ast.Name in globalSym.varTable:
			entry = globalSym.varTable[ast.Name]
			if entry[0] == "int" or entry[1]>0:
				val = getNormReg()
				printhelper("lw $s{0}, global_{1}".format(val,ast.Name),1)
				return (val,0)
			else:
				val = getFloatReg()
				printhelper("lw $f{0}, global_{1}".format(val,ast.Name),1)
				return (val,1)

	elif(ast.Type == "FCALL"):
		arg_ast = ast.l[0]
		len1 = len(arg_ast.l)
		t = (ast.Name,ast.funcstr)
		entry = globalSym.funcTable[t]
		table = entry[2]
		total_size = table.paramsize
		offset = entry[3]
		flag = [0]*len1

		for i in range(0,len1):
			if(arg_ast.l[i].Type in ["VAR","DEREF","CONST"]):
				pass
			else:
				r = ASTtoAssembly(arg_ast.l[i],funcinfo)
				flag[i] = r

		printhelper("# setting up activation record for called function",1)

		for i in range(0,len1):
			if flag[i] == 0:
				r = ASTtoAssembly(arg_ast.l[i],funcinfo)
			else:
				r = flag[i]

			if r[1]==0:
				if i==len1-1:
					printhelper("sw $s{0}, {1}($sp)".format(r[0],0),1)
				else:
					printhelper("sw $s{0}, {1}($sp)".format(r[0],-total_size+offset[i+1]-offset[i]),1)
				freeNormReg(r[0])
			else:
				if i==len1-1:
					printhelper("s.s $f{0}, {1}($sp)".format(r[0],0),1)
				else:
					printhelper("s.s $f{0}, {1}($sp)".format(r[0],-total_size+offset[i+1]-offset[i]),1)
				freeFloatReg(r[0])
		printhelper("sub $sp, $sp, {0}".format(total_size),1)
		printhelper("jal {0} # function call".format(ast.Name),1)
		printhelper("add $sp, $sp, {0} # destroying activation record of called function".format(total_size),1)
		if entry[0] == "void":
			pass
		elif entry[0] == "float":
			if entry[1] == 0:
				val = getFloatReg()
				printhelper("mov.s $f{0}, $f0 # using the return value of called function".format(val),1)
				return (val,1)
			else:
				val = getNormReg()
				printhelper("move $s{0}, $v1 # using the return value of called function".format(val),1)
				return (val,0)
		else:
			val = getNormReg()
			printhelper("move $s{0}, $v1 # using the return value of called function".format(val),1)
			return (val,0)

	elif(ast.Type == "RETURN"):
		entry = globalSym.funcTable[funcinfo]
		r = ASTtoAssembly(ast.l[0],funcinfo)
		if entry[0] == "float":
			if entry[1] == 0:
				printhelper("mov.s $f0, $f{0} # move return value to $f0".format(r[0]),1)
				freeFloatReg(r[0])
			else:
				printhelper("move $v1, $s{0} # move return value to $v1 ".format(r[0]),1)
				freeNormReg(r[0])
		else:
			printhelper("move $v1, $s{0} # move return value to $v1".format(r[0]),1)
			freeNormReg(r[0])

def p_masterprogram(p):
	"""
	master : program
	"""
	global declaration_error,is_error,globalSym
	p[0] = p[1]
	for i in p[0].l:
		globalSym.addEntry(i)
	for key, values in globalSym.funcTable.items():
		offset = 0
		for key1 in sorted(values[2].varTable):
			entry = values[2].varTable[key1]
			if entry[3]==0:
				if entry[0]=="float":
					if entry[1]==0:
						entry[2]=offset
						offset+=8
					else:
						entry[2]=offset
						offset+=4
				else:
					entry[2]=offset
					offset+=4
	globalSym.printTable()
	if(declaration_error):
		print(declaration_error_string)

		is_error = 1
	else :
		output_f1 = str(sys.argv[1]) + ".ast1"
		output_f2 = str(sys.argv[1]) + ".cfg1"
		output_f3 = str(sys.argv[1]) + ".sym1"
		output_f4 = str(sys.argv[1]) + ".s1"
		oldstdout = sys.stdout
		sys.stdout = open(output_f1,'w+')		
		p[0].printit(0)
		sys.stdout = open(output_f2,'w+')
		cfg_list = printCFG(p[0])
		sys.stdout = open(output_f3,'w+')
		printSymbolTable()
		sys.stdout = open(output_f4,'w+')
		printAssembly(cfg_list)
		sys.stdout.close()
		sys.stdout = oldstdout



def p_program(p):
	""" 
	program : function 
				| function program
				| declaration program
	"""
	global assignment_error, assignment_error_line, is_error

	if(assignment_error):
		is_error = 1
		if p:

			print("Syntax error at line no '{0}' , assignment error".format(assignment_error_line))
		else:
			print("Syntax error at EOF")
		assignment_error = 0
	else:
		if len(p) == 2:
			p[0] = AST("PROG","",[p[1]])
		else:
			if p[1].Type == "DECL":
				if(not p[2]):
					# p[0] = [p[1]]
					p[0] = AST("PROG","",[])
					p[0].appendchild(p[1])
				else:
					p[0] = p[2]
					p[0].appendchild(p[1])
			elif p[1].Type == "FUNC":
				p[0] = p[2]
				p[0].appendchild(p[1])

def p_program1(p):
	"""
	program : prototype program
	"""
	global assignment_error
	if(assignment_error):
		is_error = 1
		if p:
			print("Syntax error at line no '{0}' , assignment error".format(assignment_error_line))
		else:
			print("Syntax error at EOF")
		assignment_error = 0
	else:
		if(not p[2]):
			p[0] = AST("PROG","",[])
			p[0].appendchild(p[1])
		else:
			p[0] = p[2]
			p[0].appendchild(p[1])


def p_prototype(p):
	"""
	prototype : TYPE NAME LPAREN paramlist RPAREN SEMICOLON
	"""
	if(len(p)==7):
		p[0] = AST("PROTO",p[2],[p[1],p[4],0])
	else:
		p[0] = AST("PROTO",p[3],[p[1],p[5],p[2]])

def p_prototype_2(p):
	"""
	prototype : TYPE specialvar LPAREN paramlist RPAREN SEMICOLON
	"""
	if(len(p)==7):
		p[0] = AST("PROTO",p[2][0],[p[1],p[4],p[2][1]])
	else:
		p[0] = AST("PROTO",p[3],[p[1],p[5],p[2]])
	# print(p[1],p[2],p[4])
def is_constant(a):
	print(a)
	if a.Type == "FCALL":
		return False
	if a.Type == "CONST":
		return True
	elif(a.Type == "VAR"):
		return False
	elif(not a.l):
		return True
	else:
		return functools.reduce((lambda x,y : x and y) ,list(map(lambda l : is_constant(l),a.l)))

def p_function_stars(p):
	"""
	allthestars : TIMES 
				| TIMES allthestars
	"""
	if(len(p)==2):
		p[0] = 1
	else:
		p[0] = p[2]
		p[0]+= 1

def is_valid_asgn(a1,a2):
	# print("This is ",a2.Type)
	
	if a1.Type == "VAR":
		if(is_constant(a2)):
			return False
		else:
			return True
	else:
		return True

def p_function(p):
	"""
	function : TYPE NAME LPAREN paramlist RPAREN LBRACE fbody RBRACE
	"""
	p[0] = AST("FUNC",p[2],[p[1],p[4],p[7],0])

def p_function_2(p):
	"""
	function : TYPE specialvar LPAREN paramlist RPAREN LBRACE fbody RBRACE
	"""
	p[0] = AST("FUNC",p[2][0],[p[1],p[4],p[7],p[2][1]])


def p_paramlist(p):
	"""
	paramlist : 
			| TYPE NAME paramlist2
			| TYPE specialvar paramlist2
	"""
	if len(p)==1:
		p[0] = []
	else:
		
		p[0] = p[3]
		p[0].append([p[1],p[2]])
		p[0].reverse()


def p_paramlist2(p):
	"""
	paramlist2 : 
			|  COMMA TYPE NAME paramlist2
			|  COMMA TYPE specialvar paramlist2
	"""
	if len(p)==1:
		p[0] = []
	else:
		
		p[0] = p[4]
		p[0].append([p[2],p[3]])
		# print("p[3]2[32]4[2]4[",p[0])

def p_fbody(p):
	"""
	fbody : allstatement fbody
			| 
	"""
	if(len(p)==1):
		p[0] = AST("BLANKBODY","",[])
	if(len(p)==2):
		p[0] = [p[1]]
		p[0] = AST("BODY","",[p[1]])
	elif(len(p)==3):
		if(not p[2]):
			p[0] = [p[1]]
			p[0] = AST("BODY","",[p[1]])
		
		elif(p[2].Type=="BLANKBODY"):
			p[0] = [p[1]]
			p[0] = AST("BODY","",[p[1]])
		else:
			# print("adding ",p[1]," to ",p[2])
			p[0] = p[2]
			# p[0].append(p[1])
			p[0].appendchild(p[1])

def p_allstatement_expr(p):
	"""
	allstatement : statement
				| unmatchedstatement
	"""
	p[0] = p[1]

def p_statement_expr(p):
	"""
	statement : assignment
			| declaration
			| whileblock
			| ifblock
			| returnstatement
			| functioncall SEMICOLON
	"""
	p[0] = p[1]

def p_return_statement(p):
	"""
	returnstatement : RETURN expression SEMICOLON
	"""
	p[0] = AST("RETURN", "", [p[2]])

def p_return_statement_2(p):
	"""
	returnstatement : RETURN SEMICOLON
	"""
	p[0] = AST("RETURN", "", ["EMPTYRETURN"])

def p_function_call(p):
	"""
	functioncall : NAME LPAREN arguments RPAREN
	"""
	# newast = AST("DECL", "", [p[3]])
	p[0] = AST("FCALL", p[1], [p[3],0])
	# p[0].funcstr = makestring1(p[0].l[0])


def p_function_arguments(p):
	"""
	arguments : expression 
				| expression COMMA arguments
	"""
	if(len(p)==2):
		p[0] = AST("ARGUMENTS","",[p[1]])
	else:
		p[0] = p[3]
		p[0].appendchild(p[1])

def p_empty_statement(p):
	"""
	statement : SEMICOLON
	"""
	p[0] = AST("BLANKBODY","",[])

def p_unmatchedstatement_expr1(p):
	"""
	unmatchedstatement : IF LPAREN conditional RPAREN allstatement
				| IF LPAREN conditional RPAREN statement ELSE unmatchedstatement
				| IF LPAREN conditional RPAREN LBRACE fbody RBRACE ELSE unmatchedstatement
	"""
	if len(p) == 6:
		p[0] = AST("IF","",[p[3],p[5]])
	elif len(p) == 10:
		p[0] = AST("ITE","",[p[3],p[6],p[9]])
	else:
		p[0] = AST("ITE","",[p[3],p[5],p[7]])

def p_unmatchedstatement_expr2(p):
	"""
	unmatchedstatement : IF LPAREN conditional RPAREN LBRACE fbody RBRACE
	"""
	p[0] = AST("IF","",[p[3],p[6]])

def p_ifblock1(p):
	"""
	ifblock : IF LPAREN conditional RPAREN statement ELSE statement
			| IF LPAREN conditional RPAREN statement ELSE LBRACE fbody RBRACE
			| IF LPAREN conditional RPAREN LBRACE fbody RBRACE ELSE LBRACE fbody RBRACE
	"""
	if len(p) == 8:
		p[0] = AST("ITE","",[p[3],p[5],p[7]])
	elif len(p) == 10:
		p[0] = AST("ITE","",[p[3],p[5],p[8]])
	else:
		p[0] = AST("ITE","",[p[3],p[6],p[10]])

def p_ifblock2(p):
	"""
	ifblock : IF LPAREN conditional RPAREN LBRACE fbody RBRACE ELSE statement
	"""
	p[0] = AST("ITE","",[p[3],p[6],p[9]])
def p_while(p):
	"""
	whileblock : WHILE LPAREN conditional RPAREN LBRACE fbody RBRACE
	"""
	p[0] = AST("WHILE","",[p[3],p[6]])

def p_conditional1(p):
	"""
	conditional : LPAREN conditional RPAREN
	"""
	p[0] = p[2]

def p_conditional(p):
	"""
	conditional : conditionbase
				| NOT LPAREN conditional RPAREN
				| conditional LESSTHANEQ conditional
				| conditional GREATERTHANEQ conditional
				| conditional UNEQUAL conditional
				| conditional EQUALCHECK conditional
				| conditional LESSTHAN conditional
				| conditional GREATERTHAN conditional
				| conditional ANDOPERATOR conditional
				| conditional OROPERATOR conditional
	"""
	if len(p)==2:
		p[0] = p[1]
	elif len(p)==5:
		p[0] = AST("NOT","",[p[3]])	
	else:
		if p[2] == '<=':
			p[0] = AST("LE","",[p[1],p[3]])
		elif p[2] == '>=':
			p[0] = AST("GE","",[p[1],p[3]])
		elif p[2] == '!=':
			p[0] = AST("NE","",[p[1],p[3]])
		elif p[2] == '==':
			p[0] = AST("EQ","",[p[1],p[3]])
		elif p[2] == '<':
			p[0] = AST("LT","",[p[1],p[3]])
		elif p[2] == '>':
			p[0] = AST("GT","",[p[1],p[3]])
		elif p[2] == '&&':
			p[0] = AST("AND","",[p[1],p[3]])
		elif p[2] == '||':
			p[0] = AST("OR","",[p[1],p[3]])

def p_conditionbase(p):
	"""
	conditionbase : CS LESSTHANEQ CS
				| CS GREATERTHANEQ CS
				| CS UNEQUAL CS
				| CS EQUALCHECK CS
				| CS LESSTHAN CS
				| CS GREATERTHAN CS
	"""
	if len(p)==2:
		p[0] = p[1]
	else:
		if p[2] == '<=':
			p[0] = AST("LE","",[p[1],p[3]])
		elif p[2] == '>=':
			p[0] = AST("GE","",[p[1],p[3]])
		elif p[2] == '!=':
			p[0] = AST("NE","",[p[1],p[3]])
		elif p[2] == '==':
			p[0] = AST("EQ","",[p[1],p[3]])
		elif p[2] == '<':
			p[0] = AST("LT","",[p[1],p[3]])
		elif p[2] == '>':
			p[0] = AST("GT","",[p[1],p[3]])

def p_cs(p):
	"""
	CS : expression
		| NOT LPAREN expression RPAREN
	"""
	if len(p)==2:
		p[0] = p[1]
	else:
		p[0] = AST("NOT","",[p[3]])	
def p_declaration1(p):
	"""
		declaration : TYPE dlist1 SEMICOLON
	"""
	p[0] = AST("DECL","",[p[1],p[2]])
	# print("t_NAME returns ",p[2])
	# print(p[1],p[2])
def p_dlistname(p):
	"""
	dlist1 : NAME  
			| NAME COMMA dlist1
	"""
	global no_of_static_declarations
	no_of_static_declarations = no_of_static_declarations + 1

	if len(p) == 2:

		p[0] = [p[1]]
	else:
		p[0] = p[3]
		p[0].reverse()
		p[0].append(p[1])
		p[0].reverse()
		
def p_dlistpointer(p):
	"""
	dlist1 : specialvar
			| specialvar  COMMA dlist1  
	"""
	global no_of_pointer_declarations
	no_of_pointer_declarations = no_of_pointer_declarations + 1
	if len(p) == 2:
		p[0] = [p[1]]
	else:
		p[0] = p[3]
		p[0].reverse()
		p[0].append(p[1])
		p[0].reverse()

def p_specialvar1(p):
	"""
	specialvar : TIMES specialvar %prec VALOF
	"""
	p[0] = (p[2][0],p[2][1]+1)
def p_specialvar2(p):
	"""
	specialvar : TIMES NAME %prec VALOF
	"""
	p[0] = (p[2],1)
def p_assignment(p):
	"""
	assignment : assignment_base SEMICOLON
	"""

	global no_of_assignments
	p[0] = p[1]
	no_of_assignments = no_of_assignments + 1

def p_assignment_base_pointer(p):
	""" 
	assignment_base : TIMES pointervar EQUALS expression
			| NAME EQUALS expression 
	 """
	global assignment_error, assignment_error_line
	if len(p)==5:
		p[0] = ["ASGN",["DEREF",p[2]],p[4]]
		p[0] = AST("ASGN","",[AST("DEREF","",[p[2]]),p[4]])
	else:
		p[0] = ["ASGN",p[1],p[3]]
		a1 = AST("VAR",p[1],[])
		if(p[3].Type=="FCALL"):
			print("Ignoring")
			pass
		if(is_valid_asgn(a1,p[3])):
			pass
		else:
			assignment_error = 1
			# print("rongmodnovdngo")
			assignment_error_line = p.lexer.lineno
		p[0] = AST("ASGN","",[a1,p[3]])


		# p[0].printit(0)

def p_expression_fcall(p):
	"""
	expression : functioncall
	"""
	p[0] = p[1]

def p_expression1(p):
	"""
	expression : expression PLUS expression
				| expression MINUS expression
				| expression DIVIDE expression
	"""
	if p[2] == '+':
		p[0] = ["PLUS",p[1],p[3]]
		p[0] = AST("PLUS","",[p[1],p[3]])
	elif p[2] == '-':
		p[0] = ["MINUS",p[1],p[3]]
		p[0] = AST("MINUS","",[p[1],p[3]])
	elif p[2] == '*':
		p[0] = ["MUL",p[1],p[3]]
		p[0] = AST("MUL","",[p[1],p[3]])
	elif p[2] == '/':
		p[0] = ["DIVIDE",p[1],p[3]]
		p[0] = AST("DIV","",[p[1],p[3]])

def p_expression_mul(p):
	"""
	expression : expression TIMES expression
	"""
	if p[2] == '*':
		p[0] = ["MUL",p[1],p[3]]
		p[0] = AST("MUL","",[p[1],p[3]])

def p_expression_uminus(p):
	"""
	expression : MINUS expression %prec UMINUS
	"""
	p[0] = ["UMINUS",p[2]]
	p[0] = AST("UMINUS","",[p[2]])

def p_expression_paren(p):
	"""
	expression : LPAREN expression RPAREN
	"""
	p[0] = p[2]



def p_expression_base_number(p):
	"""
	expression : allnumbers
	"""
	# p[0] = ["CONST",p[1]]
	# print(p[1])
	p[0] = AST("CONST",p[1].Name,[p[1].l])

def p_allnumbers_float(p):
	"""
	allnumbers : FLOAT
	"""
	# print("taking float")
	p[0] = AST("CONST","float",p[1])

def p_allnumbers_int(p):
	"""
	allnumbers : NUMBER
	"""
	# print("taking int")
	p[0] = AST("CONST","int",p[1])	

def p_expression_base_pointer(p):
	"""
	expression : pointervar
	"""
	p[0] = p[1]
	# p[0].printit(0)

def p_pointervar1(p):
	"""
	pointervar : TIMES pointervar %prec VALOF
	"""
	p[0] = AST("DEREF","",[p[2]])
def p_pointervar2(p):
	"""
	pointervar : ADDROF pointervar 
	"""
	p[0] = AST("ADDR","",[p[2]])
	# p[0].printit(0)
def p_pointervar3(p):
	"""
	pointervar : NAME
	"""
	p[0] = AST("VAR",p[1],[])
	# p[0].printit(0)


def p_error(p):
	global is_error
	is_error = 1
	if p:
		# print("iuenfoidnvoidnvoi")
		print("Syntax error at '{0}' line no  '{1}' ".format(p.value,p.lexer.lineno))
	else:
		print("Syntax error at EOF")

def process(data):
	lex.lex()
	yacc.yacc(debug = 1)
	yacc.parse(data)

if __name__ == "__main__":
	filename = str(sys.argv[1])
	with open(filename,'r') as f:
		data = f.read()
	process(data)
	if(is_error==0):
		# pass
		print("Successfully parsed")
