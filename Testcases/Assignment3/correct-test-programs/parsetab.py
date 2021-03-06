
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftOROPERATORleftANDOPERATORleftEQUALCHECKUNEQUALleftLESSTHANEQLESSTHANGREATERTHANEQGREATERTHANleftPLUSMINUSleftTIMESDIVIDErightVALOFADDROFrightNOTrightUMINUSNUMBER TYPE SEMICOLON EQUALS COMMA LPAREN RPAREN LBRACE RBRACE ANDOPERATOR OROPERATOR ADDROF NAME PLUS MINUS TIMES DIVIDE WHILE IF ELSE EQUALCHECK UNEQUAL LESSTHAN LESSTHANEQ GREATERTHAN GREATERTHANEQ NOT \n\tprogram : function \n\t\t\t\t| function program\n\t\n\tfunction : TYPE NAME LPAREN RPAREN LBRACE fbody RBRACE\n\t\n\tfbody : allstatement\n\t\t\t| allstatement fbody\n\t\n\tallstatement : statement\n\t\t\t\t| unmatchedstatement\n\t\n\tstatement : assignment\n\t\t\t| declaration\n\t\t\t| whileblock\n\t\t\t| ifblock\n\t\n\tunmatchedstatement : IF LPAREN conditional RPAREN allstatement\n\t\t\t\t| IF LPAREN conditional RPAREN statement ELSE unmatchedstatement\n\t\t\t\t| IF LPAREN conditional RPAREN LBRACE fbody RBRACE ELSE unmatchedstatement\n\t\n\tunmatchedstatement : IF LPAREN conditional RPAREN LBRACE fbody RBRACE\n\t\n\tifblock : IF LPAREN conditional RPAREN statement ELSE statement\n\t\t\t| IF LPAREN conditional RPAREN statement ELSE LBRACE fbody RBRACE\n\t\t\t| IF LPAREN conditional RPAREN LBRACE fbody RBRACE ELSE LBRACE fbody RBRACE\n\t\n\tifblock : IF LPAREN conditional RPAREN LBRACE fbody RBRACE ELSE statement\n\t\n\twhileblock : WHILE LPAREN conditional RPAREN LBRACE fbody RBRACE\n\t\n\tconditional : conditionbase\n\t\t\t\t| conditional LESSTHANEQ conditional\n\t\t\t\t| conditional GREATERTHANEQ conditional\n\t\t\t\t| conditional UNEQUAL conditional\n\t\t\t\t| conditional EQUALCHECK conditional\n\t\t\t\t| conditional LESSTHAN conditional\n\t\t\t\t| conditional GREATERTHAN conditional\n\t\t\t\t| conditional ANDOPERATOR conditional\n\t\t\t\t| conditional OROPERATOR conditional\n\t\n\tconditionbase : CS LESSTHANEQ CS\n\t\t\t\t| CS GREATERTHANEQ CS\n\t\t\t\t| CS UNEQUAL CS\n\t\t\t\t| CS EQUALCHECK CS\n\t\t\t\t| CS LESSTHAN CS\n\t\t\t\t| CS GREATERTHAN CS\n\t\n\tCS : expression\n\t\t| NOT LPAREN expression RPAREN\n\t\n\t\tdeclaration : TYPE dlist1 SEMICOLON\n\t\n\tdlist1 : NAME  \n\t\t\t| NAME COMMA dlist1\n\t\n\tdlist1 : specialvar\n\t\t\t| specialvar  COMMA dlist1  \n\t\n\tspecialvar : TIMES specialvar %prec VALOF\n\t\t\t\t| TIMES NAME %prec VALOF\n\t\n\tassignment : assignment_base SEMICOLON\n\t \n\tassignment_base : TIMES pointervar EQUALS expression\n\t\t\t| NAME EQUALS expression \n\t \n\texpression : expression PLUS expression\n\t\t\t\t| expression MINUS expression\n\t\t\t\t| expression DIVIDE expression\n\t\n\texpression : expression TIMES expression\n\t\n\texpression : MINUS expression %prec UMINUS\n\t\n\texpression : LPAREN expression RPAREN\n\t\n\texpression : NUMBER\n\t\n\texpression : pointervar\n\t\n\tpointervar : TIMES pointervar %prec VALOF\n\t\n\tpointervar : ADDROF pointervar \n\t\n\tpointervar : NAME\n\t'
    
