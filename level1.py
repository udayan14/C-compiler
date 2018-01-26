#!/usr/bin/python3

import sys
import ply.lex as lex
import ply.yacc as yacc

no_of_pointer_declarations = 0
no_of_static_declarations = 0
no_of_assignments = 0
tokens = (
    'NUMBER',
    'TYPE',
    'SEMICOLON', 'EQUALS', 'COMMA',
    'LPAREN', 'RPAREN','LBRACE', 'RBRACE',
    'ADDROF','VALOF',
    'NAME',
    )

t_ignore = " \t\n"
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
    global no_of_static_declarations

    no_of_static_declarations = no_of_static_declarations + p[2]

def p_declaration2(p):
    """
        declaration : TYPE dlist2 SEMICOLON
    """
    global no_of_pointer_declarations

    no_of_pointer_declarations = no_of_pointer_declarations + p[2]

def p_dlist1(p):
    """
    dlist1 : NAME 
            | NAME COMMA dlist1  
    """
    if(len(p)==2):
        p[0] = 1
    else:  
        p[0] = p[3] + 1

def p_dlist2(p):
    """
    dlist2 : VALOF NAME 
            | VALOF NAME  COMMA dlist2  
    """
    if(len(p)==3):
        p[0] = 1
    else:  
        p[0] = p[4] + 1
    
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
                    | VALOF NAME EQUALS assignment_inter
    """
    if(len(p)==2):
        p[0] = p[1]
    else:
        p[0] = p[4] + 1

def p_assignment_base(p):

    """ 
    assignment_base : VALOF NAME EQUALS NUMBER 
            | VALOF NAME EQUALS VALOF NAME 
            | NAME EQUALS ADDROF NAME 
     """

    p[0] = 1 


def p_error(p):
    if p:
        print("syntax error at {0}".format(p.value))
    else:
        print("syntax error at EOF")

def process(data):
    lex.lex()
    yacc.yacc()
    yacc.parse(data)

if __name__ == "__main__":
    data = sys.stdin.read()
    process(data)
    print(no_of_static_declarations)
    print(no_of_pointer_declarations)
    print(no_of_assignments)
