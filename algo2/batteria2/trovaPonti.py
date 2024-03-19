def trovaPonti(G):
    Altezza = [-1]*len(G)
    Ponti = []
    DFSMod(0, 0, G, Altezza, Ponti)
    return Ponti

def DFSMod(nodo:int,altezzaCorrente:int,G:list[list[int]],Altezza:list[int],Ponti:list[int]):
    from math import inf 
    Altezza[nodo] = altezzaCorrente
    ret = inf
    for nextNodo in G[nodo]: #per ogni nodo adiacente
        if Altezza[nextNodo] == -1: #se non è stato visitato
            nextAltezza = DFSMod(nextNodo,altezzaCorrente+1,G,Altezza,Ponti) #calcolo l'altezza del nodo
            if altezzaCorrente < nextAltezza: #se il nodo è un ponte
                Ponti.append((nodo,nextNodo))#aggiungo il ponte alla lista
            ret = min(ret,nextAltezza)#aggiorno il valore di ritorno
        elif Altezza[nextNodo] != altezzaCorrente-1:#se il nodo è già stato visitato e non è il padre
            ret = min(ret, Altezza[nextNodo])#aggiorno il valore di ritorno
    return ret  #ritorno il valore di ritorno

#Perchè devo fare il minimo tra ret e nextAltezza?
#Perchè se ho un ciclo, il ret sarà uguale all'altezza del nodo che ha generato il ciclo
#e quindi se trovo un nodo che ha altezza minore di ret, allora vuol dire che ho trovato un ciclo
#e quindi devo aggiornare ret con l'altezza del nodo che ha generato il ciclo
# altrimenti se non ho trovato un ciclo, ret sarà uguale a inf e quindi non verrà aggiornato

#Perchè devo fare il minimo tra altezzaCorrente e nextAltezza?
#Perchè se ho un ciclo, allora il nextAltezza sarà uguale all'altezzaCorrente
#e quindi non devo aggiornare l'altezza del nodo
#altrimenti se non ho trovato un ciclo, allora devo aggiornare l'altezza del nodo con nextAltezza

#Perchè devo vedere se Altezza[nextNodo] != altezzaCorrente-1?
#Perchè se Altezza[nextNodo] == altezzaCorrente-1, allora vuol dire che ho trovato un ciclo
#e quindi non devo aggiornare ret con l'altezza del nodo che ha generato il ciclo
#altrimenti se Altezza[nextNodo] != altezzaCorrente-1, allora devo aggiornare ret con l'altezza del nodo che ha generato il ciclo


if __name__=="__main__":
    grafo = [[3,4,5,8],[2,7],[1,6,7],[0,4,7],[0,3],[0,8],[2],[1,2,3],[0,5]]
    print(trovaPonti(grafo))