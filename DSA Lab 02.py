#Question 1

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

#Question 2

s = input()

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
    
        
def string_reversal(s):
    lst = []
    length = len(s)
    for i in range(length):
        push(lst, s[i])
    rev = ""
    for i in range(length):
        rev = rev + pop(lst)
    return(rev)
    
print(string_reversal(s))


# Question 3

exp = input()

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

def intorfloat(n):

    if "." in n:
        return(float(n))
    else:
        return(int(n))
    
def postfixEval(exp):
    lst = []
    s = exp.split(" ")
    for i in s:
      # if i.isnumeric()==True:
        #   push(lst, i)
        if i == "+" or i == "-" or i == "*" or i == "/":
            n1 = pop(lst)
            n2 = pop(lst)
            if i == "+":
                new = (n2) + (n1)
            elif i == "-":
                new = (n2) - (n1)
            elif i == "*":
                new = (n2) * (n1)
            else:
                new = (n2) / (n1)
            push(lst, new)
        else:
            number = intorfloat(i)
            push(lst, number)
    return(float(pop(lst)))
            
    
ans = postfixEval(exp)
print(ans)

#Question 4

# Enter your code here. Read input from STDIN. Print output to STDOUT
def enQueue(lst, data):
    lst.append(data)
    
def deQueue(lst):
    if len(lst) < 1:
        return(None)
    return(lst.pop(0))

def front(lst):
    return(lst[0])

def is_empty(lst):
    if len(lst) > 0:
        return(True)
    else:
        return(False)

#Question 5

n = int(input())

def enQueue(lst, data):
    lst.append(data)
    
def deQueue(lst):
    if len(lst) < 1:
        return(None)
    return(lst.pop(0))

def front(lst):
    return(lst[0])

def is_empty(lst):
    if len(lst) > 0:
        return(True)
    else:
        return(False)
    
def BinNumsUsingQueue(n):
    lst = []
    enQueue(lst, "1")
    for i in range(n):
        first = str(deQueue(lst))
        enQueue(lst, first + "0")
        enQueue(lst, first + "1")
        
        print(first, end=" ")
    

BinNumsUsingQueue(n)

#Question 6

s = input()

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
    if len(lst) ==0:
        return(True)
    else:
        return(False)
    
def enQueue(lst, data):
    lst.append(data)
        
def deQueue(lst):
    if len(lst) < 1:
        return(None)
    return(lst.pop(0))
    
def front(lst):
    return(lst[0])

def reverse(string):
    string = ""

    for i in s:
        if i.isalpha():
            string = string + str(i)
        else:
            pass
    return(string)   
    

def is_palindrome(s):
    string = reverse(s)
    string2 = ""
    lst = []
    for i in range(len(string)):
        push(lst, string[i])
    
    while is_empty(lst)== False:
        rem = pop(lst)
        string2 = string2 + rem
        
        
    if string2.lower() == string.lower():
        return(True)
    else:
        return(False)
    
    
            

    

print(is_palindrome(s))
