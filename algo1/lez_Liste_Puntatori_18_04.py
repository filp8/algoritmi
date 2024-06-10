class Nodo:
    def __init__(self, key = None, next = None):
        self.key = key
        self.next = next
        
class NodoD:
    def __init__(self, key = None, prev = None, next = None):
        self.key = key
        self.next = next
        self.prev = prev
        

def crea(A):
    if A == []: return None
    p = Nodo(A[0])
    q = p
    for i in range(1,len(A)):
        q.next = Nodo(A[i])
        q = q.next
    return p

def creaDoppia(A):
    if A == []: return None
    p = NodoD(A[0])
    q = p
    for i in range(1,len(A)):
        q.next = NodoD(A[i],q)
        q = q.next
    return p


def stampa(p:Nodo):
    while p:
        print(p.key)
        p = p.next

def ricerca(p:Nodo, x):
    q = p
    while q and q.key != x:
        q = q.next
    return q

def inserisci_in_testa(p:Nodo, x):
   return Nodo(x,p)

def inserisci(p:Nodo, x, y):
    while p and p.key != y:
        p = p.next
    if p:
        p.next = Nodo(x,p.next)
    
def cancella(p:Nodo,x):
    if p != None:
        if p.key == x:
            p = p.next
        else:
            q = p
            while q.next != None and q.next.key != x:
                q = q.next
            if q.next != None:
                q.next = q.next.next
    return p

def get_last(p:Nodo):
    if p.next == None:
        return None
    while p.next != None:
        p = p.next
    return p

def get_penultimo(p:Nodo):
    if p.next.next == None:
        return None
    while p.next.next != None:
        p = p.next
    return p

def delete_last(p:Nodo):
    q = p
    while q.next.next != None:
        q = q.next
    q.next = None
    return p

def reverseNodo(P:Nodo):
    n = None
    while P:
        n = Nodo(P.key, n)
        P = P.next
    return n

def atLeastTwo(p:Nodo):
    dup = set()
    while p:
        q = p.next
        while q:
            if p.key == q.key:
                dup.add(p.key)
            q = q.next
        p = p.next
    return dup

def add_in_order(p:Nodo,x):
    if p == None or p.key > x:
        return Nodo(x,p)
    q = p
    while q and q.next.key < x:
        q = q.next
    q.next = Nodo(x,q.next)
    return p


    
    

#q.prev, q.next.prev = q.next.prev, q.prev
# without using extra space and without merge
def sort(p:Nodo): 
    if p == None or p.next == None:
        return p
    q = p
    while q.next != None:
        if q.key > q.next.key:
            q.key, q.next.key = q.next.key, q.key
            
            q = p
        else:
            q = q.next
    return p
# Complexity: O(n^2)
    

def evenOddPositions(p:Nodo):
    if p == None or p.next == None:
        return p
    q = p
    r = p.next
    while r and r.next:
        q.next = r.next
        q = q.next
        r.next = q.next
        r = r.next
    q.next = None
    return p

def lenDouble(p:NodoD):
    if p == None: return 0
    c = 0
    while p:
        c+=1
        p = p.next
    return c
    
def reverseDouble(p:NodoD):
    if p == None: return None
    q = p
    while q.next:
        q = q.next
    while q:
        print(q.key)
        q = q.prev
    return

def deleteDouble(p:NodoD,x):
    if p != None:
        if p.key == x:
            p = p.next
            p.prev = None
        q = p
        while q.next:
            if q.next.key == x:
                if q.next.next != None:
                    q.next = q.next.next
                    q.next.next.prev = q
                else: 
                    q.next = None
            else:
                q = q.next
    return p
        
def insertInOrderDouble(p:NodoD,x:int):
    if p != None:
        if p.key > x:
            return NodoD(x,None,p)
        q = p
        while q and q.next and q.next.key < x:
            q = q.next
        if q.next == None and q.key < x:
            q.next = NodoD(x,q,None)
        else:
            q.next = NodoD(x,q,q.next)
            q.next.next.prev = q.next
    return p
                

def atLeastTwoDouble(p:NodoD):
    while p:
        q = p.next
        while q:
            if p.key == q.key:
                if q.next.next != None:
                    q.next = q.next.next
                    q.next.next.prev = q
                else: 
                    q.next = None
                q = q.next
        p = p.next
    return p

def sumMKMarzo2024(p:Nodo,k:int):
   if p.key >= k: return 1
   return 1 + sumMKMarzo2024(p.next, k-p.key)


def minMax(p:Nodo):
    if p == None: return None, None
    if p.next == None: return p.key, p.key
    a,b = minMax(p.next)
    return min(a,p.key), max(b,p.key)
    
        
def accorpa(p:Nodo):
    if p == None: return None
    if p.next == None: return None
    p.key += p.next.key
    p.next = accorpa(p.next.next)
    return p   

def checkSum(p:Nodo,somma:int):
    if p == None: return None
    if somma == p.key:
        return p
    else:
        somma += p.key
        return checkSum(p.next,somma)
    
def checkPalindroma(P:NodoD):
    q = P
    i = j = 0
    while q.next != None:
        q = q.next
        j+=1
    while i != j:
        if P.key != q.key: return False
        P = P.next
        q = q.prev
        i+=1
        j-=1
    return True



def countEvenNode(P:Nodo):
    if P == None: return 0
    if P.key % 2 == 0:
        return countEvenNode(P.next) + 1
    return countEvenNode(P.next)

