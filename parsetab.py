
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDErightUMINUSrightVALOFNUMBER TYPE newline SEMICOLON EQUALS COMMA LPAREN RPAREN LBRACE RBRACE ADDROF VALOF NAME COMMENT PLUS MINUS TIMES DIVIDE \n\tprogram : function \n\t\t\t\t| function program\n\t\n\tfunction : TYPE NAME LPAREN RPAREN LBRACE fbody RBRACE\n\t\n\tfbody : statement\n\t\t\t| statement fbody\n\t\n\tstatement : assignment\n\t\t\t| declaration\n\t\n\t\tdeclaration : TYPE dlist1 SEMICOLON\n\t\n\tdlist1 : NAME  \n\t\t\t| NAME COMMA dlist1\n\t\n\tdlist1 : specialvar\n\t\t\t| specialvar  COMMA dlist1  \n\t\n\tspecialvar : VALOF specialvar\n\t\t\t\t| VALOF NAME\n\t\n\tassignment : assignment_base SEMICOLON\n\t \n\tassignment_base : VALOF pointervar EQUALS expression\n\t\t\t| NAME EQUALS expression \n\t \n\texpression : expression PLUS expression\n\t\t\t\t| expression MINUS expression\n\t\t\t\t| expression VALOF expression %prec TIMES \n\t\t\t\t| expression DIVIDE expression\n\t\n\texpression : MINUS expression %prec UMINUS\n\t\n\texpression : LPAREN expression RPAREN\n\t\n\texpression : NUMBER\n\t\n\texpression : pointervar\n\t\n\tpointervar : VALOF pointervar\n\t\n\tpointervar : ADDROF pointervar\n\t\n\tpointervar : NAME\n\t'
    
