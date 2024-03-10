def es9v(grafo:list[list[int]],nodoStart:int,visitati:list[int])->int:
    visitati[nodoStart] = 1
    counterpozzi = 0
    if grafo[nodoStart] == []:
            counterpozzi += 1
    for nextNodo in grafo[nodoStart]:
        if visitati[nextNodo] == 0:
            counterpozzi += es9v(grafo,nextNodo,visitati)
    return counterpozzi

if __name__ == '__main__':

    grafoEs9 = [[4],[10,3],[1,3,6,8],[],[5,7],[0],[],[10],[9],[],[0]]
    visitati = [0]*len(grafoEs9)
    print(es9v(grafoEs9,9,visitati))