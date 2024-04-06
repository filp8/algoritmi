def orient_edges(grafo:list[list[int]])->list[list[int]]: # O(n+m)
 G1 = [[] for _ in grafo] 
 for u in range(len(grafo)): 
     for v in grafo[u]: 
         if u <= v: 
            G1[u].append(v) 
 return G1

if __name__ == "__main__":
    grafo = [[1],[0,4,5],[3,4,5,6],[2,5,6],[1,2],[1,2,3],[2,3]]
    print(orient_edges(grafo))
    
