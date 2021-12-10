import numpy as np
from PIL import Image
from IPython.display import display
import random

def image_alea(H , L) :
    A = np.zeros((H,L,3) , dtype = 'uint8')
    for i in range(H) :
    for j in range(L) :
    for k in range(3) :
    A[i,j,k] = random.randint(0,255)
    return A
def ajouterBande(A , ep) :
    H,L,C = A.shape
    milieu = H // 2
    A[ milieu - ep // 2 : milieu + ep // 2 , : ] = [255 , 0 , 0 ]
    return A
def composante_rouge(A) :
    A1 = np.copy(A)
    A1[ : , : , 2] = 0 # 1 : 3 ( 3 exclu )
    return A1

# Q1

def miroir(A) : # A est une matrice image couleur
    H, L , C = A.shape
    A1 = np.copy(A)
    for j in range(L) :
        A1[ : , j] = A[ : , L-j-1]
    return A1

def miroir_Fusion(A) :
    H,L , C = A.shape
    B = np.zeros((H , 2*L , C) , dtype = 'uint8')
    B[ : , : L] = A
    B[ : , L : 2*L] = miroir(A)
    return B

# Q2 :

def rotation90(A) :
    H,L,C = A.shape
    A1 = np.zeros((L,H,C) , dtype = 'uint8')
    for i in range(L) :
    A1[i , : ] = A[ : , L-i-1]
    return A1

# Q3 :

def negatif(A) :
    return 255 #- A

# Q3

def niveau_gris(A) :
    H,L,C = A.shape
    A1 = np.copy(A)
    percentage = np.array([0.299 , 0.587 , 0.114])
    for i in range(H) :
        for j in range(L) :
            ton_gris = round( np.dot(A[i,j] , percentage) )
            A1 [i,j,:] = ton_gris
    return A1
def taille(A) : # A est une matrice image
    if A.ndim == 3 : # A est une matrice image couleur
    H,L,C = A.shape
    return H*L*3 / 2**10
    elif A.ndim == 2 : # A est une matrice image formatB ( niveau de gris)
    H,L = A.shape
    return H*L / 2**10
    # Q4

def formatB(A) : # A est une matrice image RGB
    A1 = niveau_gris(A) # A1 est une matrice RGB / R=G=B
    return A1[ : , : , 0]

    # Q5 :

# Q5 :

def fusion(A,B) : # A et B deux matrice image formatB
    H,L = A.shape
    C = np.zeros((H,L) , dtype = 'uint8')
    for i in range(H) :
        for j in range(L) :
            C[i,j] = min(A[i,j] , B[i,j])
    return C
# Q6

def moyenneur(A) :
    B = np.copy(A)
    H,L = A.shape
    for i in range(1 , H-1) :
    for j in range(1 , L-1) :
    Vij = A[i-1 : i+2 , j-1 : j + 2]
    B[i,j] = np.sum(Vij) // 9
    return B

    def compression(A , k) :
        H , L = A.shape
        B = np.zeros((H//k , L//k) , dtype = "uint8")
        for i in range(H//k) :
        for j in range(L//k) :
        B[i,j] = np.sum(A[k*i : k*i +1 , k*j : k*j+1]) // k**2
        return B
    # Q8

import matplotlib.pyplot as plt
def histogramme(A) :
    hist = [0]*256
    H,L = A.shape
    for i in range(H) :
    for j in range(L) :
    hist[A[i,j]] += 1
    return hist
def plotHistogramme(A) :
    hist = histogramme(A)
    X = np.arange(256)
    Y = np.array(hist)
    plt.plot(X,Y)
    plt.show()