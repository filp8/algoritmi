''' Stringa binaria che non ha tre zeri consecutivi 
T[i] = {
    2 se i = 1
    4 se i = 2
    7 se i = 3
    T[i-1]+T[i-2]+T[i-3] altrimenti
}'''

def es3zeri(n:int):
    T = [0]*(n+1)
    T[0] = 1
    T[1] = 2
    T[2] = 4
    for i in range(3,n+1):
        T[i] = T[i-1] + T[i-2] + T[i-3]
    return T[n]



''' Hotel con stanze da 1, da 2 e da 3 posti letto
T[i] = {
    1 se i = 0 oppure i = 1
    2 se i = 2
    5 se i = 3
    T[i-1] + (i-1)*T[i-2] + (i-1)*(i-2)*T[i-3] altrimenti
}

T[i] = numero di modi in cui è possibile sistemare i persone nell'albergo
'''
def esStanzeDa3(n:int):
    T = [0]*(n+1)
    T[0] = T[1] = 1
    T[2] = 2
    for i in range(3,n+1):
        # T[i] = numero di modi in cui è possibile sistemare i persone nell'albergo
        # Ho stanze da 1, da 2 e da 3 posti letto
        T[i] =  T[i-1] + (i-1)*T[i-2] + (((i-1)*(i-2))//2)*T[i-3]
       
    return T[n]



'''Somma massima di sottosequenza di elementi che distano almeno 2
T[i] = {
    
    A[0] se i = 0
    max(A[0],A[1]) se i = 1
    max(T[i-2],T[i-3]+A[i]) altrimenti
}

'''

def esDist2(A:list[int]):
    n = len(A)
    T = [0]*n
    T[0] = A[0]
    T[1] = max(A[0],A[1])
    T[2] = max(A[0],A[1],A[2])
    for i in range(3,n):
        T[i] = max(T[i-2],T[i-3] + A[i])
    return T[n-1]
    
def maxSottolista(A:list[int]):
    n = len(A)
    T = [0]*n
    T[0] = A[0]
    for i in range(1,n):
        T[i] = max(A[i],A[i]+T[i-1])
    return max(T)


def conta_stringhe_binarie(n):
    # Condizioni iniziali
    if n == 1:
        return 2
    if n == 2:
        return 3
    
    # Inizializza i valori per le condizioni iniziali
    a1 = 2
    a2 = 3
    a = 0
    
    # Calcola a(n) usando la relazione di ricorrenza
    for i in range(3, n + 1):
        a = a1 + a2
        a1 = a2
        a2 = a
    
    return a

# Esempio di utilizzo

def esLuglio2(S:str,I:set):
    n = len(S)
    T = [0]*n
    if S[0] in I: T[0] += 1
    if S[0:2] in I: T[1] += 1
    if S[1] in I and T[0] == 1: T[1] += 1
    for i in range(2,n):
        if S[i-1:i+1] in I:
            T[i] += T[i-2]
        if S[i] in I:
            T[i] += T[i-1]
    return T[n-1]



if __name__ == "__main__":
    #print(es3zeri(4))
    #print(esStanzeDa3(4))
   # A =[2,0,-2,1,-3,1,0,4,-2,3,-1,2,-2,2,-5,1]
    #print(esDist2(A))
    #print(maxSottolista(A))
    S = '011'
    I = set(['01','1'])
    print(esLuglio2(S,I))
    #print(f"Il numero di stringhe binarie di lunghezza {5} in cui non compaiono mai uni consecutivi è: {conta_stringhe_binarie(5)}")
    
    
     