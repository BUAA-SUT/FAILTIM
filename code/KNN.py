import math
import operator
# import KNN.TestCase as TestCase   # this line is used for testing
# from KNN.KNNMRs import *          # this line is also used for testing
from decimal import *
import random
import sys
random.seed(1)


class KNN():

    def __init__(self):
        # Configuration
        self.trainingSet = []
        self.testSet = []
        self.accuracy = 0
        self.k = 3
        self.default_label = "Iris-setosa"

    def setDefaultLabelabel(self, default_label):
        self.default_label = default_label

    def printInfo(self):
        print('Accuracy: ' + repr(self.accuracy) + '%')

    def setInput(self, trainingSet, testSet):
        self.trainingSet = trainingSet
        self.testSet = testSet

    def euclideanDistance(self, instance1, instance2, length):
        distance = 0
        for x in range(length):
            try:
                distance += pow((Decimal(instance1[x]) - Decimal(instance2[x])), 2)
            except TypeError as t:
                print(t)
        return math.sqrt(Decimal(distance))

    def getNeighbors(self, testInstance):
        distances = []
        length = len(testInstance) - 1
        for x in range(len(self.trainingSet)):
            dist = self.euclideanDistance(testInstance, self.trainingSet[x], length)
            distances.append((self.trainingSet[x], dist))
        distances.sort(key=operator.itemgetter(1))
        neighbors = []
        for x in range(self.k):
            neighbors.append(distances[x][0])
        return neighbors

    def getResponse(self, neighbors):
        classVotes = {}
        for x in range(len(neighbors)):
            response = neighbors[x][-1]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
        if sortedVotes[0][1] == 1:
            return self.default_label
        else:
            return sortedVotes[0][0]

    def getPredications(self):
        predictions = []
        for x in range(len(self.testSet)):
            neighbors = self.getNeighbors(self.testSet[x])
            result = self.getResponse(neighbors)
            predictions.append(result)
        return predictions


class MU_1_KNN(KNN):

    def __init__(self):
        super(MU_1_KNN, self).__init__()

    def euclideanDistance(self, instance1, instance2, length):
        distance = 0
        for x in range(length):
            distance += pow((Decimal(instance1[x]) + Decimal(instance2[x])), 2)  # - ---> +
        return math.sqrt(distance)


class MU_2_KNN(KNN):
    def euclideanDistance(self, instance1, instance2, length):
        distance = 0
        for x in range(length):
            distance = pow((Decimal(instance1[x]) - Decimal(instance2[x])), 2)  # += ---> =
        return math.sqrt(distance)


class MU_3_KNN(KNN):
    def euclideanDistance(self, instance1, instance2, length):
        distance = 0
        for x in range(length):
            distance += pow((Decimal(instance1[x]) - Decimal(instance2[x])), 2)
        return distance  # remove math.sqrt


class MU_4_KNN(KNN):

    def __init__(self):
        super(MU_4_KNN, self).__init__()

    def euclideanDistance(self, instance1, instance2, length):
        distance = 0
        for x in range(length):
            distance += pow((Decimal(instance1[x]) / Decimal(instance2[x])), 2)  # - ---> /
        return math.sqrt(distance)


class MU_5_KNN(KNN):
    def getNeighbors(self, testInstance):
        distances = []
        length = len(testInstance) - 1
        for x in range(len(self.trainingSet)):
            dist = self.euclideanDistance(testInstance, self.trainingSet[x], length)
            distances.append((self.trainingSet[x], dist))
        # distances.sort(key=operator.itemgetter(1))              # remove this line
        neighbors = []
        for x in range(self.k):
            neighbors.append(distances[x][0])
        return neighbors


class MU_6_KNN(KNN):
    def getResponse(self, neighbors):
        classVotes = {}
        for x in range(len(neighbors) - 1):  # len(neighbors)
            response = neighbors[x][-1]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
        return sortedVotes[0][0]


class MU_7_KNN(KNN):
    def getResponse(self, neighbors):
        classVotes = {}
        for x in range(len(neighbors)):
            response = neighbors[x][-1]
            if response in classVotes:
                classVotes[response] *= 1  # + --> *
            else:
                classVotes[response] = 1
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
        return sortedVotes[0][0]


class MU_8_KNN(KNN):
    def getResponse(self, neighbors):
        classVotes = {}
        for x in range(len(neighbors)):
            response = neighbors[x][-1]
            if response in classVotes:
                classVotes[response] = 1  # += ---> =
            else:
                classVotes[response] = 1
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
        return sortedVotes[0][0]


class MU_9_KNN(KNN):
    def getResponse(self, neighbors):
        classVotes = {}
        for x in range(len(neighbors)):
            response = neighbors[x][-1]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=False)  # True --> False
        if sortedVotes[0][1] == 1:
            return self.default_label
        else:
            return sortedVotes[0][0]

