import sys
import ply.lex as lex
import ply.yacc as yacc
import functools
from GlobalVariables import *
import copy

getSymbol = {
	"PLUS" : " + " ,
	"MINUS": " - " ,
	"MUL"  : " * " ,
	"DIV"  : " / " ,
	"ASGN" : " = " ,
	"LE"   : " <= ",
	"GE"   : " >= ",
	"LT"   : " < " ,
	"GT"   : " > " ,
	"EQ"   : " == ",
	"NE"   : " != ",
	"AND"  : " && ",
	"OR"   : " || ",
}

def makestring(l):      #Prints variable name
	lnew = copy.deepcopy(l)
	# lnew.reverse()
	for i in range(0,len(lnew)):
		if not isinstance(lnew[i][1],str):
			lnew[i] = lnew[i][0]+" "+"*"*lnew[i][1][1]+""+lnew[i][1][0]
		else:
			lnew[i] = lnew[i][0] +" " +lnew[i][1]

	return ", ".join(str(x) for x in lnew)

def makestring1(l):    #Doesn't
	lnew = copy.deepcopy(l)
	for i in range(0,len(lnew)):
		if not isinstance(lnew[i][1],str):
			lnew[i] = lnew[i][0]+" "+"*"*lnew[i][1][1]
		else:
			lnew[i] = lnew[i][0] +" "

	return ",".join(str(x) for x in lnew)

def makestring2(l):
	lnew = copy.deepcopy(l)
	for i in range(0,len(lnew)):
		if not isinstance(lnew[i][1],str):
			lnew[i] = "'"+l[i][1][0]+"'" + " : " "'"+"*"*l[i][1][1]+l[i][0] + "'"  
		else:
			lnew[i] = "'" + lnew[i][1] + "'" +" : "+ "'"+ lnew[i][0]+ "'"

	return ",".join(str(x) for x in lnew)

def getoffset(l):
	offset = 0;
	lnew = [0]*len(l)
	for i in range(len(l)):
		lnew[i] = offset
		if not isinstance(l[i][1],str):
			offset+=4
		else:
			if l[i][0] == "int":
				offset+=4
			else:
				offset+=8
	return lnew
def cleanup(n):
	# print("soirjcgosij")
	if n.Type == "ITE":
		c = n.middle
		if not c.code:
			if (c.left==-1 and c.middle==-1 and c.right==-1):
				n.middle = -1
			elif c.left.Type in ["End","IF","ITE","WHILE"]:
				n.middle = c.left
				cleanup(n.middle)
		else:
			cleanup(n.middle)
		c = n.right
		if not c.code:
			
			if (not (c.left==-1 and c.middle==-1 and c.right==-1)):
				
				n.right = c.left
			else:
				# print("Empty else block!")
				n.right = -1
				# print("Changing type!")
				n.Type = "IF"
				# print(n.Type)
				# return
		c = n.left
		if not c.code:
			if (not (c.left==-1 and c.middle==-1 and c.right==-1)):
				n.left = c.left
			else:
				#### Empty if block in ITE
				n.left = -1
		if n.left!=-1:
			cleanup(n.left)
		if n.right!=-1:
			cleanup(n.right)
	elif n.Type == "IF" or n.Type == "WHILE":
		c = n.middle
		if not c.code:
			if (c.left==-1 and c.middle==-1 and c.right==-1):
				n.middle = -1
				n.right = -1

			elif c.left.Type in ["End","IF","ITE","WHILE"]:
				n.middle = c.left
				cleanup(n.middle)
		else:
			cleanup(n.middle)
		c = n.left
		if not c.code:
			if (not (c.left==-1 and c.middle==-1 and c.right==-1)):
				n.left = c.left
			else:
				n.left = -1
		if(n.left!=-1):
			cleanup(n.left)
	elif (n.left==-1 and n.right==-1 and n.middle==-1):
		return
	elif n.Type == "Start":
		c = n.left
		if not c.code:
			n.left = c.left
			cleanup(c.left)
		else:
			cleanup(n.left)	
	else:
		cleanup(n.left)

def printList(l): 
	if not l:
		return
	for i in l:
		print(i)


