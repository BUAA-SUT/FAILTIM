# MR
import random
import re
from Execution import *
from TestCase import *
import itertools
import copy
random.seed(1)

class MR():
    def __init__(self):
        self.name = self.__class__.__name__

    def setExecutor(self, executor):
        self.executor = executor

    def setTestCase(self, ts):
        self.original_ts = ts

    # def process(self):
    #     self.executeTestCase(self.original_ts)
    #     original_input = Input(self.original_ts.infile)
    #     original_input.parseInfile()                                    # load the A,B,C and matrix information
    #     original_output = self.getResults(self.original_ts)
    #     followup_ts = self.generateFollowupTestCase(original_input)
    #     self.executeTestCase(followup_ts)
    #     followup_output = self.getResults(followup_ts)
    #     expected_output = self.getExpectedOutput(original_output)
    #     self.isViolate = self.assertViolation(expected_output, followup_output)
    #     #if self.isViolate:
    #     #    print("True")
    #     #else:
    #     #    print("False")

    def getFollowInput(self, mr):
        original_input = Input(self.original_ts.input)
        original_input.parseInfile()                             # load the A,B,C and matrix information
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
