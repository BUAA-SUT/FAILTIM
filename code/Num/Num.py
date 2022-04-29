# MR
import random
import re
from Execution import *
from TestCase import *
import itertools
import copy
import math
import operator
random.seed(1)

class MR():
    def __init__(self):
        self.name = self.__class__.__name__

    def setExecutor(self, executor):
        self.executor = executor

    def setTestCase(self, ts):
        self.original_ts = ts

    def getFollowInput(self, mr):
        original_input = Input(self.original_ts.input)
        original_input.parseInfile()
        original_output = Output(self.original_ts.output)
        original_output.parse()                             # load the A,B,C and matrix information
        followup_ts = self.generateFollowupTestCase(original_input, original_output, mr)

    def generateFollowupTestCase(self, original_input, original_output, mr):
        ts = TestCase()
        followup_infile = "{}_{}".format(self.original_ts.input, mr)
        followup_outfile = "{}_{}".format(self.original_ts.output, mr)

        ts.setInputOutput(followup_infile, followup_outfile)
        followup_input = self.getExpectedMatrix(original_input, original_output)
        followup_input.setInfile(followup_infile)
        followup_input.writeInfile()
        return ts

    def assertViolation(self, exp_output, followup_output):
        if int(followup_output.lines[0]) == int(exp_output.lines[0]):
            return False
        else:
            return True

    def strictassertViolation(self, exp_output, followup_output):
        for i in range(len(exp_output.lines)):
            if not exp_output.lines[i] == followup_output.lines[i]:
                return True
        return False

    def getExpectedOutput(self, original_output):
        expected_output = Output(original_output.output_name)
        expected_output.lines = original_output.lines
        return expected_output

    def getResults(self, ts):
        result = Output(ts.output)
        result.parse()
        return result

    def executeTestCase(self, ts):
        self.executor.setInputOutputNames(ts.infile, ts.outfile, ts.outtree)
        self.executor.executeDnapars()

    def getExpectedMatrix(self, original_input, original_output):
        return original_input

    def setKilledMutantsTable(self, table):
        self.table = table


class MR1(MR):
    # 加法
    def __init__(self):
        super(MR1, self).__init__()

    def getExpectedMatrix(self, original_input, original_output):
        followup_input = copy.deepcopy(original_output)
        # 加上标识符
        if "0x" in original_input.lines[0] or "0X" in original_input.lines[0]:
            num = int(original_output.lines[0])
            followup_input.lines[0] = hex(num + 1)
            # followup_input.lines[0] = original_input.lines[0][0:2] + followup_input.lines[0]
        elif "#" in original_input.lines[0]:
            num = int(original_output.lines[0])
            followup_input.lines[0] = hex(num + 1)
            # followup_input.lines[0] = original_input.lines[0][0] + followup_input.lines[0]
        elif '0' == original_input.lines[0][0]:
            num = int(original_output.lines[0])
            followup_input.lines[0] = oct(num + 1)
            # 末尾加字符
            if original_input.lines[0][-1] == "L" or original_input.lines[0][-1] == "l":
                followup_input.lines[0] = followup_input.lines[0] + original_input.lines[0][-1]
            # 去掉o
            if 'o' in followup_input.lines[0]:
                followup_input.lines[0] = followup_input.lines[0].replace('o', '')
        else:
            followup_input.lines[0] = str(int(original_output.lines[0]) + 1)
            # 末尾加字符
            if original_input.lines[0][-1] == "L" or original_input.lines[0][-1] == "l":
                followup_input.lines[0] = followup_input.lines[0] + original_input.lines[0][-1]
        return followup_input

    def assertViolation(self, exp_output, followup_output):
        if int(followup_output.lines[0]) == int(exp_output.lines[0]) + 1:
            return False
        else:
            return True


