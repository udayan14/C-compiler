#!/usr/bin/python3

import sys
import ply.lex as lex
import ply.yacc as yacc


tokens = (
        'NAME', 'NUMBER',
        'PLUS', 'MINUS', 'EXP', 'TIMES', 'DIVIDE', 'EQUALS',
        'LPAREN', 'RPAREN',
        'PLUSWORD', 'MINUSWORD', 'TIMESWORD', 'POWERWORD', 'DIVIDEWORD',
        'ONES', 'TENS', 'TWENTIES', 'HUNDRED', 'THOUSAND',
)


t_ignore = " \t\n"
t_PLUS = r'\+'
t_MINUS = r'-'
t_EXP = r'\*\*'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_TENS(token):
	r'\bten\b|\beleven\b|\btwelve\b|\bthirteen\b|\bfourteen\b|\bfifteen\b|\bsixteen\b|\bseventeen\b|\beighteen\b|\bnineteen\b'
	if token.value == 'ten':
		token.value = int(10)
	elif token.value == 'eleven':
		token.value = int(11)
	elif token.value == 'twelve':
		token.value = int(12)
	elif token.value == 'thirteen':
		token.value = int(13)
	elif token.value == 'fourteen':
		token.value = int(14)
	elif token.value == 'fifteen':
		token.value = int(15)
	elif token.value == 'sixteen':
		token.value = int(16)
	elif token.value == 'seventeen':
		token.value = int(17)
	elif token.value == 'eighteen':
		token.value = int(18)
	elif token.value == 'nineteen':
		token.value = int(19)
	return token

def t_HUNDRED(token):
	r'\bhundred\b'
	if token.value == 'hundred':
		token.value = int(100)

	return token

def t_THOUSAND(token):
	r'\bthousand\b'
	if token.value == 'thousand':
		# print("passing eormo")
		token.value = int(1000)
	return token

def t_TWENTIES(token):
	r'\btwenty\b|\bthirty\b|\bforty\b|\bfifty\b|\bsixty\b|\bseventy\b|\beighty\b|\bninety\b'
	if token.value == 'twenty':
		token.value = int(20)
	elif token.value == 'thirty':
		token.value = int(30)
	elif token.value == 'forty':
		token.value = int(40)
	elif token.value == 'fifty':
		token.value = int(50)
	elif token.value == 'sixty':
		token.value = int(60)
	elif token.value == 'seventy':
		token.value = int(70)
	elif token.value == 'eighty':
		token.value = int(80)
	elif token.value == 'ninety':
		token.value = int(90)
	return token

def t_ONES(token):
	r'\bone\b|\btwo\b|\bthree\b|\bfour\b|\bfive\b|\bsix\b|\bseven\b|\beight\b|\bnine\b'
	if token.value == 'one':
		token.value = int(1)
	elif token.value == 'two':
		token.value = int(2)
	elif token.value == 'three':
		token.value = int(3)
	elif token.value == 'four':
		token.value = int(4)
	elif token.value == 'five':
		token.value = int(5)
	elif token.value == 'six':
		token.value = int(6)
	elif token.value == 'seven':
		token.value = int(7)
	elif token.value == 'eight':
		token.value = int(8)
	elif token.value == 'nine':
		token.value = int(9)
	return token


def t_error(t): 
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

# Parsing rules
precedence = (
	('left', 'PLUS', 'MINUS','PLUSWORD','MINUSWORD'),
        ('left', 'TIMES', 'DIVIDE','TIMESWORD','DIVIDEWORD'),
        ('left', 'EXP','POWERWORD'),
        ('right', 'UMINUS', 'UMINUSWORD'),
)

def p_statement_assign(p):
	'statement : NAME EQUALS expression'
	p[1]=p[3]

def p_statement_expr(p):
        'statement : expression'
        print(p[1])

def p_expression_binop(p):
        """
        expression : expression PLUS expression
         		  | expression PLUSWORD expression
                  | expression MINUS expression
                  | expression MINUSWORD expression
                  | expression TIMES expression
                  | expression TIMESWORD expression
                  | expression DIVIDE expression
                  | expression DIVIDEWORD expression
                  | expression EXP expression
                  | expression POWERWORD expression
        """
        # print [repr(p[i]) for i in range(0,4)]
        
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == 'plus':
        	p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        elif p[2] == 'minus':
        	p[0] = p[1] - p[3]
        elif p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == 'times':
        	p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
        elif p[2] == 'divide':
        	p[0] = p[1] / p[3]
        elif p[2] == '**':
            p[0] = p[1] ** p[3]
        elif p[2] == 'power':
        	p[0] = p[1] ** p[3]

