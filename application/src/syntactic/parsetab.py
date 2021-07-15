
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ANDEQUAL BREAK CMP COLON COMMA CONTINUE DECREMENT DIVEQUAL DIVIDE DO ELSE ELSIF EQ EQUALS EXP FALSE FOR GE GT ID ID_LI ID_SC IF INCREMENT LAND LBRACE LBRACKET LE LNOT LOR LPAREN LSHIFT LSHIFTEQUAL LT MINUS MINUSEQUAL MODEQUAL MODULO NE NO NUMBER OR OREQUAL PERIOD PLUS PLUSEQUAL Q QQ QR QW QX RBRACE RBRACKET RETURN RPAREN RSHIFT RSHIFTEQUAL S SEMICOLON SEQ SGE SGT SLE SLT SNE SUB TERNARY TIMES TIMESEQUAL TR TRUE UNLESS UNTIL WHILE XOR XOREQUALinit : blockcode init\n        | function init\n        | blockcode\n        | function\n         blockcode : command\n        | command blockcode\n     command : interations\n        | if\n        | exp_assignment\n        | call\n        | RETURN return SEMICOLON\n        | BREAK SEMICOLON\n        | CONTINUE SEMICOLON\n    \n        if : IF LPAREN exp_condition RPAREN LBRACE blockcode RBRACE\n        | command IF LPAREN exp_condition RPAREN\n        | IF LPAREN exp_condition RPAREN LBRACE blockcode RBRACE ELSE LBRACE blockcode RBRACE\n        | IF LPAREN exp_condition RPAREN LBRACE blockcode RBRACE elsif\n    \n        elsif : ELSIF LPAREN exp_condition RPAREN LBRACE blockcode RBRACE\n        | ELSIF LPAREN exp_condition RPAREN LBRACE blockcode RBRACE elsif2\n    \n        elsif2 : elsif\n            | ELSE LBRACE blockcode RBRACE\n    \n       interations :  for\n       | dowhile\n       | while\n     for : FOR LPAREN for_assignments SEMICOLON exp_condition SEMICOLON for_assignments RPAREN LBRACE blockcode RBRACE for_assignments : exp_assignment\n        | exp_assignment COMMA for_assignments\n     dowhile :  DO LBRACE blockcode RBRACE WHILE LPAREN exp_condition RPAREN  while :  LPAREN exp_condition RPAREN LBRACE blockcode RBRACE  function : SUB ID LPAREN RPAREN LBRACE blockcode RBRACE\n        | SUB ID LPAREN function_assignments RPAREN LBRACE blockcode RBRACE\n     function_assignments : exp_assignment\n        | exp_assignment COMMA function_assignments\n    \n    exp_condition : attcond GT attcond\n            | attcond LT attcond\n            | attcond EQ attcond\n            | attcond GE attcond\n            | attcond LE attcond\n            | attcond NE attcond\n            | attcond\n            | LPAREN exp_condition RPAREN logic exp_condition_logic\n            | attcond CMP attcond\n            | attcond SEQ attcond\n            | attcond SNE attcond\n            | attcond SLT attcond\n            | attcond SGT attcond\n            | attcond SLE attcond\n            | attcond SGE attcond\n    \n        exp_condition_logic : LPAREN exp_condition RPAREN\n        | LPAREN exp_condition RPAREN logic LPAREN exp_condition RPAREN\n    \n        logic : LAND\n            | LOR\n            | LNOT\n     exp_assignment : ID_SC EQUALS arithmetic\n        | ID_LI EQUALS arithmetic\n        | ID_SC\n        | ID_LI\n        | INCREMENT ID_SC\n        | DECREMENT ID_SC\n        | ID_SC INCREMENT\n        | ID_SC DECREMENT\n    \n        arithmetic : exp\n    \n        exp : exp PLUS exp1\n            | exp MINUS exp1\n            | exp1\n    \n        exp1 : exp1 TIMES exp2\n            | exp1 DIVIDE exp2\n            | exp1 MODULO exp2\n            | exp2\n    \n    exp2 : exp3 XOR exp2\n        | exp3\n    \n    exp3 : LPAREN arithmetic RPAREN\n        | NUMBER\n        | exp_assignment\n        | exp_condition\n        | call\n        | exp\n        | TRUE\n        | FALSE\n     attcond : exp_assignment\n        | NUMBER\n        | TRUE\n        | FALSE\n    \n        call : ID LPAREN RPAREN\n            | ID LPAREN function_assignments RPAREN\n     return : attcond\n        | arithmetic\n     '
    
