
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftOROPERATORleftANDOPERATORleftEQUALCHECKUNEQUALleftLESSTHANEQLESSTHANGREATERTHANEQGREATERTHANleftPLUSMINUSleftTIMESDIVIDErightVALOFADDROFrightNOTrightUMINUSNUMBER TYPE SEMICOLON EQUALS COMMA LPAREN RPAREN LBRACE RBRACE ANDOPERATOR OROPERATOR ADDROF NAME PLUS MINUS TIMES DIVIDE WHILE IF ELSE EQUALCHECK UNEQUAL LESSTHAN LESSTHANEQ GREATERTHAN GREATERTHANEQ NOT \n\tprogram : function \n\t\t\t\t| function program\n\t\n\tfunction : TYPE NAME LPAREN RPAREN LBRACE fbody RBRACE\n\t\n\tfbody : allstatement fbody\n\t\t\t| \n\t\n\tallstatement : statement\n\t\t\t\t| unmatchedstatement\n\t\n\tstatement : assignment\n\t\t\t| declaration\n\t\t\t| whileblock\n\t\t\t| ifblock\n\t\n\tstatement : SEMICOLON\n\t\n\tunmatchedstatement : IF LPAREN conditional RPAREN allstatement\n\t\t\t\t| IF LPAREN conditional RPAREN statement ELSE unmatchedstatement\n\t\t\t\t| IF LPAREN conditional RPAREN LBRACE fbody RBRACE ELSE unmatchedstatement\n\t\n\tunmatchedstatement : IF LPAREN conditional RPAREN LBRACE fbody RBRACE\n\t\n\tifblock : IF LPAREN conditional RPAREN statement ELSE statement\n\t\t\t| IF LPAREN conditional RPAREN statement ELSE LBRACE fbody RBRACE\n\t\t\t| IF LPAREN conditional RPAREN LBRACE fbody RBRACE ELSE LBRACE fbody RBRACE\n\t\n\tifblock : IF LPAREN conditional RPAREN LBRACE fbody RBRACE ELSE statement\n\t\n\twhileblock : WHILE LPAREN conditional RPAREN LBRACE fbody RBRACE\n\t\n\tconditional : conditionbase\n\t\t\t\t| conditional LESSTHANEQ conditional\n\t\t\t\t| conditional GREATERTHANEQ conditional\n\t\t\t\t| conditional UNEQUAL conditional\n\t\t\t\t| conditional EQUALCHECK conditional\n\t\t\t\t| conditional LESSTHAN conditional\n\t\t\t\t| conditional GREATERTHAN conditional\n\t\t\t\t| conditional ANDOPERATOR conditional\n\t\t\t\t| conditional OROPERATOR conditional\n\t\n\tconditionbase : CS LESSTHANEQ CS\n\t\t\t\t| CS GREATERTHANEQ CS\n\t\t\t\t| CS UNEQUAL CS\n\t\t\t\t| CS EQUALCHECK CS\n\t\t\t\t| CS LESSTHAN CS\n\t\t\t\t| CS GREATERTHAN CS\n\t\n\tCS : expression\n\t\t| NOT LPAREN expression RPAREN\n\t\n\t\tdeclaration : TYPE dlist1 SEMICOLON\n\t\n\tdlist1 : NAME  \n\t\t\t| NAME COMMA dlist1\n\t\n\tdlist1 : specialvar\n\t\t\t| specialvar  COMMA dlist1  \n\t\n\tspecialvar : TIMES specialvar %prec VALOF\n\t\t\t\t| TIMES NAME %prec VALOF\n\t\n\tassignment : assignment_base SEMICOLON\n\t \n\tassignment_base : TIMES pointervar EQUALS expression\n\t\t\t| NAME EQUALS expression \n\t \n\texpression : expression PLUS expression\n\t\t\t\t| expression MINUS expression\n\t\t\t\t| expression DIVIDE expression\n\t\n\texpression : expression TIMES expression\n\t\n\texpression : MINUS expression %prec UMINUS\n\t\n\texpression : LPAREN expression RPAREN\n\t\n\texpression : NUMBER\n\t\n\texpression : pointervar\n\t\n\tpointervar : TIMES pointervar %prec VALOF\n\t\n\tpointervar : ADDROF pointervar \n\t\n\tpointervar : NAME\n\t'
    
