# MR
import random
import re
from Execution import *
from TestCase import *
import itertools
import copy

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
        original_input.parseInfile()  # load the A,B,C and matrix information
        followup_ts = self.generateFollowupTestCase(original_input, mr)

    def generateFollowupTestCase(self, original_input, mr):
        ts = TestCase()
        followup_infile = "{}_{}.txt".format(self.original_ts.input[:-4], mr)
        followup_outfile = "{}_{}".format(self.original_ts.output, mr)

        ts.setInputOutput(followup_infile, followup_outfile)
        followup_input = self.getExpectedMatrix(original_input)
        followup_input.setInfile(followup_infile)
        followup_input.writeInfile()
        return ts

    def assertViolation(self, exp_output, followup_output):
        # try:
        if int(exp_output.value) == int(followup_output.value):
            return False
        else:
            return True
        # except:
        #     print(exp_output.value, followup_output.value)

    def getExpectedOutput(self, original_output):
        expected_output = Output(original_output.output_name)
        expected_output.value = original_output.value
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

    def __init__(self):
        super(MR1, self).__init__()

    def getExpectedMatrix(self, original_input):
        followup_input = copy.deepcopy(original_input)
        followup_input.matrix[0][0] = int(original_input.matrix[0][1])
        followup_input.matrix[0][1] = int(original_input.matrix[0][0])
        followup_input.matrix[0][0] = str(followup_input.matrix[0][0])
        followup_input.matrix[0][1] = str(followup_input.matrix[0][1])
        return followup_input


class MR2(MR):
    def __init__(self):
        super(MR2, self).__init__()

    def getExpectedMatrix(self, original_input):
        followup_input = copy.deepcopy(original_input)
        followup_input.matrix[0][0] = int(original_input.matrix[0][0])
        followup_input.matrix[0][1] = 2 * int(original_input.matrix[0][1])
        followup_input.matrix[0][0] = str(followup_input.matrix[0][0])
        followup_input.matrix[0][1] = str(followup_input.matrix[0][1])
        return followup_input

    def assertViolation(self, exp_output, followup_output):
        if int(followup_output.value) >= int(exp_output.value):
            return False
        else:
            return True


class MR3(MR):
    def __init__(self):
        super(MR3, self).__init__()

    def getExpectedMatrix(self, original_input):
        followup_input = copy.deepcopy(original_input)
        followup_input.matrix[0][0] = 2 * int(original_input.matrix[0][0])
        followup_input.matrix[0][1] = 2 * int(original_input.matrix[0][1])
        followup_input.matrix[0][0] = str(followup_input.matrix[0][0])
        followup_input.matrix[0][1] = str(followup_input.matrix[0][1])
        return followup_input

    def getExpectedOutput(self, original_output):
        expected_output = Output(original_output.output_name)
        expected_output.value = int(original_output.value) * 2
        return expected_output


class MR4(MR):
    # MR1-2
    def __init__(self):
        super(MR4, self).__init__()

    def getExpectedMatrix(self, original_input):
        followup_input = copy.deepcopy(original_input)
        ffollowup_input = copy.deepcopy(original_input)
        followup_input.matrix[0][0] = int(original_input.matrix[0][1])
        followup_input.matrix[0][1] = int(original_input.matrix[0][0])

        ffollowup_input.matrix[0][0] = int(followup_input.matrix[0][0])
        ffollowup_input.matrix[0][1] = 2 * int(followup_input.matrix[0][1])
        ffollowup_input.matrix[0][0] = str(ffollowup_input.matrix[0][0])
        ffollowup_input.matrix[0][1] = str(ffollowup_input.matrix[0][1])
        return ffollowup_input

    def assertViolation(self, exp_output, followup_output):
        if int(followup_output.value) >= int(exp_output.value):
            return False
        else:
            return True


