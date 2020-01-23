def primes(n):
    P = []
    f = []
    for i in range(n+1):
        if i > 2 and i%2 == 0:
            f.append(1)
        else:
            f.append(0)
    i = 3
    while i*i <= n:
        if f[i] == 0:
            j = i*i
            print(j)
            while j <= n:
                f[j] = 1
                j += i+i
                print(j)
        i += 2
 
    P.append(2)
    for x in range(3,n+1,2):
        if f[x] == 0:
            P.append(x)
 
    return P
 
n = 100   #100以内的素数
P = primes(n)
# print(P)