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
        original_input.parseInfile()                             # load the A,B,C and matrix information
        followup_ts = self.generateFollowupTestCase(original_input, mr)

    def generateFollowupTestCase(self, original_input, mr):
        ts = TestCase()
        followup_infile = "{}_{}".format(self.original_ts.input, mr)
        followup_outfile = "{}_{}".format(self.original_ts.output, mr)

        ts.setInputOutput(followup_infile, followup_outfile)
        followup_input = self.getExpectedMatrix(original_input)
        followup_input.setInfile(followup_infile)
        followup_input.writeInfile()
        return ts

    def assertViolation(self, exp_output, followup_output):
        if operator.eq(exp_output.count, followup_output.count):
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
        expected_output.count = original_output.count
        return expected_output

    def getResults(self, ts):
        result = Output(ts.output)
        result.parse()
        return result

    def executeTestCase(self, ts):
        self.executor.setInputOutputNames(ts.infile, ts.outfile, ts.outtree)
        self.executor.executeDnapars()

    def getExpectedMatrix(self, original_input):
        return original_input

    def setKilledMutantsTable(self, table):
        self.table = table


class MR1(MR):
    # 随机选取语句, 大小写转换
    def __init__(self):
        super(MR1, self).__init__()

    def getExpectedMatrix(self, original_input):
        followup_input = copy.deepcopy(original_input)
        sample = random.sample(followup_input.lines, math.ceil(len(followup_input.lines) * 0.5))
        for i in sample:
            index = followup_input.lines.index(i)
            followup_input.lines[index] = followup_input.lines[index].swapcase()
        return followup_input


class MR2(MR):
    def __init__(self):
        super(MR2, self).__init__()

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
        return followup_input


class MR3(MR):
    def __init__(self):
        super(MR3, self).__init__()

    def getExpectedMatrix(self, original_input):
        followup_input = copy.deepcopy(original_input)
        sample = random.sample(followup_input.lines, math.ceil(len(followup_input.lines) * 0.5))
        for i in sample:
            index = followup_input.lines.index(i)
            followup_input.lines[index] = ';' + followup_input.lines[index]
        return followup_input

    def assertViolation(self, exp_output, followup_output):
        for i in range(len(followup_output.count)):
            if followup_output.count[i] > exp_output.count[i]:
                return True
        return False
    # def getExpectedOutput(self, original_output):
    #     expected_output = Output(original_output.output_name)
    #     expected_output.value = int(original_output.value) * 2
    #     return expected_output


class MR4(MR):
    # MR1-2
    def __init__(self):
        super(MR4, self).__init__()

    def getExpectedMatrix(self, original_input):
        followup_input = copy.deepcopy(original_input)

        sample = random.sample(followup_input.lines, math.ceil(len(followup_input.lines) * 0.5))
        for i in sample:
            index = followup_input.lines.index(i)
            followup_input.lines[index] = followup_input.lines[index].swapcase()

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


class MR5(MR):
    # MR2-1
    def __init__(self):
        super(MR5, self).__init__()

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
            ffollowup_input.lines[index] = ffollowup_input.lines[index].swapcase()

        return ffollowup_input


class MR6(MR):
    # MR1-3
    def __init__(self):
        super(MR6, self).__init__()

    def getExpectedMatrix(self, original_input):
        followup_input = copy.deepcopy(original_input)
        sample = random.sample(followup_input.lines, math.ceil(len(followup_input.lines) * 0.5))
        for i in sample:
            index = followup_input.lines.index(i)
            followup_input.lines[index] = followup_input.lines[index].swapcase()

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


class MR7(MR):
    # MR3-1
    def __init__(self):
        super(MR7, self).__init__()

    def getExpectedMatrix(self, original_input):
        followup_input = copy.deepcopy(original_input)
        sample = random.sample(followup_input.lines, math.ceil(len(followup_input.lines) * 0.5))
        for i in sample:
            index = followup_input.lines.index(i)
            followup_input.lines[index] = ';' + followup_input.lines[index]
        ffollowup_input = copy.deepcopy(followup_input)
        sample = random.sample(ffollowup_input.lines, math.ceil(len(ffollowup_input.lines) * 0.5))
        for i in sample:
            index = ffollowup_input.lines.index(i)
            ffollowup_input.lines[index] = ffollowup_input.lines[index].swapcase()

        return ffollowup_input

    def assertViolation(self, exp_output, followup_output):
        for i in range(len(followup_output.count)):
            if followup_output.count[i] > exp_output.count[i]:
                return True
        return False


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


# class MR10(MR):
#     # 打乱顺序
#     def __init__(self):
#         super(MR10, self).__init__()
#
#     def getExpectedMatrix(self, original_input):
#         followup_input = copy.deepcopy(original_input)
#         random.shuffle(followup_input.lines)
#         return followup_input


class MR10(MR):
    def __init__(self):
        super(MR10, self).__init__()

    def getExpectedMatrix(self, original_input):
        followup_input = copy.deepcopy(original_input)
        if not '\n' in followup_input.lines[-1]:
            followup_input.lines[-1] += '\n'
        sample = random.sample(followup_input.lines, math.ceil(len(followup_input.lines) * 0.1))
        for i in sample:
            followup_input.lines.append(i)
        return followup_input

    def assertViolation(self, exp_output, followup_output):
        for i in range(len(followup_output.count)):
            if followup_output.count[i] < exp_output.count[i]:
                return True
        return False


class MR11(MR):
    def __init__(self):
        super(MR11, self).__init__()

    def getExpectedMatrix(self, original_input):
        followup_input = copy.deepcopy(original_input)
        if len(followup_input.lines) <= 1:
            return followup_input
        else:
            sample = random.sample(followup_input.lines, math.ceil(len(followup_input.lines) * 0.1))  # math.ceil向上取整
            for i in sample:
                followup_input.lines.remove(i)
            return followup_input

    def assertViolation(self, exp_output, followup_output):
        for i in range(len(followup_output.count)):
            if followup_output.count[i] > exp_output.count[i]:
                return True
        return False