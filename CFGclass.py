import sys
import ply.lex as lex
import ply.yacc as yacc
import functools
from GlobalVariables import *
from HelperFunctions import *

class node:
		def __init__(self,Type,left, middle, right):
			self.Type = Type
			self.left = left
			self.right = right
			self.middle = middle
			self.code = []
			self.num = -1
			self.num1 = -1
			self.blank = 0
		def addCode(self,c):
			self.code.append(c)

class CFG:
	def __init__(self):
		self.end = node("End",-1,-1,-1)		
		self.insertnode = node("Normal",self.end,-1,-1)
		self.head = node("Start",self.insertnode,-1,-1)

	def insert(self,ast):
		if(ast.Type == "BLANKBODY"):
			return
		if(ast.Type == "RETURN" or ast.Type == "FCALL" or ast.Type == "ARGUMENTS"):
			# print("return statement",ast.l[0])
			return
		elif(ast.Type == "BODY"):
			if(not ast.l):
				pass
			else:
				for j in range(len(ast.l)-1,-1,-1):
					self.insert(ast.l[j])

		elif (not ast.isjump() and ast.Type!="DECL" and ast.Type!="BLANKBODY"):	
			a = ast.getcode()	
			if isinstance(a,str):
				self.insertnode.addCode([a])
			else:
				self.insertnode.addCode(a[0])
			
		elif (ast.Type == "ITE"):
			c_common = node("Normal",self.insertnode.left,-1,-1)
			c_true = node("Normal",-1,-1,-1)
			c_false = node("Normal",-1,-1,-1)
			c_if = node("ITE",c_true,c_common,c_false)
			a = ast.l[0].getcode()	
			if isinstance(a,str):
				c_if.addCode([a])
				c_if.num1 = temp
			else:
				c_if.addCode(a[0])
				c_if.num1 = a[1]
			self.insertnode.left = c_if
			self.insertnode = c_true
			self.insert(ast.l[1])
			self.insertnode = c_false
			self.insert(ast.l[2])
			self.insertnode = c_common

		elif(ast.Type == "IF"):
			c_common = node("Normal",self.insertnode.left,-1,-1)
			c_true = node("Normal",-1,-1,-1)
			c_if = node("IF",c_true,c_common,-1)
			a = ast.l[0].getcode()

			if isinstance(a,str):
				c_if.addCode([a])
				c_if.num1 = temp
			else:
				c_if.addCode(a[0])
				c_if.num1 = a[1]
			self.insertnode.left = c_if
			self.insertnode = c_true
			self.insert(ast.l[1])
			self.insertnode = c_common

		elif(ast.Type == "WHILE"):
			c_common = node("Normal",self.insertnode.left,-1,-1)
			c_true = node("Normal",-1,-1,-1)
			c_while = node("WHILE",c_true,c_common,-1)
			a = ast.l[0].getcode()	
			if isinstance(a,str):
				c_while.addCode([a])
				c_while.num1 = temp
			else:
				c_while.addCode(a[0])
				c_while.num1 = a[1]
			self.insertnode.left = c_while
			self.insertnode = c_true
			self.insert(ast.l[1])
			self.insertnode = c_common