_lr_action_items = {'TYPE':([0,2,8,12,13,14,15,16,17,18,28,31,37,64,87,88,89,105,106,110,111,112,113,114,116,117,118,119,120,122,],[3,3,9,9,-6,-7,-8,-9,-10,-11,-3,-45,-38,9,-12,-6,9,9,9,-16,-13,9,-15,-20,9,-17,9,-14,-19,-18,]),'$end':([1,2,4,28,],[0,-1,-2,-3,]),'NAME':([3,8,9,12,13,14,15,16,17,18,22,26,27,30,31,32,33,35,37,38,39,43,44,54,58,59,60,61,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,87,88,89,105,106,110,111,112,113,114,116,117,118,119,120,122,],[5,10,24,10,-6,-7,-8,-9,-10,-11,36,41,36,36,-45,36,36,36,-38,24,24,36,36,36,36,36,36,36,10,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-12,-6,10,10,10,-16,-13,10,-15,-20,10,-17,10,-14,-19,-18,]),'LPAREN':([5,19,21,27,30,32,43,44,51,54,58,59,60,61,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,],[6,30,32,44,44,44,44,44,79,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'RPAREN':([6,36,45,46,47,48,50,52,53,55,62,63,82,83,84,85,86,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,108,],[7,-58,-54,-55,64,-21,-36,80,-56,-57,-52,86,-48,-49,-50,-51,-53,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,108,-37,]),'LBRACE':([7,64,80,106,116,],[8,89,105,112,118,]),'IF':([8,12,13,14,15,16,17,18,31,37,64,87,88,89,105,106,110,111,112,113,114,116,117,118,119,120,122,],[19,19,-6,-7,-8,-9,-10,-11,-45,-38,19,-12,-6,19,19,19,-16,-13,19,-15,-20,19,-17,19,-14,-19,-18,]),'WHILE':([8,12,13,14,15,16,17,18,31,37,64,87,88,89,105,106,110,111,112,113,114,116,117,118,119,120,122,],[21,21,-6,-7,-8,-9,-10,-11,-45,-38,21,-12,-6,21,21,21,-16,-13,21,-15,-20,21,-17,21,-14,-19,-18,]),'TIMES':([8,9,12,13,14,15,16,17,18,22,26,27,30,31,32,33,35,36,37,38,39,42,43,44,45,46,50,53,54,55,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,85,86,87,88,89,104,105,106,110,111,112,113,114,116,117,118,119,120,122,],[22,26,22,-6,-7,-8,-9,-10,-11,33,26,33,33,-45,33,33,33,-58,-38,26,26,61,33,33,-54,-55,61,-56,33,-57,33,33,33,33,-52,61,22,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,61,61,61,-50,-51,-53,-12,-6,22,61,22,22,-16,-13,22,-15,-20,22,-17,22,-14,-19,-18,]),'EQUALS':([10,34,36,53,55,],[27,54,-58,-56,-57,]),'RBRACE':([11,12,13,14,15,16,17,18,29,31,37,87,88,107,109,110,111,113,114,115,117,119,120,121,122,],[28,-4,-6,-7,-8,-9,-10,-11,-5,-45,-38,-12,-6,113,114,-16,-13,-15,-20,117,-17,-14,-19,122,-18,]),'ELSE':([15,16,17,18,31,37,88,110,113,114,117,120,122,],[-8,-9,-10,-11,-45,-38,106,-16,116,-20,-17,-19,-18,]),'SEMICOLON':([20,23,24,25,36,40,41,42,45,46,53,55,56,57,62,81,82,83,84,85,86,],[31,37,-39,-41,-58,-43,-44,-47,-54,-55,-56,-57,-40,-42,-52,-46,-48,-49,-50,-51,-53,]),'ADDROF':([22,27,30,32,33,35,43,44,54,58,59,60,61,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'COMMA':([24,25,40,41,],[38,39,-43,-44,]),'MINUS':([27,30,32,36,42,43,44,45,46,50,53,54,55,58,59,60,61,62,63,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,85,86,104,],[43,43,43,-58,59,43,43,-54,-55,59,-56,43,-57,43,43,43,43,-52,59,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,59,-48,-49,-50,-51,-53,59,]),'NUMBER':([27,30,32,43,44,54,58,59,60,61,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'NOT':([30,32,65,66,67,68,69,70,71,72,73,74,75,76,77,78,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'PLUS':([36,42,45,46,50,53,55,62,63,81,82,83,84,85,86,104,],[-58,58,-54,-55,58,-56,-57,-52,58,58,-48,-49,-50,-51,-53,58,]),'DIVIDE':([36,42,45,46,50,53,55,62,63,81,82,83,84,85,86,104,],[-58,60,-54,-55,60,-56,-57,-52,60,60,60,60,-50,-51,-53,60,]),'LESSTHANEQ':([36,45,46,47,48,49,50,52,53,55,62,82,83,84,85,86,90,91,92,93,94,95,96,97,98,99,100,101,102,103,108,],[-58,-54,-55,65,-21,73,-36,65,-56,-57,-52,-48,-49,-50,-51,-53,-22,-23,65,65,-26,-27,65,65,-30,-31,-32,-33,-34,-35,-37,]),'GREATERTHANEQ':([36,45,46,47,48,49,50,52,53,55,62,82,83,84,85,86,90,91,92,93,94,95,96,97,98,99,100,101,102,103,108,],[-58,-54,-55,66,-21,74,-36,66,-56,-57,-52,-48,-49,-50,-51,-53,-22,-23,66,66,-26,-27,66,66,-30,-31,-32,-33,-34,-35,-37,]),'UNEQUAL':([36,45,46,47,48,49,50,52,53,55,62,82,83,84,85,86,90,91,92,93,94,95,96,97,98,99,100,101,102,103,108,],[-58,-54,-55,67,-21,75,-36,67,-56,-57,-52,-48,-49,-50,-51,-53,-22,-23,-24,-25,-26,-27,67,67,-30,-31,-32,-33,-34,-35,-37,]),'EQUALCHECK':([36,45,46,47,48,49,50,52,53,55,62,82,83,84,85,86,90,91,92,93,94,95,96,97,98,99,100,101,102,103,108,],[-58,-54,-55,68,-21,76,-36,68,-56,-57,-52,-48,-49,-50,-51,-53,-22,-23,-24,-25,-26,-27,68,68,-30,-31,-32,-33,-34,-35,-37,]),'LESSTHAN':([36,45,46,47,48,49,50,52,53,55,62,82,83,84,85,86,90,91,92,93,94,95,96,97,98,99,100,101,102,103,108,],[-58,-54,-55,69,-21,77,-36,69,-56,-57,-52,-48,-49,-50,-51,-53,-22,-23,69,69,-26,-27,69,69,-30,-31,-32,-33,-34,-35,-37,]),'GREATERTHAN':([36,45,46,47,48,49,50,52,53,55,62,82,83,84,85,86,90,91,92,93,94,95,96,97,98,99,100,101,102,103,108,],[-58,-54,-55,70,-21,78,-36,70,-56,-57,-52,-48,-49,-50,-51,-53,-22,-23,70,70,-26,-27,70,70,-30,-31,-32,-33,-34,-35,-37,]),'ANDOPERATOR':([36,45,46,47,48,50,52,53,55,62,82,83,84,85,86,90,91,92,93,94,95,96,97,98,99,100,101,102,103,108,],[-58,-54,-55,71,-21,-36,71,-56,-57,-52,-48,-49,-50,-51,-53,-22,-23,-24,-25,-26,-27,-28,71,-30,-31,-32,-33,-34,-35,-37,]),'OROPERATOR':([36,45,46,47,48,50,52,53,55,62,82,83,84,85,86,90,91,92,93,94,95,96,97,98,99,100,101,102,103,108,],[-58,-54,-55,72,-21,-36,72,-56,-57,-52,-48,-49,-50,-51,-53,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-37,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,2,],[1,4,]),'function':([0,2,],[2,2,]),'fbody':([8,12,89,105,112,118,],[11,29,107,109,115,121,]),'allstatement':([8,12,64,89,105,112,118,],[12,12,87,12,12,12,12,]),'statement':([8,12,64,89,105,106,112,116,118,],[13,13,88,13,13,110,13,120,13,]),'unmatchedstatement':([8,12,64,89,105,106,112,116,118,],[14,14,14,14,14,111,14,119,14,]),'assignment':([8,12,64,89,105,106,112,116,118,],[15,15,15,15,15,15,15,15,15,]),'declaration':([8,12,64,89,105,106,112,116,118,],[16,16,16,16,16,16,16,16,16,]),'whileblock':([8,12,64,89,105,106,112,116,118,],[17,17,17,17,17,17,17,17,17,]),'ifblock':([8,12,64,89,105,106,112,116,118,],[18,18,18,18,18,18,18,18,18,]),'assignment_base':([8,12,64,89,105,106,112,116,118,],[20,20,20,20,20,20,20,20,20,]),'dlist1':([9,38,39,],[23,56,57,]),'specialvar':([9,26,38,39,],[25,40,25,25,]),'pointervar':([22,27,30,32,33,35,43,44,54,58,59,60,61,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,],[34,46,46,46,53,55,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'expression':([27,30,32,43,44,54,58,59,60,61,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,],[42,50,50,62,63,81,82,83,84,85,50,50,50,50,50,50,50,50,50,50,50,50,50,50,104,]),'conditional':([30,32,65,66,67,68,69,70,71,72,],[47,52,90,91,92,93,94,95,96,97,]),'conditionbase':([30,32,65,66,67,68,69,70,71,72,],[48,48,48,48,48,48,48,48,48,48,]),'CS':([30,32,65,66,67,68,69,70,71,72,73,74,75,76,77,78,],[49,49,49,49,49,49,49,49,49,49,98,99,100,101,102,103,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> function','program',1,'p_program','150070001-150070018.py',449),
  ('program -> function program','program',2,'p_program','150070001-150070018.py',450),
  ('function -> TYPE NAME LPAREN RPAREN LBRACE fbody RBRACE','function',7,'p_function','150070001-150070018.py',474),
  ('fbody -> allstatement','fbody',1,'p_fbody','150070001-150070018.py',511),
  ('fbody -> allstatement fbody','fbody',2,'p_fbody','150070001-150070018.py',512),
  ('allstatement -> statement','allstatement',1,'p_allstatement_expr','150070001-150070018.py',529),
  ('allstatement -> unmatchedstatement','allstatement',1,'p_allstatement_expr','150070001-150070018.py',530),
  ('statement -> assignment','statement',1,'p_statement_expr','150070001-150070018.py',536),
  ('statement -> declaration','statement',1,'p_statement_expr','150070001-150070018.py',537),
  ('statement -> whileblock','statement',1,'p_statement_expr','150070001-150070018.py',538),
  ('statement -> ifblock','statement',1,'p_statement_expr','150070001-150070018.py',539),
  ('unmatchedstatement -> IF LPAREN conditional RPAREN allstatement','unmatchedstatement',5,'p_unmatchedstatement_expr1','150070001-150070018.py',545),
  ('unmatchedstatement -> IF LPAREN conditional RPAREN statement ELSE unmatchedstatement','unmatchedstatement',7,'p_unmatchedstatement_expr1','150070001-150070018.py',546),
  ('unmatchedstatement -> IF LPAREN conditional RPAREN LBRACE fbody RBRACE ELSE unmatchedstatement','unmatchedstatement',9,'p_unmatchedstatement_expr1','150070001-150070018.py',547),
  ('unmatchedstatement -> IF LPAREN conditional RPAREN LBRACE fbody RBRACE','unmatchedstatement',7,'p_unmatchedstatement_expr2','150070001-150070018.py',558),
  ('ifblock -> IF LPAREN conditional RPAREN statement ELSE statement','ifblock',7,'p_ifblock1','150070001-150070018.py',564),
  ('ifblock -> IF LPAREN conditional RPAREN statement ELSE LBRACE fbody RBRACE','ifblock',9,'p_ifblock1','150070001-150070018.py',565),
  ('ifblock -> IF LPAREN conditional RPAREN LBRACE fbody RBRACE ELSE LBRACE fbody RBRACE','ifblock',11,'p_ifblock1','150070001-150070018.py',566),
  ('ifblock -> IF LPAREN conditional RPAREN LBRACE fbody RBRACE ELSE statement','ifblock',9,'p_ifblock2','150070001-150070018.py',577),
  ('whileblock -> WHILE LPAREN conditional RPAREN LBRACE fbody RBRACE','whileblock',7,'p_while','150070001-150070018.py',582),
  ('conditional -> conditionbase','conditional',1,'p_conditional','150070001-150070018.py',588),
  ('conditional -> conditional LESSTHANEQ conditional','conditional',3,'p_conditional','150070001-150070018.py',589),
  ('conditional -> conditional GREATERTHANEQ conditional','conditional',3,'p_conditional','150070001-150070018.py',590),
  ('conditional -> conditional UNEQUAL conditional','conditional',3,'p_conditional','150070001-150070018.py',591),
  ('conditional -> conditional EQUALCHECK conditional','conditional',3,'p_conditional','150070001-150070018.py',592),
  ('conditional -> conditional LESSTHAN conditional','conditional',3,'p_conditional','150070001-150070018.py',593),
  ('conditional -> conditional GREATERTHAN conditional','conditional',3,'p_conditional','150070001-150070018.py',594),
  ('conditional -> conditional ANDOPERATOR conditional','conditional',3,'p_conditional','150070001-150070018.py',595),
  ('conditional -> conditional OROPERATOR conditional','conditional',3,'p_conditional','150070001-150070018.py',596),
  ('conditionbase -> CS LESSTHANEQ CS','conditionbase',3,'p_conditionbase','150070001-150070018.py',620),
  ('conditionbase -> CS GREATERTHANEQ CS','conditionbase',3,'p_conditionbase','150070001-150070018.py',621),
  ('conditionbase -> CS UNEQUAL CS','conditionbase',3,'p_conditionbase','150070001-150070018.py',622),
  ('conditionbase -> CS EQUALCHECK CS','conditionbase',3,'p_conditionbase','150070001-150070018.py',623),
  ('conditionbase -> CS LESSTHAN CS','conditionbase',3,'p_conditionbase','150070001-150070018.py',624),
  ('conditionbase -> CS GREATERTHAN CS','conditionbase',3,'p_conditionbase','150070001-150070018.py',625),
  ('CS -> expression','CS',1,'p_cs','150070001-150070018.py',645),
  ('CS -> NOT LPAREN expression RPAREN','CS',4,'p_cs','150070001-150070018.py',646),
  ('declaration -> TYPE dlist1 SEMICOLON','declaration',3,'p_declaration1','150070001-150070018.py',654),
  ('dlist1 -> NAME','dlist1',1,'p_dlistname','150070001-150070018.py',660),
  ('dlist1 -> NAME COMMA dlist1','dlist1',3,'p_dlistname','150070001-150070018.py',661),
  ('dlist1 -> specialvar','dlist1',1,'p_dlistpointer','150070001-150070018.py',668),
  ('dlist1 -> specialvar COMMA dlist1','dlist1',3,'p_dlistpointer','150070001-150070018.py',669),
  ('specialvar -> TIMES specialvar','specialvar',2,'p_specialvar','150070001-150070018.py',676),
  ('specialvar -> TIMES NAME','specialvar',2,'p_specialvar','150070001-150070018.py',677),
  ('assignment -> assignment_base SEMICOLON','assignment',2,'p_assignment','150070001-150070018.py',682),
  ('assignment_base -> TIMES pointervar EQUALS expression','assignment_base',4,'p_assignment_base_pointer','150070001-150070018.py',691),
  ('assignment_base -> NAME EQUALS expression','assignment_base',3,'p_assignment_base_pointer','150070001-150070018.py',692),
  ('expression -> expression PLUS expression','expression',3,'p_expression1','150070001-150070018.py',712),
  ('expression -> expression MINUS expression','expression',3,'p_expression1','150070001-150070018.py',713),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression1','150070001-150070018.py',714),
  ('expression -> expression TIMES expression','expression',3,'p_expression_mul','150070001-150070018.py',731),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','150070001-150070018.py',739),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_paren','150070001-150070018.py',746),
  ('expression -> NUMBER','expression',1,'p_expression_base_number','150070001-150070018.py',752),
  ('expression -> pointervar','expression',1,'p_expression_base_pointer','150070001-150070018.py',758),
  ('pointervar -> TIMES pointervar','pointervar',2,'p_pointervar1','150070001-150070018.py',765),
  ('pointervar -> ADDROF pointervar','pointervar',2,'p_pointervar2','150070001-150070018.py',771),
  ('pointervar -> NAME','pointervar',1,'p_pointervar3','150070001-150070018.py',778),
]
