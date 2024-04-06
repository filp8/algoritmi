# Dato un albero di n nodi rappresentato tramite il vettore dei padri P(per convenzione il padre del nodo radice è il nodo stesso) 
# e due nodi dell’albero u e v, dare lo pseudocodice di un algoritmo che in tempo O(n) calcola la distanza tra u e v nell’albero.


def distNodiAlbero(P:list[int],u:int,v:int):
    pu = rootToX(P,u) # calcola il cammino da u alla radice
    pv = rootToX(P,v) # calcola il cammino da v alla radice
    i = 0 # inizializza l'indice
    while pv[i] != v and pu[i] != u and pu[i+1] == pv[i+1]: # finchè i nodi sono diversi e il padre è lo stesso
        i+=1 # incrementa l'indice
    return len(pu) + len(pv) - 2*i # restituisci la distanza tra u e v meno il doppio dell'indice per evitare di contare due volte il nodo in comune


def rootToX(padri:list[int],nodo:int):
    c = [] # inizializza la lista
    while nodo != padri[nodo]: # finchè il nodo non è la radice
        c.append(nodo) # aggiungi il nodo alla lista
        nodo = padri[nodo] # vai al padre
    c.reverse() # inverte la lista
    return c