class MU_10_KNN(KNN):
    def euclideanDistance(self, instance1, instance2, length):
        distance = 0
        for x in range(length):
            try:
                distance *= pow((Decimal(instance1[x]) - Decimal(instance2[x])), 2)  # += ----> *=
            except TypeError as t:
                print(t)
        return math.sqrt(distance)

class KNNFactory:
    def __init__(self, class_name):
        self.class_name = class_name

    def getKNN(self):
        if (self.class_name == "MU_1_KNN"):
            return MU_1_KNN()
        elif (self.class_name == "MU_2_KNN"):
            return MU_2_KNN()
        elif (self.class_name == "MU_3_KNN"):
            return MU_3_KNN()
        elif (self.class_name == "MU_4_KNN"):
            return MU_4_KNN()
        elif (self.class_name == "MU_5_KNN"):
            return MU_5_KNN()
        elif (self.class_name == "MU_6_KNN"):
            return MU_6_KNN()
        elif (self.class_name == "MU_7_KNN"):
            return MU_7_KNN()
        elif (self.class_name == "MU_8_KNN"):
            return MU_8_KNN()
        elif (self.class_name == "MU_9_KNN"):
            return MU_9_KNN()
        elif (self.class_name == "MU_10_KNN"):
            return MU_10_KNN()
        else:
            return KNN()


"""Duplicate a matrix. This could be used when the original matrix is useful and need to give it to another matrix."""


def duplicateMatrix(original_matrix):
    dup_matrix = []
    for row in range(len(original_matrix)):
        temp = []
        for col in range(len(original_matrix[0])):
            temp.append(original_matrix[row][col])
        dup_matrix.append(temp)
    return dup_matrix


""" The matrix contains the label information, hence the last column should be removed"""


def shuffleAttribute(original_matrix, shuffle_map):
    shuffled_matrix = duplicateMatrix(original_matrix)
    for row in range(len(shuffled_matrix)):
        for col in range(len(shuffled_matrix[0]) - 1):  # the last column, label info, is removed
            dict_value = shuffle_map[col]
            if not col == dict_value:
                shuffled_matrix[row][col] = original_matrix[row][dict_value]
    return shuffled_matrix


def getShuffleMap(training_set):
    origin_index = list(range(len(training_set[0]) - 1))  # the last column, label info, is removed
    # random.seed(k)
    shuffle_index = random.sample(origin_index, len(origin_index))
    # shuffle_index = [1, 3, 2, 0]
    shuffle_map = dict(zip(origin_index, shuffle_index))
    return shuffle_map


"""Assert whether there is only one element in the testing set. If there are more than one, then program exit."""


def assertOneTestingSample(predictions):
    if not len(predictions) == 1:
        print("The testing sample is more than one!")
        sys.exit(-1)


"""MR-0: Consistence with affine transformation."""


def MR1(source_case, dynamic):
    training_set = source_case[0]
    testing_set = source_case[1]
    k = Decimal(-30.2)
    b = Decimal(50.3)
    ftc_train = duplicateMatrix(training_set)
    ftc_test = duplicateMatrix(testing_set)
    for row in range(len(training_set)):
        for col in range(len(training_set[0]) - 1):
            ftc_train[row][col] = k * Decimal(training_set[row][col]) + b
    for row in range(len(testing_set)):
        for col in range(len(testing_set[0]) - 1):
            ftc_test[row][col] = k * Decimal(testing_set[row][col]) + b
    dynamic.setInput(training_set, testing_set)
    predictions = dynamic.getPredications()
    dynamic.setInput(ftc_train, ftc_test)
    ftc_output = dynamic.getPredications()
    result = 0
    for i in range(len(ftc_output)):
        if not (predictions[i] == ftc_output[i]):
            result = 1
            break
        else:
            result = 0
    return result, [ftc_train, ftc_test]


"""MR-1.2: Permutation of the attribute."""


def MR2(source_case, dynamic):
    training_set = source_case[0]
    testing_set = source_case[1]
    shuffle_map = getShuffleMap(training_set)
    ftc_train = shuffleAttribute(training_set, shuffle_map)
    ftc_test = shuffleAttribute(testing_set, shuffle_map)
    dynamic.setInput(training_set, testing_set)
    predictions = dynamic.getPredications()
    dynamic.setInput(ftc_train, ftc_test)
    ftc_output = dynamic.getPredications()
    result = 0
    for i in range(len(ftc_output)):
        if not (predictions[i] == ftc_output[i]):
            result = 1
            break
        else:
            result = 0
    return result, [ftc_train, ftc_test]


"""MR-3.1: Consistence with re-prediction."""