_lr_action_items = {'SUB':([0,2,3,4,8,9,10,11,15,16,17,19,20,27,33,34,35,36,37,45,46,47,48,50,51,52,53,56,57,59,60,65,83,94,95,96,97,98,99,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,135,151,152,156,159,162,163,165,168,178,180,181,184,185,186,190,],[5,5,5,-5,-7,-8,-9,-10,-22,-23,-24,-56,-57,-6,-40,-80,-81,-82,-83,-62,-65,-69,-71,-75,-76,-12,-13,-60,-61,-58,-59,-84,-11,-54,-73,-74,-78,-79,-55,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-15,-41,-29,-30,-14,-31,-49,-17,-28,-16,-25,-50,-18,-19,-20,-21,]),'RETURN':([0,2,3,4,8,9,10,11,15,16,17,19,20,27,33,34,35,36,37,45,46,47,48,50,51,52,53,56,57,59,60,62,65,83,94,95,96,97,98,99,106,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,135,136,144,149,151,152,156,159,162,163,165,168,170,172,178,180,181,182,184,185,186,188,190,],[12,12,12,12,-7,-8,-9,-10,-22,-23,-24,-56,-57,-6,-40,-80,-81,-82,-83,-62,-65,-69,-71,-75,-76,-12,-13,-60,-61,-58,-59,12,-84,-11,-54,-73,-74,-78,-79,-55,-85,12,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-15,12,12,12,-41,-29,-30,-14,-31,-49,-17,-28,12,12,-16,-25,-50,12,-18,-19,-20,12,-21,]),'BREAK':([0,2,3,4,8,9,10,11,15,16,17,19,20,27,33,34,35,36,37,45,46,47,48,50,51,52,53,56,57,59,60,62,65,83,94,95,96,97,98,99,106,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,135,136,144,149,151,152,156,159,162,163,165,168,170,172,178,180,181,182,184,185,186,188,190,],[13,13,13,13,-7,-8,-9,-10,-22,-23,-24,-56,-57,-6,-40,-80,-81,-82,-83,-62,-65,-69,-71,-75,-76,-12,-13,-60,-61,-58,-59,13,-84,-11,-54,-73,-74,-78,-79,-55,-85,13,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-15,13,13,13,-41,-29,-30,-14,-31,-49,-17,-28,13,13,-16,-25,-50,13,-18,-19,-20,13,-21,]),'CONTINUE':([0,2,3,4,8,9,10,11,15,16,17,19,20,27,33,34,35,36,37,45,46,47,48,50,51,52,53,56,57,59,60,62,65,83,94,95,96,97,98,99,106,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,135,136,144,149,151,152,156,159,162,163,165,168,170,172,178,180,181,182,184,185,186,188,190,],[14,14,14,14,-7,-8,-9,-10,-22,-23,-24,-56,-57,-6,-40,-80,-81,-82,-83,-62,-65,-69,-71,-75,-76,-12,-13,-60,-61,-58,-59,14,-84,-11,-54,-73,-74,-78,-79,-55,-85,14,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-15,14,14,14,-41,-29,-30,-14,-31,-49,-17,-28,14,14,-16,-25,-50,14,-18,-19,-20,14,-21,]),'IF':([0,2,3,4,8,9,10,11,15,16,17,19,20,27,33,34,35,36,37,45,46,47,48,50,51,52,53,56,57,59,60,62,65,83,94,95,96,97,98,99,106,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,135,136,144,149,151,152,156,159,162,163,165,168,170,172,178,180,181,182,184,185,186,188,190,],[18,18,18,28,-7,-8,-9,-10,-22,-23,-24,-56,-57,-6,-40,-80,-81,-82,-83,-62,-65,-69,-71,-75,-76,-12,-13,-60,-61,-58,-59,18,-84,-11,-54,-73,-74,-78,-79,-55,-85,18,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-15,18,18,18,-41,-29,-30,-14,-31,-49,-17,-28,18,18,-16,-25,-50,18,-18,-19,-20,18,-21,]),'ID_SC':([0,2,3,4,7,8,9,10,11,12,15,16,17,19,20,21,22,27,30,31,33,34,35,36,37,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,94,95,96,97,98,99,106,107,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,132,133,135,136,144,149,150,151,152,154,155,156,159,162,163,165,168,170,171,172,173,178,180,181,182,184,185,186,188,190,],[19,19,19,19,19,-7,-8,-9,-10,19,-22,-23,-24,-56,-57,59,60,-6,19,19,-40,-80,-81,-82,-83,-62,-65,-69,-71,19,-75,-76,-12,-13,19,19,-60,-61,19,-58,-59,19,19,19,19,-84,19,19,19,19,19,19,19,19,19,19,19,19,19,-11,19,19,19,19,19,19,19,-54,-73,-74,-78,-79,-55,-85,19,19,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,19,19,-15,19,19,19,19,-41,-29,19,19,-30,-14,-31,-49,-17,-28,19,19,19,19,-16,-25,-50,19,-18,-19,-20,19,-21,]),'ID_LI':([0,2,3,4,7,8,9,10,11,12,15,16,17,19,20,27,30,31,33,34,35,36,37,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,94,95,96,97,98,99,106,107,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,132,133,135,136,144,149,150,151,152,154,155,156,159,162,163,165,168,170,171,172,173,178,180,181,182,184,185,186,188,190,],[20,20,20,20,20,-7,-8,-9,-10,20,-22,-23,-24,-56,-57,-6,20,20,-40,-80,-81,-82,-83,-62,-65,-69,-71,20,-75,-76,-12,-13,20,20,-60,-61,20,-58,-59,20,20,20,20,-84,20,20,20,20,20,20,20,20,20,20,20,20,20,-11,20,20,20,20,20,20,20,-54,-73,-74,-78,-79,-55,-85,20,20,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,20,20,-15,20,20,20,20,-41,-29,20,20,-30,-14,-31,-49,-17,-28,20,20,20,20,-16,-25,-50,20,-18,-19,-20,20,-21,]),'INCREMENT':([0,2,3,4,7,8,9,10,11,12,15,16,17,19,20,27,30,31,33,34,35,36,37,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,94,95,96,97,98,99,106,107,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,132,133,135,136,144,149,150,151,152,154,155,156,159,162,163,165,168,170,171,172,173,178,180,181,182,184,185,186,188,190,],[21,21,21,21,21,-7,-8,-9,-10,21,-22,-23,-24,56,-57,-6,21,21,-40,-80,-81,-82,-83,-62,-65,-69,-71,21,-75,-76,-12,-13,21,21,-60,-61,21,-58,-59,21,21,21,21,-84,21,21,21,21,21,21,21,21,21,21,21,21,21,-11,21,21,21,21,21,21,21,-54,-73,-74,-78,-79,-55,-85,21,21,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,21,21,-15,21,21,21,21,-41,-29,21,21,-30,-14,-31,-49,-17,-28,21,21,21,21,-16,-25,-50,21,-18,-19,-20,21,-21,]),'DECREMENT':([0,2,3,4,7,8,9,10,11,12,15,16,17,19,20,27,30,31,33,34,35,36,37,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,94,95,96,97,98,99,106,107,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,132,133,135,136,144,149,150,151,152,154,155,156,159,162,163,165,168,170,171,172,173,178,180,181,182,184,185,186,188,190,],[22,22,22,22,22,-7,-8,-9,-10,22,-22,-23,-24,57,-57,-6,22,22,-40,-80,-81,-82,-83,-62,-65,-69,-71,22,-75,-76,-12,-13,22,22,-60,-61,22,-58,-59,22,22,22,22,-84,22,22,22,22,22,22,22,22,22,22,22,22,22,-11,22,22,22,22,22,22,22,-54,-73,-74,-78,-79,-55,-85,22,22,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,22,22,-15,22,22,22,22,-41,-29,22,22,-30,-14,-31,-49,-17,-28,22,22,22,22,-16,-25,-50,22,-18,-19,-20,22,-21,]),'ID':([0,2,3,4,5,8,9,10,11,12,15,16,17,19,20,27,33,34,35,36,37,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,62,65,83,84,85,86,87,88,89,90,94,95,96,97,98,99,106,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,135,136,144,149,151,152,156,159,162,163,165,168,170,172,178,180,181,182,184,185,186,188,190,],[6,6,6,6,29,-7,-8,-9,-10,6,-22,-23,-24,-56,-57,-6,-40,-80,-81,-82,-83,-62,-65,-69,-71,6,-75,-76,-12,-13,6,-60,-61,6,-58,-59,6,-84,-11,6,6,6,6,6,6,6,-54,-73,-74,-78,-79,-55,-85,6,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-15,6,6,6,-41,-29,-30,-14,-31,-49,-17,-28,6,6,-16,-25,-50,6,-18,-19,-20,6,-21,]),'FOR':([0,2,3,4,8,9,10,11,15,16,17,19,20,27,33,34,35,36,37,45,46,47,48,50,51,52,53,56,57,59,60,62,65,83,94,95,96,97,98,99,106,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,135,136,144,149,151,152,156,159,162,163,165,168,170,172,178,180,181,182,184,185,186,188,190,],[23,23,23,23,-7,-8,-9,-10,-22,-23,-24,-56,-57,-6,-40,-80,-81,-82,-83,-62,-65,-69,-71,-75,-76,-12,-13,-60,-61,-58,-59,23,-84,-11,-54,-73,-74,-78,-79,-55,-85,23,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-15,23,23,23,-41,-29,-30,-14,-31,-49,-17,-28,23,23,-16,-25,-50,23,-18,-19,-20,23,-21,]),'DO':([0,2,3,4,8,9,10,11,15,16,17,19,20,27,33,34,35,36,37,45,46,47,48,50,51,52,53,56,57,59,60,62,65,83,94,95,96,97,98,99,106,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,135,136,144,149,151,152,156,159,162,163,165,168,170,172,178,180,181,182,184,185,186,188,190,],[24,24,24,24,-7,-8,-9,-10,-22,-23,-24,-56,-57,-6,-40,-80,-81,-82,-83,-62,-65,-69,-71,-75,-76,-12,-13,-60,-61,-58,-59,24,-84,-11,-54,-73,-74,-78,-79,-55,-85,24,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-15,24,24,24,-41,-29,-30,-14,-31,-49,-17,-28,24,24,-16,-25,-50,24,-18,-19,-20,24,-21,]),'LPAREN':([0,2,3,4,6,7,8,9,10,11,12,15,16,17,18,19,20,23,27,28,29,31,33,34,35,36,37,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,65,83,84,85,86,87,88,89,90,94,95,96,97,98,99,106,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,132,135,136,139,140,141,142,144,147,149,150,151,152,155,156,159,162,163,165,166,168,169,170,171,172,173,178,180,181,182,184,185,186,188,190,],[7,7,7,7,30,31,-7,-8,-9,-10,49,-22,-23,-24,54,-56,-57,61,-6,63,64,31,-40,-80,-81,-82,-83,-62,-65,-69,-71,90,-75,-76,-12,-13,31,49,-60,-61,49,-58,-59,7,31,-84,-11,49,49,49,49,49,49,90,-54,-73,-74,-78,-79,-55,-85,7,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,31,-15,7,150,-51,-52,-53,7,155,7,31,-41,-29,31,-30,-14,-31,-49,-17,171,-28,173,7,31,7,31,-16,-25,-50,7,-18,-19,-20,7,-21,]),'$end':([1,2,3,4,8,9,10,11,15,16,17,19,20,25,26,27,33,34,35,36,37,45,46,47,48,50,51,52,53,56,57,59,60,65,83,94,95,96,97,98,99,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,135,151,152,156,159,162,163,165,168,178,180,181,184,185,186,190,],[0,-3,-4,-5,-7,-8,-9,-10,-22,-23,-24,-56,-57,-1,-2,-6,-40,-80,-81,-82,-83,-62,-65,-69,-71,-75,-76,-12,-13,-60,-61,-58,-59,-84,-11,-54,-73,-74,-78,-79,-55,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-15,-41,-29,-30,-14,-31,-49,-17,-28,-16,-25,-50,-18,-19,-20,-21,]),'RBRACE':([4,8,9,10,11,15,16,17,19,20,27,33,34,35,36,37,45,46,47,48,50,51,52,53,56,57,59,60,65,83,94,95,96,97,98,99,102,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,135,143,148,151,152,153,157,159,163,165,168,174,176,178,180,181,183,184,185,186,189,190,],[-5,-7,-8,-9,-10,-22,-23,-24,-56,-57,-6,-40,-80,-81,-82,-83,-62,-65,-69,-71,-75,-76,-12,-13,-60,-61,-58,-59,-84,-11,-54,-73,-74,-78,-79,-55,134,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-15,152,156,-41,-29,159,162,-14,-49,-17,-28,178,180,-16,-25,-50,184,-18,-19,-20,190,-21,]),'NUMBER':([7,12,31,49,54,55,58,63,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,86,87,88,89,90,132,150,155,171,173,],[35,42,35,42,35,95,95,35,35,35,35,35,35,35,35,35,35,35,35,35,35,95,95,95,95,95,95,42,35,35,35,35,35,]),'TRUE':([7,12,31,49,54,55,58,63,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,86,87,88,89,90,132,150,155,171,173,],[36,43,36,43,36,97,97,36,36,36,36,36,36,36,36,36,36,36,36,36,36,97,97,97,97,97,97,43,36,36,36,36,36,]),'FALSE':([7,12,31,49,54,55,58,63,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,86,87,88,89,90,132,150,155,171,173,],[37,44,37,44,37,98,98,37,37,37,37,37,37,37,37,37,37,37,37,37,37,98,98,98,98,98,98,44,37,37,37,37,37,]),'SEMICOLON':([13,14,19,20,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,50,51,56,57,59,60,65,94,95,96,97,98,99,100,101,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,145,146,151,163,181,],[52,53,-56,-57,-40,-80,-81,-82,-83,83,-40,-87,-74,-73,-78,-79,-62,-65,-69,-71,-75,-76,-60,-61,-58,-59,-84,-54,-73,-74,-78,-79,-55,132,-26,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,154,-27,-41,-49,-50,]),'EQUALS':([19,20,],[55,58,]),'GT':([19,20,33,34,35,36,37,39,41,42,43,44,45,46,47,48,50,51,56,57,59,60,65,94,95,96,97,98,99,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,151,163,181,],[-56,-57,70,-80,-81,-82,-83,70,-80,-81,-82,-83,-62,-65,-69,-71,-75,-76,-60,-61,-58,-59,-84,-54,-73,-74,-78,-79,-55,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-41,-49,-50,]),'LT':([19,20,33,34,35,36,37,39,41,42,43,44,45,46,47,48,50,51,56,57,59,60,65,94,95,96,97,98,99,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,151,163,181,],[-56,-57,71,-80,-81,-82,-83,71,-80,-81,-82,-83,-62,-65,-69,-71,-75,-76,-60,-61,-58,-59,-84,-54,-73,-74,-78,-79,-55,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-41,-49,-50,]),'EQ':([19,20,33,34,35,36,37,39,41,42,43,44,45,46,47,48,50,51,56,57,59,60,65,94,95,96,97,98,99,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,151,163,181,],[-56,-57,72,-80,-81,-82,-83,72,-80,-81,-82,-83,-62,-65,-69,-71,-75,-76,-60,-61,-58,-59,-84,-54,-73,-74,-78,-79,-55,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-41,-49,-50,]),'GE':([19,20,33,34,35,36,37,39,41,42,43,44,45,46,47,48,50,51,56,57,59,60,65,94,95,96,97,98,99,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,151,163,181,],[-56,-57,73,-80,-81,-82,-83,73,-80,-81,-82,-83,-62,-65,-69,-71,-75,-76,-60,-61,-58,-59,-84,-54,-73,-74,-78,-79,-55,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-41,-49,-50,]),'LE':([19,20,33,34,35,36,37,39,41,42,43,44,45,46,47,48,50,51,56,57,59,60,65,94,95,96,97,98,99,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,151,163,181,],[-56,-57,74,-80,-81,-82,-83,74,-80,-81,-82,-83,-62,-65,-69,-71,-75,-76,-60,-61,-58,-59,-84,-54,-73,-74,-78,-79,-55,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-41,-49,-50,]),'NE':([19,20,33,34,35,36,37,39,41,42,43,44,45,46,47,48,50,51,56,57,59,60,65,94,95,96,97,98,99,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,151,163,181,],[-56,-57,75,-80,-81,-82,-83,75,-80,-81,-82,-83,-62,-65,-69,-71,-75,-76,-60,-61,-58,-59,-84,-54,-73,-74,-78,-79,-55,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-41,-49,-50,]),'CMP':([19,20,33,34,35,36,37,39,41,42,43,44,45,46,47,48,50,51,56,57,59,60,65,94,95,96,97,98,99,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,151,163,181,],[-56,-57,76,-80,-81,-82,-83,76,-80,-81,-82,-83,-62,-65,-69,-71,-75,-76,-60,-61,-58,-59,-84,-54,-73,-74,-78,-79,-55,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-41,-49,-50,]),'SEQ':([19,20,33,34,35,36,37,39,41,42,43,44,45,46,47,48,50,51,56,57,59,60,65,94,95,96,97,98,99,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,151,163,181,],[-56,-57,77,-80,-81,-82,-83,77,-80,-81,-82,-83,-62,-65,-69,-71,-75,-76,-60,-61,-58,-59,-84,-54,-73,-74,-78,-79,-55,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-41,-49,-50,]),'SNE':([19,20,33,34,35,36,37,39,41,42,43,44,45,46,47,48,50,51,56,57,59,60,65,94,95,96,97,98,99,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,151,163,181,],[-56,-57,78,-80,-81,-82,-83,78,-80,-81,-82,-83,-62,-65,-69,-71,-75,-76,-60,-61,-58,-59,-84,-54,-73,-74,-78,-79,-55,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-41,-49,-50,]),'SLT':([19,20,33,34,35,36,37,39,41,42,43,44,45,46,47,48,50,51,56,57,59,60,65,94,95,96,97,98,99,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,151,163,181,],[-56,-57,79,-80,-81,-82,-83,79,-80,-81,-82,-83,-62,-65,-69,-71,-75,-76,-60,-61,-58,-59,-84,-54,-73,-74,-78,-79,-55,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-41,-49,-50,]),'SGT':([19,20,33,34,35,36,37,39,41,42,43,44,45,46,47,48,50,51,56,57,59,60,65,94,95,96,97,98,99,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,151,163,181,],[-56,-57,80,-80,-81,-82,-83,80,-80,-81,-82,-83,-62,-65,-69,-71,-75,-76,-60,-61,-58,-59,-84,-54,-73,-74,-78,-79,-55,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-41,-49,-50,]),'SLE':([19,20,33,34,35,36,37,39,41,42,43,44,45,46,47,48,50,51,56,57,59,60,65,94,95,96,97,98,99,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,151,163,181,],[-56,-57,81,-80,-81,-82,-83,81,-80,-81,-82,-83,-62,-65,-69,-71,-75,-76,-60,-61,-58,-59,-84,-54,-73,-74,-78,-79,-55,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-41,-49,-50,]),'SGE':([19,20,33,34,35,36,37,39,41,42,43,44,45,46,47,48,50,51,56,57,59,60,65,94,95,96,97,98,99,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,151,163,181,],[-56,-57,82,-80,-81,-82,-83,82,-80,-81,-82,-83,-62,-65,-69,-71,-75,-76,-60,-61,-58,-59,-84,-54,-73,-74,-78,-79,-55,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-41,-49,-50,]),'RPAREN':([19,20,30,32,33,34,35,36,37,41,42,43,44,45,46,47,48,50,51,56,57,59,60,64,65,66,67,68,91,92,93,94,95,96,97,98,99,101,103,105,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,138,146,151,158,160,161,163,175,177,181,],[-56,-57,65,69,-40,-80,-81,-82,-83,-74,-73,-78,-79,-62,-65,-69,-71,-75,-76,-60,-61,-58,-59,104,-84,106,-32,108,130,108,131,-54,-73,-74,-78,-79,-55,-26,135,137,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-33,-27,-41,163,167,168,-49,179,181,-50,]),'XOR':([19,20,33,34,35,36,37,39,41,42,43,44,45,46,47,48,50,51,56,57,59,60,65,92,94,95,96,97,98,99,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,151,163,181,],[-56,-57,-40,-80,-81,-82,-83,-40,-74,-73,-78,-79,-62,-65,-69,89,-75,-76,-60,-61,-58,-59,-84,-75,-54,-73,-74,-78,-79,-55,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-41,-49,-50,]),'TIMES':([19,20,33,34,35,36,37,39,41,42,43,44,45,46,47,48,50,51,56,57,59,60,65,92,94,95,96,97,98,99,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,151,163,181,],[-56,-57,-40,-80,-81,-82,-83,-40,-74,-73,-78,-79,-62,86,-69,-71,-75,-76,-60,-61,-58,-59,-84,-75,-54,-73,-74,-78,-79,-55,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,86,86,-66,-67,-68,-69,-72,-41,-49,-50,]),'DIVIDE':([19,20,33,34,35,36,37,39,41,42,43,44,45,46,47,48,50,51,56,57,59,60,65,92,94,95,96,97,98,99,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,151,163,181,],[-56,-57,-40,-80,-81,-82,-83,-40,-74,-73,-78,-79,-62,87,-69,-71,-75,-76,-60,-61,-58,-59,-84,-75,-54,-73,-74,-78,-79,-55,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,87,87,-66,-67,-68,-69,-72,-41,-49,-50,]),'MODULO':([19,20,33,34,35,36,37,39,41,42,43,44,45,46,47,48,50,51,56,57,59,60,65,92,94,95,96,97,98,99,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,151,163,181,],[-56,-57,-40,-80,-81,-82,-83,-40,-74,-73,-78,-79,-62,88,-69,-71,-75,-76,-60,-61,-58,-59,-84,-75,-54,-73,-74,-78,-79,-55,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,88,88,-66,-67,-68,-69,-72,-41,-49,-50,]),'PLUS':([19,20,33,34,35,36,37,39,41,42,43,44,45,46,47,48,50,51,56,57,59,60,65,92,94,95,96,97,98,99,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,151,163,181,],[-56,-57,-40,-80,-81,-82,-83,-40,-74,-73,-78,-79,84,-65,-69,-71,-75,-76,-60,-61,-58,-59,-84,-75,-54,-73,-74,-78,-79,-55,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,84,-63,-64,-66,-67,-68,-69,-72,-41,-49,-50,]),'MINUS':([19,20,33,34,35,36,37,39,41,42,43,44,45,46,47,48,50,51,56,57,59,60,65,92,94,95,96,97,98,99,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,151,163,181,],[-56,-57,-40,-80,-81,-82,-83,-40,-74,-73,-78,-79,85,-65,-69,-71,-75,-76,-60,-61,-58,-59,-84,-75,-54,-73,-74,-78,-79,-55,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,85,-63,-64,-66,-67,-68,-69,-72,-41,-49,-50,]),'COMMA':([19,20,33,34,35,36,37,45,46,47,48,50,51,56,57,59,60,65,67,94,95,96,97,98,99,101,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,151,163,181,],[-56,-57,-40,-80,-81,-82,-83,-62,-65,-69,-71,-75,-76,-60,-61,-58,-59,-84,107,-54,-73,-74,-78,-79,-55,133,-85,-34,-35,-36,-37,-38,-39,-42,-43,-44,-45,-46,-47,-48,-77,-63,-64,-66,-67,-68,-69,-72,-41,-49,-50,]),'LBRACE':([24,69,104,131,135,137,164,167,179,187,],[62,109,136,144,144,149,170,172,182,188,]),'LAND':([108,163,],[140,140,]),'LOR':([108,163,],[141,141,]),'LNOT':([108,163,],[142,142,]),'WHILE':([134,],[147,]),'ELSE':([159,184,],[164,187,]),'ELSIF':([159,184,],[166,166,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,2,3,],[1,25,26,]),'blockcode':([0,2,3,4,62,109,136,144,149,170,172,182,188,],[2,2,2,27,102,143,148,153,157,174,176,183,189,]),'function':([0,2,3,],[3,3,3,]),'command':([0,2,3,4,62,109,136,144,149,170,172,182,188,],[4,4,4,4,4,4,4,4,4,4,4,4,4,]),'interations':([0,2,3,4,62,109,136,144,149,170,172,182,188,],[8,8,8,8,8,8,8,8,8,8,8,8,8,]),'if':([0,2,3,4,62,109,136,144,149,170,172,182,188,],[9,9,9,9,9,9,9,9,9,9,9,9,9,]),'exp_assignment':([0,2,3,4,7,12,30,31,49,54,55,58,61,62,63,64,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,86,87,88,89,90,107,109,132,133,136,144,149,150,154,155,170,171,172,173,182,188,],[10,10,10,10,34,41,67,34,41,34,96,96,101,10,34,67,34,34,34,34,34,34,34,34,34,34,34,34,34,96,96,96,96,96,96,41,67,10,34,101,10,10,10,34,101,34,10,34,10,34,10,10,]),'call':([0,2,3,4,12,49,55,58,62,84,85,86,87,88,89,90,109,136,144,149,170,172,182,188,],[11,11,11,11,51,51,51,51,11,51,51,51,51,51,51,51,11,11,11,11,11,11,11,11,]),'for':([0,2,3,4,62,109,136,144,149,170,172,182,188,],[15,15,15,15,15,15,15,15,15,15,15,15,15,]),'dowhile':([0,2,3,4,62,109,136,144,149,170,172,182,188,],[16,16,16,16,16,16,16,16,16,16,16,16,16,]),'while':([0,2,3,4,62,109,136,144,149,170,172,182,188,],[17,17,17,17,17,17,17,17,17,17,17,17,17,]),'exp_condition':([7,12,31,49,54,55,58,63,84,85,86,87,88,89,90,132,150,155,171,173,],[32,50,68,92,93,50,50,103,50,50,50,50,50,50,92,145,158,161,175,177,]),'attcond':([7,12,31,49,54,55,58,63,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,86,87,88,89,90,132,150,155,171,173,],[33,39,33,33,33,33,33,33,110,111,112,113,114,115,116,117,118,119,120,121,122,33,33,33,33,33,33,33,33,33,33,33,33,]),'return':([12,],[38,]),'arithmetic':([12,49,55,58,90,],[40,91,94,99,91,]),'exp':([12,49,55,58,84,85,86,87,88,89,90,],[45,45,45,45,123,123,123,123,123,123,45,]),'exp1':([12,49,55,58,84,85,86,87,88,89,90,],[46,46,46,46,124,125,46,46,46,46,46,]),'exp2':([12,49,55,58,84,85,86,87,88,89,90,],[47,47,47,47,47,47,126,127,128,129,47,]),'exp3':([12,49,55,58,84,85,86,87,88,89,90,],[48,48,48,48,48,48,48,48,48,48,48,]),'function_assignments':([30,64,107,],[66,105,138,]),'for_assignments':([61,133,154,],[100,146,160,]),'logic':([108,163,],[139,169,]),'exp_condition_logic':([139,],[151,]),'elsif':([159,184,],[165,186,]),'elsif2':([184,],[185,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> blockcode init','init',2,'p_init','syntactic.py',6),
  ('init -> function init','init',2,'p_init','syntactic.py',7),
  ('init -> blockcode','init',1,'p_init','syntactic.py',8),
  ('init -> function','init',1,'p_init','syntactic.py',9),
  ('blockcode -> command','blockcode',1,'p_blockcode','syntactic.py',13),
  ('blockcode -> command blockcode','blockcode',2,'p_blockcode','syntactic.py',14),
  ('command -> interations','command',1,'p_command','syntactic.py',18),
  ('command -> if','command',1,'p_command','syntactic.py',19),
  ('command -> exp_assignment','command',1,'p_command','syntactic.py',20),
  ('command -> call','command',1,'p_command','syntactic.py',21),
  ('command -> RETURN return SEMICOLON','command',3,'p_command','syntactic.py',22),
  ('command -> BREAK SEMICOLON','command',2,'p_command','syntactic.py',23),
  ('command -> CONTINUE SEMICOLON','command',2,'p_command','syntactic.py',24),
  ('if -> IF LPAREN exp_condition RPAREN LBRACE blockcode RBRACE','if',7,'p_if','syntactic.py',29),
  ('if -> command IF LPAREN exp_condition RPAREN','if',5,'p_if','syntactic.py',30),
  ('if -> IF LPAREN exp_condition RPAREN LBRACE blockcode RBRACE ELSE LBRACE blockcode RBRACE','if',11,'p_if','syntactic.py',31),
  ('if -> IF LPAREN exp_condition RPAREN LBRACE blockcode RBRACE elsif','if',8,'p_if','syntactic.py',32),
  ('elsif -> ELSIF LPAREN exp_condition RPAREN LBRACE blockcode RBRACE','elsif',7,'p_elsif','syntactic.py',36),
  ('elsif -> ELSIF LPAREN exp_condition RPAREN LBRACE blockcode RBRACE elsif2','elsif',8,'p_elsif','syntactic.py',37),
  ('elsif2 -> elsif','elsif2',1,'p_elsif2','syntactic.py',41),
  ('elsif2 -> ELSE LBRACE blockcode RBRACE','elsif2',4,'p_elsif2','syntactic.py',42),
  ('interations -> for','interations',1,'p_interations','syntactic.py',47),
  ('interations -> dowhile','interations',1,'p_interations','syntactic.py',48),
  ('interations -> while','interations',1,'p_interations','syntactic.py',49),
  ('for -> FOR LPAREN for_assignments SEMICOLON exp_condition SEMICOLON for_assignments RPAREN LBRACE blockcode RBRACE','for',11,'p_for','syntactic.py',53),
  ('for_assignments -> exp_assignment','for_assignments',1,'p_for_assignments','syntactic.py',56),
  ('for_assignments -> exp_assignment COMMA for_assignments','for_assignments',3,'p_for_assignments','syntactic.py',57),
  ('dowhile -> DO LBRACE blockcode RBRACE WHILE LPAREN exp_condition RPAREN','dowhile',8,'p_dowhile','syntactic.py',61),
  ('while -> LPAREN exp_condition RPAREN LBRACE blockcode RBRACE','while',6,'p_while','syntactic.py',64),
  ('function -> SUB ID LPAREN RPAREN LBRACE blockcode RBRACE','function',7,'p_function','syntactic.py',67),
  ('function -> SUB ID LPAREN function_assignments RPAREN LBRACE blockcode RBRACE','function',8,'p_function','syntactic.py',68),
  ('function_assignments -> exp_assignment','function_assignments',1,'p_function_assignments','syntactic.py',72),
  ('function_assignments -> exp_assignment COMMA function_assignments','function_assignments',3,'p_function_assignments','syntactic.py',73),
  ('exp_condition -> attcond GT attcond','exp_condition',3,'p_exp_condition','syntactic.py',78),
  ('exp_condition -> attcond LT attcond','exp_condition',3,'p_exp_condition','syntactic.py',79),
  ('exp_condition -> attcond EQ attcond','exp_condition',3,'p_exp_condition','syntactic.py',80),
  ('exp_condition -> attcond GE attcond','exp_condition',3,'p_exp_condition','syntactic.py',81),
  ('exp_condition -> attcond LE attcond','exp_condition',3,'p_exp_condition','syntactic.py',82),
  ('exp_condition -> attcond NE attcond','exp_condition',3,'p_exp_condition','syntactic.py',83),
  ('exp_condition -> attcond','exp_condition',1,'p_exp_condition','syntactic.py',84),
  ('exp_condition -> LPAREN exp_condition RPAREN logic exp_condition_logic','exp_condition',5,'p_exp_condition','syntactic.py',85),
  ('exp_condition -> attcond CMP attcond','exp_condition',3,'p_exp_condition','syntactic.py',86),
  ('exp_condition -> attcond SEQ attcond','exp_condition',3,'p_exp_condition','syntactic.py',87),
  ('exp_condition -> attcond SNE attcond','exp_condition',3,'p_exp_condition','syntactic.py',88),
  ('exp_condition -> attcond SLT attcond','exp_condition',3,'p_exp_condition','syntactic.py',89),
  ('exp_condition -> attcond SGT attcond','exp_condition',3,'p_exp_condition','syntactic.py',90),
  ('exp_condition -> attcond SLE attcond','exp_condition',3,'p_exp_condition','syntactic.py',91),
  ('exp_condition -> attcond SGE attcond','exp_condition',3,'p_exp_condition','syntactic.py',92),
  ('exp_condition_logic -> LPAREN exp_condition RPAREN','exp_condition_logic',3,'p_exp_condition_logic','syntactic.py',97),
  ('exp_condition_logic -> LPAREN exp_condition RPAREN logic LPAREN exp_condition RPAREN','exp_condition_logic',7,'p_exp_condition_logic','syntactic.py',98),
  ('logic -> LAND','logic',1,'p_logic','syntactic.py',103),
  ('logic -> LOR','logic',1,'p_logic','syntactic.py',104),
  ('logic -> LNOT','logic',1,'p_logic','syntactic.py',105),
  ('exp_assignment -> ID_SC EQUALS arithmetic','exp_assignment',3,'p_exp_assignment','syntactic.py',109),
  ('exp_assignment -> ID_LI EQUALS arithmetic','exp_assignment',3,'p_exp_assignment','syntactic.py',110),
  ('exp_assignment -> ID_SC','exp_assignment',1,'p_exp_assignment','syntactic.py',111),
  ('exp_assignment -> ID_LI','exp_assignment',1,'p_exp_assignment','syntactic.py',112),
  ('exp_assignment -> INCREMENT ID_SC','exp_assignment',2,'p_exp_assignment','syntactic.py',113),
  ('exp_assignment -> DECREMENT ID_SC','exp_assignment',2,'p_exp_assignment','syntactic.py',114),
  ('exp_assignment -> ID_SC INCREMENT','exp_assignment',2,'p_exp_assignment','syntactic.py',115),
  ('exp_assignment -> ID_SC DECREMENT','exp_assignment',2,'p_exp_assignment','syntactic.py',116),
  ('arithmetic -> exp','arithmetic',1,'p_arithmetic','syntactic.py',121),
  ('exp -> exp PLUS exp1','exp',3,'p_exp','syntactic.py',126),
  ('exp -> exp MINUS exp1','exp',3,'p_exp','syntactic.py',127),
  ('exp -> exp1','exp',1,'p_exp','syntactic.py',128),
  ('exp1 -> exp1 TIMES exp2','exp1',3,'p_exp1','syntactic.py',133),
  ('exp1 -> exp1 DIVIDE exp2','exp1',3,'p_exp1','syntactic.py',134),
  ('exp1 -> exp1 MODULO exp2','exp1',3,'p_exp1','syntactic.py',135),
  ('exp1 -> exp2','exp1',1,'p_exp1','syntactic.py',136),
  ('exp2 -> exp3 XOR exp2','exp2',3,'p_exp2','syntactic.py',141),
  ('exp2 -> exp3','exp2',1,'p_exp2','syntactic.py',142),
  ('exp3 -> LPAREN arithmetic RPAREN','exp3',3,'p_exp3','syntactic.py',147),
  ('exp3 -> NUMBER','exp3',1,'p_exp3','syntactic.py',148),
  ('exp3 -> exp_assignment','exp3',1,'p_exp3','syntactic.py',149),
  ('exp3 -> exp_condition','exp3',1,'p_exp3','syntactic.py',150),
  ('exp3 -> call','exp3',1,'p_exp3','syntactic.py',151),
  ('exp3 -> exp','exp3',1,'p_exp3','syntactic.py',152),
  ('exp3 -> TRUE','exp3',1,'p_exp3','syntactic.py',153),
  ('exp3 -> FALSE','exp3',1,'p_exp3','syntactic.py',154),
  ('attcond -> exp_assignment','attcond',1,'p_attcond','syntactic.py',158),
  ('attcond -> NUMBER','attcond',1,'p_attcond','syntactic.py',159),
  ('attcond -> TRUE','attcond',1,'p_attcond','syntactic.py',160),
  ('attcond -> FALSE','attcond',1,'p_attcond','syntactic.py',161),
  ('call -> ID LPAREN RPAREN','call',3,'p_call','syntactic.py',166),
  ('call -> ID LPAREN function_assignments RPAREN','call',4,'p_call','syntactic.py',167),
  ('return -> attcond','return',1,'p_return','syntactic.py',171),
  ('return -> arithmetic','return',1,'p_return','syntactic.py',172),
]
