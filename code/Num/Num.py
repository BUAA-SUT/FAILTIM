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


class MR:
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

    def getExpectedMatrix(self, original_input, original_output):
        followup_input = copy.deepcopy(original_input)
        for i in range(len(followup_input.lines)):
            if ';' in followup_input.lines[i]:
                # 如果存在引号, 则不做调整
                if "\"" in followup_input.lines[i] or "\'" in followup_input.lines[i]:
                    continue
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

    def getExpectedMatrix(self, original_input, original_output):
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
                index = ffollowup_input.lines[i].index(';')
                ffollowup_input.lines[i] = ffollowup_input.lines[i][:index + 1] + '\n'

        return ffollowup_input

    def assertViolation(self, exp_output, followup_output):
        for i in range(len(followup_output.count)):
            if followup_output.count[i] > exp_output.count[i]:
                return True
        return False









