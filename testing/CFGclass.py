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
			self.astList = []
			self.num = -1
			self.num1 = -1
			self.blank = 0
			self.hasreturn = 0
		def addCode(self,c):
			self.code.append(c)

class CFG:
	def __init__(self):
		self.end = node("End",-1,-1,-1)		
		self.insertnode = node("Normal",self.end,-1,-1)
		self.head = node("Start",self.insertnode,-1,-1)
		self.isnotmain = -1
		self.funcinfo = ""

	def insert(self,ast):
		if(ast.Type == "BLANKBODY"):
			return

		elif(ast.Type == "FUNC"):
			self.funcinfo = (ast.Name,makestring1(ast.l[1]))
			self.insert(ast.l[2])

		elif ast.Type == "FCALL":
			# print("return statement",ast.l[0])
			a = ast.getcode()	
			self.insertnode.astList.append(ast)
			if isinstance(a,str):
				self.insertnode.addCode([a])
			else:
				self.insertnode.addCode(a[0])

		elif ast.Type == "RETURN":
			# print("return statement",ast.l[0])
			c_common = node("Normal",self.insertnode.left,-1,-1)
			self.insertnode.left = c_common
			self.insertnode = c_common
			a = ast.getcode()	
			self.insertnode.astList.append(ast)
			if isinstance(a,str):
				self.insertnode.addCode([a])
			else:
				self.insertnode.addCode(a[0])
			self.insertnode.hasreturn = 1
			self.end.hasreturn = 1
			
		elif(ast.Type == "BODY"):
			if(not ast.l):
				pass
			else:
				for j in range(0,len(ast.l)):
					self.insert(ast.l[j])

		elif (not ast.isjump() and ast.Type!="DECL" and ast.Type!="BLANKBODY" and ast.Type!="PROTO"):	
			a = ast.getcode()
			self.insertnode.astList.append(ast)	
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
			c_if.astList.append(ast.l[0])
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
			c_if.astList.append(ast.l[0])
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
			c_while.astList.append(ast.l[0])
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