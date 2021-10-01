import numpy as np
import nonlinear

def rk4(x0, y, x1, n):
    """Beregner y(x1) gitt en start x0 og et antall steg n"""
    h = (x1-x0)/n

    for i in range(n):
        k1 = ode(x0,y)
        k2 = ode(x0+0.5*h, y+0.5*h*k1)
        k3 = ode(x0+0.5*h, y+0.5*h*k2)
        k4 = ode(x0+h, y+h*k3)
        y = y+h/6*(k1+2*k2+2*k3+k4)
        x0 = x0 + h
    return y



def eulerbaklengs(x0, y, x1, n):
    """Beregner y(x1) gitt en start x0 og et antall steg n. Bruker 
    euler fram og sekant fra første oppgave til å finne y(x+1)"""
    h = (x1-x0)/n

    for i in range(n):
        ycurr = y
        yeulerfram = y + ode(x0-h, ycurr)
        def f(x):
            return yeulerfram - y + ode(x-h, ycurr)
        y = y + h*ode(x0, nonlinear.sekant(x0-h, x0, f)[1])
        x0 = x0 + h
    return y

if __name__ == "__main__":
    def ode(x,y):
        return np.e**(-y)*(2*x-4)

    print(f"Runge-Kutta orden 4:\n{rk4(5, 0, 10, 1000):.10f}")
    print(f"Euler baklengs:\n{eulerbaklengs(5, 0, 10, 1000):.10f}")
