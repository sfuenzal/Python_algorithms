import numpy as np

class InverseMatrixGaussJordan:
    def __init__(self, n):
        self.n = n
    
    def InputMatrix(self):
        self.i = 0
        self.j = 0
        self.A = np.zeros((self.n, 2*self.n))

        for self.i in range(self.n):
            for self.j in range(self.n):
                self.A[self.i][self.j] = float(input('Please enter the elements of the matrix: '))

        for self.i in range(self.n):
            for self.j in range(self.n):
                print( 'A[' + str(self.i) + ',' + str(self.j) + '] = ' + str(self.A[self.i][self.j]) )
    
    def AugmentIdentityMatrix(self):
        self.i = 0
        self.j = 0

        for self.i in range(self.n):
            for self.j in range(self.n):
                if (self.i == self.j):
                    self.A[self.i][self.j + self.n] = 1
                else:
                    self.A[self.i][self.j + self.n] = 0

    def GaussJordanElimination(self):
        self.i = 0
        self.j = 0
        self.k = 0

        for self.i in range(self.n):
            if (self.A[self.i][self.i] == 0):
                print('Mathematical Error')
                break
            
            for self.j in range(self.n):
                if (self.i != self.j):
                    self.ratio = self.A[self.j][self.i]/self.A[self.i][self.i]

                    for self.k in range(2*self.n):
                        self.A[self.j][self.k] = self.A[self.j][self.k] - self.ratio * self.A[self.i][self.k]

    def RowConversionOperation(self):
        self.i = 0
        self.j = 0

        for self.i in range(self.n):
            for self.j in range(self.n, 2*self.n):
                self.A[self.i][self.j] = self.A[self.i][self.j]/self.A[self.i][self.i]

    def DisplayInverseMatrix(self):
        self.i = 0
        self.j = 0
        
        for self.i in range(self.n):
            for self.j in range(self.n, 2*self.n):
                print( 'A^{-1}[' + str(self.i) + ',' + str(self.j) + '] = ' + str(self.A[self.i][self.j]) )

matrix_order = int(input('Please enter the order of the matrix square matrix: '))

obj1 = InverseMatrixGaussJordan(matrix_order)
obj1.InputMatrix()
obj1.AugmentIdentityMatrix()
obj1.GaussJordanElimination()
obj1.RowConversionOperation()
obj1.DisplayInverseMatrix()