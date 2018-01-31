
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NUMBER TYPE SEMICOLON EQUALS COMMA LPAREN RPAREN LBRACE RBRACE ADDROF VALOF NAME \n    program : function \n                | function program\n    \n    function : TYPE NAME LPAREN RPAREN LBRACE fbody RBRACE\n    \n    fbody : statement\n            | statement fbody\n    \n    statement : assignment\n            | declaration\n    \n        declaration : TYPE dlist1 SEMICOLON\n    \n        declaration : TYPE dlist2 SEMICOLON\n    \n    dlist1 : NAME \n            | NAME COMMA dlist1  \n    \n    dlist2 : VALOF NAME \n            | VALOF NAME  COMMA dlist2  \n    \n    assignment : assignment_list SEMICOLON\n    \n    assignment_list : assignment_inter\n                        | assignment_inter COMMA assignment_list\n    \n    assignment_inter : assignment_base\n                    | VALOF NAME EQUALS assignment_inter\n     \n    assignment_base : VALOF NAME EQUALS NUMBER \n            | VALOF NAME EQUALS VALOF NAME\n            | NAME EQUALS NAME \n            | NAME EQUALS ADDROF NAME \n     '
    
_lr_action_items = {'ADDROF':([24,],[34,]),'TYPE':([0,3,8,9,12,16,23,28,31,32,],[1,1,11,-6,-7,11,-3,-14,-8,-9,]),'EQUALS':([14,27,44,],[24,36,36,]),'RBRACE':([9,12,13,16,26,28,31,32,],[-6,-7,23,-4,-5,-14,-8,-9,]),'COMMA':([10,15,19,30,33,39,40,41,44,],[-17,25,29,38,-21,-22,-18,-19,-20,]),'NAME':([1,8,9,11,12,16,17,20,24,25,28,29,31,32,34,36,42,],[4,14,-6,19,-7,14,27,30,33,14,-14,19,-8,-9,39,14,44,]),'SEMICOLON':([10,15,18,19,21,22,30,33,35,37,39,40,41,43,44,],[-17,-15,28,-10,31,32,-12,-21,-16,-11,-22,-18,-19,-13,-20,]),'$end':([2,3,5,23,],[0,-1,-2,-3,]),'LPAREN':([4,],[6,]),'RPAREN':([6,],[7,]),'NUMBER':([36,],[41,]),'VALOF':([8,9,11,12,16,25,28,31,32,36,38,],[17,-6,20,-7,17,17,-14,-8,-9,42,20,]),'LBRACE':([7,],[8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'assignment':([8,16,],[9,9,]),'assignment_base':([8,16,25,36,],[10,10,10,10,]),'declaration':([8,16,],[12,12,]),'statement':([8,16,],[16,16,]),'assignment_inter':([8,16,25,36,],[15,15,15,40,]),'dlist1':([11,29,],[21,37,]),'dlist2':([11,38,],[22,43,]),'fbody':([8,16,],[13,26,]),'program':([0,3,],[2,5,]),'function':([0,3,],[3,3,]),'assignment_list':([8,16,25,],[18,18,35,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> function','program',1,'p_program','level1.py',52),
  ('program -> function program','program',2,'p_program','level1.py',53),
  ('function -> TYPE NAME LPAREN RPAREN LBRACE fbody RBRACE','function',7,'p_function','level1.py',58),
  ('fbody -> statement','fbody',1,'p_fbody','level1.py',64),
  ('fbody -> statement fbody','fbody',2,'p_fbody','level1.py',65),
  ('statement -> assignment','statement',1,'p_statement_expr','level1.py',71),
  ('statement -> declaration','statement',1,'p_statement_expr','level1.py',72),
  ('declaration -> TYPE dlist1 SEMICOLON','declaration',3,'p_declaration1','level1.py',78),
  ('declaration -> TYPE dlist2 SEMICOLON','declaration',3,'p_declaration2','level1.py',86),
  ('dlist1 -> NAME','dlist1',1,'p_dlist1','level1.py',94),
  ('dlist1 -> NAME COMMA dlist1','dlist1',3,'p_dlist1','level1.py',95),
  ('dlist2 -> VALOF NAME','dlist2',2,'p_dlist2','level1.py',104),
  ('dlist2 -> VALOF NAME COMMA dlist2','dlist2',4,'p_dlist2','level1.py',105),
  ('assignment -> assignment_list SEMICOLON','assignment',2,'p_assignment','level1.py',114),
  ('assignment_list -> assignment_inter','assignment_list',1,'p_assignment_list','level1.py',123),
  ('assignment_list -> assignment_inter COMMA assignment_list','assignment_list',3,'p_assignment_list','level1.py',124),
  ('assignment_inter -> assignment_base','assignment_inter',1,'p_assignment_inter','level1.py',133),
  ('assignment_inter -> VALOF NAME EQUALS assignment_inter','assignment_inter',4,'p_assignment_inter','level1.py',134),
  ('assignment_base -> VALOF NAME EQUALS NUMBER','assignment_base',4,'p_assignment_base','level1.py',143),
  ('assignment_base -> VALOF NAME EQUALS VALOF NAME','assignment_base',5,'p_assignment_base','level1.py',144),
  ('assignment_base -> NAME EQUALS NAME','assignment_base',3,'p_assignment_base','level1.py',145),
  ('assignment_base -> NAME EQUALS ADDROF NAME','assignment_base',4,'p_assignment_base','level1.py',146),
]