def MR3(source_case, dynamic):
    training_set = source_case[0]
    testing_set = source_case[1]
    dynamic.setInput(training_set, testing_set)
    predictions = dynamic.getPredications()
    assertOneTestingSample(predictions)
    ftc_train = duplicateMatrix(testing_set)
    ftc_train[0][-1] = predictions[0]
    append_count = int(len(training_set) * 0.8)
    ftc_train *= append_count
    ftc_train += training_set
    dynamic.setInput(ftc_train, testing_set)
    ftc_output = dynamic.getPredications()
    result = 0
    for i in range(len(ftc_output)):
        if not (predictions[i] == ftc_output[i]):
            result = 1
            break
        else:
            result = 0
    return result, [ftc_train, testing_set]


"""MR-3.2:Additional training sample."""


def MR4(source_case, dynamic):
    training_set = source_case[0]
    testing_set = source_case[1]
    dynamic.setInput(training_set, testing_set)
    predictions = dynamic.getPredications()
    assertOneTestingSample(predictions)
    ftc_train = duplicateMatrix(training_set)
    for row in range(len(training_set)):
        if training_set[row][-1] == predictions[0]:
            ftc_train.append(training_set[row])
            break
    dynamic.setInput(ftc_train, testing_set)
    ftc_output = dynamic.getPredications()
    result = 0
    for i in range(len(ftc_output)):
        if not (predictions[i] == ftc_output[i]):
            result = 1
            break
        else:
            result = 0
    return result, [ftc_train, testing_set]


"""MR-4.2: Addition of classes by re-labeling samples."""


def MR5(source_case, dynamic):
    training_set = source_case[0]
    testing_set = source_case[1]
    split = 0.67
    dynamic.setInput(training_set, testing_set)
    predictions = dynamic.getPredications()
    assertOneTestingSample(predictions)
    ftc_train = duplicateMatrix(training_set)
    for row in range(len(ftc_train)):
        if not ftc_train[row][-1] == predictions[0]:
            if random.random() < split:
                ftc_train[row][-1] = training_set[row][-1] + "_suffix"
    dynamic.setInput(ftc_train, testing_set)
    ftc_output = dynamic.getPredications()
    result = 0
    for i in range(len(ftc_output)):
        if not (predictions[i] == ftc_output[i]):
            result = 1
            break
        else:
            result = 0
    return result, [ftc_train, testing_set]


def MR6(source_case, dynamic):
    training_set = source_case[0]
    testing_set = source_case[1]
    k = Decimal(-30.2)
    b = Decimal(50.3)
    ftc_train = duplicateMatrix(training_set)
    ftc_test = duplicateMatrix(testing_set)
    for row in range(len(training_set)):
        for col in range(len(training_set[0]) - 1):
            ftc_train[row][col] = k * Decimal(training_set[row][col]) + b
    for row in range(len(testing_set)):
        for col in range(len(testing_set[0]) - 1):
            ftc_test[row][col] = k * Decimal(testing_set[row][col]) + b

    shuffle_map = getShuffleMap(ftc_train)
    fftc_train = shuffleAttribute(ftc_train, shuffle_map)
    fftc_test = shuffleAttribute(ftc_test, shuffle_map)

    dynamic.setInput(training_set, testing_set)
    predictions = dynamic.getPredications()
    dynamic.setInput(fftc_train, fftc_test)
    ftc_output = dynamic.getPredications()
    result = 0
    for i in range(len(ftc_output)):
        if not (predictions[i] == ftc_output[i]):
            result = 1
            break
        else:
            result = 0
    return result, [fftc_train, fftc_test]


def MR7(source_case, dynamic):
    training_set = source_case[0]
    testing_set = source_case[1]
    shuffle_map = getShuffleMap(training_set)
    ftc_train = shuffleAttribute(training_set, shuffle_map)
    ftc_test = shuffleAttribute(testing_set, shuffle_map)

    k = Decimal(-30.2)
    b = Decimal(50.3)
    fftc_train = duplicateMatrix(ftc_train)
    fftc_test = duplicateMatrix(ftc_test)
    for row in range(len(training_set)):
        for col in range(len(training_set[0]) - 1):
            fftc_train[row][col] = k * Decimal(ftc_train[row][col]) + b
    for row in range(len(testing_set)):
        for col in range(len(testing_set[0]) - 1):
            fftc_test[row][col] = k * Decimal(ftc_test[row][col]) + b

    dynamic.setInput(training_set, testing_set)
    predictions = dynamic.getPredications()
    dynamic.setInput(fftc_train, fftc_test)
    ftc_output = dynamic.getPredications()
    result = 0
    for i in range(len(ftc_output)):
        if not (predictions[i] == ftc_output[i]):
            result = 1
            break
        else:
            result = 0
    return result, [fftc_train, fftc_test]


