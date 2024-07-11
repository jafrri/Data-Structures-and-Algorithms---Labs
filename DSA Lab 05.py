#Question 1

import ast
lst = input()
lst = ast.literal_eval(lst)
item = int(input())

def binary_search_iterative(lst,item):
    start = 0
    end = len(lst)
    while start < end:
        mid = (start + end) // 2
        if int(lst[mid]) == item:
            return(mid)
        elif int(lst[mid]) > item:
            end = mid
        else:
            start = mid + 1
    return(-1)
    
    
print(binary_search_iterative(lst, item))


# Question 2

import ast
lst = input()
lst = ast.literal_eval(lst)
item = int(input())
def binary_search_iterative_modified(lst,item):
    start = 0
    end = len(lst)
    while start < end:
        mid = (start + end) // 2
        if int(lst[mid]) == item:
            return(mid)
        elif int(lst[mid]) > item:
            end = mid
        else:
            start = mid + 1
    lst.insert(end,item)
    return(end)

print(binary_search_iterative_modified(lst, item))

# Question 3

import ast
lst = input()
lst = ast.literal_eval(lst)
item = int(input())
low = int(input())
high = int(input())

def binary_search_recursive(lst, item, low, high):
    if high >= low:
        mid = (high + low) // 2
        if lst[mid] == item:
            return(mid)
        elif lst[mid] > item:
            return(binary_search_recursive(lst,item,low,mid-1))
        else:
            return(binary_search_recursive(lst,item,mid + 1 , high))
    else:
        return(-1)            
print(binary_search_recursive(lst, item, low, high))



# Question 4

import ast
lst = input()
lst = ast.literal_eval(lst)
item = int(input())
low = int(input())
high = int(input())

def binary_search_recursive_modified(lst, item, low, high):
    if high >= low:
        mid = (high + low) // 2
        if lst[mid] == item:
            return(mid)
        elif lst[mid] > item:
            return(binary_search_recursive_modified(lst,item,low,mid-1))
        else:
            return(binary_search_recursive_modified(lst,item,mid + 1 , high))
    else:
        lst.insert(low,item)
        return(low)           

print(binary_search_recursive_modified(lst, item, low, high))


# Question 5

import ast
student_records = input()
student_records = ast.literal_eval(student_records)
ID = input()
record_title = input()
data = input()

def update_record(student_records, ID, record_title, data):
    bs = binarysearch(student_records, ID)
    if bs == -1:
        return("Record not found")
    else:
        if record_title == "ID":
            return("ID cannot be updated")
        elif record_title == "Email":
            student_records[bs] = (ID, data, student_records[bs][2], student_records[bs][3])
            return(student_records)
        elif record_title == "Mid1":
            student_records[bs] = (ID, student_records[bs][1], int(data), student_records[bs][3])
            return(student_records)
        else:
            student_records[bs] = (ID, student_records[bs][1], student_records[bs][2], int(data))
            return(student_records)
           
            
    
    
def binarysearch(student_records, ID):
    start = 0
    end = len(student_records)
    while start < end:
        mid = (start + end) // 2
        if (student_records[mid][0]) == ID:
            return(mid)
        elif (student_records[mid][0]) > ID:
            end = mid
        elif student_records[mid][0] < ID:
            start = mid + 1
    return(-1)
       
print(update_record(student_records, ID, record_title, data))


# Question 6

import ast
points_list = input()
points_list = ast.literal_eval(points_list)
length = float(input())

def length_of_line(points_list, length):
    
    lsttt = Distances(points_list)
    start = 0
    end = len(lsttt)
    while start < end:
        mid = (start + end) // 2
        if (lsttt[mid]) == length:
            return(mid)
        elif (lsttt[mid]) > length:
            end = mid
        else:
            start = mid + 1
    return(-1)
    
    
    
    
def Coordinates(points_list, length):
    lst = []
    for i in range(len(points_list)):
        a1 = points_list[i][0][0]
        a2 = points_list[i][0][1]
        b1 = points_list[i][1][0]
        b2 = points_list[i][1][1]
        lst.append([a1,a2,b1,b2])
    return(lst)
        
def Distances(lst):
    lst = Coordinates(points_list, length)
    lstt = []
    for i in range(len(lst)):
        a = lst[i][0]
        b = lst[i][1]
        c = lst[i][2]
        d = lst[i][3]
        xd = (a-c)**2
        yd = (b-d)**2
        distance = (xd+yd)**(1/2)
        lstt.append(round(distance,2))
    return(lstt)
        
        

print(length_of_line(points_list, length))

# Question 7


import ast
lst = input()
lst = ast.literal_eval(lst)
item = int(input())
high = len(lst)
a = len(lst)
low = 0
nl = []
lstt = lst[::]


def finding_multiple(lst,item):
    a = binarysearch(lst,item,low,high)
    return(a)
    
    
    
    
def binarysearch(lst,item,low,high):
    if high >= low:
        mid = (high + low) // 2
        if lst[mid] == item:
            if lst[mid-1] == item:
                return(binarysearch(lst,item,0,mid-1))
            else:
                for i in range(mid,a):
                    if lstt[i] == item:
                        nl.append(i)
                return(nl)
                
        elif lst[mid] > item:
            return(binarysearch(lst,item,low,mid-1))
        else:
            return(binarysearch(lst,item,mid + 1 , high))
    else:
        return([])    
        
    
    
    
    
    

    
    

print(finding_multiple(lst, item))
