def sposta(A:list[int]):
    if A == []: return None
    for i in range(len(A)-1):
        if A[i] >= 0:
            num = A.pop(i)
            A.append(num)
    return A

def sposta2(A:list[int]):
    if A == []: return None
    i = 0
    j = len(A)-1
    while i < j:
        if A[i] >= 0 and A[j] < 0:
            A[i],A[j] = A[j],A[i]
            i+=1
            j-=1
        else:
           if A[i]<0: i+=1 
           if A[i]>0: j-=1
    return A

def posizione2_3(A:list[int]):
    if len(A) < 1: return 1
    if A[1] % 2 == 1: return 0
    max2,min3 = A[1]
    i = 2
    while i<len(A):
        if A[i] % 2 == 1: return 0
        max2 = max(max2,A[i])
        i = 2*i
    i = 3
    while i < len(A):
        if A[i] % 2 == 1: return 0
        min3 = min(min3,A[i])
        i = 3*i
    if max2 <= min3 : return 1
    return 0

def maxConsecutivi(A:list[int]):
    massimo = 1
    count = 1
    i = 0
    for j in range(i+1,len(A)):
        if A[i]==A[j]:
            count+=1
        else:
            massimo = max(massimo,count)
            count = 1
            i = j
    return massimo
            
def findDup(A:list[int]):
    i = 0
    j = len(A)-1
    while True:
        m = (i+j)//2
        if A[m] == m:
            i = m
            if A[i-1] == m or A[i+1] == m:
                return m
        else:
            j = m-1
            if A[j-1] == m or A[j+1] == m:
                return m
            
def maxDistance(A:list[int]):
    vect = [-1]*51
    massimo = 0
    for i in range(len(A)-1):
        x = A[i]
        if vect[x] == -1:
            vect[x] = i
        else:
            dist = i-vect[x]
            massimo = max(dist,massimo)
    return massimo 
    
    
def maxTerna(A:list[int]):
    vect = [-1]*100
    for i in range(len(A)):
        if A[i] < 100:
            if vect[A[i]] == -1:
                vect[A[i]] = A[i]
    
    for j in range(len(vect)-1,1,-1):
        if vect[j-1] != -1 and vect [j-2] != -1 and vect[j] != -1:
            return vect[j-1]
    return -1
                
def moreFrequentElement(A:list[int]):
    vect = [0]*(10*len(A))
    for i in range(len(A)):
        vect[A[i]]+=1
    
    massimo = vect[0]
    posiz = 0
    for j in range(1,len(vect)):
        if massimo < vect[j]:
            massimo = vect[j]
            posiz = j
        elif massimo == vect[j]:
            posiz = min(posiz,j)
    return posiz
            

def checkSubArray(A:list[int],B:list[int]):
    first = B[0]
    posiz = -1
    for i in range(len(A)-1):
        if A[i] == first:
            posiz = i
            
    if posiz != -1:
        for j in range(1,len(B)):
            if A[posiz+j] != B[j]:
                return 0
    else:
        return 0
    
    return 1
            
def evenOddArrangement(A:list[int]):
    i = 0
    j = i+1
    while i < len(A)-2 and j <= len(A)-1:
        if A[i] % 2 == 0:
            i+=2
        if A[j] % 2 == 1:
            j+=2
        if A[i] % 2 == 1 and A[j] % 2 == 0:
            A[i],A[j] = A[j],A[i]
    return A

def evenOddArrangementM(A:list[int]):
    i = 0
    j = i+1
    while i < len(A) and j <= len(A):
        if A[i] % 2 == 0:
            i+=2
        if A[j] % 2 == 1:
            j+=2
        else:
            A[i],A[j] = A[j],A[i]
            i+=2
            j+=2
    return A

def diffPosition(A:list[int]):
    i = 0
    j = len(A)-1
    if A[0] != 0: return 0
    while i <= j:
        m = (i+j)//2
        if A[m] == m:
            i = m+1
        elif A[m] != m and A[m-1]==(m-1) and m >= 1:
            return m
        elif A[m] != m and A[m-1]!=(m-1) and m >= 1:
            j = m
    return -1

