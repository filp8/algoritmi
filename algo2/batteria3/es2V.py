def calcolaGrafoQuadrato(grafo:list[list[int]]) -> list[list[int]]:
    grafoQuadrato = [[] for _ in range(len(grafo))]
    for nodo in range(len(grafo)):
        for nextnodo in grafo[nodo]:
            grafoQuadrato[nodo].append(grafo[nodo][0])
            for nextnextnodo in grafo[nextnodo]:
                if nextnextnodo not in grafoQuadrato[nodo]:
                    grafoQuadrato[nodo].append(nextnextnodo)
    return grafoQuadrato


if __name__ == "__main__":
    grafo = [[1],[2],[3],[4],[5],[0]] # result = [[1,2],[2,3],[3,4],[4,5],[5,0],[0,1]]
    print(calcolaGrafoQuadrato(grafo))
    


    