class TrapezoidalMethod:
    def __init__(self, ll, ul, sub):
        self.ll = ll
        self.ul = ul
        self.sub = sub
    
    def InputFunction(self, x):
        self.x = x
        return x**2
    
    def TrapezoidalMethodIntegrator(self):
        self.step_size = abs(self.ul - self.ll)/self.sub
        self.integration_value = self.InputFunction(self.ll) + self.InputFunction(self.ul)
        self.i = 1

        while True:
            self.k = self.ll + self.i * self.step_size
            self.integration_value = self.integration_value + 2 * self.InputFunction(self.k)
            
            if (self.i < self.sub):
                break

        self.integration_value = self.integration_value * self.step_size/2.

        print('Value of the inegral = ' + str(self.integration_value))

lower_limit = float(input('Please enter the lower limit integral: '))
upper_limit = float(input('Please enter the upper limit of the integral: '))
number_of_subintervals = int(input('Please enter the number of subintervals: '))

obj1 = TrapezoidalMethod(lower_limit, upper_limit, number_of_subintervals)
obj1.TrapezoidalMethodIntegrator()

