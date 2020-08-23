import lexer
import parser
import ply.lex as lex
import ply.yacc as yacc
import sys, os

env = {}

def typecheck(val1, val2):
    typecheckans = isinstance(val1, int) or isinstance(val1, float) or isinstance(val1, str)
    typecheckval = isinstance(val2, int) or isinstance(val2, float) or isinstance(val2, str)
    if((type(val1) is int) or (type(val1) is float)) and ((type(val2) is int) or (type(val2) is float)):
        check = True
    else:
        check = type(val1) == type(val2)
    return typecheckans and typecheckval and check

def addition(val1,val2):
    if type(val1) is tuple and type(val2) is tuple:
        if val1[0] == "listfunc":
            val1 = ("list",val1)
            exp1 = run(env, val1) 
            exp2 = run(env, val2)
        elif val2[0] == "listfunc":
            val2 = ("list",val2)
            exp1 = run(env, val1) 
            exp2 = run(env, val2)
        else:
            exp1 = run(env, val1) 
            exp2 = run(env, val2)
        if exp1 in ["true", "false"] or exp2 in ["true","false"]:
            exit("UNDEFINED")
        else:
            if typecheck(exp1, exp2):
                return exp1 + exp2
            else:
                exit("UNDEFINED")
    elif type(val1) is tuple:
        if val1[0] == "listfunc":
            val1 = ("list",val1)
            ans = run(env, val1) 
        else:
            ans = run(env, val1)
        val = val2
        if ans in ["true", "false"] or val in ["true","false"]:
            exit("UNDEFINED")
        else:
            if typecheck(ans,val):
                return val + ans
            else:
                exit("UNDEFINED")
    elif type(val2) is tuple:
        if val2[0] == "listfunc":
            val2 = ("list",val2)
            ans = run(env, val2)
        else:
            ans = run(env, val2)
        val = val1
        if ans in ["true", "false"] or val in ["true","false"]:
            exit("UNDEFINED")
        else:
            if typecheck(ans,val):
                return val + ans
            else:
                exit("UNDEFINED")
    else:
        exp1 = val1
        exp2 = val2
        if exp1 in ["true", "false"] or exp2 in ["true","false"]:
            exit("UNDEFINED")
        else:
            if typecheck(exp1, exp2):
                return exp1 + exp2
            else:
                exit("UNDEFINED")

def subtraction(val1,val2):
    if type(val1) is tuple and type(val2) is tuple:
        if val1[0] == "listfunc":
            val1 = ("list",val1)
            exp1 = run(env, val1) 
            exp2 = run(env, val2)
        elif val2[0] == "listfunc":
            val2 = ("list",val2)
            exp1 = run(env, val1) 
            exp2 = run(env, val2)
        else:
            exp1 = run(env, val1) 
            exp2 = run(env, val2)
        if exp1 in ["true", "false"] or exp2 in ["true","false"] or isinstance(exp1,str) or isinstance(exp2, str):
            exit("UNDEFINED")
        else:
            if typecheck(exp1, exp2):
                return exp1 - exp2
            else:
                exit("UNDEFINED")
    elif type(val1) is tuple:
        if val1[0] == "listfunc":
            val1 = ("list",val1)
            ans = run(env, val1) 
        else:
            ans = run(env, val1)
        val = val2
        if ans in ["true", "false"] or val in ["true","false"] or isinstance(ans,str) or isinstance(val, str):
            exit("UNDEFINED")
        else:
            if typecheck(ans,val):
                return val - ans
            else:
                exit("UNDEFINED")
    elif type(val2) is tuple:
        if val2[0] == "listfunc":
            val2 = ("list",val2)
            ans = run(env, val2)
        else:
            ans = run(env, val2)
        val = val1
        if ans in ["true", "false"] or val in ["true","false"] or isinstance(ans,str) or isinstance(val, str):
            exit("UNDEFINED")
        else:
            if typecheck(ans,val):
                return val - ans
            else:
                exit("UNDEFINED")
    else:
        exp1 = val1
        exp2 = val2
        if exp1 in ["true", "false"] or exp2 in ["true","false"] or isinstance(exp1,str) or isinstance(exp2, str):
            exit("UNDEFINED")
        else:
            if typecheck(exp1, exp2):
                return exp1 - exp2
            else:
                exit("UNDEFINED")

