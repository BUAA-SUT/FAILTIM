import random
from Execution import *
# from MRs import *
import os, random, shutil
import codecs
random.seed(1)

class TestCase():
    def __init__(self):
        pass

    def setInputOutput(self, input_name, output_name):
        self.input = input_name
        self.output = output_name

    # def generateInput(self):
    #     self.A = 1
    #     self.B = 2
    #     self.matrix = self.getMatrix()
    #     myInput = Input(self.input)
    #     myInput.setMatrix(self.A, self.B, self.matrix)
    #     myInput.writeInfile()
    #
    # def setTestCase(self, A, B, matrix):
    #     self.A = A
    #     self.B = B
    #     self.matrix = matrix
    #
    # def getMatrix(self):
    #     matrix = []
    #     for row in range(self.A):
    #         temp = []
    #         for col in range(self.B):
    #             temp.append(str(random.randint(0, 9)))
    #         matrix.append(temp)
    #     return matrix


if __name__ == "__main__":
    firstdir = 'D:/程序/博士/MT/P1/Siemens-suite-master/printtokens/inputs/'  # 要复制文件所在路径
    tardir = './inputs/'  # 想要复制到的路径
    pathdir = os.listdir(firstdir)  # 获取所在路径下的所有文件
    path = []
    for path2 in pathdir:
        path.append(firstdir + path2)
    sample = random.sample(path, 100)
    # sample[0] = 'D:/程序/博士/MT/P1/Siemens-suite-master/printtokens/inputs/newtst552.tst'
    for i in range(len(path)):
        # shutil.copyfile(sample[i], tardir + "input{}.txt".format(i))  # 复制操作
        file = open(path[i], 'r')
        lines = file.readlines()
        with open(tardir + "input{}".format(i), "w") as f:
            f.writelines(lines)

