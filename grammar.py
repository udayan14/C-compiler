import sys
import ply.lex as lex
import ply.yacc as yacc
import functools


def p_function(p):
	"""
	function : TYPE NAME LPAREN paramlist RPAREN LBRACE fbody RBRACE
	"""
	# global main_found,assignment_error,return_error
	# void_return = 0
	# global is_error
	# # print(p[2])
	# if str(p[2])=='main':
	# 	main_found = 1
	# if str(p[1])=='void':
	# 	void_return = 1
	# # print(p[6][::-1])
	# if(assignment_error):
	# 	is_error = 1
	# 	if p:
	# 		print("Syntax error at line no  '{0}' , assignment error ".format(p.lexer.lineno))
	# 	else:
	# 		print("Syntax error at EOF")
	# 	# print("Main function not found || Return type of main is not void || Invalid Assignment")
	# elif(not main_found):
	# 	is_error = 1
	# 	print("Syntax error at line no  '{0}' , main not found".format(p.lexer.lineno))
	# elif(not void_return):
	# 	is_error = 1
	# 	print("Syntax error at line no  '{0}' , return type of main function not void".format(p.lexer.lineno))
	# else:
	# 	output_f1 = str(sys.argv[1]) + ".ast"
	# 	output_f2 = str(sys.argv[1]) + ".cfg"
	# 	oldstdout = sys.stdout
	# 	sys.stdout = open(output_f1,'w+')		
	# 	p[6].printit(0)
	# 	sys.stdout = open(output_f2,'w+')
	# 	printCFG(p[6])
	# 	sys.stdout.close()
	# 	sys.stdout = oldstdout
	p[0] = AST("FUNC",p[2],[p[1],p[4],p[7]])
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
		p[0].append(p[2])
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
		p[0].append(p[3])

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
	"""
	p[0] = p[1]

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
		if(is_valid_asgn(a1,p[3])):
			pass
		else:
			assignment_error = 1
			assignment_error_line = p.lexer.lineno
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
		print("Syntax error at '{0}' line no  '{1}' ".format(p.value,p.lexer.lineno))
	else:
		print("Syntax error at EOF")