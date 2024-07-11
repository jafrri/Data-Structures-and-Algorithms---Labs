#Question 1

def matrix_subtraction(A,B):
    c = []
    for i in range(len(A)):
        r = []
        for j in range(len(A[i])):
            if len(A[i]) != len(B[i]):
                return("Matrices A and B don't have the same dimension required for matrix subtraction.")
            elif len(A[i]) == len(B[i]):
                y = A[i][j]
                z = B[i][j]
                diff = y - z
            r.append(diff)
        c.append(r)
    return(c)
    
print(matrix_subtraction(A,B))


#QUestion 2

def matrix_transpose(A):
    c = []
    
    for i in range(len(A[0])):
        r = []
        for j in range(len(A)):
            z = A[j][i]
            r.append(z)
        
        c.append(r)
        
    return(c)
            
    

print(matrix_transpose(A))


#Question 3

def matrix_multiplication(A,B):
    c = []
    for i in range(len(A)):
        rowC = []
        for j in range(len(B[0])):
            num = 0
            for k in range(len(B)):
                if len(A[0]) != len(B):
                    return("The number of columns in Matrix A does not equal the number of rows in Matrix B required for Matrix Multiplication.")
                elif len(A[0]) == len(B):
                    num = num + (A[i][k] * B[k][j])
            rowC.append(num)
        c.append(rowC)
    return(c)
        
    
print(matrix_multiplication(A,B))

#Question 4

def sharpen_image(A):
    L = copy.deepcopy(A)
    for i in range(len(A)):
        for j in range(len(A[i])):
            if i == 0:
                if j == 0:
                    num = A[i][j]
                    n1 = A[i+1][j]
                    n2 = A[i][j+1]
                    L[i][j] = round(abs((num*2)-(((n1*2)+(n2*2))/2)),2)
                elif j == (len(A[0])-1):
                    num = A[i][j]
                    n1 = A[i][j-1]
                    n2 = A[i+1][j]
                    L[i][j] = round(abs((num*2)-(((n1*2)+(n2*2))/2)),2)
                else:
                    num = A[i][j]
                    n1 = A[i][j+1]
                    n2 = A[i][j-1]
                    n3 = A[i+1][j]
                    L[i][j] = round(abs((num*2)-(((n1*2)+(n2*2)+(n3*2))/3)),2)
            elif i == (len(A)-1):
                if j == 0:
                    num = A[i][j]
                    n1 = A[i-1][j]
                    n2 = A[i][j+1]
                    L[i][j] = round(abs((num*2)-(((n1*2)+(n2*2))/2)),2)
                elif j == (len(A[0])-1):
                    num = A[i][j]
                    n1 = A[i][j-1]
                    n2 = A[i-1][j]
                    L[i][j] = round(abs((num*2)-(((n1*2)+(n2*2))/2)),2)
                else:
                    num = A[i][j]
                    n1 = A[i][j+1]
                    n2 = A[i][j-1]
                    n3 = A[i-1][j]
                    L[i][j] = round(abs((num*2)-(((n1*2)+(n2*2)+(n3*2))/3)),2)    
            else:
                if j == 0:
                    num = A[i][j]
                    n1 = A[i-1][j]
                    n2 = A[i][j+1]
                    n3  = A[i+1][j]
                    L[i][j] = round(abs((num*2)-(((n1*2)+(n2*2)+(n3*2))/3)),2)
                elif j == (len(A[0])-1):
                    num = A[i][j]
                    n1 = A[i][j-1]
                    n2 = A[i-1][j]
                    n3 = A[i+1][j]
                    L[i][j] = round(abs((num*2)-(((n1*2)+(n2*2)+(n3*2))/3)),2)
                else:
                    num = A[i][j]
                    n1 = A[i][j+1]
                    n2 = A[i][j-1]
                    n3 = A[i-1][j]
                    n4  = A[i+1][j]
                    L[i][j] = round(abs((num*2)-(((n1*2)+(n2*2)+(n3*2)+(n4*2))/4)),2) 
                                    
                                
                                      
                    
                    
    return(L)


