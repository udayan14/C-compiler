
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDErightVALOFrightUMINUSNUMBER TYPE SEMICOLON EQUALS COMMA LPAREN RPAREN LBRACE RBRACE ADDROF NAME PLUS MINUS TIMES DIVIDE \n\tprogram : function \n\t\t\t\t| function program\n\t\n\tfunction : TYPE NAME LPAREN RPAREN LBRACE fbody RBRACE\n\t\n\tfbody : statement\n\t\t\t| statement fbody\n\t\n\tstatement : assignment\n\t\t\t| declaration\n\t\n\t\tdeclaration : TYPE dlist1 SEMICOLON\n\t\n\tdlist1 : NAME  \n\t\t\t| NAME COMMA dlist1\n\t\n\tdlist1 : specialvar\n\t\t\t| specialvar  COMMA dlist1  \n\t\n\tspecialvar : TIMES specialvar %prec VALOF\n\t\t\t\t| TIMES NAME %prec VALOF\n\t\n\tassignment : assignment_base SEMICOLON\n\t \n\tassignment_base : TIMES pointervar EQUALS expression\n\t\t\t| NAME EQUALS expression \n\t \n\texpression : expression PLUS expression\n\t\t\t\t| expression MINUS expression\n\t\t\t\t| expression DIVIDE expression\n\t\n\texpression : expression TIMES expression\n\t\n\texpression : MINUS expression %prec UMINUS\n\t\n\texpression : LPAREN expression RPAREN\n\t\n\texpression : NUMBER\n\t\n\texpression : pointervar\n\t\n\tpointervar : TIMES pointervar %prec VALOF\n\t\n\tpointervar : ADDROF pointervar\n\t\n\tpointervar : NAME\n\t'
    
