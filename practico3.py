def ilagrange(x,y,z):
    w = []
    for k in z:
        suma = 0 
        for i in range(len(x)):
            prod = 1
            for j in x:
                if x[i] != j:
                    prod = prod * (k - j)/(x[i]-j)
            suma = suma + prod * y[i]
        w.append(suma)
    return w

x = [-2, 0, 2]
y = [4, 0, 4]
z = [-5, 0, 3]

#print(ilagrange(x, y, z))

def inewton(x, y):
    n = len(x) - 1
    suma = 0
    for i in range(n):
        suma = suma +pyth
    dif_divididas(x, y)
    
def dif_divididas(x, y):
    coefs = []
    n = len(x)
    for i in range(n):
        coefs.append(y[:n-i])

    for i in range(1, n):
        for j in range(n-i):
            coefs[i][j] = coefs[i-1][j+1] - coefs[i-1][j]
            coefs[i][j] = coefs[i][j]/(x[j+i] - x[j])
    return [x[0] for x in coefs]
x = [3, 1, 5, 6]
y = [1, -3, 2, 4]

print(dif_divididas(x, y))

