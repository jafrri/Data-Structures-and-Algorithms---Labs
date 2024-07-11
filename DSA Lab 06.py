#Question 1  Selection sort

import ast
lst = input()
lst = ast.literal_eval(lst)

def selection_sort(lst):
    for front in range(len(lst)):
        minn = front
        for j in range(front,len(lst)):
            if lst[j] < lst[minn]:
                minn = j
        lst[front],lst[minn] = lst[minn],lst[front]
        print(lst)
        
    
selection_sort(lst)



#Question 2 Insertion Sort


import ast
lst = input()
lst = ast.literal_eval(lst)

def insertion_sort(lst):
    for front in range(1,len(lst)):
        i = front - 1
        while i >= 0 and lst[front] < lst[i]:
            i = i -1
        lst.insert(i+1,lst[front])
        del(lst[front+1])
        print(lst)

insertion_sort(lst)


#Question 3  Bubble Sort

import ast
lst = input()
lst = ast.literal_eval(lst)

def bubble_sort(lst):
    if len(lst) > 1:
        for i in range(len(lst)-1):
            for j in range(len(lst)-i-1):
                if lst[j] > lst[j+1]:
                    lst[j],lst[j+1] = lst[j+1],lst[j]
            print(lst)
    else:
        print(lst)

bubble_sort(lst)


# Queestion  4


import ast
lst = input()
lst = ast.literal_eval(lst)
def sort_matrix_by_row(lst):
    lstt = []
    for i in range(len(lst)):
        a = selection_sort(lst[i])
        lstt.append(a)
    return(lstt)

def selection_sort(lst):
    for front in range(len(lst)):
        minn = front
        for j in range(front,len(lst)):
            if lst[j] < lst[minn]:
                minn = j
        lst[front],lst[minn] = lst[minn],lst[front]
    return(lst)
        

print(sort_matrix_by_row(lst))


# Question 5

import ast
lst = input()
lst = ast.literal_eval(lst)
column = int(input())


def sort_matrix_by_columnNumber(lst, column):
    for front in range(len(lst)):
        minn = front
        for j in range(front,len(lst)):
            if lst[j][column] < lst[minn][column]:
                minn = j
        lst[front],lst[minn] = lst[minn],lst[front]
    return(lst)

print(sort_matrix_by_columnNumber(lst, column))



# Question 6


import ast
rectangle_records = input()
rectangle_records = ast.literal_eval(rectangle_records)
record_title = input()

def sort_rectangles(rectangle_records, record_title):
    for front in range(1,len(rectangle_records)):
        for i in range(front-1,-1,-1):
            if rectangle_records[front][record_title] > rectangle_records[i][record_title]:
                rectangle_records.insert(i+1,rectangle_records[front])
                del(rectangle_records[front+1])
                break
            elif i == 0:
                rectangle_records.insert(0,rectangle_records[front])
                del(rectangle_records[front+1])
    return(rectangle_records)
print(sort_rectangles(rectangle_records, record_title))
