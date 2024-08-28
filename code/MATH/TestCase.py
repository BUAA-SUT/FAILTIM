import random
from Execution import *
#from MRs import *

class TestCase():
    def __init__(self):
        pass

    def setInputOutput(self, input_name, output_name):
        self.input = input_name
        self.output = output_name

    def generateInput(self):
        self.A = 1
        self.B = 2
        self.matrix = self.getMatrix()
        myInput = Input(self.input)
        myInput.setMatrix(self.A, self.B, self.matrix)
        myInput.writeInfile()


    def setTestCase(self, A, B, matrix):
        self.A = A
        self.B = B
        self.matrix = matrix

    def getMatrix(self):
        matrix = []
        for row in range(self.A):
            temp = []
            for col in range(self.B):
                temp.append(str(random.randint(0, 9)))
            matrix.append(temp)
        return matrix