def removeDup(P:Nodo):
    q = P
    r = P
    while q:
        if r.key == q.key:
            if q.next != None:
                r.next = q.next.next
            else:
                r.next = None
        else:
            r = r.next
        q = q.next
    return P
    
    
def evensSort(P:Nodo):
    sol = set()
    q = P
    while q.next != None:
        if q.key % 2 == 0:
            sol.add(q.key)
        q = q.next
    sol = sorted(list(sol))
    head = Nodo(sol[0])
    t = head
    for i in range(1,len(sol)):
        t.next = Nodo(sol[i])
        t = t.next
    return head

def negativeBeforePos(P:NodoD):
    begin = P
    end = P
    i = 0
    j = 0
    while end.next:
        end = end.next
        j +=1
    while i<j:
        if begin.key < 0 and end.key < 0:
            i+=1
            begin=begin.next
        elif begin.key > 0 and end.key > 0:
            j-=1
            end = end.prev
        elif begin.key > 0 and end.key < 0:
            begin.key, end.key = end.key, begin.key
            i+=1
            j-=1
            begin = begin.next
            end = end.prev
        else:
            i+=1
            j-=1
            begin = begin.next
            end = end.prev
    return P
                
                
def powerOftwoAndPowerOfthree(A:list[int]):
    i = 0
    j = 0
    dim = len(A)
    massimo = 0
    while (2**i) < dim:
        if A[2**i] % 2 == 0:
            if A[2**i] > massimo:
                massimo = A[2**i]
            i+=1
        else:
            return False
        
    while (3**j) < dim:
        if A[3**j] % 2 == 0:
            if massimo > A[3**j]:
                return False
            j+=1
        else:
            return False
    return True

def circularListEs(P:Nodo):
    start = P.key
    minimo = P.key
    P = P.next
    while P.key != start:
        if P.key < minimo:
            minimo = P.key
        P = P.next
    return minimo

def circularListEs2(P:Nodo):
    start = P.key
    minimo = P.key
    P = P.next
    return circularListEsRec(P,start,minimo)

def circularListEsRec(P:Nodo,start,minimo):
    if P.key == start:
        return minimo
    if P.key < minimo:
        minimo = P.key
    return circularListEsRec(P.next,start,minimo)
    
if __name__ == "__main__":
    A = crea([8,6,4,9])
    B = crea([1,2,3,4,5])
    C = creaDoppia([1,2,3,4,5,6,7,7,7,8,9,10])
    D = crea([1,8,-4,9,-2,2])
    E = crea([3,2,8,-4,6,1,2])
    F = crea([1,2,3,6])
    Pal = creaDoppia([1,1,0,1,1])
    C1 = crea([1,2,3,4,5,6,7,7,7,8,9,10])
    D1 = crea([3,3,3,4,4,7,7,7,9,9,9,9])
    test = crea([1,8,4,9,3,4])
    
    #stampa(A)
    #A = inserisci_in_testa(A, 9)
    #stampa(A)
    #inserisci(A, 7, 6)
    #inserisci(A, 9, 7)
    #inserisci(A, 8, 6)
    #cancella(A, 4)
    #stampa(A)
    #last = get_last(A).key
    #print("Last: "+ str(last))
    #penultimo = get_penultimo(A).key
    #print("Penultimo: "+ str(penultimo))
    #delete_last(A)
    #stampa(A)
    #stampa(reverseNodo(A))
    #print(atLeastTwo(A))
    #B = add_in_order(B, 4)
    #B = add_in_order(B, 8)
    #stampa(B)
    #stampa(A)
    #A = sort(A)
    #stampa(A)
    #P = evenOddPositions(B)
    #stampa(P)
    #print(lenDouble(C))
    #reverseDouble(C)
    #C = deleteDouble(C,5)
    #C = insertInOrderDouble(C,7)
    #C = insertInOrderDouble(C,11)
    #C = atLeastTwoDouble(C)
    #stampa(C)
    #reverseDouble(C)
    #print(minMax(D))
    #stampa(accorpa(E))
    #stampa(checkSum(F,0))
    #print(checkPalindroma(Pal))
    #print(countEvenNode(C1))
    #stampa(removeDup(D1))
    #stampa(sort(E))
    #head = evensSort(test)
    #print(head)
    #testList = creaDoppia([1,8,-4,9,-2,2])
    #head = negativeBeforePos(testList)
    #print(head)
    testListF = [1,50,20,70,6,11,10,21,40,85,1,1,13,1,22,64,30,1]
    testListF2 = [1,50,20,70,6,11,10,21,40,80,1,1,13,1,22,64,90,1]
    testListT = [1,50,20,70,6,11,10,21,40,80,1,1,13,1,22,64,30,1]
    #print(powerOftwoAndPowerOfthree(testListF))
    #print(powerOftwoAndPowerOfthree(testListF2))
    #print(powerOftwoAndPowerOfthree(testListT))
    
    circular = Nodo(31)
    c1 = Nodo(10)
    c2 = Nodo(15)
    c3 = Nodo(12)
    c4 = Nodo(14)
    c5 = Nodo(3)
    c6 = Nodo(9)
    c7 = Nodo(7)
    circular.next = c1
    c1.next = c2
    c2.next = c3
    c3.next = c4
    c4.next = c5
    c5.next = c6
    c6.next = c7
    c7.next = circular
    
    print(circularListEs(circular))
    print(circularListEs2(circular))
    