_lr_action_items = {'LBRACE':([7,],[8,]),'TIMES':([8,9,10,12,13,14,18,19,20,21,23,27,29,30,31,32,33,34,35,36,39,40,41,42,43,44,45,46,47,48,51,52,53,54,55,],[13,13,-7,-6,20,23,20,20,20,-28,23,-15,42,-25,20,-24,20,-27,-26,20,-8,23,23,20,20,20,20,-22,42,42,-21,-20,42,42,-23,]),'COMMA':([25,26,37,38,],[40,41,-14,-13,]),'PLUS':([21,29,30,32,34,35,46,47,48,51,52,53,54,55,],[-28,44,-25,-24,-27,-26,-22,44,44,-21,-20,-18,-19,-23,]),'NAME':([1,8,9,10,12,13,14,18,19,20,23,27,31,33,36,39,40,41,42,43,44,45,],[4,11,11,-7,-6,21,26,21,21,21,37,-15,21,21,21,-8,26,26,21,21,21,21,]),'SEMICOLON':([15,21,24,25,26,29,30,32,34,35,37,38,46,48,49,50,51,52,53,54,55,],[27,-28,39,-11,-9,-17,-25,-24,-27,-26,-14,-13,-22,-16,-12,-10,-21,-20,-18,-19,-23,]),'MINUS':([18,21,29,30,31,32,33,34,35,36,42,43,44,45,46,47,48,51,52,53,54,55,],[31,-28,45,-25,31,-24,31,-27,-26,31,31,31,31,31,-22,45,45,-21,-20,-18,-19,-23,]),'ADDROF':([13,18,19,20,31,33,36,42,43,44,45,],[19,19,19,19,19,19,19,19,19,19,19,]),'TYPE':([0,3,8,9,10,12,27,28,39,],[1,1,14,14,-7,-6,-15,-3,-8,]),'DIVIDE':([21,29,30,32,34,35,46,47,48,51,52,53,54,55,],[-28,43,-25,-24,-27,-26,-22,43,43,-21,-20,43,43,-23,]),'LPAREN':([4,18,31,33,36,42,43,44,45,],[6,33,33,33,33,33,33,33,33,]),'EQUALS':([11,21,22,34,35,],[18,-28,36,-27,-26,]),'$end':([2,3,5,28,],[0,-1,-2,-3,]),'RBRACE':([9,10,12,16,17,27,39,],[-4,-7,-6,28,-5,-15,-8,]),'NUMBER':([18,31,33,36,42,43,44,45,],[32,32,32,32,32,32,32,32,]),'RPAREN':([6,21,30,32,34,35,46,47,51,52,53,54,55,],[7,-28,-25,-24,-27,-26,-22,55,-21,-20,-18,-19,-23,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([8,9,],[9,9,]),'dlist1':([14,40,41,],[24,49,50,]),'fbody':([8,9,],[16,17,]),'specialvar':([14,23,40,41,],[25,38,25,25,]),'declaration':([8,9,],[10,10,]),'program':([0,3,],[2,5,]),'expression':([18,31,33,36,42,43,44,45,],[29,46,47,48,51,52,53,54,]),'assignment_base':([8,9,],[15,15,]),'function':([0,3,],[3,3,]),'assignment':([8,9,],[12,12,]),'pointervar':([13,18,19,20,31,33,36,42,43,44,45,],[22,30,34,35,30,30,30,30,30,30,30,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> function','program',1,'p_program','150070001-150070018.py',123),
  ('program -> function program','program',2,'p_program','150070001-150070018.py',124),
  ('function -> TYPE NAME LPAREN RPAREN LBRACE fbody RBRACE','function',7,'p_function','150070001-150070018.py',148),
  ('fbody -> statement','fbody',1,'p_fbody','150070001-150070018.py',169),
  ('fbody -> statement fbody','fbody',2,'p_fbody','150070001-150070018.py',170),
  ('statement -> assignment','statement',1,'p_statement_expr','150070001-150070018.py',187),
  ('statement -> declaration','statement',1,'p_statement_expr','150070001-150070018.py',188),
  ('declaration -> TYPE dlist1 SEMICOLON','declaration',3,'p_declaration1','150070001-150070018.py',193),
  ('dlist1 -> NAME','dlist1',1,'p_dlistname','150070001-150070018.py',199),
  ('dlist1 -> NAME COMMA dlist1','dlist1',3,'p_dlistname','150070001-150070018.py',200),
  ('dlist1 -> specialvar','dlist1',1,'p_dlistpointer','150070001-150070018.py',207),
  ('dlist1 -> specialvar COMMA dlist1','dlist1',3,'p_dlistpointer','150070001-150070018.py',208),
  ('specialvar -> TIMES specialvar','specialvar',2,'p_specialvar','150070001-150070018.py',215),
  ('specialvar -> TIMES NAME','specialvar',2,'p_specialvar','150070001-150070018.py',216),
  ('assignment -> assignment_base SEMICOLON','assignment',2,'p_assignment','150070001-150070018.py',221),
  ('assignment_base -> TIMES pointervar EQUALS expression','assignment_base',4,'p_assignment_base_pointer','150070001-150070018.py',230),
  ('assignment_base -> NAME EQUALS expression','assignment_base',3,'p_assignment_base_pointer','150070001-150070018.py',231),
  ('expression -> expression PLUS expression','expression',3,'p_expression1','150070001-150070018.py',251),
  ('expression -> expression MINUS expression','expression',3,'p_expression1','150070001-150070018.py',252),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression1','150070001-150070018.py',253),
  ('expression -> expression TIMES expression','expression',3,'p_expression_mul','150070001-150070018.py',270),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','150070001-150070018.py',278),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_paren','150070001-150070018.py',285),
  ('expression -> NUMBER','expression',1,'p_expression_base_number','150070001-150070018.py',291),
  ('expression -> pointervar','expression',1,'p_expression_base_pointer','150070001-150070018.py',297),
  ('pointervar -> TIMES pointervar','pointervar',2,'p_pointervar1','150070001-150070018.py',304),
  ('pointervar -> ADDROF pointervar','pointervar',2,'p_pointervar2','150070001-150070018.py',310),
  ('pointervar -> NAME','pointervar',1,'p_pointervar3','150070001-150070018.py',317),
]
