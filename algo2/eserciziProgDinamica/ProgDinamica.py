def uniNonConsecutivi(n:int):
    # F0[i] = Stringhe lunghe i+1 che finiscono con 0 e che non hanno uni consecutivi
    # F1[i] = stringhe lunghe i+1 che finiscono con 1 e che non hanno uni consecutivi
    F0 = [0]*n
    F1 = [0]*n
    F0[0] = 1
    F1[0] = 1
    for i in range(1,n):
        F1[i] = F0[i-1]
        F0[i] = F1[i-1]+F0[i-1]
         
    return F0[n-1]+F1[n-1]
     

def treuniNonConsecutivi(n:int):
    # F0[i] = Stringhe lunghe i+1 che finiscono con 0 e che non hanno tre uni consecutivi
    # F01[i] = stringhe lunghe i+1 che finiscono con 01 e che non hanno tre uni consecutivi
    # F11[i] = stringhe lunghe i+1 che finiscono con 11 e che non hanno tre uni consecutivi
    F0 = [0]*n
    F01 = [0]*n
    F11 = [0]*n
    F0[0] = 1
    F01[0] = 1
    F11[0] = 0
    for i in range(1,n):
        F11[i] = F01[i-1]  
        F01[i] = F0[i-1] 
        F0[i] = F0[i-1]+ F01[i-1]+F11[i-1]
    
    return F0[n-1] + F01[n-1] + F11[n-1]
         
  

if __name__ == "__main__":
    #print(uniNonConsecutivi(4))
    print(treuniNonConsecutivi(4))