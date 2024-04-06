def nodoPrincipale(grafo:list[list[int]],nodo:int)->bool:
    def verificaNodoPrincipale(grafo:list[list[int]], nodo:int, visitati:list[int]):
        visitati[nodo] = 1
        for nextNodo in grafo[nodo]:
            if visitati[nextNodo] == 0:
                verificaNodoPrincipale(grafo, nextNodo, visitati)
            
    visitati = [0 for _ in range(len(grafo))]
    verificaNodoPrincipale(grafo, nodo, visitati)
    for i in range(len(visitati)):
        if visitati[i] == 0:
            return False
    return True

def checkPrincipal(grafo:list[list[int]])->bool:
    for nodo in range(len(grafo)):
        if nodoPrincipale(grafo, nodo):
            return True
    return False
    

if __name__ == "__main__":
    grafo = [[],[0],[4,5],[2,5,6],[1],[1],[2]] # nodo principale è 3
    print(nodoPrincipale(grafo, 2)) # True