class MR5(MR):
    # MR2-1
    def __init__(self):
        super(MR5, self).__init__()

    def getExpectedMatrix(self, original_input):
        followup_input = copy.deepcopy(original_input)
        ffollowup_input = copy.deepcopy(original_input)
        followup_input.matrix[0][0] = int(original_input.matrix[0][0])
        followup_input.matrix[0][1] = 2 * int(original_input.matrix[0][1])

        ffollowup_input.matrix[0][0] = int(followup_input.matrix[0][1])
        ffollowup_input.matrix[0][1] = int(followup_input.matrix[0][0])
        ffollowup_input.matrix[0][0] = str(ffollowup_input.matrix[0][0])
        ffollowup_input.matrix[0][1] = str(ffollowup_input.matrix[0][1])
        return ffollowup_input

    def assertViolation(self, exp_output, followup_output):
        if int(followup_output.value) >= int(exp_output.value):
            return False
        else:
            return True


class MR6(MR):
    # MR1-3
    def __init__(self):
        super(MR6, self).__init__()

    def getExpectedMatrix(self, original_input):
        followup_input = copy.deepcopy(original_input)
        ffollowup_input = copy.deepcopy(original_input)
        followup_input.matrix[0][0] = int(original_input.matrix[0][1])
        followup_input.matrix[0][1] = int(original_input.matrix[0][0])

        ffollowup_input.matrix[0][0] = 2 * int(followup_input.matrix[0][0])
        ffollowup_input.matrix[0][1] = 2 * int(followup_input.matrix[0][1])
        ffollowup_input.matrix[0][0] = str(ffollowup_input.matrix[0][0])
        ffollowup_input.matrix[0][1] = str(ffollowup_input.matrix[0][1])
        return ffollowup_input

    def getExpectedOutput(self, original_output):
        expected_output = Output(original_output.output_name)
        expected_output.value = int(original_output.value) * 2
        return expected_output


class MR7(MR):
    # MR3-1
    def __init__(self):
        super(MR7, self).__init__()

    def getExpectedMatrix(self, original_input):
        followup_input = copy.deepcopy(original_input)
        ffollowup_input = copy.deepcopy(original_input)
        followup_input.matrix[0][0] = 2 * int(original_input.matrix[0][0])
        followup_input.matrix[0][1] = 2 * int(original_input.matrix[0][1])

        ffollowup_input.matrix[0][0] = int(followup_input.matrix[0][1])
        ffollowup_input.matrix[0][1] = int(followup_input.matrix[0][0])
        ffollowup_input.matrix[0][0] = str(ffollowup_input.matrix[0][0])
        ffollowup_input.matrix[0][1] = str(ffollowup_input.matrix[0][1])
        return ffollowup_input

    def getExpectedOutput(self, original_output):
        expected_output = Output(original_output.output_name)
        expected_output.value = int(original_output.value) * 2
        return expected_output


class MR8(MR):
    # MR2-3
    def __init__(self):
        super(MR8, self).__init__()

    def getExpectedMatrix(self, original_input):
        followup_input = copy.deepcopy(original_input)
        ffollowup_input = copy.deepcopy(original_input)
        followup_input.matrix[0][0] = int(original_input.matrix[0][0])
        followup_input.matrix[0][1] = 2 * int(original_input.matrix[0][1])

        ffollowup_input.matrix[0][0] = 2 * int(followup_input.matrix[0][0])
        ffollowup_input.matrix[0][1] = 2 * int(followup_input.matrix[0][1])
        ffollowup_input.matrix[0][0] = str(ffollowup_input.matrix[0][0])
        ffollowup_input.matrix[0][1] = str(ffollowup_input.matrix[0][1])
        return ffollowup_input

    def getExpectedOutput(self, original_output):
        expected_output = Output(original_output.output_name)
        expected_output.value = int(original_output.value) * 2
        return expected_output

    def assertViolation(self, exp_output, followup_output):
        if int(followup_output.value) >= int(exp_output.value):
            return False
        else:
            return True


