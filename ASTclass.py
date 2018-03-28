import sys
import ply.lex as lex
import ply.yacc as yacc
import functools
from HelperFunctions import *
from GlobalVariables import *


class AST:
	def __init__(self,Type,Name,l):
		self.Type = Type
		self.Name = Name
		self.l = l

	def printit(self,i):

		if(self.Type == "BLANKBODY"):
			return
		elif(self.Type == "CONST"):
			printhelper(self.Type+"("+str(self.l[0])+")",i)

		elif(self.Type == "VAR"):
			printhelper(self.Type+"("+str(self.Name)+")",i)

		elif(self.Type == "DEREF" or self.Type == "UMINUS" or self.Type == "ADDR" or self.Type == "NOT"):
			printhelper(self.Type,i)
			printhelper("(",i)
			self.l[0].printit(i+1)
			printhelper(")",i)

		elif(self.Type == "RETURN"):
			printhelper(self.Type,i-1)
			printhelper("(",i-1)
			self.l[0].printit(i)
			printhelper(")",i-1)

		elif (self.Type == "ARGUMENTS"):
			for k in range(len(self.l)):
				self.l[k].printit(i)
				if k<len(self.l)-1:
					printhelper(",",i)

		elif(self.Type == "FCALL"):


			printhelper("call" + " "+self.Name+"(" , i)
			self.l[0].printit(i+1)
			printhelper(")",i)
			
				

		elif(self.Type == "WHILE"):
			printhelper(self.Type,i)
			printhelper("(",i)
			self.l[0].printit(i+1)
			printhelper(",",i+1)
			self.l[1].printit(i+1)
			printhelper(")",i)

		elif(self.Type == "ITE"):
			printhelper("IF",i)
			printhelper("(",i)
			self.l[0].printit(i+1)
			printhelper(",",i+1)
			# printhelper("THEN",i)
			# printhelper("(",i)
			self.l[1].printit(i+1)
			# printhelper(")",i)
			printhelper(",",i+1)
			# printhelper("(",i)
			self.l[2].printit(i+1)
			printhelper(")",i)	

		elif(self.Type == "IF"):
			printhelper("IF",i)
			printhelper("(",i)
			self.l[0].printit(i+1)
			# printhelper(")",i)
			printhelper(",",i+1)
			# printhelper("(",i)
			self.l[1].printit(i+1)
			printhelper(")",i)	

		elif(self.Type == "PLUS" or self.Type == "MINUS" or self.Type == "MUL" or self.Type == "DIV" or self.Type == "ASGN" or self.Type == "LE" or self.Type == "GE" or self.Type == "GT" or self.Type == "LT" or self.Type == "EQ" or self.Type == "NE" or self.Type == "AND" or self.Type == "OR"):
			printhelper(self.Type,i)
			printhelper("(",i)
			self.l[0].printit(i+1)
			printhelper(",",i+1)
			self.l[1].printit(i+1)
			printhelper(")",i)
			if(self.Type == "ASGN"):
				print("")
		elif(self.Type == "FUNC"):

			printhelper("FUNCTION "+ self.Name,i)
			printhelper("PARAMS "+"("+ makestring(self.l[1]) +")",i)
			printhelper("RETURNS " + "*"*self.l[3] + self.l[0],i)	
			self.l[2].printit(i+1)
			print("")

		elif(self.Type in ["PROG","BODY"]):
			if(not self.l):
				pass
			else:
				for j in range(0,len(self.l)):
					self.l[j].printit(i)
					if(j!=0):
						# print("")
						pass


	def appendchild(self,ast):
		self.l.reverse()
		self.l.append(ast)
		self.l.reverse()

	def isSimple(self):
		if self.Type in ["CONST","VAR","DEREF","ADDR"]:
			return True
		elif self.Type in ["PLUS","MINUS","MUL","DIVIDE","AND","OR"]:
			return False
		elif self.Type in ["UMINUS","NOT"]:
			return self.l[0].isSimple()

	def getcode(self):
		global temp
		if self.Type in ["PLUS","MINUS","MUL","DIV","AND","OR","LE","GE","LT","GT","EQ","NE"]:
			if self.l[0].isSimple():
				if self.l[1].isSimple():
					l = ["t{0} = {1}{2}{3}".format(temp,self.l[0].getcode(),getSymbol[self.Type],self.l[1].getcode())]
					temp+=1
					return (l,temp-1)
				else:
					l1,t_val = self.l[1].getcode()
					s = "t{0} = {1}{2}t{3}".format(temp,self.l[0].getcode(),getSymbol[self.Type],t_val)
					temp+=1
					l1.append(s)
					return (l1,temp-1)
			else:
				if self.l[1].isSimple():
					l1,t_val = self.l[0].getcode()
					s = "t{0} = t{1}{2}{3}".format(temp,t_val,getSymbol[self.Type],self.l[1].getcode())
					temp+=1
					l1.append(s)
					return (l1,temp-1)
				else:
					l1,t_val1 = self.l[0].getcode()
					l2,t_val2 = self.l[1].getcode()
					s = "t{0} = t{1}{2}t{3}".format(temp,t_val1,getSymbol[self.Type],t_val2)
					temp+=1
					l = l1 + l2
					l.append(s)
					return(l,temp-1)
		elif self.Type == "ASGN":
			if self.l[1].isSimple():
				l = ["{0}{1}{2}".format(self.l[0].getcode(),getSymbol[self.Type],self.l[1].getcode())]				
				return (l,temp)
			else:
				l1,t_val1 = self.l[1].getcode()
				s = "{0}{1}t{2}".format(self.l[0].getcode(),getSymbol[self.Type],t_val1)				
				l1.append(s)
				return (l1,temp)
		elif self.Type == "FCALL":
			pass

		elif self.Type == "ARGUMENTS":
			pass
		elif self.Type == "CONST":
			return str(self.Name)
		elif self.Type == "VAR":
			return str(self.Name)
		elif self.Type == "DEREF":
			return "*" + self.l[0].getcode()
		elif self.Type == "ADDR":
			return "&" + self.l[0].getcode()
		elif self.Type == "UMINUS":
			if self.l[0].isSimple():
				return "-" + self.l[0].getcode()
			else:
				l1,t_val1 = self.l[0].getcode()
				s = "t{0} = -t{1}".format(temp,t_val1) 
				temp+=1
				l1.append(s)
				return (l1,temp-1)
		elif self.Type == "NOT":
			if self.l[0].isSimple():
				return "!" + self.l[0].getcode()
			else:
				l1,t_val1 = self.l[0].getcode()
				s = "t{0} = !t{1}".format(temp,t_val1) 
				temp+=1
				l1.append(s)
				return (l1,temp-1)


	def isjump(self):
		if self.Type in ["IF","ITE","WHILE"]:
			return True
		return False