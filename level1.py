#!/usr/bin/python3

import sys
import ply.lex as lex
import ply.yacc as yacc

no_of_pointer_declarations = 0
no_of_static_declarations = 0

tokens = (
    'NUMBER',
    'TYPE',
    'DELIM', 'EQUALS',
    'LPAREN', 'RPAREN','LBRACE', 'RBRACE',
    'ADDROF','VALOF',
    'NAME',
    'MAIN',
    )

t_ignore = " \t\n"
t_DELIM = ";"
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
    print("some datatype found")
    return t

def t_MAIN(t):
    r'\bmain\b'
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
    """program : TYPE MAIN LPAREN RPAREN LBRACE fbody RBRACE"""
    print(p[2])

def p_fbody(p):
    """fbody : statement
            | statement fbody"""
    p[0] = p[1]

def p_statement_expr(p):
        """statement : assignment
                | declaration
        """
        p[0]=p[1]

def p_declaration(p):
    """declaration : TYPE NAME DELIM
            | TYPE VALOF NAME DELIM 
    """
    global no_of_static_declarations, no_of_pointer_declarations
    if(len(p)==4):
        no_of_static_declarations = no_of_static_declarations + 1
    else:
        no_of_pointer_declarations = no_of_pointer_declarations + 1
    p[0] = p[1]

def p_assignment(p):
    """assignment : VALOF NAME EQUALS NUMBER DELIM
            | VALOF NAME EQUALS VALOF NAME DELIM"""
    p[0] = p[1]



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
    print("Enter the Program")
    data = sys.stdin.read()
    process(data)
    print("Static variables : ",no_of_static_declarations)
    print("Pointer variables : ",no_of_pointer_declarations)
