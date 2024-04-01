from sympy import *
def conj1(n,j,w):
    som1 = som2 = 0
    z = (j-w)/n
    if z == int(z):
        z = int(z)
    for a in range(j,j+n):
        som1 += a
    for a in range(w,w+n):
        som2 += a
    k = som1-som2
    l = int((n**2)*z )
    if k == l:
        h = True
    else:
        h = False
    return k,l,h
def conj2(k,j,p):
    med = 0
    som1=0
    pa = 0
    if p == 'impar':
        n = 2*k-1
        Ann = (n+1)/2
        h = (j + (j+n-1))/2
    elif p == 'par':
        n = 2 * k
        Ann = (n+2)/2
        h = (j + (j+n-1)+1)/2
        if h == int(h):
            h = int(h)
        pa = n/2
    for a in range(j,j+n):
        som1 += a
        if a-j+1 == Ann:
            med = a
    l = (pa + som1)/n
    if l == int(l):
        l = int(l)
    if l == med and h == med:
        m = True
    else:
        m = False
    return l,h,med,m
def conj3(k,p):
    pa = 0
    h = 0
    if p == 'impar':
        j = 2*k-1
    elif p == 'par':
        j = 2*k
        pa=k
    l = j**2
    for a in range(k,k+j):
        h+=a
    h+=pa
    if h == l:
        m = True
    else: 
        m = False
    return l, h, m 
def conj4(k,a):
    h = (a**k - 1)**k+(a**k-1)**(k+1)
    j = h**(1/k)
    if int(round(j))**k == h:
        j = int(round(j))
    l = j**k
    if h == 
    return h,l,j

    
    
    


exp2 = conj4(6,13)

print(exp2)