def rotated(A:list[int]):
    i, j = 0, len(A)-1
    while True:
        m = (i+j)//2
        if A[m] > A[m+1]:
            return len(A)-(m+1)
        if A[i] < A[m]:
            i = m+1
        else:
            j = m
            
            
def subArrayValue(A:list[int],s:int):
    if A[0] == s: return 0,0
    i = 0
    j = 1
    somma = A[0]
    while j < len(A)-1:
        somma += A[j]
        if somma > s:
            somma = A[i+1]
            i += 1
            j = i+1
        elif somma == s:
            return i,j
        else:
            j += 1
    return None

def sommaArray(A:list[int],k:int):
    i = 0
    j = 1
    count = 0
    while i < len(A)-1:
        if A[i] + A[j] == k:
            count += 1
        if j <= len(A)-2:
            j +=1
        elif j == len(A)-1:
            i += 1
            j = i+1
    return count
        
        
def sommaAbs(A:list[int],B:list[int]):
    i = 0
    j = 0
    while i < len(A)-1:
        if abs(A[i]-B[j]) <= 3:
            return 1
        if j <= len(B)-2:
            j += 1
        elif j == len(B)-1:
            i += 1
            j = 0
    return 0
          

def negativeFirst(A:list[int]):
    i = 0
    j = len(A)-1
    while i < j:
        if A[i] < 0 and A[j] < 0:
            i+=1
        elif A[i] > 0 and A[j] > 0:
            j-=1
        elif A[i] > 0 and A[j] < 0:
            A[i], A[j] = A[j], A[i]
            i+=1
            j-=1
        else:
            i+=1
            j-=1
    return A 
    
    
    
def evenOddArrangement2(A:list[int]):
    i = 0
    j = i+1
    while j <= len(A)-1:
       if A[i] % 2 == 0:
           i+=2
       if A[j] % 2 != 0:
           j+=2
       else:
           A[i], A[j] = A[j], A[i]
           i+=2
           j+=2
    return A
         
  

if __name__ == "__main__":
    A = [3,-5,-7,1,-8]
    B = [5,7,3,3,8,9,9,9,5,3,2,2]
    C = [5,7,3,9,9,9,9,9,4,9,1,1,1]
    D = [0,1,2,3,4,4,5,6,7]
    E = [3,3,4,6,6,3,5,5,5,6,6,9,9,1]
    F = [101,-5,9,31,-33,10,100,4,8,32,-500,11,-99]
    G = [2,6,8,5,2,3,6,8,9,5,8,1,2]
    A1 = [5,9,1,3,4,8,2]
    B1 = [5,9,1]
    A3 = [7,3,1,8,8,2,1,4]
    G1 = [3,6,8,5,2,3,6,8,9,5,8,1]
    A4 = [0,5,6,20,30]
    A5 = [9,2,3,5,7]
    A6 = [1,3,5,2,9,3,3,1,6]
    A7 = [1,2,2,3,4,5,5,5,8,9,9]
    A8 = [1,5,5,5,9]
    A9 = [1,2,20,30]
    B9 = [6,7,10]
    A10 = [1,2,9,10,12]
    B10 = [6,14,16,20]
    #print(sposta2(A))
    #print(maxConsecutivi(C))
    #print(findDup(D))
    #print(maxDistance(E))
    #print(maxTerna(F))
    #print(moreFrequentElement(G))
    #print(checkSubArray(A1,B1))
    #print(evenOddArrangement(A3))
    #print(diffPosition(A4))
    #print(rotated(A5))
    #print(subArrayValue(A6,7))
    #print(sommaArray(A7,7))
    #print(sommaAbs(A10,B10))
    #print(negativeFirst(F))
    print(evenOddArrangement2(A3))
    
    
