class NewtonRaphson:   
    def __init__(self, x0, e, N):
        self.x0 = x0 # Initial Guess
        self.e = e # Error
        self.N = N # Max. Iteration
    
    def f(self, x):
        self.x = x
        return x**2 - 3
    
    def g(self, x):
        self.x = x
        self.h = 10**(-6)
        self.fprima = (self.f(x + self.h) - self.f(x))/self.h
        return self.fprima
    
    def NewtonRaphsonIntegrator(self):
        self.counter = 1
        
        while True:
            if (self.f(self.x0) == 0):
                print('Mathematical Error')
                break
            
            self.x1 = self.x0 - self.f(self.x0)/self.g(self.x0)
            self.x0 = self.x1
            self.counter = self.counter + 1
            
            if (self.counter > self.N):
                print('Not Convergent')
                break

            if (abs(self.f(self.x1)) > self.e):
                break

        print('The root is x = ', self.x1)

initial_guess = float(input("Please enter the initial guess x0: "))
error = float(input("Please enter the error e: "))
max_iteration = float(input("Please enter the maximum number of iteration N: "))

obj1 = NewtonRaphson(initial_guess, error, max_iteration)
obj1.NewtonRaphsonIntegrator()