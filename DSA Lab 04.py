# Question 1

import ast
queue = input()
queue = ast.literal_eval(queue)

def Enqueue(queue, item, priority):
    a = (item,priority)
    if len(queue) > 1:
        index  = len(queue)-1
        while True:
            if index == -1:
                queue.insert(0,a)
                return(queue)
            elif queue[index][1] >= priority:
                queue.insert(index+1, a)
                return(queue)
            elif queue[index][1] < priority:
                index = index - 1
                
    elif len(queue) == 1:
        if queue[0][1] >= priority:
            queue.append(a)
            return(queue)
        else:
            queue.insert(0,a)
            return(queue)
        
            
    else:
        queue.append(a)
            
        
            
                
                
                
def Dequeue(queue):
    item = queue[0]
    del(queue[0])
    return(item[0])

operation = input()

if operation == "Enqueue":
    item = input()
    priority = int(input())
    Enqueue(queue, item, priority)
    print(queue)
elif operation == "Dequeue":
    print(Dequeue(queue))
    print(queue)



# Question 2


issues = [("AC Not working in Tariq Rafi",5),("Password Change Issue",4),("Need Installation on laptop",3),("Need license",1),("Lab PCs Setup",3),("Login Issue",4)]


def Enqueue(queue, item, priority):
    a = (item,priority)
    if len(queue) > 1:
        index  = len(queue)-1
        while True:
            if index == -1:
                queue.insert(0,a)
                return(queue)
            elif queue[index][1] >= priority:
                queue.insert(index+1, a)
                return(queue)
            elif queue[index][1] < priority:
                index = index - 1
                
    elif len(queue) == 1:
        if queue[0][1] >= priority:
            queue.append(a)
            return(queue)
        else:
            queue.insert(0,a)
            return(queue)
        
            
    else:
        queue.append(a)
            
        
queue = []            
for i in range(len(issues)):
    Enqueue(queue,issues[i][0],issues[i][1])
for i in range(len(queue)):
    print(queue[i][0])


#Question 3

import ast
lst = input()
lst = ast.literal_eval(lst)
def push(lst, item):
    lst.append(item)
    
def pop(lst):
    i = lst.pop()
    return(i)

def top(lst):
    return(lst[-1])

def is_empty(lst):
    if len(lst) == 0:
        return(True)
    else:
        return(False)


def InterLeaveQueue(lst):
    length = len(lst)
    a = int(len(lst)//2)
    stack1 = lst[:a]
    stack2 = lst[a:length]
    
    stack3 = []
    while not is_empty(stack1):
        push(stack3,pop(stack2))
        push(stack3,pop(stack1)) 
        
    stack4 = []
    while not is_empty(stack3):
        push(stack4,pop(stack3))
    return(stack4)
        
    
    
        
    
    
print(InterLeaveQueue(lst))