def giveNumbering(n,i):
	if n.Type == "End":
		if not n.hasreturn:
			n.num = i
			return i+1
		return i
	elif n.Type in ["Start","Normal"]:
		n.num = i
		if (not(n.left==-1 and n.middle==-1 and n.right==-1)):
			# print(n.Type + "calling " + n.left.Type)
			i1 = giveNumbering(n.left,i+1)
			return i1
		return i+1
	elif n.Type == "ITE":
		# print("sgrfh")
		n.num = i
		if n.left!=-1 and n.middle!=-1 and n.right!=-1:
			# print(n.Type + "calling " + n.left.Type + " " + n.middle.Type + " " + n.right.Type)
			i1 = giveNumbering(n.left,i+1)
			i2 = giveNumbering(n.right,i1)
			i3 = giveNumbering(n.middle,i2)
			return i3
		elif n.left!=-1 and n.right!=-1:
			# print(n.Type + "calling " + n.left.Type + " " + n.right.Type)
			i1 = giveNumbering(n.left,i+1)
			i2 = giveNumbering(n.right,i1)
			return i2
		elif n.middle!=-1 and n.right!=-1:
			# print(n.Type + "calling " +  n.middle.Type + " " + n.right.Type)
			i1 = giveNumbering(n.right,i+1)
			i2 = giveNumbering(n.middle,i1)
			return i2
		elif n.left!=-1 and n.middle!=-1:
			# print(n.Type + "calling " + n.left.Type + " " + n.middle.Type )
			i1 = giveNumbering(n.left,i+1)
			i2 = giveNumbering(n.middle,i1)
			return i2
		elif n.right!=-1:
			# print(n.Type + "calling " + n.right.Type)
			i1 = giveNumbering(n.right,i+1)
			return i1
		elif n.left!=-1:
			# print(n.Type + "calling " + n.left.Type)
			i1 = giveNumbering(n.left,i+1)
			return i1
		elif n.middle!=-1:
			# print(n.Type + "calling " + n.middle.Type)
			i1 = giveNumbering(n.middle,i+1)
			return i1
	elif n.Type == "IF" or n.Type == "WHILE":
		# print("sdbsnbson")
		n.num = i
		if n.left!=-1 and n.middle!=-1:
			# print(n.Type + "calling " + n.left.Type + " " + n.middle.Type )
			i1 = giveNumbering(n.left,i+1)
			i2 = giveNumbering(n.middle,i1)
			return i2
		elif n.left!=-1:
			# print(n.Type + "calling " + n.left.Type)
			i1 = giveNumbering(n.left,i+1)
			return i1
		elif n.middle!=-1:
			# print(n.Type + "calling " + n.middle.Type)
			i1 = giveNumbering(n.middle,i+1)
			return i1
		else:
			return i
	else:
		return i

