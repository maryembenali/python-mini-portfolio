import numpy as np
#Q1:
def pivot_index(A , j) :
    n,m = A.shape
    for p in range(j , n) :
    if A[p,j] != 0 :
    return p # sortie brutale de la fonction

#Q2 :
import math
    def pivot_index_partiel(A , j ) :
    n,p = A.shape
    p_max = j
    for p in range(j+1 , n) :
    if math.fabs(A[p,j]) > math.fabs(A[p_max, j ]) :
    p_max = p
    return p_max
    #Q3 :
def swap_lines(A , i , j ) : # i et j deux indices lignes
    aux = np.copy(A[i])
    A[i] = np.copy(A[j])
    A[j] = aux

#Q4 :

def transvection(A , i1 , i2 , lamda) :
    A[i1] = A[i1] + lamda*A[i2]

#Q5 :

def triangulaire(A0 , b0) :
    A,b = np.copy(A0) , np.copy(b0)
    2

    n,p = A.shape
    for j in range(p) :
    indice_pivot = pivot_index(A , j)
    if indice_pivot != j :
    swap_lines(A , indice_pivot , j )
    swap_lines(b , indice_pivot , j )
    for i in range(j+1 , n) :
        transvection(b , i , j , -A[i,j] / A[j,j])
        transvection(A , i , j , -A[i,j] / A[j,j])
    return A,b

    #Q6 :

def gauss(A0 , b0 ) :
    A, b = triangulaire(A0 , b0)
    n,m = A.shape
    X = np.zeros(m)
    for i in range(m-1 , -1 , -1) :
        somme = np.dot(A[i , i+1 : ] , X[i+1 :])
        somme = 0
        for k in range(i+1 , m) :
            somme += A[i,k]*X[k]
        X[i] = ( b[i] - somme ) / A[i,i]
    return X

    # Q7 :

def inverse(A) :
    n,m = A.shape
    Ainv = np.zeros((n,m))
    In = np.eye(n)
    for k in range(n) :
        Ainv[ : , k ] = gauss(A , In[ k ] )
    return Ainv