def multiplication(val1,val2):
    if type(val1) is tuple and type(val2) is tuple:
        if val1[0] == "listfunc":
            val1 = ("list",val1)
            exp1 = run(env, val1) 
            exp2 = run(env, val2)
        elif val2[0] == "listfunc":
            val2 = ("list",val2)
            exp1 = run(env, val1) 
            exp2 = run(env, val2)
        else:
            exp1 = run(env, val1) 
            exp2 = run(env, val2)
        if exp1 in ["true", "false"] or exp2 in ["true","false"] or isinstance(exp1,str) or isinstance(exp2, str):
            exit("UNDEFINED")
        else:
            if typecheck(exp1, exp2):
                return exp1 * exp2
            else:
                exit("UNDEFINED")
    elif type(val1) is tuple:
        if val1[0] == "listfunc":
            val1 = ("list",val1)
            ans = run(env, val1) 
        else:
            ans = run(env, val1)
        val = val2
        if ans in ["true", "false"] or val in ["true","false"] or isinstance(ans,str) or isinstance(val, str):
            exit("UNDEFINED")
        else:
            if typecheck(ans,val):
                return val * ans
            else:
                exit("UNDEFINED")
    elif type(val2) is tuple:
        if val2[0] == "listfunc":
            val2 = ("list",val2)
            ans = run(env, val2)
        else:
            ans = run(env, val2)
        val = val1
        if ans in ["true", "false"] or val in ["true","false"] or isinstance(ans,str) or isinstance(val, str):
            exit("UNDEFINED")
        else:
            if typecheck(ans,val):
                return val * ans
            else:
                exit("UNDEFINED")
    else:
        exp1 = val1
        exp2 = val2
        if exp1 in ["true", "false"] or exp2 in ["true","false"] or isinstance(exp1,str) or isinstance(exp2, str):
            exit("UNDEFINED")
        else:
            if typecheck(exp1, exp2):
                return exp1 * exp2
            else:
                exit("UNDEFINED")

def division(val1,val2):
    if type(val1) is tuple and type(val2) is tuple:
        if val1[0] == "listfunc":
            val1 = ("list",val1)
            exp1 = run(env, val1) 
            exp2 = run(env, val2)
        elif val2[0] == "listfunc":
            val2 = ("list",val2)
            exp1 = run(env, val1) 
            exp2 = run(env, val2)
        else:
            exp1 = run(env, val1) 
            exp2 = run(env, val2)
        if exp1 in ["true", "false"] or exp2 in ["true","false"] or isinstance(exp1,str) or isinstance(exp2, str):
            exit("UNDEFINED")
        else:
            if typecheck(exp1, exp2):
                return exp1 / exp2
            else:
                exit("UNDEFINED")
    elif type(val1) is tuple:
        if val1[0] == "listfunc":
            val1 = ("list",val1)
            ans = run(env, val1) 
        else:
            ans = run(env, val1)
        val = val2
        if ans in ["true", "false"] or val in ["true","false"] or isinstance(ans,str) or isinstance(val, str):
            exit("UNDEFINED")
        else:
            if typecheck(ans,val):
                return val / ans
            else:
                exit("UNDEFINED")
    elif type(val2) is tuple:
        if val2[0] == "listfunc":
            val2 = ("list",val2)
            ans = run(env, val2)
        else:
            ans = run(env, val2)
        val = val1
        if ans in ["true", "false"] or val in ["true","false"] or isinstance(ans,str) or isinstance(val, str):
            exit("UNDEFINED")
        else:
            if typecheck(ans,val):
                return val / ans
            else:
                exit("UNDEFINED")
    else:
        exp1 = val1
        exp2 = val2
        if exp1 in ["true", "false"] or exp2 in ["true","false"] or isinstance(exp1,str) or isinstance(exp2, str):
            exit("UNDEFINED")
        else:
            if typecheck(exp1, exp2):
                return exp1 / exp2
            else:
                exit("UNDEFINED")

