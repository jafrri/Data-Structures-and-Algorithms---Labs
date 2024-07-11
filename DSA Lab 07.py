# Question 1  Unimodel Sequence

unimodel_sequence = input().split(" ")
unimodel_sequence = [int(i) for i in unimodel_sequence]
def getTopIndex_UnimodelSequence(unimodel_sequence):
    start = 0
    end = len(unimodel_sequence)
    while end >= start:
        mid = (start+end) // 2
        if unimodel_sequence[mid] < unimodel_sequence[mid-1]:
            end =mid - 1
        elif unimodel_sequence[mid] <= unimodel_sequence[mid+1]:
            start = mid + 1 
        elif unimodel_sequence[mid+1]< unimodel_sequence[mid] and unimodel_sequence[mid] >= unimodel_sequence[mid-1]:
            return(mid)
print(getTopIndex_UnimodelSequence(unimodel_sequence))


# Question 2  Find the missing number

import ast
powerTwoList = input()
powerTwoList = ast.literal_eval(powerTwoList)
size = int(input())
def findMissingNumber(powerTwoList, size):
    start = 0
    end = size - 1
    while end > start:
        mid = (start + end) // 2
        if powerTwoList[mid] > 2**mid:
            end = end - 1 
        elif powerTwoList[mid] == 2**mid:
            start = mid + 1
        
    return(2**end)
            
        
print(findMissingNumber(powerTwoList, size))


# Question 3  Pairs of element having smallest absolute differences

import ast
lst = input()
lst = ast.literal_eval(lst)

def smallest_absdiff_pairs(lst):
    s_lst = quicksort(lst)
    lstt = []
    min_intial = abs(s_lst[0] - s_lst[1])
    for i in range(len(s_lst)-1):
        min_cal = abs(s_lst[i]-s_lst[i+1])
        if min_cal < min_intial:
            min_intial = min_cal
    for j in range(len(s_lst)-1):
        min_cal = abs(s_lst[j]-s_lst[j+1])
        if min_cal == min_intial:
            tup = (s_lst[j],s_lst[j+1])
            lstt.append(tup)
    return(lstt)
        
                    
    
    
    
    
def partition(lst,pivot):
    del(lst[0])
    less, great = [], []
    for i in lst:
        if i <= pivot:
            less.append(i)
        elif i > pivot:
            great.append(i)
    return(less,great)
    
    
def quicksort(lst):
    if len(lst) < 1:
        return(lst)
    else:
        pivot = lst[0]
        l,g = partition(lst,pivot)
        less = quicksort(l)
        great = quicksort(g)
        return(less+[pivot]+great)
        
        
print(smallest_absdiff_pairs(lst))


# Question 4  Sort an array according to absolute difference with given vslue 

import ast
lst = input()
lst = ast.literal_eval(lst)
x = int(input())

# Enter your code here. Read input from STDIN. Print output to STDOUT
def sort_abs_difference(lst, x):
    lstt = quicksort(lst)
    alst = []
    for i in range(len(lstt)):
        for j in range(len(lstt) - i -1):
            if abs(x-lstt[j]) > abs(x-lstt[j+1]):
                lstt[j],lstt[j+1] = lstt[j+1], lstt[j]
    return(lstt)
            
            
        
    
    
        

def partition(lst,pivot):
    del(lst[0])
    less, great = [], []
    for i in lst:
        if i <= pivot:
            less.append(i)
        elif i > pivot:
            great.append(i)
    return(less,great)
    
    
def quicksort(lst):
    if len(lst) < 1:
        return(lst)
    else:
        pivot = lst[0]
        l,g = partition(lst,pivot)
        less = quicksort(l)
        great = quicksort(g)
        return(less+[pivot]+great)
print(sort_abs_difference(lst, x))
