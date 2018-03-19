



class SymbolTable:

	def __init__(self):
		self.parent = None
		self.table = dict()

	def addEntry(self,ast):
		if(ast.Type == "DECL"):
			t = ast.l[0]
			for i in range(0,len(ast.l[1])):
				if isinstance(ast.l[1][i],str):
					self.table[ast.l[1][i]] = (t,0)
				else:
					self.table[ast.l[1][i][0]] = (t,ast.l[1][i][1])
	def __str__(self):
		return str(self.table)
		

