 # ------------------------------------------------------------
 # tokenizer for a simple expression evaluator for
 # numbers and +,-,*,/
 # ------------------------------------------------------------

import ply.lex as lex
 
reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'elif' : 'ELSEIF'
}

 # List of token names.   This is always required
tokens = [
    'INT',
    'FLOAT',
    'CHAR', 
    'STRING',
    'BOOL',
    'COMMA',
    'PLUS',
    'EQUAL',
    'MINUS',
    'MULTIPLY',
    'INCR',
    'DECR',
    'DIVIDE',
    'POWER',
    'MOD',
    'LBRAC',
    'RBRAC',
    'CLBRAC',
    'CRBRAC',
    'SLBRAC',
    'SRBRAC',
    'FATARROW',
    'SEMICOLON',
    'AND',
    'NOT',
    'OR',
    'EQUALEQUAL',
    'LESSTHAN',
    'GREATERTHAN',
    'LESSEQUAL',
    'GREATEREQUAL',
    'NOTEQUAL',
    'TYPE',
    'NAME',
    'PRINT',
    'PUSH',
    'POP',
    'SLICE',
    'INDEX',
    'COLON',
    'DOT'
] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE  = r'\/'
t_MOD = r'\%'
t_EQUAL = r'\='
t_LBRAC = r'\('
t_RBRAC = r'\)'
t_CLBRAC = r'\{'
t_CRBRAC = r'\}'
t_FATARROW = r'\=\>'
t_SEMICOLON = r'\;'
t_EQUALEQUAL = r'\=\='
t_LESSEQUAL = r'\<\='
t_GREATEREQUAL = r'\>\='
t_LESSTHAN = r'\<'
t_GREATERTHAN = r'\>'
t_NOTEQUAL = r'\!\='
t_ignore = ' \t'
t_COMMA = r'\,'
t_COLON = r'\:'
t_DOT = r'\.'

def t_TYPE(t):
    r'int|float|string|bool|char'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_PUSH(t):
    r'push'
    return t

def t_POP(t):
    r'pop'
    return t

def t_SLICE(t):
    r'slice'
    return t

def t_INDEX(t):
    r'index'
    return t

def t_FLOAT(t):
   r'\d+\.\d+'
   t.value = float(t.value)
   return t

def t_BOOL(t):
    r'true|false'
    return t
   
def t_INT(t):
   r'\d+'
   t.value = int(t.value)
   return t

def t_CHAR(t):
    r"'\\?[^']'"
    t.value = t.value[1:-1]
    return t

def t_STRING(t):
    r'"[^"\n]*"'
    t.value = t.value[1:-1]
    return t

def t_POWER(t):
    r'\^'
    return t

def t_INCR(t):
    r'\+\+'
    return t

def t_DECR(t):
    r'\-\-'
    return t

def t_AND(t):
  r'and'
  return t

def t_OR(t):
  r'or'
  return t

def t_NOT(t):
  r'not'
  return t

# def t_IF(t):
#     r'if'
#     return t

# def t_ELSEIF(t):
#     r'elif'
#     return t
    
# def t_ELSE(t):
#     r'else'
#     return t

def t_SLBRAC(t):
    r'\['
    return t
def t_SRBRAC(t):
    r'\]'
    return t

def t_NAME(t):
    r'[a-zA-z_][a-zA-Z_0-9]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    else:
        t.type = 'NAME'
    return t

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

def t_error(t):
   print("Illegal characters!")
   t.lexer.skip(1)



lexer = lex.lex()

