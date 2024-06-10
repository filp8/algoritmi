def count_occurrencies(A:list[int]):
    check = {}
    for n in A:
        if n in check:
            return True
        else:
            check[n] = 1
    return False


'''def merge_insertion(A,k,start,end,dim):
    if dim > k:
        m = (start+end)//2
        merge_insertion(A,k,start,m,m-start+1)
        merge_insertion(A,k,m+1,end,end-start)
        fondi(start,m,end)
    else:
        InsertionSort(A,start,end)'''

'''def fondi(start,m,end):
    i = start
    j = m+1
    B = []
    while i <= m and j <= end:
        if A[i] < A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1
    while i <= m:
        B.append(A[i])
        i += 1
    while j <= end:
        B.append(A[j])
        j += 1
    for i in range(start,end+1):
        A[i] = B[i-start]
        
def InsertionSort(A,start,end):
    for i in range(start+1,end+1):
        j = i
        while j > start and A[j] < A[j-1]:
            A[j],A[j-1] = A[j-1],A[j]
            j -= 1'''
            
def mergeSortIterative(A:list[int],k:int):
    n = len(A)
    l = 1
    while l < n:
        i = 0
        while i - l < n:
            fondi(i,i+l-1,i+2*l-1)
            i +=2
        l *= 2




if __name__ == "__main__":
    A = [1,2,3,1,5,6,7,8,9,10]
    print(count_occurrencies(A)) # False