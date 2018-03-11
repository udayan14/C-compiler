#!/usr/bin/python3

import sys
import ply.lex as lex
import ply.yacc as yacc
import functools

no_of_pointer_declarations = 0
no_of_static_declarations = 0
no_of_assignments = 0
is_error = 0
main_found = 0
assignment_error = 0
return_error = 0
temp = 0
previous = 1
tokens = (
	'NUMBER',
	'TYPE',
	'SEMICOLON', 'EQUALS', 'COMMA',
	'LPAREN', 'RPAREN','LBRACE', 'RBRACE',
	'ANDOPERATOR','OROPERATOR','ADDROF',
	'NAME',
	'PLUS','MINUS','TIMES','DIVIDE',
	'WHILE','IF','ELSE',
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
	r'\bvoid\b | \bint\b'
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

getSymbol = {
	"PLUS" : "+" ,
	"MINUS": "-" ,
	"MUL"  : "*" ,
	"DIV"  : "/" ,
	"ASGN" : "=" ,
	"LE"   : "<=",
	"GE"   : ">=",
	"LT"   : "<" ,
	"GT"   : ">" ,
	"EQ"   : "==",
	"NE"   : "!=",
	"AND"  : "&&",
	"OR"   : "||",
}



class node:
		def __init__(self,Type,l):
			self.Type = Type
			self.l = l
			self.code = []
			self.num = -1
			self.num1 = -1
		def addCode(self,c):
			self.code.append(c)

class CFG:
	def __init__(self):
		self.end = node("End",[])		
		self.insertnode = node("Normal",[self.end])
		self.head = node("Start",[self.insertnode])

	def insert(self,ast):
		if(ast.Type == "FUNC"):
			if(not ast.l):
				pass
			else:
				for j in range(len(ast.l)-1,-1,-1):
					self.insert(ast.l[j])

		elif (not ast.isjump() and ast.Type!="DECL"):	
			a = ast.getcode()	
			if isinstance(a,str):
				self.insertnode.addCode([a])
			else:
				self.insertnode.addCode(a[0])
			
		elif (ast.Type == "ITE"):
			c_common = node("Normal",self.insertnode.l)
			c_true = node("Normal",[])
			c_false = node("Normal",[])
			c_if = node("ITE",[c_true,c_false,c_common])
			a = ast.l[0].getcode()	
			if isinstance(a,str):
				c_if.addCode([a])
				c_if.num1 = temp
			else:
				c_if.addCode(a[0])
				c_if.num1 = a[1]
			self.insertnode.l = [c_if]
			self.insertnode = c_true
			self.insert(ast.l[1])
			self.insertnode = c_false
			self.insert(ast.l[2])
			self.insertnode = c_common

		elif(ast.Type == "IF"):
			c_common = node("Normal",self.insertnode.l)
			c_true = node("Normal",[])
			c_if = node("IF",[c_true,c_common])
			a = ast.l[0].getcode()

			if isinstance(a,str):
				c_if.addCode([a])
				c_if.num1 = temp
			else:
				c_if.addCode(a[0])
				c_if.num1 = a[1]
			self.insertnode.l = [c_if]
			self.insertnode = c_true
			self.insert(ast.l[1])
			self.insertnode = c_common

		elif(ast.Type == "WHILE"):
			c_common = node("Normal",self.insertnode.l)
			c_true = node("Normal",[])
			c_while = node("WHILE",[c_true,c_common])
			a = ast.l[0].getcode()	
			if isinstance(a,str):
				c_while.addCode([a])
				c_while.num1 = temp
			else:
				c_while.addCode(a[0])
				c_while.num1 = a[1]
			self.insertnode.l = [c_while]
			self.insertnode = c_true
			self.insert(ast.l[1])
			self.insertnode = c_common

class AST:
	def __init__(self,Type,Name,l):
		self.Type = Type
		self.Name = Name
		self.l = l

	def printit(self,i):


		if(self.Type == "CONST"):
			printhelper(self.Type+"("+str(self.Name)+")",i)

		elif(self.Type == "VAR"):
			printhelper(self.Type+"("+str(self.Name)+")",i)

		elif(self.Type == "DEREF" or self.Type == "UMINUS" or self.Type == "ADDR" or self.Type == "NOT"):
			printhelper(self.Type,i)
			printhelper("(",i)
			self.l[0].printit(i+1)
			printhelper(")",i)

		elif(self.Type == "WHILE"):
			printhelper(self.Type+"(",i)
			# printhelper("(",i)
			self.l[0].printit(i+1)
			printhelper(",",i+1)
			self.l[1].printit(i+1)
			printhelper(")",i)

		elif(self.Type == "ITE"):
			printhelper("IF(",i)
			# printhelper("(",i)
			self.l[0].printit(i+1)
			printhelper(",",i+1)
			# printhelper("THEN",i)
			# printhelper("(",i)
			self.l[1].printit(i+1)
			# printhelper(")",i)
			printhelper(",",i+1)
			# printhelper("(",i)
			self.l[2].printit(i+1)
			printhelper(")",i)	

		elif(self.Type == "IF"):
			printhelper("IF"+"(",i)
			# printhelper("(",i)
			self.l[0].printit(i+1)
			# printhelper(")",i)
			printhelper(",",i+1)
			# printhelper("(",i)
			self.l[1].printit(i+1)
			printhelper(")",i)	

		elif(self.Type == "PLUS" or self.Type == "MINUS" or self.Type == "MUL" or self.Type == "DIV" or self.Type == "ASGN" or self.Type == "LE" or self.Type == "GE" or self.Type == "GT" or self.Type == "LT" or self.Type == "EQ" or self.Type == "NE" or self.Type == "AND" or self.Type == "OR"):
			printhelper(self.Type,i)
			printhelper("(",i)
			self.l[0].printit(i+1)
			printhelper(",",i+1)
			self.l[1].printit(i+1)
			printhelper(")",i)
			if(self.Type == "ASGN"):
				print("")

		elif(self.Type == "FUNC"):
			if(not self.l):
				pass
			else:
				for j in range(len(self.l)-1,-1,-1):
					self.l[j].printit(i)
					if(j!=0):
						# print("")
						pass

	def appendchild(self,ast):
		self.l.append(ast)

	def isSimple(self):
		if self.Type in ["CONST","VAR","DEREF","ADDR"]:
			return True
		elif self.Type in ["PLUS","MINUS","MUL","DIVIDE","AND","OR"]:
			return False
		elif self.Type in ["UMINUS","NOT"]:
			return self.l[0].isSimple()

	def getcode(self):
		global temp
		if self.Type in ["PLUS","MINUS","MUL","DIV","AND","OR","LE","GE","LT","GT","EQ","NE"]:
			if self.l[0].isSimple():
				if self.l[1].isSimple():
					l = ["t{0} = {1}{2}{3}".format(temp,self.l[0].getcode(),getSymbol[self.Type],self.l[1].getcode())]
					temp+=1
					return (l,temp-1)
				else:
					l1,t_val = self.l[1].getcode()
					s = "t{0} = {1}{2}t{3}".format(temp,self.l[0].getcode(),getSymbol[self.Type],t_val)
					temp+=1
					l1.append(s)
					return (l1,temp-1)
			else:
				if self.l[1].isSimple():
					l1,t_val = self.l[0].getcode()
					s = "t{0} = t{1}{2}{3}".format(temp,t_val,getSymbol[self.Type],self.l[1].getcode())
					temp+=1
					l1.append(s)
					return (l1,temp-1)
				else:
					l1,t_val1 = self.l[0].getcode()
					l2,t_val2 = self.l[1].getcode()
					s = "t{0} = t{1}{2}t{3}".format(temp,t_val1,getSymbol[self.Type],t_val2)
					temp+=1
					l = l1 + l2
					l.append(s)
					return(l,temp-1)
		elif self.Type == "ASGN":
			if self.l[1].isSimple():
				l = ["{0}{1}{2}".format(self.l[0].getcode(),getSymbol[self.Type],self.l[1].getcode())]				
				return (l,temp)
			else:
				l1,t_val1 = self.l[1].getcode()
				s = "{0}{1}t{2}".format(self.l[0].getcode(),getSymbol[self.Type],t_val1)				
				l1.append(s)
				return (l1,temp)
		elif self.Type == "CONST":
			return str(self.Name)
		elif self.Type == "VAR":
			return str(self.Name)
		elif self.Type == "DEREF":
			return "*" + self.l[0].getcode()
		elif self.Type == "ADDR":
			return "&" + self.l[0].getcode()
		elif self.Type == "UMINUS":
			if self.l[0].isSimple():
				return "-" + self.l[0].getcode()
			else:
				l1,t_val1 = self.l[0].getcode()
				s = "t{0} = -t{1}".format(temp,t_val1) 
				temp+=1
				l1.append(s)
				return (l1,temp-1)
		elif self.Type == "NOT":
			if self.l[0].isSimple():
				return "!" + self.l[0].getcode()
			else:
				l1,t_val1 = self.l[0].getcode()
				s = "t{0} = !t{1}".format(temp,t_val1) 
				temp+=1
				l1.append(s)
				return (l1,temp-1)


	def isjump(self):
		if self.Type in ["IF","ITE","WHILE"]:
			return True
		return False

def printCFG(ast):
	cfg = CFG()
	cfg.insert(ast)
	cleanup(cfg.head)
	giveNumbering(cfg.head,0)
	printCFGhelper(cfg.head,-1)

def cleanup(n):
	if n.Type == "ITE":
		c = n.l[2]
		if not c.code:
			if not c.l:
				n.l = n.l[0:2]
			else:
				n.l[2] = c.l[0]
		cleanup(n.l[0])
		cleanup(n.l[1])
	elif n.Type == "IF" or n.Type == "WHILE":
		c = n.l[1]
		if not c.code:
			if not c.l:
				n.l = n.l[0:1]
			else:
				n.l[1] = c.l[0]
		cleanup(n.l[0])
	elif not n.l:
		return
	else:
		for i in n.l:
			cleanup(i)

  

def printList(l): 
	if not l:
		return
	for i in l:
		print(i)

def giveNumbering(n,i):
	if n.Type in ["Start","Normal","End"]:
		n.num = i
		if n.l!=[]:
			i1 = giveNumbering(n.l[0],i+1)
			return i1
		return i+1
	elif n.Type == "ITE":
		n.num = i
		if(len(n.l)==3):
			i1 = giveNumbering(n.l[0],i+1)
			i2 = giveNumbering(n.l[1],i1)
			i3 = giveNumbering(n.l[2],i2)
			return i3
		else:
			i1 = giveNumbering(n.l[0],i+1)
			i2 = giveNumbering(n.l[1],i1)
			return i2
	elif n.Type == "IF" or n.Type == "WHILE":
		n.num = i
		if(len(n.l)==2):
			i1 = giveNumbering(n.l[0],i+1)
			i2 = giveNumbering(n.l[1],i1)
			return i2
		else:
			i1 = giveNumbering(n.l[0],i+1)
			return i1



def printCFGhelper(n1,nextstatenum):
	if n1.Type == "End":
		print("<bb {0}>".format(n1.num))
		print("End")
		pass
	elif n1.Type == "Start":
		printCFGhelper(n1.l[0],nextstatenum)


	elif n1.Type == "Normal":
		print("<bb {0}>".format(n1.num))
		# print("{0} has child {1}".format(n1.num,n1.l))	
		for c in n1.code:
			printList(c)
		if n1.l:			
			print("goto <bb {0}>".format(n1.num+1))
			print("")
			printCFGhelper(n1.l[0],nextstatenum)
		else:
			print("goto <bb {0}>".format(nextstatenum))
			print("")

	elif n1.Type == "ITE":
		print("<bb {0}>".format(n1.num))
		printList(n1.code[0])
		print("if (t{0}) goto <bb {1}>".format(n1.num1,n1.l[0].num))
		print("else goto <bb {0}>".format(n1.l[1].num))
		print("")
		if(len(n1.l)==3):
			printCFGhelper(n1.l[0],n1.l[2].num)
			printCFGhelper(n1.l[1],n1.l[2].num)		
			printCFGhelper(n1.l[2],nextstatenum)
	elif n1.Type == "IF":
		print("<bb {0}>".format(n1.num))
		printList(n1.code[0])
		print("if (t{0}) goto <bb {1}>".format(n1.num1,n1.l[0].num))
		print("else goto <bb {0}>".format(n1.l[1].num))
		print("")
		if(len(n1.l)==2):
			printCFGhelper(n1.l[0],n1.l[1].num)
			printCFGhelper(n1.l[1],nextstatenum)
	elif n1.Type == "WHILE":
		print("<bb {0}>".format(n1.num))			
		printList(n1.code[0])
		print("if (t{0}) goto <bb {1}>".format(n1.num1,n1.l[0].num))
		print("else goto <bb {0}>".format(n1.l[1].num))
		print("")
		if(len(n1.l)==2):
			printCFGhelper(n1.l[0],n1.num)
			printCFGhelper(n1.l[1],nextstatenum)
	
def printhelper(s,i):
	print("\t"*i + s)

def p_program(p):
	""" 
	program : function 
				| function program
	"""

def is_constant(a):
	if a.Type == "CONST":
		return True
	elif(a.Type == "VAR"):
		return False
	elif(not a.l):
		return True
	else:
		return functools.reduce((lambda x,y : x and y) ,list(map(lambda l : is_constant(l),a.l)))

def is_valid_asgn(a1,a2):
	if a1.Type == "VAR":
		if(is_constant(a2)):
			return False
		else:
			return True
	else:
		return True

def p_function(p):
	"""
	function : TYPE NAME LPAREN RPAREN LBRACE fbody RBRACE
	"""
	global main_found,assignment_error,return_error
	void_return = 0
	global is_error
	# print(p[2])
	if str(p[2])=='main':
		main_found = 1
	if str(p[1])=='void':
		void_return = 1
	# print(p[6][::-1])
	if(assignment_error):
		is_error = 1
		if p:
			print("Syntax error at line no  '{0}' , assignment error ".format(p.lexer.lineno))
		else:
			print("Syntax error at EOF")
		# print("Main function not found || Return type of main is not void || Invalid Assignment")
	elif(not main_found):
		is_error = 1
		print("Syntax error at line no  '{0}' , main not found".format(p.lexer.lineno))
	elif(not void_return):
		is_error = 1
		print("Syntax error at line no  '{0}' , return type of main function not void".format(p.lexer.lineno))
	else:
		output_f1 = str(sys.argv[1]) + ".ast1"
		output_f2 = str(sys.argv[1]) + ".cfg1"
		oldstdout = sys.stdout
		sys.stdout = open(output_f1,'w+')		
		p[6].printit(0)
		sys.stdout = open(output_f2,'w+')
		printCFG(p[6])
		sys.stdout.close()
		sys.stdout = oldstdout

def p_fbody(p):
	"""
	fbody : allstatement
			| allstatement fbody
	"""
	if(len(p)==2):
		p[0] = [p[1]]
		p[0] = AST("FUNC","",[p[1]])
	elif(len(p)==3):
		if(not p[2]):
			p[0] = [p[1]]
			p[0] = AST("FUNC","",[p[1]])
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
	"""
	p[0] = p[1]

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

def p_conditional(p):
	"""
	conditional : conditionbase
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
	p[0] = AST("DECL","",[])

def p_dlistname(p):
	"""
	dlist1 : NAME  
			| NAME COMMA dlist1
	"""
	global no_of_static_declarations
	no_of_static_declarations = no_of_static_declarations + 1
		
def p_dlistpointer(p):
	"""
	dlist1 : specialvar
			| specialvar  COMMA dlist1  
	"""
	global no_of_pointer_declarations
	no_of_pointer_declarations = no_of_pointer_declarations + 1

def p_specialvar(p):
	"""
	specialvar : TIMES specialvar %prec VALOF
				| TIMES NAME %prec VALOF
	"""

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
	global assignment_error
	if len(p)==5:
		p[0] = ["ASGN",["DEREF",p[2]],p[4]]
		p[0] = AST("ASGN","",[AST("DEREF","",[p[2]]),p[4]])
	else:
		p[0] = ["ASGN",p[1],p[3]]
		a1 = AST("VAR",p[1],[])
		if(is_valid_asgn(a1,p[3])):
			pass
		else:
			assignment_error = 1
		p[0] = AST("ASGN","",[a1,p[3]])


		# p[0].printit(0)
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
	expression : NUMBER
	"""
	p[0] = ["CONST",p[1]]
	p[0] = AST("CONST",p[1],[])
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
	p[0] = ["DEREF",p[2]]
	p[0] = AST("DEREF","",[p[2]])
def p_pointervar2(p):
	"""
	pointervar : ADDROF pointervar 
	"""
	p[0] = ["ADDR",p[2]]
	p[0] = AST("ADDR","",[p[2]])
	# p[0].printit(0)
def p_pointervar3(p):
	"""
	pointervar : NAME
	"""
	p[0] = ["VAR",p[1]]
	p[0] = AST("VAR",p[1],[])
	# p[0].printit(0)


def p_error(p):
	global is_error
	is_error = 1
	if p:
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
		# print(no_of_static_declarations)
		# print(no_of_pointer_declarations)
		# print(no_of_assignments)