def typecheckcompare(val1, val2):
    typecheckans = isinstance(val1, int) or isinstance(val1, float) or isinstance(val1, str)
    typecheckval = isinstance(val2, int) or isinstance(val2, float) or isinstance(val2, str)
    if (val1 == "false" or val1 == "true") and (type(val2) is int or type(val2) is float):
        check = True
    elif (val2 == "false" or val2 == "true") and (type(val1) is int or type(val1) is float):
        check = True
    else:
        check = type(val1) == type(val2)
    return typecheckans and typecheckval and check

def lessthan(val1, val2):
    if type(val1) is tuple and type(val2) is tuple:
        ans1 = run(env,val1)
        ans2 = run(env,val2)
        if typecheckcompare(ans1,ans2):
            if ans1 == "true":
                ans1 = 1
            if ans1 == "false":
                ans1 = 0
            if ans2 == "true":
                ans2 = 1
            if ans2 == "false":
                ans2 = 0
            if(ans1 < ans2):
                return "true"
            else:
                return "false"
        else:
            exit("TYPEERROR!")
    if type(val1) is tuple:
        ans = run(env,val1)
        if typecheckcompare(ans,val2):
            if ans == "true":
                ans = 1
            if ans == "false":
                ans = 0
            if val2 == "true":
                val2 = 1
            if val2 == "false":
                val2 = 0
            if(ans < val2):
                return "true"
            else:
                return "false"
        else:
            exit("TYPEERROR!")
    elif type(val2) is tuple:
        ans = run(env,val2)
        if typecheckcompare(val1,ans):
            if val1 == "true":
                val1 = 1
            if val1 == "false":
                val1 = 0
            if ans == "true":
                ans = 1
            if ans == "false":
                ans = 0
            if(val1 < ans):
                return "true"
            else:
                return "false"
        else:
            exit("TYPEERROR!")
    else:
        if typecheckcompare(val1,val2):
            if val1 == "true":
                val1 = 1
            if val1 == "false":
                val1 = 0
            if val2 == "true":
                val2 = 1
            if val2 == "false":
                val2 = 0
            if(val1 < val2):
                return "true"
            else:
                return "false"
        else:
            exit("TYPEERROR!")

def lessequalthan(val1, val2):
    if type(val1) is tuple and type(val2) is tuple:
        ans1 = run(env,val1)
        ans2 = run(env,val2)
        if typecheckcompare(ans1,ans2):
            if ans1 == "true":
                ans1 = 1
            if ans1 == "false":
                ans1 = 0
            if ans2 == "true":
                ans2 = 1
            if ans2 == "false":
                ans2 = 0
            if(ans1 <= ans2):
                return "true"
            else:
                return "false"
        else:
            exit("TYPEERROR!")
    if type(val1) is tuple:
        ans = run(env,val1)
        if typecheckcompare(ans,val2):
            if ans == "true":
                ans = 1
            if ans == "false":
                ans = 0
            if val2 == "true":
                val2 = 1
            if val2 == "false":
                val2 = 0
            if(ans <= val2):
                return "true"
            else:
                return "false"
        else:
            exit("TYPEERROR!")
    elif type(val2) is tuple:
        ans = run(env,val2)
        if typecheckcompare(val1,ans):
            if val1 == "true":
                val1 = 1
            if val1 == "false":
                val1 = 0
            if ans == "true":
                ans = 1
            if ans == "false":
                ans = 0
            if(val1 <= ans):
                return "true"
            else:
                return "false"
        else:
            exit("TYPEERROR!")
    else:
        if typecheckcompare(val1,val2):
            if val1 == "true":
                val1 = 1
            if val1 == "false":
                val1 = 0
            if val2 == "true":
                val2 = 1
            if val2 == "false":
                val2 = 0
            if(val1 <= val2):
                return "true"
            else:
                return "false"
        else:
            exit("TYPEERROR!")

