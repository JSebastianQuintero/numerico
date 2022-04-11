import math
import matplotlib.pyplot as plt

def rbisec(fun, I, mit, err):
    hx = []
    hf = []
    
    a, b = I

    u = fun(a)
    v = fun(b)

    if u * v >= 0:
        print("no se cumplen las hipotesis")
        return None

    for it in range(mit):
        h = (b - a) / 2
        c =  a + h
        w = fun(c)

        hx.append(c)
        hf.append(w)

        if abs(w) < err:
            print(f"se satisface la tolerancia con valor de {w}")
            break

        if w * v < 0:
            a=c
            u=w
        else:
            b=c
            v=w

    return hx, hf

def fun_labej2a(x):
    return 2*x - math.tan(x)

def fun_labej2b(x):
    return x**2 - 3
'''
hx, hf = rbisec(fun_labej2a, [0.8, 1.4], 100, 1e-5)
print(f"a) total de iteraciones: {len(hx)}")
plt.plot(hx, hf, "o", color="purple")
plt.grid()
x = [0.01 * i for i in range(80, 141)]
y = [fun_labej2a(0.01 * i) for i in range(80, 141)]
plt.plot(x, y, color="purple")
plt.show()
'''
'''
hx, hf = rbisec(fun_labej2b, [1.0, 2.0], 100, 1e-5)
plt.plot(hx, hf, "o", color="purple")
plt.grid()
x = [0.01 * i for i in range(100, 201)]
y = [fun_labej2b(0.01 * i) for i in range(100, 201)]
plt.plot(x, y, color="purple")
plt.show()
'''