def MR8(source_case, dynamic):
    training_set = source_case[0]
    testing_set = source_case[1]
    k = Decimal(-30.2)
    b = Decimal(50.3)
    ftc_train = duplicateMatrix(training_set)
    ftc_test = duplicateMatrix(testing_set)
    for row in range(len(training_set)):
        for col in range(len(training_set[0]) - 1):
            ftc_train[row][col] = k * Decimal(training_set[row][col]) + b
    for row in range(len(testing_set)):
        for col in range(len(testing_set[0]) - 1):
            ftc_test[row][col] = k * Decimal(testing_set[row][col]) + b

    dynamic.setInput(training_set, testing_set)
    predictions = dynamic.getPredications()
    assertOneTestingSample(predictions)
    fftc_train = duplicateMatrix(ftc_test)
    fftc_train[0][-1] = predictions[0]
    append_count = int(len(ftc_train) * 0.8)
    fftc_train *= append_count
    fftc_train += ftc_train
    dynamic.setInput(fftc_train, ftc_test)
    ftc_output = dynamic.getPredications()
    result = 0
    for i in range(len(ftc_output)):
        if not (predictions[i] == ftc_output[i]):
            result = 1
            break
        else:
            result = 0
    return result, [fftc_train, ftc_test]


def MR9(source_case, dynamic):
    training_set = source_case[0]
    testing_set = source_case[1]
    dynamic.setInput(training_set, testing_set)
    predictions = dynamic.getPredications()
    assertOneTestingSample(predictions)
    ftc_train = duplicateMatrix(testing_set)
    ftc_train[0][-1] = predictions[0]
    append_count = int(len(training_set) * 0.8)
    ftc_train *= append_count
    ftc_train += training_set

    k = Decimal(-30.2)
    b = Decimal(50.3)
    fftc_train = duplicateMatrix(ftc_train)
    fftc_test = duplicateMatrix(testing_set)
    for row in range(len(training_set)):
        for col in range(len(training_set[0]) - 1):
            fftc_train[row][col] = k * Decimal(ftc_train[row][col]) + b
    for row in range(len(testing_set)):
        for col in range(len(testing_set[0]) - 1):
            fftc_test[row][col] = k * Decimal(testing_set[row][col]) + b

    dynamic.setInput(fftc_train, fftc_test)
    ftc_output = dynamic.getPredications()
    result = 0
    for i in range(len(ftc_output)):
        if not (predictions[i] == ftc_output[i]):
            result = 1
            break
        else:
            result = 0
    return result, [fftc_train, fftc_test]


def MR10(source_case, dynamic):
    training_set = source_case[0]
    testing_set = source_case[1]
    shuffle_map = getShuffleMap(training_set)
    ftc_train = shuffleAttribute(training_set, shuffle_map)
    ftc_test = shuffleAttribute(testing_set, shuffle_map)
    dynamic.setInput(training_set, testing_set)
    predictions = dynamic.getPredications()
    assertOneTestingSample(predictions)
    fftc_train = duplicateMatrix(ftc_test)
    fftc_train[0][-1] = predictions[0]
    append_count = int(len(ftc_train) * 0.8)
    fftc_train *= append_count
    fftc_train += ftc_train
    dynamic.setInput(fftc_train, ftc_test)
    ftc_output = dynamic.getPredications()
    result = 0
    for i in range(len(ftc_output)):
        if not (predictions[i] == ftc_output[i]):
            result = 1
            break
        else:
            result = 0
    return result, [fftc_train, ftc_test]


def MR11(source_case, dynamic):
    training_set = source_case[0]
    testing_set = source_case[1]
    dynamic.setInput(training_set, testing_set)
    predictions = dynamic.getPredications()
    assertOneTestingSample(predictions)
    ftc_train = duplicateMatrix(testing_set)
    ftc_train[0][-1] = predictions[0]
    append_count = int(len(training_set) * 0.8)
    ftc_train *= append_count
    ftc_train += training_set

    shuffle_map = getShuffleMap(ftc_train)
    fftc_train = shuffleAttribute(ftc_train, shuffle_map)
    fftc_test = shuffleAttribute(testing_set, shuffle_map)

    dynamic.setInput(training_set, testing_set)
    predictions = dynamic.getPredications()
    dynamic.setInput(fftc_train, fftc_test)
    ftc_output = dynamic.getPredications()
    result = 0
    for i in range(len(ftc_output)):
        if not (predictions[i] == ftc_output[i]):
            result = 1
            break
        else:
            result = 0
    return result, [fftc_train, fftc_test]


def MTG(source_case, dynamic):
    training_set = source_case[0]
    testing_set = source_case[1]
    follow_case = []
    MG = []
    current_module = sys.modules[__name__]
    for i in range(1, 12):  # MR
        result, follow = getattr(current_module, 'MR' + str(i))([training_set, testing_set], dynamic)
        MG.append(result)
        follow_case.append(follow)
    return MG, follow_case