def greaterthan(val1, val2):
    if type(val1) is tuple and type(val2) is tuple:
        ans1 = run(env,val1)
        ans2 = run(env,val2)
        if typecheckcompare(ans1,ans2):
            if ans1 == "true":
                ans1 = 1
            if ans1 == "false":
                ans1 = 0
            if ans2 == "true":
                ans2 = 1
            if ans2 == "false":
                ans2 = 0
            if(ans1 > ans2):
                return "true"
            else:
                return "false"
        else:
            exit("TYPEERROR!")
    if type(val1) is tuple:
        ans = run(env,val1)
        if typecheckcompare(ans,val2):
            if ans == "true":
                ans = 1
            if ans == "false":
                ans = 0
            if val2 == "true":
                val2 = 1
            if val2 == "false":
                val2 = 0
            if(ans > val2):
                return "true"
            else:
                return "false"
        else:
            exit("TYPEERROR!")
    elif type(val2) is tuple:
        ans = run(env,val2)
        if typecheckcompare(val1,ans):
            if val1 == "true":
                val1 = 1
            if val1 == "false":
                val1 = 0
            if ans == "true":
                ans = 1
            if ans == "false":
                ans = 0
            if(val1 > ans):
                return "true"
            else:
                return "false"
        else:
            exit("TYPEERROR!")
    else:
        if typecheckcompare(val1,val2):
            if val1 == "true":
                val1 = 1
            if val1 == "false":
                val1 = 0
            if val2 == "true":
                val2 = 1
            if val2 == "false":
                val2 = 0
            if(val1 > val2):
                return "true"
            else:
                return "false"
        else:
            exit("TYPEERROR!")

def greaterequalthan(val1, val2):
    if type(val1) is tuple and type(val2) is tuple:
        ans1 = run(env,val1)
        ans2 = run(env,val2)
        if typecheckcompare(ans1,ans2):
            if ans1 == "true":
                ans1 = 1
            if ans1 == "false":
                ans1 = 0
            if ans2 == "true":
                ans2 = 1
            if ans2 == "false":
                ans2 = 0
            if(ans1 >= ans2):
                return "true"
            else:
                return "false"
        else:
            exit("TYPEERROR!")
    if type(val1) is tuple:
        ans = run(env,val1)
        # print(ans)
        if typecheckcompare(ans,val2):
            if ans == "true":
                ans = 1
            if ans == "false":
                ans = 0
            if val2 == "true":
                val2 = 1
            if val2 == "false":
                val2 = 0
            if(ans >= val2):
                return "true"
            else:
                return "false"
        else:
            exit("TYPEERROR!")
    elif type(val2) is tuple:
        ans = run(env,val2)
        if typecheckcompare(val1,ans):
            if val1 == "true":
                val1 = 1
            if val1 == "false":
                val1 = 0
            if ans == "true":
                ans = 1
            if ans == "false":
                ans = 0
            if(val1 >= ans):
                return "true"
            else:
                return "false"
        else:
            exit("TYPEERROR!")
    else:
        if typecheckcompare(val1,val2):
            if val1 == "true":
                val1 = 1
            if val1 == "false":
                val1 = 0
            if val2 == "true":
                val2 = 1
            if val2 == "false":
                val2 = 0
            if(val1 >= val2):
                return "true"
            else:
                return "false"
        else:
            exit("TYPEERROR!")

def typecheckequal(val1, val2):
    typecheckans = isinstance(val1, int) or isinstance(val1, float) or isinstance(val1, bool) or isinstance(val1, str) 
    typecheckval = isinstance(val2, int) or isinstance(val2, float) or isinstance(val2, bool) or isinstance(val1, str)  
    if(val1 == "true" or val1 == "false") and ((val2 == 1 or val2 == 0) or (val2 == "true" or val2 == "false")):
        check = True
    elif(val2 == "true" or val2 == "false") and ((val1 == 1 or val1 == 0) or (val1 == "true" or val1 == "false")):
        check = True
    else:
        check = type(val1) == type(val2)
    return typecheckans and typecheckval and check

