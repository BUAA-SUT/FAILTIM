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


class Dnapars():
    def __init__(self):
        env = MyEnv()
        self.workspace = env.workspace_dir

    def setInputOutputNames(self, infile_name, outfile_name):
        self.infile = infile_name
        self.outfile = outfile_name

    def setVersion(self, version_num):
        self.version_num = version_num

    def executeDnapars(self):
        # exit_code = os.system("D:/程序/博士/MT/metamorphic-testing-master/tests/DnaparsTest-master/exe/run.sh {} {} {} {}".format
        #                       (self.version_num, self.infile, self.outfile, self.outtree))
        exit_code = os.system("D:/程序/博士/MT/metamorphic-testing-master/tests/DnaparsTest-master/exe/run1.sh")
        if not exit_code == 0:
            print("error")

if __name__ == "__main__":
    dna = Dnapars()