_lr_action_items = {'TYPE':([0,2,8,12,13,14,22,24,29,],[3,3,9,9,-6,-7,-3,-15,-8,]),'$end':([1,2,4,22,],[0,-1,-2,-3,]),'NAME':([3,8,9,12,13,14,16,20,21,24,25,27,29,30,31,35,36,40,44,45,46,47,],[5,10,18,10,-6,-7,28,33,28,-15,28,28,-8,18,18,28,28,28,28,28,28,28,]),'LPAREN':([5,21,35,36,40,44,45,46,47,],[6,36,36,36,36,36,36,36,36,]),'RPAREN':([6,28,37,38,39,41,48,49,51,52,53,54,55,],[7,-28,-24,-25,-26,-27,-22,55,-18,-19,-20,-21,-23,]),'LBRACE':([7,],[8,]),'VALOF':([8,9,12,13,14,16,20,21,24,25,27,28,29,30,31,34,35,36,37,38,39,40,41,44,45,46,47,48,49,50,51,52,53,54,55,],[16,20,16,-6,-7,25,20,25,-15,25,25,-28,-8,20,20,46,25,25,-24,-25,-26,25,-27,25,25,25,25,46,46,46,46,46,46,46,-23,]),'EQUALS':([10,26,28,39,41,],[21,40,-28,-26,-27,]),'RBRACE':([11,12,13,14,23,24,29,],[22,-4,-6,-7,-5,-15,-8,]),'SEMICOLON':([15,17,18,19,28,32,33,34,37,38,39,41,42,43,48,50,51,52,53,54,55,],[24,29,-9,-11,-28,-13,-14,-17,-24,-25,-26,-27,-10,-12,-22,-16,-18,-19,-20,-21,-23,]),'ADDROF':([16,21,25,27,35,36,40,44,45,46,47,],[27,27,27,27,27,27,27,27,27,27,27,]),'COMMA':([18,19,32,33,],[30,31,-13,-14,]),'MINUS':([21,28,34,35,36,37,38,39,40,41,44,45,46,47,48,49,50,51,52,53,54,55,],[35,-28,45,35,35,-24,-25,-26,35,-27,35,35,35,35,-22,45,45,-18,-19,-20,-21,-23,]),'NUMBER':([21,35,36,40,44,45,46,47,],[37,37,37,37,37,37,37,37,]),'PLUS':([28,34,37,38,39,41,48,49,50,51,52,53,54,55,],[-28,44,-24,-25,-26,-27,-22,44,44,-18,-19,-20,-21,-23,]),'DIVIDE':([28,34,37,38,39,41,48,49,50,51,52,53,54,55,],[-28,47,-24,-25,-26,-27,-22,47,47,47,47,-20,-21,-23,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,2,],[1,4,]),'function':([0,2,],[2,2,]),'fbody':([8,12,],[11,23,]),'statement':([8,12,],[12,12,]),'assignment':([8,12,],[13,13,]),'declaration':([8,12,],[14,14,]),'assignment_base':([8,12,],[15,15,]),'dlist1':([9,30,31,],[17,42,43,]),'specialvar':([9,20,30,31,],[19,32,19,19,]),'pointervar':([16,21,25,27,35,36,40,44,45,46,47,],[26,38,39,41,38,38,38,38,38,38,38,]),'expression':([21,35,36,40,44,45,46,47,],[34,48,49,50,51,52,53,54,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> function','program',1,'p_program','150070001-150070018.py',74),
  ('program -> function program','program',2,'p_program','150070001-150070018.py',75),
  ('function -> TYPE NAME LPAREN RPAREN LBRACE fbody RBRACE','function',7,'p_function','150070001-150070018.py',80),
  ('fbody -> statement','fbody',1,'p_fbody','150070001-150070018.py',90),
  ('fbody -> statement fbody','fbody',2,'p_fbody','150070001-150070018.py',91),
  ('statement -> assignment','statement',1,'p_statement_expr','150070001-150070018.py',100),
  ('statement -> declaration','statement',1,'p_statement_expr','150070001-150070018.py',101),
  ('declaration -> TYPE dlist1 SEMICOLON','declaration',3,'p_declaration1','150070001-150070018.py',107),
  ('dlist1 -> NAME','dlist1',1,'p_dlistname','150070001-150070018.py',113),
  ('dlist1 -> NAME COMMA dlist1','dlist1',3,'p_dlistname','150070001-150070018.py',114),
  ('dlist1 -> specialvar','dlist1',1,'p_dlistpointer','150070001-150070018.py',121),
  ('dlist1 -> specialvar COMMA dlist1','dlist1',3,'p_dlistpointer','150070001-150070018.py',122),
  ('specialvar -> VALOF specialvar','specialvar',2,'p_specialvar','150070001-150070018.py',129),
  ('specialvar -> VALOF NAME','specialvar',2,'p_specialvar','150070001-150070018.py',130),
  ('assignment -> assignment_base SEMICOLON','assignment',2,'p_assignment','150070001-150070018.py',135),
  ('assignment_base -> VALOF pointervar EQUALS expression','assignment_base',4,'p_assignment_base_pointer','150070001-150070018.py',144),
  ('assignment_base -> NAME EQUALS expression','assignment_base',3,'p_assignment_base_pointer','150070001-150070018.py',145),
  ('expression -> expression PLUS expression','expression',3,'p_expression1','150070001-150070018.py',155),
  ('expression -> expression MINUS expression','expression',3,'p_expression1','150070001-150070018.py',156),
  ('expression -> expression VALOF expression','expression',3,'p_expression1','150070001-150070018.py',157),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression1','150070001-150070018.py',158),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','150070001-150070018.py',173),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_paren','150070001-150070018.py',179),
  ('expression -> NUMBER','expression',1,'p_expression_base_number','150070001-150070018.py',185),
  ('expression -> pointervar','expression',1,'p_expression_base_pointer','150070001-150070018.py',190),
  ('pointervar -> VALOF pointervar','pointervar',2,'p_pointervar1','150070001-150070018.py',196),
  ('pointervar -> ADDROF pointervar','pointervar',2,'p_pointervar2','150070001-150070018.py',201),
  ('pointervar -> NAME','pointervar',1,'p_pointervar3','150070001-150070018.py',206),
]