def equalto(val1,val2):
    if type(val1) is tuple and type(val2) is tuple:
        ans1 = run(env,val1)
        ans2 = run(env,val2)
        if typecheckequal(ans1, ans2):
            if ans1 == 0:
                ans1 = "false"
            if ans2 == 0:
                ans2 = "false"
            if ans1 == 1:
                ans1 = "true"
            if ans2 == 1:
                ans2 = "true"
            if(ans1 == ans2):
                return "true"
            else:
                return "false"
        else:
            exit("TYPEERROR!")
    elif type(val1) is tuple:
        ans = run(env,val1)
        if typecheckequal(ans, val2):
            if ans == 0:
                ans = "false"
            if val2 == 0:
                val2 = "false"
            if ans == 1:
                ans = "true"
            if val2 == 1:
                val2 = "true"
            if(ans == val2):
                return "true"
            else:
                return "false"
        else:
            exit("TYPEERROR!")
    elif type(val2) is tuple:
        ans = run(env,val2)
        if typecheckequal(ans, val1):
            if ans == 0:
                ans = "false"
            if val1 == 0:
                val1 = "false"
            if ans == 1:
                ans = "true"
            if val1 == 1:
                val1 = "true"
            if(ans == val1):
                return "true"
            else:
                return "false"
        else:
            exit("TYPEERROR!")
    else:
        if typecheckequal(val1,val2):
            if val1 == 0:
                val1 = "false"
            if val2 == 0:
                val2 = "false"
            if val1 == 1:
                val1 = "true"
            if val2 == 1:
                val2 = "true"
            if(val1 == val2):
                return "true"
            else:
                return "false"
        else:
            exit("TYPEERROR")

def notequalto(val1,val2):
    if type(val1) is tuple and type(val2) is tuple:
        ans1 = run(env,val1)
        ans2 = run(env,val2)
        if typecheckequal(ans1, ans2):
            if ans1 == 0:
                ans1 = "false"
            if ans2 == 0:
                ans2 = "false"
            if ans1 == 1:
                ans1 = "true"
            if ans2 == 1:
                ans2 = "true"
            if(ans1 != ans2):
                return "true"
            else:
                return "false"
        else:
            exit("TYPEERROR!")
    elif type(val1) is tuple:
        ans = run(env,val1)
        if typecheckequal(ans, val2):
            if ans == 0:
                ans = "false"
            if val2 == 0:
                val2 = "false"
            if ans == 1:
                ans = "true"
            if val2 == 1:
                val2 = "true"
            if(ans != val2):
                return "true"
            else:
                return "false"
        else:
            exit("TYPEERROR!")
    elif type(val2) is tuple:
        ans = run(env,val2)
        if typecheckequal(ans, val1):
            if ans == 0:
                ans = "false"
            if val1 == 0:
                val1 = "false"
            if ans == 1:
                ans = "true"
            if val1 == 1:
                val1 = "true"
            if(ans != val1):
                return "true"
            else:
                return "false"
        else:
            exit("TYPEERROR!")
    else:
        if typecheckequal(val1,val2):
            if val1 == 0:
                val1 = "false"
            if val2 == 0:
                val2 = "false"
            if val1 == 1:
                val1 = "true"
            if val2 == 1:
                val2 = "true"
            if(val1 != val2):
                return "true"
            else:
                return "false"
        else:
            exit("TYPEERROR")

def andfunc(val1,val2):
    if type(val1) is tuple and type(val2) is tuple:
        ans1 = run(env, val1)
        ans2 = run(env, val2)
        if ans1 == "true":
            ans1 = True
        elif ans1 == "false":
            ans1 = False
        if ans2 == "true":
            ans2 = True
        elif ans2 == "false":
            ans2 = False
        if(ans1 & ans2):
            return "true"
        else:
            return "false"
    if type(val2) is tuple:
        ans = run(env, val2)
        if ans == "true":
            ans = True
        elif ans == "false":
            ans = False
        if val1 == "true":
            val1 = True
        elif val1 == "false":
            val1 = False
        if(val1 & ans):
            return "true"
        else:
            return "false"
    elif type(val1) is tuple:
        ans = run(env,val1)
        if ans == "true":
            ans = True
        elif ans == "false":
            ans = False
        if val2 == "true":
            val2 = True
        elif val2 == "false":
            val2 = False 
        if(ans & val2):
            return "true"
        else:
            return "false"
    else:
        if val2 == "true":
            val2 = True
        elif val2 == "false":
            val2 = False
        if val1 == "true":
            val1 = True
        elif val1 == "false":
            val1 = False
        if(val1 & val2):
            return "true"
        else:
            return "false"

