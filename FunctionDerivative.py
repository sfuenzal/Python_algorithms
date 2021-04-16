import numpy as np
import matplotlib.pyplot as plt

class FuntionDerivative:
    def __init__(self, xi, xf, n):
        self.xi = xi
        self.xf = xf
        self.n = n
    
    def f(self, x):
        self.x = x
        return np.sin(x)
    
    def fprima(self, x):
        self.x = x
        self.h = 10**(-6)
        return (self.f(x + self.h) - self.f(x))/self.h
    
    def Plotf(self):
        self.xx = np.linspace(self.xi, self.xf, self.n)
        plt.figure(figsize = (10, 8))
        plt.plot(self.xx, self.f(self.xx), label = r'$f(x) = \sin(x)$')
        plt.xlabel(r'$x$', fontsize = 18)
        plt.ylabel(r'$f(x)$', fontsize = 18)
        plt.title(r'Initial function', fontsize = 20)
        plt.legend(loc = 'best', fontsize = 16)
        plt.grid()
    
    def Plotfprima(self):
        self.xx = np.linspace(self.xi, self.xf, self.n)
        plt.figure(figsize = (10, 8))
        plt.plot(self.xx, self.fprima(self.xx), label = r'$f(x) = \cos(x)$')
        plt.xlabel(r'$x$', fontsize = 18)
        plt.ylabel(r'$f^\prime(x)$', fontsize = 18)
        plt.title(r'Function derivative', fontsize = 20)
        plt.legend(loc = 'best', fontsize = 16)
        plt.grid()

    def ShowPlots(self):
        plt.show()

number_of_points = int(input('Please enter the number of points to make the plots of the function and its derivative: '))
initial_point_interval = float(input('Please enter the initial point of the interval to make the plots of the function and its derivative: '))
final_point_interval = float(input('Please enter the final point of the interval to make the plots of the function and its derivative: '))

obj1 = FuntionDerivative(initial_point_interval, final_point_interval, number_of_points)
obj1.Plotf()
obj1.Plotfprima()
obj1.ShowPlots()