def p_expression_uminus(p):
        'expression : MINUS expression %prec UMINUS'
        p[0] = -p[2]

def p_expression_uminus2(p):
        'expression : MINUSWORD expression %prec UMINUSWORD'
        p[0] = -p[2]

def p_expression_group(p):
        'expression : LPAREN expression RPAREN'
        p[0] = p[2]

def p_expression_number(p):
        """expression : NUMBER
         | ONES 
         | TENS 
         | TWENTIES 
         | TWENTIES ONES """
        if(len(p)==3):
        	p[0] = p[1] + p[2]
        	return
        p[0] = p[1]

def p_expression_thousands_five_terms(p):
	'expression : TWENTIES ONES THOUSAND TWENTIES ONES'
	p[0] = (p[1]+p[2])*p[3] + p[4] + p[5] 

def p_expression_thousands_four_terms2(p):
	"""
	expression : TWENTIES ONES THOUSAND ONES
			| TWENTIES ONES THOUSAND TENS
			| TWENTIES ONES THOUSAND TWENTIES
			| TWENTIES ONES THOUSAND ONEHUNDRED
	"""
	p[0] = (p[1]+p[2])*p[3] + p[4]

def p_expression_thousands_four_terms(p):
	"""
	expression : ONES THOUSAND TWENTIES ONES
			| TENS THOUSAND TWENTIES ONES
			| TWENTIES THOUSAND TWENTIES ONES
			| ONEHUNDRED THOUSAND TWENTIES ONES
	"""
	p[0] = p[1]*p[2] + p[3] + p[4]

def p_expression_thousands_both(p):
	"""
	expression : ONES THOUSAND ONES
			| TENS THOUSAND ONES
			| TWENTIES THOUSAND ONES
			| ONEHUNDRED THOUSAND ONES
			| ONES THOUSAND TENS
			| TENS THOUSAND TENS
			| TWENTIES THOUSAND TENS
			| ONEHUNDRED THOUSAND TENS
			| ONES THOUSAND TWENTIES
			| TENS THOUSAND TWENTIES
			| TWENTIES THOUSAND TWENTIES
			| ONEHUNDRED THOUSAND TWENTIES
			| ONES THOUSAND ONEHUNDRED
			| TENS THOUSAND ONEHUNDRED
			| TWENTIES THOUSAND ONEHUNDRED
			| ONEHUNDRED THOUSAND ONEHUNDRED
	"""
	p[0] = p[1]*p[2] + p[3]  
	
def p_expression_thousands_basic2(p):
	'expression : TWENTIES ONES THOUSAND'
	p[0] = (p[1] + p[2]) * p[3]

def p_expression_thousands_basic(p):
	"""
	expression : ONES THOUSAND
			| TENS THOUSAND
			| TWENTIES THOUSAND
			| ONEHUNDRED THOUSAND
	"""
	p[0] = p[1]*p[2]	

def p_expression_hundreds(p):
	'expression : ONEHUNDRED'
	p[0] = p[1]

def p_hundred_final(p):
	'ONEHUNDRED : ONES HUNDREDTERM'
	p[0] = p[1]*100 + (p[2]-100)

def p_hundred_full(p):
	'HUNDREDTERM : HUNDRED TWENTIES ONES'

	p[0] = p[1] + p[2] + p[3] 

def p_hundreds(p):
	"""
	HUNDREDTERM : HUNDRED ONES
		| HUNDRED TENS
		| HUNDRED TWENTIES
	"""
	p[0] = p[1] + p[2]

def p_hundreds_tens(p):
	'HUNDREDTERM : HUNDRED'
	p[0] = p[1]

def p_expression_name(p):
        'expression : NAME'
        try:
            p[0] = p[1]
        except LookupError:
            print("Undefined name '%s'" % p[1])
            p[0] = 0

def p_error(p):
	if p:
		print("syntax error at {0}".format(p.value))
	else:
		print("syntax error at EOF")	

def t_PLUSWORD(token):
	r'plus'
	return token	

def t_MINUSWORD(token):
	r'minus'
	return token

def t_TIMESWORD(token):
	r'times'
	return token

def t_DIVIDEWORD(token):
	r'divide'
	return token

def t_POWERWORD(token):
	r'power'
	return token

def process(data):
	lex.lex()
	yacc.yacc()
	yacc.parse(data)

if __name__ == "__main__":
	print("Enter the Equation")
	data = sys.stdin.readline()
	process(data)
