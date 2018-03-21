
from GlobalVariables import *
from HelperFunctions import *


# class SymbolTable:

# 	def __init__(self):
# 		self.parent = None
# 		self.varTable = dict()
# 		self.funcTable = dict()

# 	def addEntry(self,ast):
# 		global declaration_error
# 		if(ast.Type == "DECL"):
# 			t = ast.l[0]
# 			for i in range(0,len(ast.l[1])):
# 				if isinstance(ast.l[1][i],str):
# 					if ast.l[1][i] in self.varTable:
# 						declaration_error = 1
# 					else:
# 						self.varTable[ast.l[1][i]] = (t,0)
# 				else:
# 					if ast.l[1][i][0] in self.varTable:
# 						declaration_error = 1
# 					else:
# 						self.varTable[ast.l[1][i][0]] = (t,ast.l[1][i][1])
# 	def __str__(self):
# 		return str(self.varTable)
		

