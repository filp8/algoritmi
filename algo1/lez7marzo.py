# algoritmo con H(1) perche dopo 100 torna sempre 1
def es1_1(n)->int:
      t = 0 
      n = abs(n)  # H(1)
      if n>100:   # H(1)
        return 1
      else:
        for i in range(n):
            t+=3
        return t
      
# algoritmo con H(n) perche dopo 100 incrementa t di 3 n volte 
def es1_2(n)->int:
      t = 0 
      n = abs(n)  # H(1)
      if n<100:   # H(n)
        return 1
      else:
        for i in range(n):
            t+=3
        return t


# caso ottimo quando il numero e dispari H(1)
# caso pessimo quando il numero e pari H(n)
def es2(n)->int:
        if n<0: n-=n
        while n>0:
            if n%2==1:return 1
            n-=2
        return 0


# complessita H(sqrt(n))
def es3(n):
    n=abs(n)
    x = r =0
    while x*x < n:
        x+=1
        r+=3*x
    return r









