#Descrivere un algoritmo che, dato un grafo connesso G, trova un cammino in G
#che attraversa tutti gli archi una e una sola volta in ognuna delle due direzioni.
#L’algoritmo deve avere complessit‘a O(m)

def passeggiata(G): 
    P=[] # lista della passeggiata 
    V=[0]*len(G) # visitati a 3 valori 
    dfsP(G,0,0,P,V) 
    return P


def dfsP(G:list[list[int]],nodo:int,padre:int,P:list[int],visitati:list[int]):
    P.append(nodo)
    visitati[nodo] = 1 # entro in nodo
    for nextnodo in G[nodo]:
        if nextnodo != padre:
            if visitati[nextnodo] == 1:
                P.append(nextnodo)
                P.append(nodo)
            elif visitati[nextnodo] == 0:
                dfsP(G,nextnodo,nodo,P,visitati)
                P.append(nodo)
    # esco da nodo per sempre            
    visitati[nodo] = 2