class MR9(MR):
    # MR3-2
    def __init__(self):
        super(MR9, self).__init__()

    def getExpectedMatrix(self, original_input):
        followup_input = copy.deepcopy(original_input)
        ffollowup_input = copy.deepcopy(original_input)
        followup_input.matrix[0][0] = 2 * int(original_input.matrix[0][0])
        followup_input.matrix[0][1] = 2 * int(original_input.matrix[0][1])

        ffollowup_input.matrix[0][0] = int(followup_input.matrix[0][0])
        ffollowup_input.matrix[0][1] = 2 * int(followup_input.matrix[0][1])
        ffollowup_input.matrix[0][0] = str(ffollowup_input.matrix[0][0])
        ffollowup_input.matrix[0][1] = str(ffollowup_input.matrix[0][1])
        return ffollowup_input

    def getExpectedOutput(self, original_output):
        expected_output = Output(original_output.output_name)
        expected_output.value = int(original_output.value) * 2
        return expected_output

    def assertViolation(self, exp_output, followup_output):
        if int(followup_output.value) >= int(exp_output.value):
            return False
        else:
            return True


class MR10(MR):

    def __init__(self):
        super(MR10, self).__init__()

    def getExpectedMatrix(self, original_input):
        followup_input = copy.deepcopy(original_input)
        followup_input.matrix[0][0] = -int(original_input.matrix[0][0])
        followup_input.matrix[0][1] = int(original_input.matrix[0][1])
        followup_input.matrix[0][0] = str(followup_input.matrix[0][0])
        followup_input.matrix[0][1] = str(followup_input.matrix[0][1])
        return followup_input


class MR11(MR):

    def __init__(self):
        super(MR11, self).__init__()

    def getExpectedMatrix(self, original_input):
        followup_input = copy.deepcopy(original_input)
        if int(original_input.matrix[0][1]) == 0:
            followup_input.matrix[0][0] = int(original_input.matrix[0][0])
            followup_input.matrix[0][1] = int(original_input.matrix[0][1])
        else:
            followup_input.matrix[0][0] = int(original_input.matrix[0][1])
            followup_input.matrix[0][1] = int(int(original_input.matrix[0][0]) % int(original_input.matrix[0][1]))
        followup_input.matrix[0][0] = str(followup_input.matrix[0][0])
        followup_input.matrix[0][1] = str(followup_input.matrix[0][1])
        return followup_input


class MR12(MR):

    def __init__(self):
        super(MR12, self).__init__()

    def getExpectedMatrix(self, original_input):
        followup_input = copy.deepcopy(original_input)
        followup_input.matrix[0][0] = int(original_input.matrix[0][1])
        followup_input.matrix[0][1] = int(int(original_input.matrix[0][0]) - int(original_input.matrix[0][1]))
        followup_input.matrix[0][0] = str(followup_input.matrix[0][0])
        followup_input.matrix[0][1] = str(followup_input.matrix[0][1])
        return followup_input


class MR13(MR):

    def __init__(self):
        self.m = 2
        super(MR13, self).__init__()

    def getExpectedMatrix(self, original_input):
        followup_input = copy.deepcopy(original_input)
        followup_input.matrix[0][0] = self.m * int(original_input.matrix[0][0])
        followup_input.matrix[0][1] = self.m * int(original_input.matrix[0][1])
        followup_input.matrix[0][0] = str(followup_input.matrix[0][0])
        followup_input.matrix[0][1] = str(followup_input.matrix[0][1])
        return followup_input

    def getExpectedOutput(self, original_output):
        expected_output = Output(original_output.output_name)
        expected_output.value = int(original_output.value) * self.m
        return expected_output


class MR14(MR):

    def __init__(self):
        self.m = 2
        super(MR14, self).__init__()

    def getExpectedMatrix(self, original_input):
        followup_input = copy.deepcopy(original_input)
        followup_input.matrix[0][0] = int(original_input.matrix[0][0]) + self.m * int(original_input.matrix[0][1])
        followup_input.matrix[0][1] = int(original_input.matrix[0][1])
        followup_input.matrix[0][0] = str(followup_input.matrix[0][0])
        followup_input.matrix[0][1] = str(followup_input.matrix[0][1])
        return followup_input