_lr_action_items = {'$end':([2,3,5,30,],[-1,0,-2,-3,]),'NOT':([35,36,66,67,69,70,71,72,73,74,76,77,78,79,80,81,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'EQUALCHECK':([34,43,45,46,47,48,51,52,54,55,64,83,84,85,86,87,88,89,91,92,93,94,95,96,98,99,100,101,102,103,108,],[-59,-57,-58,-22,-55,-37,-56,66,77,66,-53,-49,-52,-51,-50,-54,-26,66,-24,66,-25,-28,-27,-23,-32,-34,-33,-35,-36,-31,-38,]),'RPAREN':([6,34,43,45,46,47,48,51,52,55,64,65,83,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,108,],[7,-59,-57,-58,-22,-55,-37,-56,68,82,-53,87,-49,-52,-51,-50,-54,-26,-29,-24,-30,-25,-28,-27,-23,108,-32,-34,-33,-35,-36,-31,-38,]),'ELSE':([10,12,15,16,19,29,38,104,111,112,115,118,119,123,],[-11,-9,-8,-12,-10,-46,-39,109,-21,-17,117,-18,-20,-19,]),'NUMBER':([35,36,37,44,49,50,60,61,62,63,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'OROPERATOR':([34,43,45,46,47,48,51,52,55,64,83,84,85,86,87,88,89,91,92,93,94,95,96,98,99,100,101,102,103,108,],[-59,-57,-58,-22,-55,-37,-56,70,70,-53,-49,-52,-51,-50,-54,-26,-29,-24,-30,-25,-28,-27,-23,-32,-34,-33,-35,-36,-31,-38,]),'ADDROF':([18,31,33,35,36,37,44,49,50,60,61,62,63,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'TYPE':([0,2,8,9,10,11,12,15,16,19,21,29,30,38,82,90,104,105,106,109,111,112,113,114,115,117,118,119,120,121,123,],[1,1,13,-6,-11,13,-9,-8,-12,-10,-7,-46,-3,-39,13,13,-6,-13,13,13,-21,-17,13,-14,-16,13,-18,-20,13,-15,-19,]),'LBRACE':([7,68,82,109,117,],[8,90,106,113,120,]),'IF':([8,9,10,11,12,15,16,19,21,29,38,82,90,104,105,106,109,111,112,113,114,115,117,118,119,120,121,123,],[22,-6,-11,22,-9,-8,-12,-10,-7,-46,-39,22,22,-6,-13,22,22,-21,-17,22,-14,-16,22,-18,-20,22,-15,-19,]),'EQUALS':([23,32,34,43,45,],[37,44,-59,-57,-58,]),'SEMICOLON':([8,9,10,11,12,14,15,16,19,21,25,27,28,29,34,38,39,40,43,45,47,51,56,57,58,59,64,82,83,84,85,86,87,90,104,105,106,109,111,112,113,114,115,117,118,119,120,121,123,],[16,-6,-11,16,-9,29,-8,-12,-10,-7,38,-42,-40,-46,-59,-39,-44,-45,-57,-58,-55,-56,-48,-43,-41,-47,-53,16,-49,-52,-51,-50,-54,16,-6,-13,16,16,-21,-17,16,-14,-16,16,-18,-20,16,-15,-19,]),'MINUS':([34,35,36,37,43,44,45,47,48,49,50,51,56,59,60,61,62,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,85,86,87,97,],[-59,49,49,49,-57,49,-58,-55,63,49,49,-56,63,63,49,49,49,49,-53,63,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-49,-52,-51,-50,-54,63,]),'LESSTHANEQ':([34,43,45,46,47,48,51,52,54,55,64,83,84,85,86,87,88,89,91,92,93,94,95,96,98,99,100,101,102,103,108,],[-59,-57,-58,-22,-55,-37,-56,74,81,74,-53,-49,-52,-51,-50,-54,74,74,-24,74,74,-28,-27,-23,-32,-34,-33,-35,-36,-31,-38,]),'ANDOPERATOR':([34,43,45,46,47,48,51,52,55,64,83,84,85,86,87,88,89,91,92,93,94,95,96,98,99,100,101,102,103,108,],[-59,-57,-58,-22,-55,-37,-56,67,67,-53,-49,-52,-51,-50,-54,-26,-29,-24,67,-25,-28,-27,-23,-32,-34,-33,-35,-36,-31,-38,]),'COMMA':([27,28,39,40,],[41,42,-44,-45,]),'TIMES':([8,9,10,11,12,13,15,16,18,19,21,26,29,31,33,34,35,36,37,38,41,42,43,44,45,47,48,49,50,51,56,59,60,61,62,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,90,97,104,105,106,109,111,112,113,114,115,117,118,119,120,121,123,],[18,-6,-11,18,-9,26,-8,-12,31,-10,-7,26,-46,31,31,-59,31,31,31,-39,26,26,-57,31,-58,-55,61,31,31,-56,61,61,31,31,31,31,-53,61,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,18,61,-52,-51,61,-54,18,61,-6,-13,18,18,-21,-17,18,-14,-16,18,-18,-20,18,-15,-19,]),'LPAREN':([4,20,22,35,36,37,44,49,50,53,60,61,62,63,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,],[6,35,36,50,50,50,50,50,50,75,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'GREATERTHANEQ':([34,43,45,46,47,48,51,52,54,55,64,83,84,85,86,87,88,89,91,92,93,94,95,96,98,99,100,101,102,103,108,],[-59,-57,-58,-22,-55,-37,-56,69,76,69,-53,-49,-52,-51,-50,-54,69,69,-24,69,69,-28,-27,-23,-32,-34,-33,-35,-36,-31,-38,]),'DIVIDE':([34,43,45,47,48,51,56,59,64,65,83,84,85,86,87,97,],[-59,-57,-58,-55,62,-56,62,62,-53,62,62,-52,-51,62,-54,62,]),'UNEQUAL':([34,43,45,46,47,48,51,52,54,55,64,83,84,85,86,87,88,89,91,92,93,94,95,96,98,99,100,101,102,103,108,],[-59,-57,-58,-22,-55,-37,-56,71,78,71,-53,-49,-52,-51,-50,-54,-26,71,-24,71,-25,-28,-27,-23,-32,-34,-33,-35,-36,-31,-38,]),'WHILE':([8,9,10,11,12,15,16,19,21,29,38,82,90,104,105,106,109,111,112,113,114,115,117,118,119,120,121,123,],[20,-6,-11,20,-9,-8,-12,-10,-7,-46,-39,20,20,-6,-13,20,20,-21,-17,20,-14,-16,20,-18,-20,20,-15,-19,]),'PLUS':([34,43,45,47,48,51,56,59,64,65,83,84,85,86,87,97,],[-59,-57,-58,-55,60,-56,60,60,-53,60,-49,-52,-51,-50,-54,60,]),'RBRACE':([8,9,10,11,12,15,16,17,19,21,24,29,38,90,104,105,106,107,110,111,112,113,114,115,116,118,119,120,121,122,123,],[-5,-6,-11,-5,-9,-8,-12,30,-10,-7,-4,-46,-39,-5,-6,-13,-5,111,115,-21,-17,-5,-14,-16,118,-18,-20,-5,-15,123,-19,]),'GREATERTHAN':([34,43,45,46,47,48,51,52,54,55,64,83,84,85,86,87,88,89,91,92,93,94,95,96,98,99,100,101,102,103,108,],[-59,-57,-58,-22,-55,-37,-56,72,80,72,-53,-49,-52,-51,-50,-54,72,72,-24,72,72,-28,-27,-23,-32,-34,-33,-35,-36,-31,-38,]),'LESSTHAN':([34,43,45,46,47,48,51,52,54,55,64,83,84,85,86,87,88,89,91,92,93,94,95,96,98,99,100,101,102,103,108,],[-59,-57,-58,-22,-55,-37,-56,73,79,73,-53,-49,-52,-51,-50,-54,73,73,-24,73,73,-28,-27,-23,-32,-34,-33,-35,-36,-31,-38,]),'NAME':([1,8,9,10,11,12,13,15,16,18,19,21,26,29,31,33,35,36,37,38,41,42,44,49,50,60,61,62,63,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,82,90,104,105,106,109,111,112,113,114,115,117,118,119,120,121,123,],[4,23,-6,-11,23,-9,28,-8,-12,34,-10,-7,40,-46,34,34,34,34,34,-39,28,28,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,23,23,-6,-13,23,23,-21,-17,23,-14,-16,23,-18,-20,23,-15,-19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([8,11,82,90,106,109,113,117,120,],[9,9,104,9,9,112,9,119,9,]),'ifblock':([8,11,82,90,106,109,113,117,120,],[10,10,10,10,10,10,10,10,10,]),'program':([0,2,],[3,5,]),'allstatement':([8,11,82,90,106,113,120,],[11,11,105,11,11,11,11,]),'fbody':([8,11,90,106,113,120,],[17,24,107,110,116,122,]),'specialvar':([13,26,41,42,],[27,39,27,27,]),'function':([0,2,],[2,2,]),'declaration':([8,11,82,90,106,109,113,117,120,],[12,12,12,12,12,12,12,12,12,]),'conditionbase':([35,36,66,67,69,70,71,72,73,74,],[46,46,46,46,46,46,46,46,46,46,]),'conditional':([35,36,66,67,69,70,71,72,73,74,],[52,55,88,89,91,92,93,94,95,96,]),'whileblock':([8,11,82,90,106,109,113,117,120,],[19,19,19,19,19,19,19,19,19,]),'expression':([35,36,37,44,49,50,60,61,62,63,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,],[48,48,56,59,64,65,83,84,85,86,48,48,48,48,48,48,48,48,97,48,48,48,48,48,48,]),'dlist1':([13,41,42,],[25,57,58,]),'unmatchedstatement':([8,11,82,90,106,109,113,117,120,],[21,21,21,21,21,114,21,121,21,]),'assignment_base':([8,11,82,90,106,109,113,117,120,],[14,14,14,14,14,14,14,14,14,]),'assignment':([8,11,82,90,106,109,113,117,120,],[15,15,15,15,15,15,15,15,15,]),'pointervar':([18,31,33,35,36,37,44,49,50,60,61,62,63,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,],[32,43,45,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'CS':([35,36,66,67,69,70,71,72,73,74,76,77,78,79,80,81,],[54,54,54,54,54,54,54,54,54,54,98,99,100,101,102,103,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> function','program',1,'p_program','better.py',634),
  ('program -> function program','program',2,'p_program','better.py',635),
  ('function -> TYPE NAME LPAREN RPAREN LBRACE fbody RBRACE','function',7,'p_function','better.py',659),
  ('fbody -> allstatement fbody','fbody',2,'p_fbody','better.py',696),
  ('fbody -> <empty>','fbody',0,'p_fbody','better.py',697),
  ('allstatement -> statement','allstatement',1,'p_allstatement_expr','better.py',720),
  ('allstatement -> unmatchedstatement','allstatement',1,'p_allstatement_expr','better.py',721),
  ('statement -> assignment','statement',1,'p_statement_expr','better.py',727),
  ('statement -> declaration','statement',1,'p_statement_expr','better.py',728),
  ('statement -> whileblock','statement',1,'p_statement_expr','better.py',729),
  ('statement -> ifblock','statement',1,'p_statement_expr','better.py',730),
  ('statement -> SEMICOLON','statement',1,'p_empty_statement','better.py',736),
  ('unmatchedstatement -> IF LPAREN conditional RPAREN allstatement','unmatchedstatement',5,'p_unmatchedstatement_expr1','better.py',742),
  ('unmatchedstatement -> IF LPAREN conditional RPAREN statement ELSE unmatchedstatement','unmatchedstatement',7,'p_unmatchedstatement_expr1','better.py',743),
  ('unmatchedstatement -> IF LPAREN conditional RPAREN LBRACE fbody RBRACE ELSE unmatchedstatement','unmatchedstatement',9,'p_unmatchedstatement_expr1','better.py',744),
  ('unmatchedstatement -> IF LPAREN conditional RPAREN LBRACE fbody RBRACE','unmatchedstatement',7,'p_unmatchedstatement_expr2','better.py',755),
  ('ifblock -> IF LPAREN conditional RPAREN statement ELSE statement','ifblock',7,'p_ifblock1','better.py',761),
  ('ifblock -> IF LPAREN conditional RPAREN statement ELSE LBRACE fbody RBRACE','ifblock',9,'p_ifblock1','better.py',762),
  ('ifblock -> IF LPAREN conditional RPAREN LBRACE fbody RBRACE ELSE LBRACE fbody RBRACE','ifblock',11,'p_ifblock1','better.py',763),
  ('ifblock -> IF LPAREN conditional RPAREN LBRACE fbody RBRACE ELSE statement','ifblock',9,'p_ifblock2','better.py',774),
  ('whileblock -> WHILE LPAREN conditional RPAREN LBRACE fbody RBRACE','whileblock',7,'p_while','better.py',779),
  ('conditional -> conditionbase','conditional',1,'p_conditional','better.py',785),
  ('conditional -> conditional LESSTHANEQ conditional','conditional',3,'p_conditional','better.py',786),
  ('conditional -> conditional GREATERTHANEQ conditional','conditional',3,'p_conditional','better.py',787),
  ('conditional -> conditional UNEQUAL conditional','conditional',3,'p_conditional','better.py',788),
  ('conditional -> conditional EQUALCHECK conditional','conditional',3,'p_conditional','better.py',789),
  ('conditional -> conditional LESSTHAN conditional','conditional',3,'p_conditional','better.py',790),
  ('conditional -> conditional GREATERTHAN conditional','conditional',3,'p_conditional','better.py',791),
  ('conditional -> conditional ANDOPERATOR conditional','conditional',3,'p_conditional','better.py',792),
  ('conditional -> conditional OROPERATOR conditional','conditional',3,'p_conditional','better.py',793),
  ('conditionbase -> CS LESSTHANEQ CS','conditionbase',3,'p_conditionbase','better.py',817),
  ('conditionbase -> CS GREATERTHANEQ CS','conditionbase',3,'p_conditionbase','better.py',818),
  ('conditionbase -> CS UNEQUAL CS','conditionbase',3,'p_conditionbase','better.py',819),
  ('conditionbase -> CS EQUALCHECK CS','conditionbase',3,'p_conditionbase','better.py',820),
  ('conditionbase -> CS LESSTHAN CS','conditionbase',3,'p_conditionbase','better.py',821),
  ('conditionbase -> CS GREATERTHAN CS','conditionbase',3,'p_conditionbase','better.py',822),
  ('CS -> expression','CS',1,'p_cs','better.py',842),
  ('CS -> NOT LPAREN expression RPAREN','CS',4,'p_cs','better.py',843),
  ('declaration -> TYPE dlist1 SEMICOLON','declaration',3,'p_declaration1','better.py',851),
  ('dlist1 -> NAME','dlist1',1,'p_dlistname','better.py',857),
  ('dlist1 -> NAME COMMA dlist1','dlist1',3,'p_dlistname','better.py',858),
  ('dlist1 -> specialvar','dlist1',1,'p_dlistpointer','better.py',865),
  ('dlist1 -> specialvar COMMA dlist1','dlist1',3,'p_dlistpointer','better.py',866),
  ('specialvar -> TIMES specialvar','specialvar',2,'p_specialvar','better.py',873),
  ('specialvar -> TIMES NAME','specialvar',2,'p_specialvar','better.py',874),
  ('assignment -> assignment_base SEMICOLON','assignment',2,'p_assignment','better.py',879),
  ('assignment_base -> TIMES pointervar EQUALS expression','assignment_base',4,'p_assignment_base_pointer','better.py',888),
  ('assignment_base -> NAME EQUALS expression','assignment_base',3,'p_assignment_base_pointer','better.py',889),
  ('expression -> expression PLUS expression','expression',3,'p_expression1','better.py',909),
  ('expression -> expression MINUS expression','expression',3,'p_expression1','better.py',910),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression1','better.py',911),
  ('expression -> expression TIMES expression','expression',3,'p_expression_mul','better.py',928),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','better.py',936),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_paren','better.py',943),
  ('expression -> NUMBER','expression',1,'p_expression_base_number','better.py',949),
  ('expression -> pointervar','expression',1,'p_expression_base_pointer','better.py',955),
  ('pointervar -> TIMES pointervar','pointervar',2,'p_pointervar1','better.py',962),
  ('pointervar -> ADDROF pointervar','pointervar',2,'p_pointervar2','better.py',968),
  ('pointervar -> NAME','pointervar',1,'p_pointervar3','better.py',975),
]
