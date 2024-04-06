#Descrivere un algoritmo che, dato un grafo G non diretto e connesso e due suoi
#nodi u e v, in tempo O(n+ m) trova i nodi che hanno la stessa distanza da u e v.

def check_same_distance(grafo:list[list[int]], u:int, v:int)->list[int]: # O(n+m)
    dist_u = bfs(grafo, u) # calcola le distanze di tutti i nodi da u
    dist_v = bfs(grafo, v) # calcola le distanze di tutti i nodi da v
    result = []
    for i in range(len(grafo)):
        if dist_u[i] == dist_v[i]:
            result.append(i)
    return result


def bfs(grafo:list[list[int]], s:int)->list[int]: # O(n+m)
    dist = [-1]*len(grafo) # inizializza il vettore delle distanze
    dist[s] = 0 # la distanza di s da s è 0
    queue = [s] # coda con s
    while queue: # finchè la coda non è vuota
        u = queue.pop(0) # estrai il primo elemento della coda
        for v in grafo[u]: # per ogni nodo v adiacente a u
            if dist[v] == -1: # se non è stato visitato
                dist[v] = dist[u]+1 # la distanza di v da s è la distanza di u da s + 1
                queue.append(v) # aggiungi v alla coda
    return dist

if __name__ == "__main__":
    grafo = [[1],[0,4,5],[3,4,5,6],[2,5,6],[1,2],[1,2,3],[2,3]]
    u = 0
    v = 3
    print(check_same_distance(grafo, u, v)) # [4]
