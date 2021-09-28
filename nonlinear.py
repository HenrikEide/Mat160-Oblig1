import math
import numpy as np


def newton(x_0, maxErr = 0.0000000001) -> str:
    """Tilnærming til en rot og antall iterasjoner brukt 
    gitt et startpunkt x_0 samt en nøyaktighet maxErr"""
    x = x_0
    iter = 0

    while abs(f(x)) > maxErr:
        x -= f(x)/fd(x)
        iter += 1
    
    return f"{x:.10f} etter {iter} iterasjoner"

def sekant(x_0, x_1, maxErr = 0.0000000001):
    """Tilnærming til en rot og antall iterasjoner brukt 
    gitt to startpunkt x_0, x_1 samt en nøyaktighet maxErr"""
    iter = 0
    x_next = 0; x_curr = math.inf
    
    while abs(x_curr-x_next) > maxErr:
        iter += 1
        x_curr = (x_0*f(x_1)-x_1*f(x_0))/(f(x_1)-f(x_0))
        if f(x_0)*f(x_1) == 0:
            break
        x_0 = x_1
        x_1 = x_curr
        x_next = (x_0*f(x_1)-x_1*f(x_0))/(f(x_1)-f(x_0))
    return f"{x_0:.10f} etter {iter} iterasjoner"

def halvering(a, b, maxErr = 0.0000000001):
    iter = 0
    x = a
    while abs(f(x)) > maxErr:
        iter += 1
        x_last = x
        x = (a+b)/2
        if f(x)*f(b) < 0:
            a = x
        else:
            b = x
    return f"{(x+x_last)/2:.10f} etter {iter} iterasjoner"

if __name__ == "__main__":
    def f(x : int = 0) -> float:
        return x**3+10*math.cos(2*x)+math.log(x+11)

    def fd(x : int = 0) -> float:
        return 3*x**2-20*math.sin(2*x)+1/(x+11)
    
    print("Newtons metode:")
    print(newton(-0.9))
    print(newton(1))
    print(newton(2))

    print("\nSekantmetoden:")
    print(sekant(-1, -0.9))
    print(sekant(0.9, 1.1))
    print(sekant(1.6, 2))

    print("\nHalveringsmetoden")
    print(halvering(-0.9, -0.8))
    print(halvering(0.9, 1))
    print(halvering(1.8, 1.9))