class MR2(MR):
    # 减法
    def __init__(self):
        super(MR2, self).__init__()

    def getExpectedMatrix(self, original_input, original_output):
        followup_input = copy.deepcopy(original_output)
        # 加上标识符
        if "0x" in original_input.lines[0] or "0X" in original_input.lines[0]:
            num = int(original_output.lines[0])
            followup_input.lines[0] = hex(num - 1)
            # followup_input.lines[0] = original_input.lines[0][0:2] + followup_input.lines[0]
        elif "#" in original_input.lines[0]:
            num = int(original_output.lines[0])
            followup_input.lines[0] = hex(num - 1)
            # followup_input.lines[0] = original_input.lines[0][0] + followup_input.lines[0]
        elif '0' == original_input.lines[0][0]:
            num = int(original_output.lines[0])
            followup_input.lines[0] = oct(num - 1)
            # 末尾加字符
            if original_input.lines[0][-1] == "L" or original_input.lines[0][-1] == "l":
                followup_input.lines[0] = followup_input.lines[0] + original_input.lines[0][-1]
            # 去掉o
            if 'o' in followup_input.lines[0]:
                followup_input.lines[0] = followup_input.lines[0].replace('o', '')
        else:
            followup_input.lines[0] = str(int(original_output.lines[0]) - 1)
            # 末尾加字符
            if original_input.lines[0][-1] == "L" or original_input.lines[0][-1] == "l":
                followup_input.lines[0] = followup_input.lines[0] + original_input.lines[0][-1]
        return followup_input

    def assertViolation(self, exp_output, followup_output):
        if int(followup_output.lines[0]) == int(exp_output.lines[0]) - 1:
            return False
        else:
            return True

class MR3(MR):
    # 乘法
    def __init__(self):
        super(MR3, self).__init__()

    def getExpectedMatrix(self, original_input, original_output):
        followup_input = copy.deepcopy(original_output)
        # 加上标识符
        if "0x" in original_input.lines[0] or "0X" in original_input.lines[0]:
            num = int(original_output.lines[0])
            followup_input.lines[0] = hex(num * 2)
            # followup_input.lines[0] = original_input.lines[0][0:2] + followup_input.lines[0]
        elif "#" in original_input.lines[0]:
            num = int(original_output.lines[0])
            followup_input.lines[0] = hex(num * 2)
            # followup_input.lines[0] = original_input.lines[0][0] + followup_input.lines[0]
        elif '0' == original_input.lines[0][0]:
            num = int(original_output.lines[0])
            followup_input.lines[0] = oct(num * 2)
            # 末尾加字符
            if original_input.lines[0][-1] == "L" or original_input.lines[0][-1] == "l":
                followup_input.lines[0] = followup_input.lines[0] + original_input.lines[0][-1]
            # 去掉o
            if 'o' in followup_input.lines[0]:
                followup_input.lines[0] = followup_input.lines[0].replace('o', '')
        else:
            followup_input.lines[0] = str(int(original_output.lines[0]) * 2)
            # 末尾加字符
            if original_input.lines[0][-1] == "L" or original_input.lines[0][-1] == "l":
                followup_input.lines[0] = followup_input.lines[0] + original_input.lines[0][-1]
        return followup_input

    def assertViolation(self, exp_output, followup_output):
        if int(followup_output.lines[0]) == int(exp_output.lines[0]) * 2:
            return False
        else:
            return True


class MR4(MR):
    # 除法
    def __init__(self):
        super(MR4, self).__init__()

    def getExpectedMatrix(self, original_input, original_output):
        followup_input = copy.deepcopy(original_output)
        # 加上标识符
        if "0x" in original_input.lines[0] or "0X" in original_input.lines[0]:
            followup_input.lines[0] = hex(int(int(original_output.lines[0]) / 2))
        elif "#" in original_input.lines[0]:
            followup_input.lines[0] = hex(int(int(original_output.lines[0]) / 2))
        elif '0' == original_input.lines[0][0]:
            followup_input.lines[0] = oct(int(int(original_output.lines[0]) / 2))
            # 末尾加字符
            if original_input.lines[0][-1] == "L" or original_input.lines[0][-1] == "l":
                followup_input.lines[0] = followup_input.lines[0] + original_input.lines[0][-1]
            # 去掉o
            if 'o' in followup_input.lines[0]:
                followup_input.lines[0] = followup_input.lines[0].replace('o', '')
        else:
            followup_input.lines[0] = str(int(int(original_output.lines[0]) / 2))
            # 末尾加字符
            if original_input.lines[0][-1] == "L" or original_input.lines[0][-1] == "l":
                followup_input.lines[0] = followup_input.lines[0] + original_input.lines[0][-1]
        return followup_input

    def assertViolation(self, exp_output, followup_output):
        if int(followup_output.lines[0]) == int(int(exp_output.lines[0]) / 2):
            return False
        else:
            return True


