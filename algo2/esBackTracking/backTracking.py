def es3_aprile_2020(n:int,i=0,Sol=[]):
    if i == n:
        print(Sol)
        return
    for x in [0,1,2]:  
        if i == 0:
            Sol.append(x)
            es3_aprile_2020(n,i+1,Sol)
            Sol.pop()
            
        if i > 0:
            if x % 2 == 0:
                if Sol[i-1] % 2 == 1:
                    Sol.append(x)
                    es3_aprile_2020(n,i+1,Sol)
                    Sol.pop()
            else:
                Sol.append(x)
                es3_aprile_2020(n,i+1,Sol)
                Sol.pop()
                
    return        


def es3_Luglio_2022(n:int):
    sol = [[0]*n for _ in range(n)]
    R = [0]*n
    es3Back(n,0,0,sol,R)
    
def es3Back(n:int,i,j,sol,R):
    if i == n:
        for r in range(n):
            print(sol[r])
        print()
        return
    if j-R[i] < n-i:
        sol[i][j] = 0
        if j < n-1:
            es3Back(n,i,j+1,sol,R)
        else:
            es3Back(n,i+1,0,sol,R)
    
    if R[i] < i:
        sol[i][j] = 1
        R[i]+=1
        if j < n-1:
            es3Back(n,i,j+1,sol,R)
        else:
            es3Back(n,i+1,0,sol,R)
        R[i]-=1
        
def es2Back(n,i,tot,sol):
    if i == 2*n:
        print(sol)
        return
    if i < n: 
        for x in [0,1]:
            sol.append(x)
            es2Back(n,i+1,tot+x,sol)
            sol.pop()
    else:
        if tot > 0: 
            sol.append(1)
            es2Back(n,i+1,tot-1,sol)
            sol.pop()
        if 2*n - (i+1) >= tot: 
            sol.append(0)
            es2Back(n,i+1,tot,sol)
            sol.pop()
            
def esLuglioBack(n:int,S = ''):
    if len(S) == n:
        print(S)
        return
    if S == '':
        esLuglioBack(n,'a')
        esLuglioBack(n,'b')
        esLuglioBack(n,'c')

    else:
        if S[-1] == 'a':
            esLuglioBack(n,S+'b')
        elif len(S) > 1 and S[-2] == 'a':
            esLuglioBack(n,S+'b')
        else: 
            esLuglioBack(n,S+'b')
            esLuglioBack(n,S+'c')
            if len(S) < n-2:
                esLuglioBack(n,S+'a')
                
         
def esLuglioNumZeri(n,k):
    sol = [0]*n     
    esLuglioNumZeriBack(0,n,k,0,False,sol)    
                
def esLuglioNumZeriBack(i,n,k,tot,inserito,sol):
    if i == n:
        print(sol)
        return
    sol[i] = 0
    if tot+1 == k:
        esLuglioNumZeriBack(i+1,n,k,tot+1,True,sol)
    else:
        esLuglioNumZeriBack(i+1,n,k,tot+1,inserito,sol)
    if inserito or n-(i+1) >= k:
        sol[i] = 1
        esLuglioNumZeriBack(i+1,n,k,0,inserito,sol)
        
        
def contazerouno(s):
    T = [0]*len(s)
    cntz = 0
    for i in range(len(s)):
        if s[i]=='0':
            cntz+=1
        elif s[i]=='1':
            if cntz!=0:
                T[i]=cntz
    return sum(T)

def contazerounoDin(s):
    T = [0]*len(s)
    cntz = 0
    lastOne = 0
    for i in range(len(s)):
        if s[i]=='0':
            T[i]=T[lastOne]
            cntz+=1
        elif s[i]=='1':
            if cntz!=0:
                T[i]=cntz+T[lastOne]
                lastOne = i
    return T[-1]

def contazerounowtf(s):
    T = [0]*len(s)
    cntz = 0 if s[0] == '1' else 1
    for i in range(1,len(s)):
        if s[i]=='0':
            T[i]=T[i-1]
            cntz+=1
        elif s[i]=='1':
            if cntz!=0:
                T[i]=cntz+T[i-1]
    return T[-1]

def contazerounoMonti(s):
    n = len(s)
    t = [[0,0] for _ in range(n)]
    if s[0] == '0':
        t[0][0] = 1
    for i in range(1,n):
        if s[i] == '0':
            t[i][0] = t[i-1][0] + 1
            t[i][1] = t[i-1][1]
        else:
            t[i][0] = t[i-1][0]
            t[i][1] = t[i-1][1] + t[i-1][0]
    return t[n-1][1]

def contazerounoNoAr(s):
    cntz = 0
    result = 0
    for char in s:
        if char == '0':
            cntz += 1
        elif char == '1':
            result += cntz
    return result

def discesa(M:list[list[int]]):
    n = len(M)
    T = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        T[0][i] = M[0][i]
    for y in range(1,n):
        for x in range(n):
            if x == 0:
                T[y][x] = max(T[y-1][x],T[y-1][x+1]) + M[y][x]
            if x == n-1:
                T[y][x] = max(T[y-1][x],T[y-1][x-1]) + M[y][x]
            else:
                T[y][x] = max(T[y-1][x],T[y-1][x+1],T[y-1][x-1]) + M[y][x]
    return max(T[-1])



if __name__ == "__main__":
    #es3_aprile_2020(2)
    #es3_Luglio_2022(3)
    #es2Back(3,0,0,[])
    #esLuglioBack(4)
    #esLuglioNumZeri(4,2)
    #print(contazerouno('010010'))
    #print(contazerouno('1110100'))
    #print(contazerounoMonti('1110100'))
    #print(contazerounoDin('010010'))
    #print(contazerounoDin('1110100'))
    #print(contazerounoNoAr('010010'))
    #print(contazerounoNoAr('1110100'))
    #print(contazerounowtf('010010'))
    #print(contazerounowtf('1110100'))
    #print(contazerounowtf('0110'))
    M = [[12,10,3,14,9],
         [0,1,13,15,13],
         [8,10,1,2,7],
         [7,11,10,5,7],
         [18,4,6,10,0]]
    
    print(discesa(M))