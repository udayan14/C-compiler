
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftOROPERATORleftANDOPERATORleftEQUALCHECKUNEQUALleftLESSTHANEQLESSTHANGREATERTHANEQGREATERTHANleftPLUSMINUSleftTIMESDIVIDErightVALOFADDROFrightNOTrightUMINUSNUMBER FLOAT TYPE SEMICOLON EQUALS COMMA LPAREN RPAREN LBRACE RBRACE ANDOPERATOR OROPERATOR ADDROF NAME PLUS MINUS TIMES DIVIDE WHILE IF ELSE RETURN EQUALCHECK UNEQUAL LESSTHAN LESSTHANEQ GREATERTHAN GREATERTHANEQ NOT\n\tmaster : program\n\t \n\tprogram : function \n\t\t\t\t| function program\n\t\t\t\t| declaration program\n\t\n\tprogram : prototype program\n\t\n\tprototype : TYPE NAME LPAREN paramlist RPAREN SEMICOLON\n\t\n\tfunction : TYPE NAME LPAREN paramlist RPAREN LBRACE fbody RBRACE\n\t\n\tparamlist : \n\t\t\t| TYPE NAME paramlist2\n\t\t\t| TYPE specialvar paramlist2\n\t\n\tparamlist2 : \n\t\t\t|  COMMA TYPE NAME paramlist2\n\t\t\t|  COMMA TYPE specialvar paramlist2\n\t\n\tfbody : allstatement fbody\n\t\t\t| \n\t\n\tallstatement : statement\n\t\t\t\t| unmatchedstatement\n\t\n\tstatement : assignment\n\t\t\t| declaration\n\t\t\t| whileblock\n\t\t\t| ifblock\n\t\t\t| returnstatement\n\t\t\t| functioncall\n\t\n\treturnstatement : RETURN expression SEMICOLON\n\t\n\tfunctioncall : NAME LPAREN arguments RPAREN SEMICOLON\n\t\n\targuments : expression \n\t\t\t\t| expression COMMA arguments\n\t\n\tstatement : SEMICOLON\n\t\n\tunmatchedstatement : IF LPAREN conditional RPAREN allstatement\n\t\t\t\t| IF LPAREN conditional RPAREN statement ELSE unmatchedstatement\n\t\t\t\t| IF LPAREN conditional RPAREN LBRACE fbody RBRACE ELSE unmatchedstatement\n\t\n\tunmatchedstatement : IF LPAREN conditional RPAREN LBRACE fbody RBRACE\n\t\n\tifblock : IF LPAREN conditional RPAREN statement ELSE statement\n\t\t\t| IF LPAREN conditional RPAREN statement ELSE LBRACE fbody RBRACE\n\t\t\t| IF LPAREN conditional RPAREN LBRACE fbody RBRACE ELSE LBRACE fbody RBRACE\n\t\n\tifblock : IF LPAREN conditional RPAREN LBRACE fbody RBRACE ELSE statement\n\t\n\twhileblock : WHILE LPAREN conditional RPAREN LBRACE fbody RBRACE\n\t\n\tconditional : LPAREN conditional RPAREN\n\t\n\tconditional : conditionbase\n\t\t\t\t| NOT LPAREN conditional RPAREN\n\t\t\t\t| conditional LESSTHANEQ conditional\n\t\t\t\t| conditional GREATERTHANEQ conditional\n\t\t\t\t| conditional UNEQUAL conditional\n\t\t\t\t| conditional EQUALCHECK conditional\n\t\t\t\t| conditional LESSTHAN conditional\n\t\t\t\t| conditional GREATERTHAN conditional\n\t\t\t\t| conditional ANDOPERATOR conditional\n\t\t\t\t| conditional OROPERATOR conditional\n\t\n\tconditionbase : CS LESSTHANEQ CS\n\t\t\t\t| CS GREATERTHANEQ CS\n\t\t\t\t| CS UNEQUAL CS\n\t\t\t\t| CS EQUALCHECK CS\n\t\t\t\t| CS LESSTHAN CS\n\t\t\t\t| CS GREATERTHAN CS\n\t\n\tCS : expression\n\t\t| NOT LPAREN expression RPAREN\n\t\n\t\tdeclaration : TYPE dlist1 SEMICOLON\n\t\n\tdlist1 : NAME  \n\t\t\t| NAME COMMA dlist1\n\t\n\tdlist1 : specialvar\n\t\t\t| specialvar  COMMA dlist1  \n\t\n\tspecialvar : TIMES specialvar %prec VALOF\n\t\n\tspecialvar : TIMES NAME %prec VALOF\n\t\n\tassignment : assignment_base SEMICOLON\n\t \n\tassignment_base : TIMES pointervar EQUALS expression\n\t\t\t| NAME EQUALS expression \n\t \n\texpression : expression PLUS expression\n\t\t\t\t| expression MINUS expression\n\t\t\t\t| expression DIVIDE expression\n\t\n\texpression : expression TIMES expression\n\t\n\texpression : MINUS expression %prec UMINUS\n\t\n\texpression : LPAREN expression RPAREN\n\t\n\texpression : FLOAT\n\t\t\t\t| NUMBER\n\t\n\texpression : pointervar\n\t\n\tpointervar : TIMES pointervar %prec VALOF\n\t\n\tpointervar : ADDROF pointervar \n\t\n\tpointervar : NAME\n\t'
    
