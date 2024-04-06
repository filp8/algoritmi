def soottoalbero(f_padri, radice, inizioAlbero): 
    def _sottoalbero(f_padri, radice, sottoalbero, inizioAlbero):
        sottoalbero.append(radice)
        i = inizioAlbero
        for nodo in f_padri:
            if nodo == radice:
                _sottoalbero(f_padri, i, sottoalbero, inizioAlbero)
            i+=1
    sottoalbero = []
    _sottoalbero(f_padri, radice, sottoalbero, inizioAlbero)
    return sottoalbero

# Quant'è la complessità di questo algoritmo?
# Il costo di questo algoritmo è O(n) dove n è il numero di nodi dell'albero.


if __name__ == '__main__':
    padri = [3, 4, 3, 5, 3, 4, 5, 1]
    print(soottoalbero(padri, 8, 1))