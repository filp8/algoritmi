'''def minimalCover(G:list[list[int]])->list[int]:
    quantiVisitati = [0]*len(G)
    visitati = [0]*len(G)
       
    for i,nodo in enumerate(G):
        quantiVisitati[i] = calcCover(G,i,i,visitati,quantiVisitati)
    
    massimo = max(quantiVisitati)
    '''
'''
def minimalCover(G:list[list[int]])->list[int]:
    
    
    
    
def calcCover(G,radice,padre,visitati,quantiVisitati):
    visitati[radice] = 1
    for nodo in G:
        for nextnodo in G[nodo]:
            


if __name__ == "__main__":
    grafo = [[1],[0,4,5],[3,4,5,6],[2,5,6],[1,2],[1,2,3],[2,3]]
    print(minimalCover(grafo))'''
    