def orfunc(val1,val2):
    if type(val1) is tuple and type(val2) is tuple:
        ans1 = run(env, val1)
        ans2 = run(env, val2)
        if ans1 == "true":
            ans1 = True
        elif ans1 == "false":
            ans1 = False
        if ans2 == "true":
            ans2 = True
        elif ans2 == "false":
            ans2 = False
        if(ans1 | ans2):
            return "true"
        else:
            return "false"
    if type(val2) is tuple:
        ans = run(env, val2)
        if ans == "true":
            ans = True
        elif ans == "false":
            ans = False
        if val1 == "true":
            val1 = True
        elif val1 == "false":
            val1 = False
        if(val1 | ans):
            return "true"
        else:
            return "false"
    elif type(val1) is tuple:
        ans = run(env,val1)
        if ans == "true":
            ans = True
        elif ans == "false":
            ans = False
        if val2 == "true":
            val2 = True
        elif val2 == "false":
            val2 = False 
        if(ans | val2):
            return "true"
        else:
            return "false"
    else:
        if val2 == "true":
            val2 = True
        elif val2 == "false":
            val2 = False
        if val1 == "true":
            val1 = True
        elif val1 == "false":
            val1 = False
        if(val1 | val2):
            return "true"
        else:
            return "false"


def typecheckpower(val1, val2):
    typecheckans = isinstance(val1, int) or isinstance(val1, float) 
    typecheckval = isinstance(val2, int) or isinstance(val2, float)   
    return typecheckans and typecheckval

def powerfunc(val1, val2):
    if type(val1) is tuple and type(val2) is tuple:
        ans1 = run(env, val1)
        ans2 = run(env, val2)
        if typecheckpower(ans1, ans2):
            return ans1**ans2
        else:
            exit("TYPEERROR!")
    elif type(val1) is tuple:
        ans1 = run(env, val1)
        if typecheckpower(ans1, val2):
            return ans1**val2
        else:
            exit("ERRTYPEERROROR!")
    elif type(val2) is tuple:
        ans1 = run(env, val2)
        if typecheckpower(ans1, val1):
            return val1**ans1
        else:
            exit("TYPEERROR!")
    else:
        return val1**val2 

def modfunc(val1, val2):
    if type(val1) is tuple and type(val2) is tuple:
        ans1 = run(env, val1)
        ans2 = run(env, val2)
        if typecheckpower(ans1, ans2):
            return ans1%ans2
        else:
            exit("TYPEERROR!")
    elif type(val1) is tuple:
        ans1 = run(env, val1)
        if typecheckpower(ans1, val2):
            return ans1%val2
        else:
            exit("TYPEERROR!")
    elif type(val2) is tuple:
        ans1 = run(env, val2)
        if typecheckpower(ans1, val1):
            return val1%ans1
        else:
            exit("TYPEERROR!")
    else:
        return val1%val2 

def incrfunc(val1):
    if type(val1) is tuple:
        ans = run(env, val1)
        if isinstance(ans,int) or isinstance(ans,float):
            value = val1[1]
            oldvalue = env[value]["value"]
            env[value]["value"] = oldvalue + 1
            return ""
        else:
            exit("TYPEERROR!")
    else:
        if isinstance(val1,int) or isinstance(val1,float):
            return val1+1
        else:
            exit("TYPEERROR!")

def decrfunc(val1):
    if type(val1) is tuple:
        ans = run(env, val1)
        if isinstance(ans,int) or isinstance(ans,float):
            value = val1[1]
            oldvalue = env[value]["value"]
            env[value]["value"] = oldvalue - 1
            return ""
        else:
            exit("TYPEERROR!")
    else:
        if isinstance(val1,int) or isinstance(val1,float):
            return val1-1
        else:
            exit("TYPEERROR!")

