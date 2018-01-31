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


def p_fbody(p):
    """
    fbody : statement
            | statement fbody
    """
    p[0] = p[1]

def p_statement_expr(p):
    """
    statement : assignment
            | declaration
    """
    p[0]=p[1]

def p_declaration1(p):
    """
        declaration : TYPE dlist1 SEMICOLON
    """
    # no_of_static_declarations = no_of_static_declarations + p[2]

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
    assignment : assignment_list SEMICOLON
    """
    global no_of_assignments

    p[0] = p[1]
    no_of_assignments = no_of_assignments + p[0]

def p_assignment_list(p):
    """
    assignment_list : assignment_inter
                        | assignment_inter COMMA assignment_list
    """
    if(len(p)==2):
        p[0] = p[1]
    else:
        p[0] = p[1] + p[3]

def p_assignment_inter(p):
    """
    assignment_inter : assignment_base
                    | VALOF pointervar EQUALS assignment_inter
                    | NAME EQUALS assignment_inter

    """
    if(len(p)==2):
        p[0] = p[1]
    elif(len(p)==4):
        p[0] = p[3] + 1
    else:
    	p[0] = p[4] + 1

def p_assignment_base(p):

    """ 
    assignment_base : VALOF pointervar EQUALS NUMBER
    		| VALOF pointervar EQUALS pointervar 
    		| NAME EQUALS pointervar 
     """

    p[0] = 1 

def p_pointervar(p):
	"""
	pointervar : VALOF pointervar
				| ADDROF pointervar
				| NAME
	"""
	# print("pointervar found",p[1])
	p[0]=1


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
