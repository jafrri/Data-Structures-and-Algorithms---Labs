#Question 1

expression = input()
def push(lst, item):
    lst.append(item)

def pop(lst):
    l = lst[-1]
    del(lst[-1])
    return(l)

def top(lst):
    if len(lst) == 0:
        print("No item exists.")
        return(None)
    return(lst[-1])

def is_empty(lst):
    if len(lst) > 0:
        return(True)
    else:
        return(False)
        
def EvalutePrefix(expression):
    operandStack = []
    lstt = expression.split(" ")
    lst = lstt[::-1]
    for i in lst:
        if i == "+" or i == "-" or i == "*" or i == "/":
            num1 = pop(operandStack)
            num2 = pop(operandStack)
            if i == "+":
                num = num2 + num1
            elif i == "-":
                num = num1 - num2
            elif i == "*":
                num = num2 * num1
            else:
                num = int(num1 / num2)
            push(operandStack,num)
            
        else:
            int_num = int(i)
            push(operandStack,int_num)
    return(pop(operandStack))
    
    
print(EvalutePrefix(expression))


#Question 2

expression = input()

def push(lst, item):
    lst.append(item)

def pop(lst):
    l = lst[-1]
    del(lst[-1])
    return(l)

def top(lst):
    if len(lst) == 0:
       # print("No item exists.")
        return(0)
    return(lst[-1])

def is_empty(lst):
    if len(lst) == 0:
        return(True)
    else:
        return(False)

def isOperand(n):
    return(n >= "A" and n <= "Z")
    
operators = "+-*/"

def isOperator(n):
    return(n in operators)
    
def getprecedence(n):
    
    if n not in operators:
        return(0)
    else:
        p = {}
        p['*'] = 3
        p['/'] = 3
        p['+'] = 2
        p['-'] = 2
        
    return(p[n])

def Infix_to_Postfix(expression):
    op_stack = []
    output = []
    res = ""
    lst = expression.split(" ")
    for i in lst:
        if isOperand(i):
            res = res  + i 
        elif isOperator(i):
            while True:
                tc = top(op_stack)
                if is_empty(op_stack)== True or tc == "(":
                    push(op_stack,i)
                    break
                else:
                    pc = getprecedence(str(i))
                    ptc = getprecedence(str(tc))
                    if pc > ptc:
                        push(op_stack,i)
                        break
                    else:
                        res = res + pop(op_stack) 
                       
                        
                    
                    
        elif i == "(":
            push(op_stack,i)
        elif i == ")":
            m = pop(op_stack)
            while m != "(":
                res = res +  m
                m = pop(op_stack)
                
    while is_empty(op_stack) == False:
        m = pop(op_stack)
        res = res +  m
    ress = list(res)
    resss = " ".join(ress)   
    return(resss)
    
    
print(Infix_to_Postfix(expression))       

        
                

#Question 3

expression = input()
def push(lst, item):
    lst.append(item)

def pop(lst):
    l = lst[-1]
    del(lst[-1])
    return(l)

def top(lst):
    if len(lst) == 0:
       # print("No item exists.")
        return(None)
    return(lst[-1])

def is_empty(lst):
    if len(lst) == 0:
        return(True)
    else:
        return(False)
        
def isOperand(n):
        return(n >= "A" and n <= "Z")
            
operators = "+-*/"
        
def isOperator(n):
    return(n in operators)
            
def getprecedence(n):
            
    if n not in operators:
        return(0)
    else:
        p = {}
        p['*'] = 3
        p['/'] = 3
        p['+'] = 2
        p['-'] = 2
                
        return(p[n])

def Infix_to_Prefix(expression):
    exp = expression[::-1]
    op_stack = []
    output = []
    res = ""
    lst = exp.split(" ")
    for i in lst:
        if isOperand(i):
            res = res  + i 
        elif isOperator(i):
            while True:
                tc = top(op_stack)
                if is_empty(op_stack)== True or tc == "(":
                    push(op_stack,i)
                    break
                else:
                    pc = getprecedence(str(i))
                    ptc = getprecedence(str(tc))
                    if pc > ptc:
                        push(op_stack,i)
                        break
                    else:
                        res = res + pop(op_stack) 
                       
                        
                    
                    
        elif i == ")":
            push(op_stack,i)
        elif i == "(":
            m = pop(op_stack)
            while m != ")":
                res = res +  m
                m = pop(op_stack)
                
    while is_empty(op_stack) == False:
        m = pop(op_stack)
        res = res +  m
    ress = list(res)
    re = ress[::-1]
    resss = " ".join(re)   
    return(resss)
    
print(Infix_to_Prefix(expression))