class MR5(MR):
    # 转化为16进制
    def __init__(self):
        super(MR5, self).__init__()

    def getExpectedMatrix(self, original_input, original_output):
        followup_input = copy.deepcopy(original_output)
        if "0x" in original_input.lines[0] or "0X" in original_input.lines[0] or "#" in original_input.lines[0]:
            pass
        elif '0' == original_input.lines[0][0]:
            followup_input.lines[0] = hex(int(original_output.lines[0]))
        else:
            followup_input.lines[0] = hex(int(original_output.lines[0]))

        return followup_input


class MR6(MR):
    # 转化为8进制
    def __init__(self):
        super(MR6, self).__init__()

    def getExpectedMatrix(self, original_input, original_output):
        followup_input = copy.deepcopy(original_output)
        if "0x" in original_input.lines[0] or "0X" in original_input.lines[0] or "#" in original_input.lines[0]:
            followup_input.lines[0] = oct(int(original_output.lines[0]))
            followup_input.lines[0] = followup_input.lines[0].replace('o', '')
        elif '0' == original_input.lines[0][0]:
            pass
        else:
            followup_input.lines[0] = oct(int(original_output.lines[0]))
            followup_input.lines[0] = followup_input.lines[0].replace('o', '')
        return followup_input


class MR7(MR):
    # 转化为10进制
    def __init__(self):
        super(MR7, self).__init__()

    def getExpectedMatrix(self, original_input, original_output):
        followup_input = copy.deepcopy(original_output)
        if "0x" in original_input.lines[0] or "0X" in original_input.lines[0] or "#" in original_input.lines[0]:
            followup_input.lines[0] = str(int(original_output.lines[0]))
        elif '0' == original_input.lines[0][0]:
            followup_input.lines[0] = str(int(original_output.lines[0]))
        else:
            pass
        return followup_input

class MR8(MR):
    # MR2-3
    def __init__(self):
        super(MR8, self).__init__()

    def getExpectedMatrix(self, original_input):
        followup_input = copy.deepcopy(original_input)
        for i in range(len(followup_input.lines)):
            if ';' in followup_input.lines[i]:
                # 如果存在引号, 则不做调整
                if "\"" in followup_input.lines[i] or "\'" in followup_input.lines[i]:
                    continue
                # count = followup_input.lines[i].count("\"")
                # if count >= 2:
                #     start = followup_input.lines[i].index('\"')
                #     end = followup_input.lines[i].index('\"', start + 1)
                #     str = followup_input.lines[i][start: end+1]
                #     if ';' in str:
                #         continue
                index = followup_input.lines[i].index(';')
                followup_input.lines[i] = followup_input.lines[i][:index + 1] + '\n'
        ffollowup_input = copy.deepcopy(followup_input)
        sample = random.sample(ffollowup_input.lines, math.ceil(len(ffollowup_input.lines) * 0.5))
        for i in sample:
            index = ffollowup_input.lines.index(i)
            ffollowup_input.lines[index] = ';' + ffollowup_input.lines[index]

        return ffollowup_input

    def assertViolation(self, exp_output, followup_output):
        for i in range(len(followup_output.count)):
            if followup_output.count[i] > exp_output.count[i]:
                return True
        return False


class MR9(MR):
    # MR3-2
    def __init__(self):
        super(MR9, self).__init__()

    def getExpectedMatrix(self, original_input):
        followup_input = copy.deepcopy(original_input)
        sample = random.sample(followup_input.lines, math.ceil(len(followup_input.lines) * 0.5))
        for i in sample:
            index = followup_input.lines.index(i)
            followup_input.lines[index] = ';' + followup_input.lines[index]
        ffollowup_input = copy.deepcopy(followup_input)
        for i in range(len(ffollowup_input.lines)):
            if ';' in ffollowup_input.lines[i]:
                # 如果存在引号, 则不做调整
                if "\"" in ffollowup_input.lines[i] or "\'" in ffollowup_input.lines[i]:
                    continue
                # count = followup_input.lines[i].count("\"")
                # if count >= 2:
                #     start = followup_input.lines[i].index('\"')
                #     end = followup_input.lines[i].index('\"', start + 1)
                #     str = followup_input.lines[i][start: end+1]
                #     if ';' in str:
                #         continue
                index = ffollowup_input.lines[i].index(';')
                ffollowup_input.lines[i] = ffollowup_input.lines[i][:index + 1] + '\n'

        return ffollowup_input

    def assertViolation(self, exp_output, followup_output):
        for i in range(len(followup_output.count)):
            if followup_output.count[i] > exp_output.count[i]:
                return True
        return False