def run(env, tree):
    
    if tree[0] == "string":
        return tree[1]
    if tree[0] == "char":
        return tree[1]
    if tree[0] == "bool":
        return tree[1]
    if tree[0] == "declare":
        if tree[2] in env:
            exit("Variable already declared once! Please use a different name.")
        else:
            if(len(tree) > 3):
                typevar = tree[1]
                var = tree[2]
                valuevar = tree[3]
                if type(valuevar) is tuple:
                    env[var] = {"type": typevar, "value": run(env,valuevar)}
                    return ""
                else:
                    if typevar == "bool":
                        if valuevar == 1:
                            valuevar = "true"
                        elif valuevar == 0:
                            valuevar = "false"
                    env[var] = {"type": typevar, "value": valuevar}
                    return ""
            else:
                typevar = tree[1]
                var = tree[2]
                env[var] = {"type": typevar, "value": 0}
                return ""
    
    if tree[0] == "=":
        if tree[1] in env:
            var = tree[1]
            valvar = tree[2]
            if type(valvar) is tuple:
                env[var]["value"] = run(env,valvar)
                return ""
            else:
                if valvar == 0 and env[var]["type"] == "bool":
                    valvar = "false"
                elif valvar == 1 and env[var]["type"] == "bool":
                    valvar = "true"
                env[var]["value"] = valvar
                return ""
        else:
            exit("Variable doesn't exist! Please declare first.")

    if tree[0] == "print":
        printchild = tree[1]
        i = 1
        ans = ""
        while i <= len(printchild):
            if i == len(printchild):
                val = printchild[i-1]
                if type(val) is tuple:
                    if val[0] == "listaccess":
                        val = ("list",(val))
                        result = run(env, val)
                        ans = ans + str(result)
                    elif val[0] == "listfunc":
                        val= ("list", val)
                        result = run(env, val)
                        ans = ans + str(result)
                    else:  
                        val = run(env, val)
                        ans = ans + str(val)
                else:
                    ans = ans + str(val)
            else:
                val = printchild[i-1]
                if type(val) is tuple:
                    if val[0] == "listaccess":
                        val = ("list",(val))
                        result = run(env, val)
                        ans = ans + str(result) + " "
                    elif val[0] == "listfunc":
                        val= ("list", val)
                        result = run(env, val)
                        ans = ans + str(result) + " "
                    else:  
                        val = run(env, val)
                        ans = ans + str(val) + " "
                else:
                    ans = ans + str(val) + " "
            i = i+1
        return ans

    if tree[0] == "var":
        if tree[1] in env:
            return env[tree[1]]["value"]
        else:
            exit("Error! Undeclared variable!")

    if tree[0] == "+":
        return addition(tree[1], tree[2])
    elif tree[0] == "-":
        return subtraction(tree[1], tree[2])
    elif tree[0] == "*":
        return multiplication(tree[1], tree[2])
    elif tree[0] == "/":
        return division(tree[1], tree[2])
    elif tree[0] == "<":
        return lessthan(tree[1], tree[2])
    elif tree[0] == ">":
        return greaterthan(tree[1], tree[2])
    elif tree[0] == "<=":
        return lessequalthan(tree[1], tree[2])
    elif tree[0] == ">=":
        return greaterequalthan(tree[1], tree[2])
    elif tree[0] == "!=":
        return notequalto(tree[1], tree[2])
    elif tree[0] == "==":
        return equalto(tree[1], tree[2])
    elif tree[0] == "and":
        return andfunc(tree[1], tree[2])
    elif tree[0] == "or":
        return orfunc(tree[1], tree[2])
    elif tree[0] == "not":
        if type(tree[1]) is tuple:
            ans = run(env,tree[1])
            if ans == "true" or ans == 1:
                return "false"
            elif ans == "false" or ans == 0:
                return "true"
        else:
            if tree[1] == "true" or tree[1] == 1:
                return "false"
            elif tree[1] == "false" or tree[1] == 0:
                return "true"

    elif tree[0] == "^":
        return powerfunc(tree[1], tree[2])
    elif tree[0] == "%":
        return modfunc(tree[1], tree[2])
    elif tree[1] == "++":
        return incrfunc(tree[0])      
    elif tree[1] == "--":
        return decrfunc(tree[0])
    elif tree[0] == "ifstmt":
        ifcond = run(env, tree[1][1])
        if(ifcond == "true"):
            print(run(env,tree[1]))
            return ""
    elif tree[0] == "ifelsestmt":
        ifcond = run(env, tree[1][1])
        if(ifcond == "true"):
            print(run(env,tree[1]))
            return ""
        else:
            print(run(env,tree[2]))
            return ""
    elif tree[0] == "ifelifelsestmt":
        ifcond = run(env, tree[1][1])
        elifcond = run(env, tree[2][1])
        if(ifcond == "true"):
            print(run(env,tree[1]))
            return ""
        elif(elifcond == "true"):
            print(run(env,tree[2]))
            return ""
        else:
            print(run(env,tree[3]))
            return ""
    elif tree[0] == "if":
        if(tree[2][0]) == "block":
            code = tree[2][1]
            a = len(code)
            i = 0
            while i < a:
                result = run(env, code[i])
                i = i+1
            return result
    elif tree[0] == "else":
        if(tree[1][0]) == "block":
            code = tree[1][1]
            a = len(code)
            i = 0
            while i < a:
                result = run(env, code[i])
                i = i+1
            return(result)
    elif tree[0] == "else_if":
        if(tree[2][0]) == "block":
            code = tree[2][1]
            a = len(code)
            i = 0
            while i < a:
                result = run(env, code[i])
                i = i+1
            return result
    elif tree[0] == "list":        
        detail = tree[1]
        if detail[0] == "listdeclare":
            listname = detail[1]
            env[listname] = {"type": "list", "value": []}
            return ""
        elif detail[0] == "listassign":
            listname = detail[1]
            value = detail[2]
            i = 0
            store = []
            while i != len(value):
                if(type(value[i]) is tuple):
                    valtuple = value[i]
                    fetchval = valtuple[1]
                    store.append(fetchval)
                else:
                    store.append(value[i])
                i = i + 1
            env[listname]["value"] = store
            return ""
        elif detail[0] == "listaccess":
            listname = detail[1]
            index = detail[2]
            fetchlist = env[listname]["value"]
            length = len(fetchlist)
            if index >= length or index < 0:
                exit("List index out of range!")
            else:
                return fetchlist[index]
        elif detail[0] == "listfunc":
            func = detail[1]
            functype = func[0]
            if functype == "pop":
                listname = func[1]
                popindex = func[2]
                fetchlist = env[listname]["value"]
                if fetchlist != []:
                    if popindex >= len(fetchlist):
                        exit("List index out of range!")
                    else:
                        val = fetchlist.pop(popindex);
                        env[listname]["value"] = fetchlist
                        return val
            elif functype == "push":
                listname = func[1]
                pushvalue = func[2]
                fetchlist = env[listname]["value"]
                fetchlist.append(pushvalue)
                env[listname]["value"] = fetchlist
                return ""
            elif functype == "index":
                listname = func[1]
                index = func[2]
                fetchlist = env[listname]["value"]
                length = len(fetchlist)
                if index >= length or index < 0:
                    exit("List index out of range!")
                else:
                    return fetchlist[index]
            elif functype == "slice":
                listname = func[1]
                slicerange = func[2]
                fetchlist = env[listname]["value"]
                if slicerange[0] == "start":
                    start = slicerange[1]
                    return fetchlist[start:]
                elif slicerange[0] == "end":
                    end = slicerange[1]
                    return fetchlist[:end]
                elif slicerange[0] == "all":
                    return fetchlist[:]
                else:
                    start = slicerange[0]
                    end = slicerange[1]
                    return fetchlist[start:end]
            else:
                exit("No such function exists!")
    else:
        return ""

