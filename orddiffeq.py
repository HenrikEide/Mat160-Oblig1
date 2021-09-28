import numpy as np

def rk4(x0, y, xslut, n):
    t = 5
    h = 5/n

    for i in n:
        k1 = f(t,y)
        k2 = f(t+0.5*h, y+0.5*h*k1)
        k3 = f(t+0.5*h, y+0.5*h*k2)
        k4 = f(t+h, y+h*k3)
        y = y+h/6*(k1+2*k2+2*k3+k4)
        t = i*h
    return y

if __name__ == "__main__":
    def f(t,y):
        np.e**(-y)*(2*t-4)
    
