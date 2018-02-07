#!/usr/bin/python3

import sys
import ply.lex as lex
import ply.yacc as yacc

no_of_pointer_declarations = 0
no_of_static_declarations = 0
no_of_assignments = 0
is_error = 0
main_found = 0
tokens = (
	'NUMBER',
	'TYPE',
	'newline',
	'SEMICOLON', 'EQUALS', 'COMMA',
	'LPAREN', 'RPAREN','LBRACE', 'RBRACE',
	'ADDROF','VALOF',
	'NAME',
	'COMMENT',
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
t_VALOF = r'\*'
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
	('right','UMINUS'),
	('right','VALOF'),
	)


def p_program(p):
	""" 
	program : function 
				| function program
	"""

def p_function(p):
	"""
	function : TYPE NAME LPAREN RPAREN LBRACE fbody RBRACE
	"""
	global main_found
	# print(p[2])
	if str(p[2])=='main':
		main_found = 1
	print(p[6][::-1])
def p_fbody(p):
	"""
	fbody : statement
			| statement fbody
	"""
	if(len(p)==2):
		p[0] = [p[1]]
	elif(len(p)==3):
		if(not p[2]):
			p[0] = [p[1]]
		else:
			# print("adding ",p[1]," to ",p[2])
			p[0] = p[2]
			p[0].append(p[1])


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
	p[0] = ["DECL"]

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
	specialvar : VALOF specialvar
				| VALOF NAME
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
	assignment_base : VALOF pointervar EQUALS expression
			| NAME EQUALS expression 
	 """
	if len(p)==5:
		p[0] = ["ASGN",["DEREF",p[2]],p[4]]
	else:
		p[0] = ["ASGN",p[1],p[3]]

def p_expression1(p):
	"""
	expression : expression PLUS expression
				| expression MINUS expression
				| expression VALOF expression %prec TIMES 
				| expression DIVIDE expression
	"""
	if p[2] == '+':
		p[0] = ["PLUS",p[1],p[3]]
	elif p[2] == '-':
		p[0] = ["MINUS",p[1],p[3]]
	elif p[2] == '*':
		p[0] = ["MUL",p[1],p[3]]
	elif p[2] == '/':
		p[0] = ["DIVIDE",p[1],p[3]]



def p_expression_uminus(p):
	"""
	expression : MINUS expression %prec UMINUS
	"""
	p[0] = ["UMINUS",p[2]]

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
def p_expression_base_pointer(p):
	"""
	expression : pointervar
	"""
	p[0] = p[1]

def p_pointervar1(p):
	"""
	pointervar : VALOF pointervar
	"""
	p[0] = ["DEREF",p[2]]
def p_pointervar2(p):
	"""
	pointervar : ADDROF pointervar
	"""
	p[0] = ["ADDR",p[2]]
def p_pointervar3(p):
	"""
	pointervar : NAME
	"""
	p[0] = ["VAR",p[1]]



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
	data = sys.stdin.read()
	process(data)
	if(main_found==0):
		print("Program has no main function! ")
	elif(is_error==0):
		print(no_of_static_declarations)
		print(no_of_pointer_declarations)
		print(no_of_assignments)