_lr_action_items = {'COMMA':([7,9,15,16,20,25,26,52,53,59,65,67,69,79,81,84,92,115,116,117,118,119,],[14,17,-63,-62,17,28,28,28,28,-78,-75,-73,-74,-76,-77,113,-71,-68,-67,-70,-69,-72,]),'EQUALCHECK':([59,65,67,69,73,75,76,78,79,81,85,92,109,110,115,116,117,118,119,120,121,122,124,125,126,127,128,130,131,132,133,134,135,136,137,138,144,145,],[-78,-75,-73,-74,-39,95,101,-55,-76,-77,101,-71,101,-55,-68,-67,-70,-69,-72,101,-55,-51,-52,-53,-49,-50,-54,-44,101,-42,-43,-45,-41,101,-46,-38,-40,-56,]),'$end':([2,3,6,11,12,13,55,],[-1,0,-2,-4,-5,-3,-7,]),'FLOAT':([51,54,60,61,62,68,70,77,80,86,87,89,90,93,94,95,96,97,98,99,101,102,103,104,105,106,107,108,113,146,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'LESSTHAN':([59,65,67,69,73,75,76,78,79,81,85,92,109,110,115,116,117,118,119,120,121,122,124,125,126,127,128,130,131,132,133,134,135,136,137,138,144,145,],[-78,-75,-73,-74,-39,96,105,-55,-76,-77,105,-71,105,-55,-68,-67,-70,-69,-72,105,-55,-51,-52,-53,-49,-50,-54,105,105,-42,105,-45,-41,105,-46,-38,-40,-56,]),'LBRACE':([27,100,114,149,156,],[32,129,141,154,159,]),'GREATERTHAN':([59,65,67,69,73,75,76,78,79,81,85,92,109,110,115,116,117,118,119,120,121,122,124,125,126,127,128,130,131,132,133,134,135,136,137,138,144,145,],[-78,-75,-73,-74,-39,99,108,-55,-76,-77,108,-71,108,-55,-68,-67,-70,-69,-72,108,-55,-51,-52,-53,-49,-50,-54,108,108,-42,108,-45,-41,108,-46,-38,-40,-56,]),'UNEQUAL':([59,65,67,69,73,75,76,78,79,81,85,92,109,110,115,116,117,118,119,120,121,122,124,125,126,127,128,130,131,132,133,134,135,136,137,138,144,145,],[-78,-75,-73,-74,-39,94,104,-55,-76,-77,104,-71,104,-55,-68,-67,-70,-69,-72,104,-55,-51,-52,-53,-49,-50,-54,-44,104,-42,-43,-45,-41,104,-46,-38,-40,-56,]),'NUMBER':([51,54,60,61,62,68,70,77,80,86,87,89,90,93,94,95,96,97,98,99,101,102,103,104,105,106,107,108,113,146,],[69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,]),'DIVIDE':([59,65,66,67,69,78,79,81,82,84,91,92,110,111,115,116,117,118,119,121,150,],[-78,-75,90,-73,-74,90,-76,-77,90,90,90,-71,90,90,90,90,-70,-69,-72,90,90,]),'RBRACE':([19,32,34,35,36,38,39,41,43,46,47,48,50,63,64,88,129,139,141,142,143,147,148,151,152,153,154,155,157,158,159,160,161,162,163,],[-57,-15,-17,-22,-18,55,-19,-16,-20,-15,-28,-23,-21,-14,-64,-24,-15,-25,-15,-16,-29,151,152,-37,-32,-30,-15,-33,161,-31,-15,-36,-34,163,-35,]),'TIMES':([1,8,14,17,19,23,32,33,34,35,36,39,40,41,43,44,46,47,48,50,51,54,56,58,59,60,61,62,64,65,66,67,68,69,70,77,78,79,80,81,82,84,86,87,88,89,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,108,110,111,113,114,115,116,117,118,119,121,129,139,141,142,143,146,149,150,151,152,153,154,155,156,158,159,160,161,163,],[8,8,8,8,-57,8,40,8,-17,-22,-18,-19,56,-16,-20,8,40,-28,-23,-21,56,56,56,56,-78,56,56,56,-64,-75,89,-73,56,-74,56,56,89,-76,56,-77,89,89,56,56,-24,56,56,89,-71,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,89,89,56,40,89,89,-70,-69,-72,89,40,-25,40,-16,-29,56,40,89,-37,-32,-30,40,-33,40,-31,40,-36,-34,-35,]),'NAME':([1,8,14,17,19,23,32,33,34,35,36,39,40,41,43,44,46,47,48,50,51,54,56,58,60,61,62,64,68,70,77,80,86,87,88,89,90,93,94,95,96,97,98,99,101,102,103,104,105,106,107,108,113,114,129,139,141,142,143,146,149,151,152,153,154,155,156,158,159,160,161,163,],[9,15,20,20,-57,25,42,52,-17,-22,-18,-19,59,-16,-20,20,42,-28,-23,-21,59,59,59,59,59,59,59,-64,59,59,59,59,59,59,-24,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,42,42,-25,42,-16,-29,59,42,-37,-32,-30,42,-33,42,-31,42,-36,-34,-35,]),'PLUS':([59,65,66,67,69,78,79,81,82,84,91,92,110,111,115,116,117,118,119,121,150,],[-78,-75,87,-73,-74,87,-76,-77,87,87,87,-71,87,87,-68,-67,-70,-69,-72,87,87,]),'RPAREN':([15,16,18,24,25,26,29,30,52,53,59,65,67,69,71,72,73,76,78,79,81,83,84,85,91,92,109,110,115,116,117,118,119,120,121,122,124,125,126,127,128,130,131,132,133,134,135,136,137,138,140,144,145,150,],[-63,-62,-8,27,-11,-11,-9,-10,-11,-11,-78,-75,-73,-74,-12,-13,-39,100,-55,-76,-77,112,-26,114,119,-71,138,119,-68,-67,-70,-69,-72,144,145,-51,-52,-53,-49,-50,-54,-44,-47,-42,-43,-45,-41,-48,-46,-38,-27,-40,-56,145,]),'TYPE':([0,4,5,6,18,19,28,31,32,34,35,36,39,41,43,46,47,48,50,55,64,88,114,129,139,141,142,143,149,151,152,153,154,155,156,158,159,160,161,163,],[1,1,1,1,23,-57,33,-6,44,-17,-22,-18,-19,-16,-20,44,-28,-23,-21,-7,-64,-24,44,44,-25,44,-16,-29,44,-37,-32,-30,44,-33,44,-31,44,-36,-34,-35,]),'RETURN':([19,32,34,35,36,39,41,43,46,47,48,50,64,88,114,129,139,141,142,143,149,151,152,153,154,155,156,158,159,160,161,163,],[-57,51,-17,-22,-18,-19,-16,-20,51,-28,-23,-21,-64,-24,51,51,-25,51,-16,-29,51,-37,-32,-30,51,-33,51,-31,51,-36,-34,-35,]),'EQUALS':([42,57,59,79,81,],[60,80,-78,-76,-77,]),'ELSE':([19,35,36,39,43,47,48,50,64,88,139,142,151,152,155,160,161,163,],[-57,-22,-18,-19,-20,-28,-23,-21,-64,-24,-25,149,-37,156,-33,-36,-34,-35,]),'IF':([19,32,34,35,36,39,41,43,46,47,48,50,64,88,114,129,139,141,142,143,149,151,152,153,154,155,156,158,159,160,161,163,],[-57,45,-17,-22,-18,-19,-16,-20,45,-28,-23,-21,-64,-24,45,45,-25,45,-16,-29,45,-37,-32,-30,45,-33,45,-31,45,-36,-34,-35,]),'SEMICOLON':([7,9,10,15,16,19,20,21,22,27,32,34,35,36,39,41,43,46,47,48,49,50,59,64,65,66,67,69,79,81,82,88,92,111,112,114,115,116,117,118,119,129,139,141,142,143,149,151,152,153,154,155,156,158,159,160,161,163,],[-60,-58,19,-63,-62,-57,-58,-61,-59,31,47,-17,-22,-18,-19,-16,-20,47,-28,-23,64,-21,-78,-64,-75,88,-73,-74,-76,-77,-66,-24,-71,-65,139,47,-68,-67,-70,-69,-72,47,-25,47,-16,-29,47,-37,-32,-30,47,-33,47,-31,47,-36,-34,-35,]),'GREATERTHANEQ':([59,65,67,69,73,75,76,78,79,81,85,92,109,110,115,116,117,118,119,120,121,122,124,125,126,127,128,130,131,132,133,134,135,136,137,138,144,145,],[-78,-75,-73,-74,-39,98,103,-55,-76,-77,103,-71,103,-55,-68,-67,-70,-69,-72,103,-55,-51,-52,-53,-49,-50,-54,103,103,-42,103,-45,-41,103,-46,-38,-40,-56,]),'WHILE':([19,32,34,35,36,39,41,43,46,47,48,50,64,88,114,129,139,141,142,143,149,151,152,153,154,155,156,158,159,160,161,163,],[-57,37,-17,-22,-18,-19,-16,-20,37,-28,-23,-21,-64,-24,37,37,-25,37,-16,-29,37,-37,-32,-30,37,-33,37,-31,37,-36,-34,-35,]),'LPAREN':([9,37,42,45,51,54,60,61,62,68,70,74,77,80,86,87,89,90,93,94,95,96,97,98,99,101,102,103,104,105,106,107,108,113,123,146,],[18,54,61,62,68,77,68,68,77,68,68,93,77,68,68,68,68,68,77,68,68,68,68,68,68,77,77,77,77,77,77,77,77,68,146,68,]),'OROPERATOR':([59,65,67,69,73,76,78,79,81,85,92,109,115,116,117,118,119,120,122,124,125,126,127,128,130,131,132,133,134,135,136,137,138,144,145,],[-78,-75,-73,-74,-39,107,-55,-76,-77,107,-71,107,-68,-67,-70,-69,-72,107,-51,-52,-53,-49,-50,-54,-44,-47,-42,-43,-45,-41,-48,-46,-38,-40,-56,]),'MINUS':([51,54,59,60,61,62,65,66,67,68,69,70,77,78,79,80,81,82,84,86,87,89,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,108,110,111,113,115,116,117,118,119,121,146,150,],[70,70,-78,70,70,70,-75,86,-73,70,-74,70,70,86,-76,70,-77,86,86,70,70,70,70,86,-71,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,86,86,70,-68,-67,-70,-69,-72,86,70,86,]),'NOT':([54,62,77,93,94,95,96,97,98,99,101,102,103,104,105,106,107,108,],[74,74,74,74,123,123,123,123,123,123,74,74,74,74,74,74,74,74,]),'LESSTHANEQ':([59,65,67,69,73,75,76,78,79,81,85,92,109,110,115,116,117,118,119,120,121,122,124,125,126,127,128,130,131,132,133,134,135,136,137,138,144,145,],[-78,-75,-73,-74,-39,97,106,-55,-76,-77,106,-71,106,-55,-68,-67,-70,-69,-72,106,-55,-51,-52,-53,-49,-50,-54,106,106,-42,106,-45,-41,106,-46,-38,-40,-56,]),'ANDOPERATOR':([59,65,67,69,73,76,78,79,81,85,92,109,115,116,117,118,119,120,122,124,125,126,127,128,130,131,132,133,134,135,136,137,138,144,145,],[-78,-75,-73,-74,-39,102,-55,-76,-77,102,-71,102,-68,-67,-70,-69,-72,102,-51,-52,-53,-49,-50,-54,-44,-47,-42,-43,-45,-41,102,-46,-38,-40,-56,]),'ADDROF':([40,51,54,56,58,60,61,62,68,70,77,80,86,87,89,90,93,94,95,96,97,98,99,101,102,103,104,105,106,107,108,113,146,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'unmatchedstatement':([32,46,114,129,141,149,154,156,159,],[34,34,34,34,34,153,34,158,34,]),'functioncall':([32,46,114,129,141,149,154,156,159,],[48,48,48,48,48,48,48,48,48,]),'paramlist2':([25,26,52,53,],[29,30,71,72,]),'master':([0,],[3,]),'CS':([54,62,77,93,94,95,96,97,98,99,101,102,103,104,105,106,107,108,],[75,75,75,75,122,124,125,126,127,128,75,75,75,75,75,75,75,75,]),'fbody':([32,46,129,141,154,159,],[38,63,147,148,157,162,]),'declaration':([0,4,5,6,32,46,114,129,141,149,154,156,159,],[4,4,4,4,39,39,39,39,39,39,39,39,39,]),'assignment_base':([32,46,114,129,141,149,154,156,159,],[49,49,49,49,49,49,49,49,49,]),'conditionbase':([54,62,77,93,101,102,103,104,105,106,107,108,],[73,73,73,73,73,73,73,73,73,73,73,73,]),'function':([0,4,5,6,],[6,6,6,6,]),'statement':([32,46,114,129,141,149,154,156,159,],[41,41,142,41,41,155,41,160,41,]),'whileblock':([32,46,114,129,141,149,154,156,159,],[43,43,43,43,43,43,43,43,43,]),'assignment':([32,46,114,129,141,149,154,156,159,],[36,36,36,36,36,36,36,36,36,]),'conditional':([54,62,77,93,101,102,103,104,105,106,107,108,],[76,85,109,120,130,131,132,133,134,135,136,137,]),'program':([0,4,5,6,],[2,11,12,13,]),'pointervar':([40,51,54,56,58,60,61,62,68,70,77,80,86,87,89,90,93,94,95,96,97,98,99,101,102,103,104,105,106,107,108,113,146,],[57,65,65,79,81,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,]),'allstatement':([32,46,114,129,141,154,159,],[46,46,143,46,46,46,46,]),'returnstatement':([32,46,114,129,141,149,154,156,159,],[35,35,35,35,35,35,35,35,35,]),'paramlist':([18,],[24,]),'specialvar':([1,8,14,17,23,33,44,],[7,16,7,7,26,53,7,]),'arguments':([61,113,],[83,140,]),'ifblock':([32,46,114,129,141,149,154,156,159,],[50,50,50,50,50,50,50,50,50,]),'dlist1':([1,14,17,44,],[10,21,22,10,]),'prototype':([0,4,5,6,],[5,5,5,5,]),'expression':([51,54,60,61,62,68,70,77,80,86,87,89,90,93,94,95,96,97,98,99,101,102,103,104,105,106,107,108,113,146,],[66,78,82,84,78,91,92,110,111,115,116,117,118,121,78,78,78,78,78,78,78,78,78,78,78,78,78,78,84,150,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> master","S'",1,None,None,None),
  ('master -> program','master',1,'p_masterprogram','Parser.py',274),
  ('program -> function','program',1,'p_program','Parser.py',299),
  ('program -> function program','program',2,'p_program','Parser.py',300),
  ('program -> declaration program','program',2,'p_program','Parser.py',301),
  ('program -> prototype program','program',2,'p_program1','Parser.py',330),
  ('prototype -> TYPE NAME LPAREN paramlist RPAREN SEMICOLON','prototype',6,'p_prototype','Parser.py',351),
  ('function -> TYPE NAME LPAREN paramlist RPAREN LBRACE fbody RBRACE','function',8,'p_function','Parser.py',376),
  ('paramlist -> <empty>','paramlist',0,'p_paramlist','Parser.py',414),
  ('paramlist -> TYPE NAME paramlist2','paramlist',3,'p_paramlist','Parser.py',415),
  ('paramlist -> TYPE specialvar paramlist2','paramlist',3,'p_paramlist','Parser.py',416),
  ('paramlist2 -> <empty>','paramlist2',0,'p_paramlist2','Parser.py',427),
  ('paramlist2 -> COMMA TYPE NAME paramlist2','paramlist2',4,'p_paramlist2','Parser.py',428),
  ('paramlist2 -> COMMA TYPE specialvar paramlist2','paramlist2',4,'p_paramlist2','Parser.py',429),
  ('fbody -> allstatement fbody','fbody',2,'p_fbody','Parser.py',440),
  ('fbody -> <empty>','fbody',0,'p_fbody','Parser.py',441),
  ('allstatement -> statement','allstatement',1,'p_allstatement_expr','Parser.py',464),
  ('allstatement -> unmatchedstatement','allstatement',1,'p_allstatement_expr','Parser.py',465),
  ('statement -> assignment','statement',1,'p_statement_expr','Parser.py',471),
  ('statement -> declaration','statement',1,'p_statement_expr','Parser.py',472),
  ('statement -> whileblock','statement',1,'p_statement_expr','Parser.py',473),
  ('statement -> ifblock','statement',1,'p_statement_expr','Parser.py',474),
  ('statement -> returnstatement','statement',1,'p_statement_expr','Parser.py',475),
  ('statement -> functioncall','statement',1,'p_statement_expr','Parser.py',476),
  ('returnstatement -> RETURN expression SEMICOLON','returnstatement',3,'p_return_statement','Parser.py',482),
  ('functioncall -> NAME LPAREN arguments RPAREN SEMICOLON','functioncall',5,'p_function_call','Parser.py',488),
  ('arguments -> expression','arguments',1,'p_function_arguments','Parser.py',495),
  ('arguments -> expression COMMA arguments','arguments',3,'p_function_arguments','Parser.py',496),
  ('statement -> SEMICOLON','statement',1,'p_empty_statement','Parser.py',506),
  ('unmatchedstatement -> IF LPAREN conditional RPAREN allstatement','unmatchedstatement',5,'p_unmatchedstatement_expr1','Parser.py',512),
  ('unmatchedstatement -> IF LPAREN conditional RPAREN statement ELSE unmatchedstatement','unmatchedstatement',7,'p_unmatchedstatement_expr1','Parser.py',513),
  ('unmatchedstatement -> IF LPAREN conditional RPAREN LBRACE fbody RBRACE ELSE unmatchedstatement','unmatchedstatement',9,'p_unmatchedstatement_expr1','Parser.py',514),
  ('unmatchedstatement -> IF LPAREN conditional RPAREN LBRACE fbody RBRACE','unmatchedstatement',7,'p_unmatchedstatement_expr2','Parser.py',525),
  ('ifblock -> IF LPAREN conditional RPAREN statement ELSE statement','ifblock',7,'p_ifblock1','Parser.py',531),
  ('ifblock -> IF LPAREN conditional RPAREN statement ELSE LBRACE fbody RBRACE','ifblock',9,'p_ifblock1','Parser.py',532),
  ('ifblock -> IF LPAREN conditional RPAREN LBRACE fbody RBRACE ELSE LBRACE fbody RBRACE','ifblock',11,'p_ifblock1','Parser.py',533),
  ('ifblock -> IF LPAREN conditional RPAREN LBRACE fbody RBRACE ELSE statement','ifblock',9,'p_ifblock2','Parser.py',544),
  ('whileblock -> WHILE LPAREN conditional RPAREN LBRACE fbody RBRACE','whileblock',7,'p_while','Parser.py',549),
  ('conditional -> LPAREN conditional RPAREN','conditional',3,'p_conditional1','Parser.py',555),
  ('conditional -> conditionbase','conditional',1,'p_conditional','Parser.py',561),
  ('conditional -> NOT LPAREN conditional RPAREN','conditional',4,'p_conditional','Parser.py',562),
  ('conditional -> conditional LESSTHANEQ conditional','conditional',3,'p_conditional','Parser.py',563),
  ('conditional -> conditional GREATERTHANEQ conditional','conditional',3,'p_conditional','Parser.py',564),
  ('conditional -> conditional UNEQUAL conditional','conditional',3,'p_conditional','Parser.py',565),
  ('conditional -> conditional EQUALCHECK conditional','conditional',3,'p_conditional','Parser.py',566),
  ('conditional -> conditional LESSTHAN conditional','conditional',3,'p_conditional','Parser.py',567),
  ('conditional -> conditional GREATERTHAN conditional','conditional',3,'p_conditional','Parser.py',568),
  ('conditional -> conditional ANDOPERATOR conditional','conditional',3,'p_conditional','Parser.py',569),
  ('conditional -> conditional OROPERATOR conditional','conditional',3,'p_conditional','Parser.py',570),
  ('conditionbase -> CS LESSTHANEQ CS','conditionbase',3,'p_conditionbase','Parser.py',596),
  ('conditionbase -> CS GREATERTHANEQ CS','conditionbase',3,'p_conditionbase','Parser.py',597),
  ('conditionbase -> CS UNEQUAL CS','conditionbase',3,'p_conditionbase','Parser.py',598),
  ('conditionbase -> CS EQUALCHECK CS','conditionbase',3,'p_conditionbase','Parser.py',599),
  ('conditionbase -> CS LESSTHAN CS','conditionbase',3,'p_conditionbase','Parser.py',600),
  ('conditionbase -> CS GREATERTHAN CS','conditionbase',3,'p_conditionbase','Parser.py',601),
  ('CS -> expression','CS',1,'p_cs','Parser.py',621),
  ('CS -> NOT LPAREN expression RPAREN','CS',4,'p_cs','Parser.py',622),
  ('declaration -> TYPE dlist1 SEMICOLON','declaration',3,'p_declaration1','Parser.py',630),
  ('dlist1 -> NAME','dlist1',1,'p_dlistname','Parser.py',637),
  ('dlist1 -> NAME COMMA dlist1','dlist1',3,'p_dlistname','Parser.py',638),
  ('dlist1 -> specialvar','dlist1',1,'p_dlistpointer','Parser.py',654),
  ('dlist1 -> specialvar COMMA dlist1','dlist1',3,'p_dlistpointer','Parser.py',655),
  ('specialvar -> TIMES specialvar','specialvar',2,'p_specialvar1','Parser.py',669),
  ('specialvar -> TIMES NAME','specialvar',2,'p_specialvar2','Parser.py',674),
  ('assignment -> assignment_base SEMICOLON','assignment',2,'p_assignment','Parser.py',679),
  ('assignment_base -> TIMES pointervar EQUALS expression','assignment_base',4,'p_assignment_base_pointer','Parser.py',688),
  ('assignment_base -> NAME EQUALS expression','assignment_base',3,'p_assignment_base_pointer','Parser.py',689),
  ('expression -> expression PLUS expression','expression',3,'p_expression1','Parser.py',710),
  ('expression -> expression MINUS expression','expression',3,'p_expression1','Parser.py',711),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression1','Parser.py',712),
  ('expression -> expression TIMES expression','expression',3,'p_expression_mul','Parser.py',729),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','Parser.py',737),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_paren','Parser.py',744),
  ('expression -> FLOAT','expression',1,'p_expression_base_number','Parser.py',750),
  ('expression -> NUMBER','expression',1,'p_expression_base_number','Parser.py',751),
  ('expression -> pointervar','expression',1,'p_expression_base_pointer','Parser.py',766),
  ('pointervar -> TIMES pointervar','pointervar',2,'p_pointervar1','Parser.py',773),
  ('pointervar -> ADDROF pointervar','pointervar',2,'p_pointervar2','Parser.py',778),
  ('pointervar -> NAME','pointervar',1,'p_pointervar3','Parser.py',784),
]
