def calcolaGrafoQuadrato(grafo:list[list[int]]) -> list[list[int]]:
    grafoQuadrato = [[] for _ in range(len(grafo))]
    for i,nodo in enumerate(grafo):
        for nextnodo in nodo:
            if nextnodo not in grafoQuadrato[i]:
                grafoQuadrato[i].append(nextnodo)
            for nextnextnodo in grafo[nextnodo]:
                if nextnextnodo not in grafoQuadrato[i]:
                    grafoQuadrato[i].append(nextnextnodo)
    return grafoQuadrato


if __name__ == "__main__":
    grafo = [[1],[2],[3,4],[4],[5],[0]] # result = [[1,2],[2,3,4],[3,4,5],[4,5],[5,0],[0,1]]
    print(calcolaGrafoQuadrato(grafo))
    