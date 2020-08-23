import ply.yacc as yacc
from lexer import tokens

precedence = (
	('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQUAL'),
    ('left', 'EQUALEQUAL', 'NOTEQUAL'),
    ('nonassoc', 'LESSTHAN', 'LESSEQUAL', 'GREATERTHAN', 'GREATEREQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE', 'MOD'),
    ('left', 'POWER'),
    ('right', 'NOT'),
    ('nonassoc','INCR', 'DECR'),
    ('nonassoc', 'LBRAC', 'RBRAC'),
)


def p_line(p):
	'''
	lines : last SEMICOLON
		  | last SEMICOLON lines
	'''
	if(len(p) > 3):
		p[0] = [p[1]] + p[3]
	else:
		p[0] = [p[1]]



def p_last(p):
	'''
	last : codestmt 
		 | output 
		 | list
		 | var_assign 
		 | var_declare 
		 | if_exp 
		 | empty

	'''
	p[0] = p[1]

def p_list(p):
	'''
	list : list_declare
		 | list_assign
		 | list_access
		 | list_funcs
	'''
	p[0] = ("list", p[1])

def p_list_declare(p):
	'''
	list_declare : NAME FATARROW SLBRAC SRBRAC
	'''
	p[0] = ("listdeclare", p[1])

def p_list_assign(p):
	'''
	list_assign : NAME EQUAL SLBRAC result SRBRAC
	'''
	p[0] = ("listassign", p[1], p[4])

def p_list_access(p):
	'''
	list_access : NAME SLBRAC INT SRBRAC
	'''
	p[0] = ("listaccess", p[1], p[3])

def p_list_funcs(p):
	'''
	list_funcs : list_pop
			   | list_push
			   | list_slice
			   | list_index
	'''
	p[0] = ("listfunc", p[1])

def p_list_pop(p):
	'''
	list_pop : NAME DOT POP LBRAC INT RBRAC
	'''
	p[0] = ("pop", p[1], p[5])

def p_list_push(p):
	'''
	list_push : NAME DOT PUSH LBRAC INT RBRAC
			  | NAME DOT PUSH LBRAC FLOAT RBRAC
			  | NAME DOT PUSH LBRAC CHAR RBRAC
			  | NAME DOT PUSH LBRAC STRING RBRAC
			  | NAME DOT PUSH LBRAC BOOL RBRAC
	'''
	p[0] = ("push", p[1], p[5])


def p_list_slice(p):
	'''
	list_slice : NAME DOT SLICE LBRAC sliceval RBRAC
	'''
	p[0] = ("slice", p[1], p[5])

def p_list_slice_val(p):
	'''
	sliceval : INT COLON
	         | COLON INT
			 | INT COLON INT
			 | COLON
	'''
	if len(p) == 3:
		if p[1] == ":":
			p[0] = ("end", p[2])
		else:
			p[0] = ("start", p[1])
	elif len(p) == 2:
		p[0] = ("all", p[1])
	else:
		p[0] = (p[1], p[3])

def p_list_index(p):
	'''
	list_index : NAME DOT INDEX LBRAC INT RBRAC
	'''
	p[0] = ("index", p[1], p[5])

def p_ifexp(p):
	'''
	if_exp : if_statement
		   | if_statement else_statement
		   | if_statement elif_stmt
		   | if_statement elif_stmt else_statement
	'''
	if len(p) == 2:
		p[0] = ("ifstmt", p[1])
	elif len(p) == 3:
		p[0] = ("ifelsestmt", p[1], p[2])
	else:
		p[0] = ("ifelifelsestmt",p[1], p[2], p[3])

def p_ifstmt(p):
	'''
	if_statement : IF LBRAC codestmt RBRAC block
	'''
	p[0] = ("if",p[3], p[5])

def p_else(p):
	'''
	else_statement : ELSE block
	'''
	p[0] = ("else", p[2])

def p_elif(p):
	'''
	elif_stmt : else_if_statement
			  | else_if_statement elif_stmt
	'''
	if(len(p) > 2):
		p[0] = [p[1]] + p[2]
	else:
		p[0] = p[1]


def p_elseif(p):
	'''
	else_if_statement : ELSEIF LBRAC codestmt RBRAC block
	'''
	p[0] = ("else_if", p[3], p[5])

def p_block(p):
	'''
	block : CLBRAC codeblock CRBRAC
	'''
	p[0] = ("block",p[2])