def mainmenu():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        global env
        with open(filename, 'r') as f:
            code = f.read()
        tokenprint = ""
        print("\t\t\tWELCOME TO MY COMPILER\n")
        print("MENU:\n1. Press 1 to print tokens.\n2. Press 2 to print parse tree.\n3. Press 3 to compile code.\n")
        val = input(">>")
        token = False
        parse = False
        compileit = False
        if val == "1":
            token = True
        elif val == "2":
            parse = True
        elif val == "3":
            compileit = True
        else:
            exit("WRONG INPUT")
        lexinput = lex.lex(module=lexer)
        lexinput.input(code)
        if(token):
            os.system('clear')
            print("\t\t\t\t| TOKENS |\n")
            while(1):
                printtok = lexinput.token()
                if printtok: 
                    print(printtok)
                else:
                    break
        parseinput = yacc.yacc(module=parser)
        parse_tree = parseinput.parse(code, lexer=lexinput)
        if(parse):
            os.system('clear')
            print("\t\t\t\t| PARSER |\n")
            for t in parse_tree:
                print(t)
        if(compileit):
            os.system('clear')
            compileit = True
            print("\t\t\t\t| OUTPUT |\n")
            i = 0
            for t in parse_tree:
                result = run(env, parse_tree[i])
                if result  == "":
                    pass
                else:
                    print(result)
                i = i + 1
    else:
        exit("WRONG ARGUMENTS IN TERMINAL INPUT")
    
mainmenu()