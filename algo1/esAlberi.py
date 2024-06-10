class NodoAB:
    def __init__(self,key=None,left=None,right=None):
        self.key = key
        self.left = left
        self.right = right
        

class NodoABR:
    def __init__(self,key=None,left=None,right=None,parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent  

def getPositionalRepr(P:list[int],Pos:list[int]):
    diz_pos = {i:False for i in range(len(P))}
    for i in range(len(P)):
        if P[i] == i:
            Pos[i] = i
        elif diz_pos[P[i]] == False:
            Pos[(2*P[i])+1] = i
            diz_pos[P[i]] = True
        else:
            Pos[(2*P[i])+2] = i
    return Pos

def countValidNodes(P:NodoAB):
    if P == None: return 0
    c = countValidNodes(P.left) + countValidNodes(P.right)
    if P.left and P.right and ((P.left.key < P.key and P.right.key > P.key) or (P.left.key > P.key and P.right.key < P.key)):
        c+=1
    return c



def evenNodesWithTwoSons(P:NodoAB):
    if P == None: return 0
    c = evenNodesWithTwoSons(P.left) + evenNodesWithTwoSons(P.right)
    if P.left and P.right and P.key % 2 == 0:
        c+=1
    return c

def validNodes2(P:NodoAB,tot = 0):
    if P == None: return 0
    validi = 0
    if P.key == tot:
        validi+=1
    validi += validNodes2(P.left,tot+P.key)
    validi += validNodes2(P.right,tot+P.key)
    return validi
    
def checkAlberoRicercaRec(P:NodoAB,A:list[int]):
    if P == None: return 
    checkAlberoRicercaRec(P.left,A)
    A.append(P.key)
    checkAlberoRicercaRec(P.right,A)
    
    
def checkAlberoRicerca(P:NodoAB):
    A = []
    checkAlberoRicercaRec(P,A)
    for i in range(1,len(A)):
        if A[i] < A[i-1]: return False
    return True

def sommaFigli(P:NodoAB):
    if P == None: return None
    if P.left:
        P.key += P.left.key
    if P.right:
        P.key += P.right.key
    sommaFigli(P.left)
    sommaFigli(P.right)
    return P

def switchSons(P:NodoAB):
    if P == None: return None
    if P.left and P.right:
        P.left.key, P.right.key = P.right.key, P.left.key
    if P.left:
        switchSons(P.left)
    if P.right:
        switchSons(P.right)
    return P

def minimalH(P:NodoAB):
    if P == None: return -1
    h = min(minimalH(P.left),minimalH(P.right))
    return h+1

def convertPositionalReprToTree(Pos:list[int],i=0):
    if i >= len(Pos) or Pos[i] == None: return None 
    # Se l'indice è maggiore della lunghezza di Pos o il nodo è None ritorno None per indicare che non c'è nessun nodo
    return NodoAB(Pos[i],convertPositionalReprToTree(Pos,2*i+1),convertPositionalReprToTree(Pos,2*i+2)) 
    # Altrimenti ritorno un nodo con la chiave Pos[i] e come figli i figli di Pos[i] nell'array Pos
    #T(N) = 2*T(N/2) + O(1) => O(N)
    

def convertTreeToPositionalRepr(P:NodoAB,Pos:list[int],i=0):
    if P == None: return
    Pos[i] = P.key
    convertTreeToPositionalRepr(P.left,Pos,2*i+1)
    convertTreeToPositionalRepr(P.right,Pos,2*i+2)
    # T(N) = 2*T(N/2) + O(1) => O(N)

def calculatePositionalVectorDim(h:int):
    return 2**(h+1)-1

def calcolaAltezzaAlbero(P:NodoAB):
    if P == None: return -1
    return max(calcolaAltezzaAlbero(P.left),calcolaAltezzaAlbero(P.right))+1

def stampa_albero_radice_primo(nodo):
    # Visita l'albero in ordine radice-sinistra-destro
    if nodo is not None:
        print(nodo.key, end=" ")
        stampa_albero_radice_primo(nodo.left)
        stampa_albero_radice_primo(nodo.right)




# Generare tutte le stringhe di lunghezza n con caratteri che vanno da 0 a k-1 e la cui somma dei caratteri è uguale a t in tempo O(n*k*S(n)) 
def generaStringhe(n:int,k:int,t:int):
    # n = lunghezza della stringa
    # k = numero di caratteri possibili
    # t = somma dei caratteri
    def generaStringheRec(n:int,k:int,t:int,curr:str):
        if n == 0:
            if t == 0:
                print(curr)
            return
        for i in range(k):
            if t-i >= 0:
                generaStringheRec(n-1,k,t-i,curr+str(i))
    generaStringheRec(n,k,t,"")
    # T(n) = k*T(n-1) => O(k^n)
    # S(n) = n
    
    
    
def generate_strings(n, k, t):
    result = []

    def backtrack(index, current_sum, current_string):
        if index == n:
            if current_sum == t:
                result.append("".join(current_string))
            return

        for i in range(k):
            if current_sum + i <= t:
                current_string[index] = str(i)
                backtrack(index + 1, current_sum + i, current_string)

    backtrack(0, 0, ['0'] * n)
    return result


    
def genStringAlBack(x:list[int],sol=[],i=0):
    if i == len(x):
        print(sol)
        return
    for j in [0,1,2]:
        if j != x[i] and (i==0 or j != sol[i-1]):
            sol.append(j)
            genStringAlBack(x,sol,i+1)
            sol.pop()
    
def genMatrix(n:int):
    sol = [[0]*n for _ in range(n)]
    c = [0]*n
    genMatrixBack(n,sol,c)
    
def genMatrixBack(n:int,sol:list[list[int]],c:list[int],i=0,j=0):
    if i == n:
        for riga in range(n):
            print(sol[riga])
        print()
        return
    if c[j] < (n//2):
        sol[i][j] = 0
        c[j]+=1
        if j < n-1:
            genMatrixBack(n,sol,c,i,j+1)
        else:
            genMatrixBack(n,sol,c,i+1,0)
        c[j]-=1 
    sol[i][j] = 1
    if j < n-1:
        genMatrixBack(n,sol,c,i,j+1)
    else:
        genMatrixBack(n,sol,c,i+1,0)

def genMatrixIones(n:int):
    sol = [[0]*n for _ in range(n)]
    c = [0]*n
    genMatrixIonesBack(n,sol,c)
    

def genMatrixIonesBack(n:int,sol:list[list[int]],c:list[int],i=0,j=0):
    if i == n:
        for riga in range(n):
            print(sol[riga])
        print()
        return
    if c[i] < i:
        sol[i][j] = 1
        c[i]+=1
        if j < n-1:
            genMatrixIonesBack(n,sol,c,i,j+1)
        else:
            genMatrixIonesBack(n,sol,c,i+1,0)
        c[i]-=1
    if (j-c[i]) < n-i: 
        sol[i][j] = 0
        if j < n-1:
            genMatrixIonesBack(n,sol,c,i,j+1)
        else:
            genMatrixIonesBack(n,sol,c,i+1,0)
            
def genMatrixGoingDown(M:list[list[int]]):
    n = len(M)
    sol = []*n
    genMatrixGoingDownBack(M,n,sol)
    
def genMatrixGoingDownBack(M:list[list[int]],n:int,sol=list[int],i=0,j=0):
    if i == n:
        #sol.reverse()
        print(sol)
        return
    sol.append(M[i][j])
    if j > 0:
        genMatrixGoingDownBack(M,n,sol,i+1,j-1)
        sol.pop()
    genMatrixGoingDownBack(M,n,sol,i+1,j)
    if j < n-1:
        genMatrixGoingDownBack(M,n,sol,i+1,j+1)
        sol.pop()
    # DA RIFARE
    
    
def convertiVettoredeiPadriInNodoAB(padri:list[int]):
    n = len(padri)
    nodi = [NodoAB(i) for i in range(n)]
    for i in range(n):
        if padri[i] == None:
            root = nodi[i]
        else:
            if nodi[padri[i]].left is None:
                nodi[padri[i]].left = nodi[i]
            else:
                nodi[padri[i]].right = nodi[i]
    return root

def convertiNodoABinVettoredeiPadri(P:NodoAB):
    if P == None: return []
    padri = [None]*nodi(P)
    convertiNodoABinVettoredeiPadriRec(P,padri)
    return padri

def convertiNodoABinVettoredeiPadriRec(P:NodoAB,padri:list[int]):
    if P.left:
        padri[P.left.key] = P.key
        convertiNodoABinVettoredeiPadriRec(P.left,padri)
    if P.right:
        padri[P.right.key] = P.key
        convertiNodoABinVettoredeiPadriRec(P.right,padri)
    
def nodi(P:NodoAB):
    if P == None: return 0
    return 1 + nodi(P.left) + nodi(P.right)


def posRepr(P:NodoAB,vect:list[int],i=0):
    if P == None: return
    vect[i] = P.key
    posRepr(P.left,vect,2*i+1)
    posRepr(P.right,vect,2*i+2)
# T(N) = 2*T(N/2) + O(1) => O(N)

def minH(P:NodoAB):
    if P == None: return -1
    return min(minH(P.left),minH(P.right)) + 1

def growingPath(P:NodoAB):
    if P.left == P.right == None: return True
    if P.left != None:
        if P.left.key > P.key:
            return growingPath(P.left)
    if P.right != None:
        if P.right.key > P.key:
            return growingPath(P.right)
    return False
# T(n) = T(k) + T(n-k-1) + O(1) => O(N)

def triplaNumFigli(P:NodoAB):
    if P == None: return 0, 0, 0
    ds,us,zs = triplaNumFigli(P.left)
    dd,ud,zd = triplaNumFigli(P.right)
    if P.left == P.right == None: return (ds+dd,us+ud,zs+zd+1)
    if P.left != None and P.right != None: return(ds+dd+1,us+ud,zs+zd)
    else: return (ds+dd,us+ud+1,zs+zd)


def kth_node(root:NodoAB, k):
    # Helper function to perform in-order traversal
    result, _ = in_order_traversal(root, k, 0)
    return result

def in_order_traversal(node:NodoAB, k, count):
    if node is None:
        return None, count

    # Traverse the left subtree
    result, count = in_order_traversal(node.left, k, count)
    if result is not None:
        return result, count
    
    # Increment the count and check if current node is the k-th node
    count += 1
    if count == k:
        return node.key, count

    # Traverse the right subtree
    return in_order_traversal(node.right, k, count)



def equilibratedNodes(P:NodoAB):
    if P == None: return 0
    if P.left == P.right == None: return 1
    valsx = equilibratedNodes(P.left)     
    valdx = equilibratedNodes(P.right)
    if valsx == valdx: return valsx + valdx + 1
    else: return valsx + valdx 
    
    
def esame3(r:NodoAB): 
    if r ==None: return 0, 0 
    equilibratiS, nodiS = esame3(r.left) 
    equilibratiD, nodiD = esame3(r.right) 
    equilibrati = equilibratiS + equilibratiD 
    if nodiS == nodiD: equilibrati += 1 
    return equilibrati, nodiS + nodiD +1

def bothSonsBiggersmaller(P:NodoAB,count=0):
    if P == None: return 0
    if P.left and P.right and ((P.left.key > P.key and P.right.key < P.key) or (P.left.key < P.key and P.right.key > P.key) ):
        count+=1
    return count + bothSonsBiggersmaller(P.left,count) + bothSonsBiggersmaller(P.right,count)


def maxDistance(P:NodoAB):
    if P == None: return 0
    sommasx = maxDistance(P.left) + P.key
    sommadx = maxDistance(P.right) + P.key
    return max(sommasx,sommadx)
#T(n) = T(k) + T(n-1-k) + O(1) ==> O(n)


def sommaAntentati(P:NodoAB,somma = 0):
    if P == None: return 0
    validi = 0
    if somma == P.key:
        validi+= 1
    if P.left != None:
        validi += sommaAntentati(P.left,somma+P.key)
    if P.right != None:
        validi += sommaAntentati(P.right,somma+P.key)
    return validi


def sameValuesTreeNodes(P:NodoAB):
    if P == None: return 1
    val = P.key
    if verifica(P,val):
        return 1
    else:
        return 0
    
def verifica(P:NodoAB,val):
    if P == None: return True
    if P.key != val:
        return False
    return verifica(P.left,val) and verifica(P.right,val)
    
    
def sameNodesMonti(P:NodoAB):
    if P == None: return 1
    if not sameNodesMonti(P.left): return 0
    if not sameNodesMonti(P.right): return 0
    if (P.left == None or P.left.key == P.key) and (P.right == None or P.right.key == P.key):
        return 1
    return 0
    



if __name__ == "__main__":
    #P = [0,0,1,1,0,4,4,5,6]
    #print(str(P))
    #h = 3
    #dim = 2**(h+1)-1
    #Pos = [-1]*dim
    #print(getPositionalRepr(P,Pos))
    P = NodoAB(0,NodoAB(2,NodoAB(1),NodoAB(7,NodoAB(9))),NodoAB(5,NodoAB(6),NodoAB(-40,NodoAB(-35))))
    test = NodoAB(5,NodoAB(6),NodoAB(2,NodoAB(4,NodoAB(5)),NodoAB(3,NodoAB(1),NodoAB(4))))
    Psame = NodoAB(1,NodoAB(1,NodoAB(1),NodoAB(1,NodoAB(1))),NodoAB(1,NodoAB(1),NodoAB(1,NodoAB(0))))
    #print(maxDistance(P))
    #print(evenNodesWithTwoSons(P))
    #print(validNodes2(P))
    #print(sameValuesNodes(P))
    #print(checkAlberoRicerca(test))
    #sommaFigli(test)
    #switchSons(test)
    #print(test)
    #print(minimalH(test))
    posizione = [1, 2, 4, None, None, None, 3, None, None]
    padri = [None, 0, 1, 1, 0, 4, 4, 5, 6]
    #albero = convertPositionalReprToTree(posizione)
    #h = calcolaAltezzaAlbero(albero)
    #dim = calculatePositionalVectorDim(h)
    #pos = [None]*dim
    #convertTreeToPositionalRepr(albero,pos)
    #stampa_albero_radice_primo(albero)
    #generaStringhe(6,4,12)
    #print(generate_strings(6,4,12))
    #X = [2,0,0,1]
    #genStringAlBack(X)
    #genMatrix(2)
    #genMatrixIones(3)
    #mat = [[1,2],
     #      [3,4]]
    #genMatrixGoingDown(mat)
    #albero = convertiVettoredeiPadriInNodoAB(padri)
    #treetest = NodoAB(2,NodoAB(10),NodoAB(4,NodoAB(3,None,NodoAB(7))))
    #altezza = calcolaAltezzaAlbero(treetest)
    #dim = calculatePositionalVectorDim(altezza)
    #vect = [None]*dim
    #stampa_albero_radice_primo(albero)
    #print(convertiNodoABinVettoredeiPadri(albero))
    #treeGrowPath1 = NodoAB(2,NodoAB(1),NodoAB(4,NodoAB(3,None,NodoAB(7)))) 
    #treeGrowPath2 = NodoAB(2,NodoAB(1),NodoAB(4,NodoAB(5,None,NodoAB(7)))) 
    #print(growingPath(treeGrowPath1))
    #print(growingPath(treeGrowPath2))
    
    #triplaFigliTree = NodoAB(1,NodoAB(1,NodoAB(1),NodoAB(1,NodoAB(1,NodoAB(1),NodoAB(1)),NodoAB(1))),NodoAB(1,NodoAB(1),NodoAB(1,None,NodoAB(1))))
    #print(triplaNumFigli(triplaFigliTree))
    # Example usage:
    # Constructing the BST
    #       5
    #      / \
    #     3   7
    #    / \ / \
    #   2  4 6  8
    root = NodoAB(5)
    root.left = NodoAB(3)
    root.right = NodoAB(7)
    root.left.left = NodoAB(2)
    root.left.right = NodoAB(4)
    root.right.left = NodoAB(6)
    root.right.right = NodoAB(8)
    #k = 8
    #print(kth_node(root,k))
    #print(equilibratedNodes(treeGrowPath1))
    #print(equilibratedNodes(treeGrowPath1))
    #print(sommaAntentati(P))
    #print(sameValuesTreeNodes(Psame))
    #print(sameValuesTreeNodes(Psame))
    print(sameNodesMonti(Psame))