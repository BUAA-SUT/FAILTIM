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
    firstdir = 'D:/程序/博士/MT/metamorphic-testing-master/NumberUtil_main/TestCases/'  # 要复制文件所在路径
    tardir = './input/'  # 想要复制到的路径
    pathdir = os.listdir(firstdir)  # 获取所在路径下的所有文件
    path = []
    for path2 in pathdir:
        path.append(firstdir + path2)
    file = open(path[0], 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        with open(tardir + "input{}".format(i), "w") as f:
            start = lines[i].index('(')
            end = lines[i].index(')', start + 1)
            str = lines[i][start+1: end]
            f.writelines(str)

    # for i in range(56):
    #     with open("./input/input{}".format(i), "r") as f:
    #         lines = f.readlines()
    #     with open("./output/output{}_int".format(i), "w") as f:
    #         f.writelines(int(lines[0]))