def p_codeblock(p):
	'''
	codeblock : code SEMICOLON
			  | code SEMICOLON codeblock
	'''
	if(len(p) > 3):
		p[0] = [p[1]] + p[3]
	else:
		p[0] = [p[1]]

def p_code(p):
	'''
	code : codestmt
		 | var_assign
		 | var_declare
		 | output
		 | list
		 | if_exp
	'''
	p[0] = p[1]
	
def p_print(p):
	'''
	output : PRINT LBRAC result RBRAC
	'''
	p[0] = ("print", p[3])

def p_result(p):
	'''
	result : printstmt
		   | printstmt COMMA result
		   | list_access 
		   | list_access COMMA result
		   | list_funcs
		   | list_funcs COMMA result
	'''
	if len(p) == 2:
		p[0] = [p[1]]
	else:
		p[0] = [p[1]] + p[3]


def p_printstmt(p):
	'''
	printstmt : codestmt
	'''
	p[0] = p[1]

def p_var_assign(p):
	'''
	var_assign : NAME EQUAL codestmt
	'''
	p[0] = ('=', p[1],p[3])

def p_var_declare(p):
    '''
    var_declare : TYPE NAME
                | TYPE NAME EQUAL codestmt
    ''' 
    if(len(p) < 5):
    	p[0] = ("declare", p[1], p[2])
    else:
    	p[0] = ("declare", p[1], p[2], p[4])
        

def p_empty(p):
	'''
	empty :
	'''
	return None
def p_negative_num(p):
	'''
	codestmt : MINUS codestmt
	'''
	p[0] = (p[1], 0, p[2])

def p_codestmt_operands(p):
	'''
	codestmt : codestmt PLUS codestmt
			 | codestmt MINUS codestmt
			 | codestmt MULTIPLY codestmt
			 | codestmt DIVIDE codestmt
			 | codestmt MOD codestmt
			 | codestmt POWER codestmt		   

	'''
	p[0] = (p[2], p[1], p[3])
	
def p_codestmt_list(p):
	'''
	codestmt : list_funcs PLUS codestmt
			 | list_funcs MINUS codestmt
			 | list_funcs MULTIPLY codestmt
			 | list_funcs DIVIDE codestmt
			 | list_funcs MOD codestmt
			 | list_funcs POWER codestmt
			 | codestmt PLUS list_funcs
			 | codestmt MINUS list_funcs
			 | codestmt MULTIPLY list_funcs
			 | codestmt DIVIDE list_funcs
			 | codestmt MOD list_funcs
			 | codestmt POWER list_funcs				   

	'''
	p[0] = (p[2], p[1], p[3])
def p_codestmt_comparison(p):
	'''
	codestmt : codestmt LESSTHAN codestmt
			 | codestmt GREATERTHAN codestmt
			 | codestmt LESSEQUAL codestmt
			 | codestmt GREATEREQUAL codestmt
			 | codestmt NOTEQUAL codestmt
			 | codestmt EQUALEQUAL codestmt
			 | codestmt AND codestmt
			 | codestmt OR codestmt
	'''
	p[0] = (p[2], p[1], p[3])

def p_codestmt_brac(p):
	'''
	codestmt : LBRAC codestmt RBRAC
	'''
	p[0] = (p[2])

def p_codestmt_not(p):
	'''
	codestmt : NOT codestmt
	'''
	p[0] = (p[1],p[2])

def p_codestmt_INCR(p):
	'''
	codestmt : codestmt INCR
	'''
	p[0] = (p[1],p[2])

def p_codestmt_DECR(p):
	'''
	codestmt : codestmt DECR
	'''
	p[0] = (p[1],p[2])

def p_codestmt_var(p):
	'''
	codestmt : NAME
	'''
	p[0] = ('var',p[1])

def p_codestmt_bool(p):
	'''
	codestmt : BOOL
	'''
	p[0] = ('bool',p[1])

def p_codestmt_char(p):
	'''
	codestmt : CHAR
	'''
	p[0] = ('char',p[1])

def p_codestmt_string(p):
	'''
	codestmt : STRING
	'''
	p[0] = ('string',p[1])


def p_codestmt_digits(p):
	'''
	codestmt : INT
			 | FLOAT
	'''
	p[0] = p[1]

def p_error(p):
     print("Syntax error in input!")

