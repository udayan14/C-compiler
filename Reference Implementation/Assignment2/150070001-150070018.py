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
tokens = (
	'NUMBER',
	'TYPE',
	'SEMICOLON', 'EQUALS', 'COMMA',
	'LPAREN', 'RPAREN','LBRACE', 'RBRACE',
	'ADDROF',
	'NAME',
	'PLUS','MINUS','TIMES','DIVIDE',
	)

t_ignore = " \t"
t_SEMICOLON = ";"
t_COMMA = ","
t_EQUALS = "="
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ADDROF = r'&'
t_TIMES = r'\*'
t_PLUS = r'\+'
t_MINUS = r'-'
t_DIVIDE = r'/'

def t_TYPE(t):
	r'\bvoid\b | \bint\b'
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
	('left','PLUS','MINUS'),
	('left','TIMES','DIVIDE'),
	('right','VALOF'),
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

		elif(self.Type == "DEREF" or self.Type == "UMINUS" or self.Type == "ADDR"):
			printhelper(self.Type,i)
			printhelper("(",i)
			self.l[0].printit(i+1)
			printhelper(")",i)

		elif(self.Type == "PLUS" or self.Type == "MINUS" or self.Type == "MUL" or self.Type == "DIV" or self.Type == "ASGN"):
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
				for i in range(len(self.l)-1,-1,-1):
					self.l[i].printit(0)
					if(i!=0):
						# print("")
						pass




	def appendchild(self,ast):
		self.l.append(ast)

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
	global is_error
	# print(p[2])
	if str(p[2])=='main':
		main_found = 1
	if str(p[1]=='int'):
		void_return = 1
	# print(p[6][::-1])
	if(assignment_error or not main_found or not void_return):
		is_error = 1
		print("Main function not found || Return type of main is not void || Invalid Assignment")
	else:
		output_f = "Parser_ast_" + str(sys.argv[1]) + ".txt1"
		oldstdout = sys.stdout
		sys.stdout = open(output_f,'w')		
		p[6].printit(0)
		sys.stdout.close()
		sys.stdout = oldstdout

def p_fbody(p):
	"""
	fbody : statement
			| statement fbody
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

def p_statement_expr(p):
	"""
	statement : assignment
			| declaration
	"""
	p[0] = p[1]
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
	yacc.yacc()
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
