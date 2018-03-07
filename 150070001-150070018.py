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
counter1 = 1
counter2 = 0
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

	def getcode(self):
		if self.Type == "PLUS":
			return self.l[0].getcode() + "+" + self.l[1].getcode()
		elif self.Type == "MINUS":
			return self.l[0].getcode() + "-" + self.l[1].getcode()
		elif self.Type == "MUL":
			return self.l[0].getcode() + "*" + self.l[1].getcode()
		elif self.Type == "DIV":
			return self.l[0].getcode() + "/" + self.l[1].getcode()
		elif self.Type == "ASGN":
			return self.l[0].getcode() + "=" + self.l[1].getcode()
		elif self.Type == "LE":
			return self.l[0].getcode() + "<=" + self.l[1].getcode()
		elif self.Type == "GE":
			return self.l[0].getcode() + ">=" + self.l[1].getcode()
		elif self.Type == "LT":
			return self.l[0].getcode() + "<" + self.l[1].getcode()
		elif self.Type == "GT":
			return self.l[0].getcode() + ">" + self.l[1].getcode()
		elif self.Type == "EQ":
			return self.l[0].getcode() + "==" + self.l[1].getcode()
		elif self.Type == "NE":
			return self.l[0].getcode() + "!=" + self.l[1].getcode()
		elif self.Type == "AND":
			return self.l[0].getcode() + "&&" + self.l[1].getcode()
		elif self.Type == "OR":
			return self.l[0].getcode() + "||" + self.l[1].getcode()
		elif self.Type == "CONST":
			return str(self.Name)
		elif self.Type == "VAR":
			return str(self.Name)
		elif self.Type == "DEREF":
			return "*" + self.l[0].getcode()
		elif self.Type == "UMINUS":
			return "-" + self.l[0].getcode()
		elif self.Type == "ADDR":
			return "&" + self.l[0].getcode()
		elif self.Type == "NOT":
			return "!" + self.l[0].getcode()

	def isjump(self):
		if self.Type in ["IF","ITE","WHILE"]:
			return True
		return False

	def printCFG(self, statenumber):

		global counter1,counter2,previous
		if(self.Type == "FUNC"):
			if(not self.l):
				pass
			else:
				x = 1
				for j in range(len(self.l)-1,-1,-1):
					x = self.l[j].printCFG(x)
					if(j!=0):
						# print("")
						pass
		elif(self.Type == "IF"):
			previous = 1
			print("")
			print("<bb {0}>".format(statenumber))
			counter1 = counter1 + 1
			print("t{0} = ".format(counter2) + self.l[0].getcode())
			print("if(t{0}) goto <bb {1}>".format(counter2,counter1))
			print("else goto <bb {0}>".format(counter1))
			print("")
			counter2 = counter2 + 1
			self.l[1].printCFG(counter1)
			print("<bb {0}>".format(counter1))

		elif(self.Type == "ITE"):
			previous = 1
			print("")
			print("<bb {0}>".format(statenumber))
			statenumber = statenumber + 1
			counter1 = counter1 + 1
			print("t{0} = ".format(counter2) + self.l[0].getcode())
			print("if(t{0}) goto <bb {1}>".format(counter2,counter1))
			print("else goto <bb {0}>".format(counter1 + 1))
			counter2 = counter2 + 1
			# counter1 = counter1 + 2
			self.l[1].printCFG(counter1-2)
			previous = 1
			self.l[2].printCFG(counter1-1)

		else:
			if previous==1:
				print("")
				print("<bb {0}>".format(statenumber))
				counter1 = counter1 + 1
				print(self.getcode())
				previous = 0
				return statenumber + 1
			else:
				print(self.getcode())
				return statenumber

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
		p[6].printCFG(1)
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