class CompositionMR(MR):
    def __init__(self):
        super(CompositionMR, self).__init__()
        self.MRs = [MR7(), MR4()]
        self.name = self.getName()
        self.MRs.reverse()

    def setMRs(self, mr_list):
        self.MRs = mr_list
        self.name = self.getName()
        self.MRs.reverse()

    def getName(self):
        return ''.join([mr.__class__.__name__ for mr in self.MRs])

    def getExpectedOutput(self, original_output):
        for mr in self.MRs:
            original_output = mr.getExpectedOutput(original_output)
        return original_output

    def getExpectedMatrix(self, original_input):
        followup_input = copy.deepcopy(original_input)
        for mr in self.MRs:
            followup_input = mr.getExpectedMatrix(followup_input)
        return followup_input

    def assertViolation(self, exp_output, followup_output):
        return self.MRs[-1].assertViolation(exp_output, followup_output)


def getCMRTestMR5List():
    mr_list = [[MR5(),MR1()],[MR5(),MR2()],[MR5(),MR3()],[MR5(),MR4()],[MR5(),MR6()]]
    cmr_list = []
    for cmr_c in mr_list:
        temp = CompositionMR()
        temp.setMRs(cmr_c)
        cmr_list.append(temp)
    return cmr_list


def getCMRPermutationsList(mr_list):
    cmr_list = []
    cmr_permutations = itertools.permutations(mr_list, 2)
    for cmr_p in cmr_permutations:
        temp = CompositionMR()
        temp.setMRs(list(cmr_p))
        cmr_list.append(temp)
    return cmr_list


def recordResult(file_name, mutants_list, mr_list):
    result = open("../results/"+file_name,"w")
    temp = [v+"\t" for v in mutants_list]
    temp.insert(0, "\t")
    temp.append("\n")
    for cmr in mr_list:
        temp.append("{}\t".format(cmr.name))
        for v in mutants_list:
            temp.append(str(cmr.table[v])+"\t")
        temp.append("\n")
    result.writelines(temp)
    result.close()


def MetamorphicTesting(executor, mutants_list, mr_list, test_case, num_of_samples):
    for mr in mr_list:
        table = dict(zip(mutants_list, [0]*len(mutants_list)))
        for i in range(num_of_samples):
            mr.setTestCase(test_case)
            mr.original_ts.setInputOutput("infile_{}".format(i), "outfile_{}".format(i), "outtree_{}".format(i))
            mr.original_ts.generateRandomTestcase()
            mr.setExecutor(executor)
            for v in mutants_list:
                executor.setVersion(v)
                mr.process()
                if mr.isViolate:
                    table[v] = table[v]+1
        mr.setKilledMutantsTable(table)


def testSingleMR():
    ts_1 = TestCase()
    dna = Dnapars()
    num_of_samples = 10  # 测试用例个数
    result_to_save_1 = "SMR_1000_part1.result"
    result_to_save_2 = "SMR_1000_part2.result"
    mr_list_1 = [MR1(), MR2(), MR3(), MR4(), MR6(), MR7()]
    mr_list_2 = [MR5()]
    mutants_list = ["v0.exe", "v1.exe", "v2.exe", "v3.exe", "v4.exe", "v5.exe",
                    "v6.exe", "v7.exe", "v8.exe", "v9.exe", "v10.exe"]
    MetamorphicTesting(dna, mutants_list, mr_list_1, ts_1, num_of_samples)
    recordResult(result_to_save_1, mutants_list, mr_list_1)
    recordResult(result_to_save_2, mutants_list, mr_list_2)


if __name__ == "__main__":
    myenv = MyEnv()
    myenv.CreateWorkingDirs()
    testSingleMR()
