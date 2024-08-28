import re
import os
import re

class MyEnv():
    def __init__(self):
        self.workspace_dir = "."
        self.inputs_dir = "/Applications/work/data/MT/FAILTIM/Result/MATH/input"
        self.outputs_dir = "/Applications/work/data/MT/FAILTIM/Result/MATH/output"
        self.results_dir = self.workspace_dir + "/result"

    def CreateWorkingDirs(self):
        self.checkDir(self.inputs_dir)
        self.checkDir(self.outputs_dir)
        self.checkDir(self.results_dir)

    def checkDir(self, dir):
        if not os.path.exists(dir):
            os.makedirs(dir)
            print("created dir of {}".format(dir))

class Input():
    def __init__(self, infile):
        self.setInfile(infile)

    def setMatrix(self, A, B, matrix):
        self.A = A
        self.B = B
        self.matrix = matrix

    def parseInfile(self):
        self.tokens = self.getTokens()
        self.matrix= self.getMatrix()
        # self.A = self.tokens[0][0]
        # self.B = self.tokens[0][1]

    def getInput(self):
        return (self.A, self.B, self.matrix)

    def getTokens(self):
        tokens = []
        file = open(self.infile, "r")
        lines = file.readlines()
        file.close()
        for l in lines:
            tokens.append(l.split(','))
        return tokens

    def getInfile(self):
        return self.infile

    def setInfile(self, infile):
        env = MyEnv()
        self.infile = env.inputs_dir+"/{}".format(infile)

    def getMatrix(self):
        matrix = self.tokens
        return matrix

    def writeInfile(self):
        temp_lines = [','.join(col) for col in self.matrix]
        new_lines = []
        for i in range(len(self.matrix)):
            new_lines.append(temp_lines[i])
        temp_file = open(self.infile, "w")
        temp_file.writelines(new_lines)
        temp_file.close()


class Output:
    def __init__(self, output):
        env = MyEnv()
        self.output_name = env.outputs_dir + "/{}".format(output)

    def parse(self):
        self.value = self.getValue()

    def setResults(self, value):
        self.value = value


    def getValue(self):
        file = open(self.output_name, 'r')
        lines = file.readlines()
        value = ''.join(lines)
        value = value.replace('\n', '')
        return value