def printCFGhelper(n1,nextstatenum):
	if n1==-1:
		return -1
	elif n1.Type == "Start":
		printCFGhelper(n1.left,nextstatenum)

	elif n1.Type == "End":
		if(not n1.hasreturn):
			print("<bb {0}>".format(n1.num))
			print("return")
			print("")

	elif n1.Type == "Normal":
		print("<bb {0}>".format(n1.num))
		# print("{0} has child {1}".format(n1.num,n1.l))	
		for c in n1.code:
			printList(c)
		if n1.hasreturn == 1:
			print("")
		elif (not (n1.left==-1 and n1.right==-1 and n1.middle==-1)):			
			print("goto <bb {0}>".format(n1.num+1))
			print("")
			printCFGhelper(n1.left,nextstatenum)
		else:
			print("goto <bb {0}>".format(nextstatenum))
			print("")

	elif n1.Type == "ITE":
		print("<bb {0}>".format(n1.num))
		printList(n1.code[0])
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
			print("if(t{0}) goto <bb {1}>".format(n1.num1,n1.left.num))
			print("else goto <bb {0}>".format(n1.right.num))
			print("")
			printCFGhelper(n1.left,n1.middle.num)
			printCFGhelper(n1.right,n1.middle.num)
			printCFGhelper(n1.middle,nextstatenum)
		elif n1.left!=-1 and n1.middle!=-1:
			print("if(t{0}) goto <bb {1}>".format(n1.num1,n1.left.num))
			print("else goto <bb {0}>".format(n1.middle.num))
			print("")
			printCFGhelper(n1.left,n1.middle.num)
			printCFGhelper(n1.middle,nextstatenum)
		elif n1.right!=-1 and n1.middle!=-1:
			print("if(t{0}) goto <bb {1}>".format(n1.num1,n1.middle.num))
			print("else goto <bb {0}>".format(n1.right.num))
			print("")
			printCFGhelper(n1.right,n1.middle.num)
			printCFGhelper(n1.middle,nextstatenum)
		elif n1.left!=-1 and n1.right!=-1:
			print("if(t{0}) goto <bb {1}>".format(n1.num1,n1.left.num))
			print("else goto <bb {0}>".format(n1.right.num))
			print("")
			printCFGhelper(n1.left,nextstatenum)
			printCFGhelper(n1.right,nextstatenum)
		elif n1.left!=-1:
			print("if(t{0}) goto <bb {1}>".format(n1.num1,n1.left.num))
			print("else goto <bb {0}>".format(nextstatenum))
			print("")
			printCFGhelper(n1.left,nextstatenum)
		elif n1.right!=-1:
			print("if(t{0}) goto <bb {1}>".format(n1.num1,nextstatenum))
			print("else goto <bb {0}>".format(n1.right.num))
			print("")
			printCFGhelper(n1.right,nextstatenum)
		elif n1.middle!=-1:
			print("if(t{0}) goto <bb {1}>".format(n1.num1,nextstatenum))
			print("else goto <bb {0}>".format(nextstatenum))
			print("")
			printCFGhelper(n1.middle,nextstatenum)
	elif n1.Type == "IF":
		print("<bb {0}>".format(n1.num))
		printList(n1.code[0])
		
		if (n1.left!=-1 and n1.middle!=-1):
			print("if(t{0}) goto <bb {1}>".format(n1.num1,n1.left.num))
			print("else goto <bb {0}>".format(n1.middle.num))
			print("")
			printCFGhelper(n1.left,n1.middle.num)
			printCFGhelper(n1.middle,nextstatenum)
		elif n1.left!=-1:
			print("if(t{0}) goto <bb {1}>".format(n1.num1,n1.left.num))
			print("else goto <bb {0}>".format(nextstatenum))
			print("")
			printCFGhelper(n1.left,nextstatenum)
		elif n1.middle!=-1:
			print("if(t{0}) goto <bb {1}>".format(n1.num1,n1.middle.num))
			print("else goto <bb {0}>".format(n1.middle.num))
			print("")
			printCFGhelper(n1.middle,nextstatenum)
		else:
			print("if(t{0}) goto <bb {1}>".format(n1.num1,nextstatenum))
			print("else goto <bb {0}>".format(nextstatenum))
			print("")
	elif n1.Type == "WHILE":
		print("<bb {0}>".format(n1.num))			
		printList(n1.code[0])
		
		# print("")
		if (n1.left!=-1 and n1.middle!=-1):
			print("if(t{0}) goto <bb {1}>".format(n1.num1,n1.left.num))
			print("else goto <bb {0}>".format(n1.middle.num))
			print("")
			printCFGhelper(n1.left,n1.num)
			printCFGhelper(n1.middle,nextstatenum)
		elif n1.left!=-1:
			print("if(t{0}) goto <bb {1}>".format(n1.num1,n1.left.num))
			print("else goto <bb {0}>".format(nextstatenum))
			print("")
			printCFGhelper(n1.left,n1.num)
		elif n1.middle!=-1:
			print("if(t{0}) goto <bb {1}>".format(n1.num1,n1.num))
			print("else goto <bb {0}>".format(n1.middle.num))
			print("")
			printCFGhelper(n1.middle,nextstatenum)
		else:
			print("if(t{0}) goto <bb {1}>".format(n1.num1,nextstatenum))
			print("else goto <bb {0}>".format(nextstatenum))
			print("")

def getNormReg():
	global norm_reg
	if 0 in norm_reg:
		ind = norm_reg.index(0)
		norm_reg[ind] = 1
		# printNormReg()

		return ind
	else:
		return "All normal registers full"

def printNormReg():
	global norm_reg
	print(norm_reg)

def freeNormReg(i):
	global norm_reg
	norm_reg[i] = 0
	# printNormReg()

def getFloatReg():
	global float_reg
	if 0 in float_reg:
		ind = float_reg.index(0)
		float_reg[ind] = 1
		return 10 + ind*2
	else:
		return "All float registers full"

def freeFloatReg(i):
	global float_reg
	ind = (i - 10) / 2
	float_reg[int(ind)] = 0

def printhelper(s,i):
	print("\t"*i + s)