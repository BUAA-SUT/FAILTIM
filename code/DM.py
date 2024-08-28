import math
import numpy as np
import sys


class DeterMinant:

    def Determinant(self, A, n):
        f1 = f2 = f3 = f4 = True
        symbol = 0
        for i in range(n):
            for j in range(n):
                if f1 and j > i and A[i * n + j] != 0:
                    f1 = False
                if f2 and i > j and A[i * n + j] != 0:
                    f2 = False
                if f3 and i+j < n-1 and A[i * n + j] != 0:
                    f3 = False
                if f4 and i+j > n-1 and A[i * n + j] != 0:
                    f4 = False
        if f1 or f2:  # 主对角线含有非0元素的三角矩阵
            result = 1
            for i in range(n):
                result *= A[i*n+i]
            return result, symbol
        elif f3 or f4:  # 次对角线含有非0元素的三角矩阵
            result = int(math.pow(-1, n*(n-1)/2))
            for i in range(n):
                result *= A[i*n+(n-1-i)]
            return result, symbol
        else:  # 展开法求行列式值
            return self.DeterComp(A, n), symbol

    def DeterComp(self, A, n):
        mid = 0
        temp = []
        for i in range(n*n):
            temp.append(A[i])
        if n == 1:
            result = A[0]
        else:
            for i in range(n):
                mid += int(math.pow(-1, 2+i)) * A[i] * self.DeterComp(self.AlgComp(temp, n, i), n-1)
            result = mid
        return result

    def AlgComp(self, x, n, i):
        array = []
        for j in range(n, n*n):
            if j % n == i:
                pass
            else:
                array.append(x[j])
        return array


class Mutant1(DeterMinant):
    def Determinant(self,A,n):
        f1 = f2 = f3 = f4 = True  # 分别标识4种三角矩阵
        symbol = 0
        for i in range(n):
            for j in range(n):
                if (f1 and j>i and A[i*n+j] != 0):
                    f1 = False
                if (f2 and i>j and A[i*n+j] != 0):
                    f2 = False
                if (f3 and i+j<n-1 and A[i*n+j] != 0):
                    f3 = False
                if (f4 and i+j>n-1 and A[i*n+j] != 0):
                    f4 = False
        if (f1 or f2):  # 主对角线含有非0元素的三角矩阵
            result = 1
            for i in range(n):
                result += A[i*n+i]      # result *= A[i*n+i]  --> result += A[i*n+i]
                symbol = 1
            return result, symbol
        elif (f3 or f4):  # 次对角线含有非0元素的三角矩阵
            result = int(math.pow(-1, n*(n-1)/2))
            for i in range(n):
                result *= A[i*n+(n-1-i)]
            return result, symbol
        else:  # 展开法求行列式值
            return self.DeterComp(A, n), symbol

class Mutant2(DeterMinant):
    def Determinant(self,A,n):
        f1 = f2 = f3 = f4 = True
        symbol = 0
        for i in range(n):
            for j in range(n):
                if (f1 and j>i and A[i*n+j] != 0):
                    f1 = False
                if (f2 and i>j and A[i*n+j] != 0):
                    f2 = False
                if (f3 and i+j<n-1 and A[i*n+j] != 0):
                    f3 = False
                if (f4 and i+j>n-1 and A[i*n+j] != 0):
                    f4 = False
        if (f1 or f2):
            result = 1
            for i in range(n):
                result *= A[i*n+i]
            return result, symbol
        elif (f3 or f4):
            result = int(math.pow(1,n*(n-1)/2))   # int(math.pow(-1,n*(n-1)/2))  -->  int(math.pow(1,n*(n-1)/2))
            symbol = 1
            for i in range(n):
                result *= A[i*n+(n-1-i)]
            return result, symbol
        else:
            return self.DeterComp(A,n), symbol


class Mutant3(DeterMinant):
    def Determinant(self,A,n):
        f1 = f2 = f3 = f4 = True  # 分别标识4种三角矩阵
        symbol = 0
        for i in range(n):
            for j in range(n):
                if (f1 and j>i and A[i*n+j] != 0):
                    f1 = False
                if (f2 and i>j and A[i*n+j] != 0):
                    f2 = False
                if (f3 and i+j<n-1 and A[i*n+j] != 0):
                    f3 = False
                if (f4 and i+j>n-1 and A[i*n+j] != 0):
                    f4 = False
        if (f1 or f2):  # 主对角线含有非0元素的三角矩阵
            result = 1
            for i in range(n):
                result *= A[i*n]      # result *= A[i*n+i]  --> result *= A[i*n]
                symbol = 1
            return result, symbol
        elif (f3 or f4):  # 次对角线含有非0元素的三角矩阵(主对角线全0)
            result = int(math.pow(-1, n*(n-1)/2))
            for i in range(n):
                result *= A[i*n+(n-1-i)]
            return result, symbol
        else:  # 展开法求行列式值
            return self.DeterComp(A, n), symbol


class Mutant4(DeterMinant):
    def Determinant(self,A,n):
        f1 = f2 = f3 = f4 = True  # 分别标识4种三角矩阵
        symbol = 0
        for i in range(n):
            for j in range(n):
                if f1 and j>i and A[i * n + j] != 0:
                    f1 = False
                if f2 and i>j and A[i * n + j] != 0:
                    f2 = False
                if f3 and i+j<n-1 and A[i * n + j] != 0:
                    f3 = False
                if f4 and i+j>n-1 and A[i * n + j] != 0:
                    f4 = False
        if f1 or f2:  # 主对角线含有非0元素的三角矩阵
            result = 1
            for i in range(n):
                result *= A[i*n+1]      # result *= A[i*n+i]  --> result *= A[i*n+1]
                symbol = 1
            return result, symbol
        elif f3 or f4:  # 次对角线含有非0元素的三角矩阵
            result = int(math.pow(-1, n*(n-1)/2))
            for i in range(n):
                result *= A[i*n+(n-1-i)]
            return result, symbol
        else:  # 展开法求行列式值
            return self.DeterComp(A, n), symbol


class Mutant5(DeterMinant):
    def Determinant(self,A,n):
        f1 = f2 = f3 = f4 = True
        symbol = 0
        for i in range(n):
            for j in range(n):
                if f1 and j>i and A[i * n + j] != 0:
                    f1 = False
                if f2 and i>j and A[i * n + j] != 0:
                    f2 = False
                if f3 and i+j<n-1 and A[i * n + j] != 0:
                    f3 = False
                if f4 and i+j>n-1 and A[i * n + j] != 0:
                    f4 = False
        if f1 or f2:
            result = 1
            for i in range(n):
                result *= A[i*n+i]
            return result, symbol
        elif f3 or f4:
            result = int(math.pow(-1, n*(n-1)/2))
            symbol = 1
            for i in range(n):
                result += A[i*n+(n-1-i)]  # result *= A[i*n+(n-1-i)]  --->  result += A[i*n+(n-1-i)]
            return result, symbol
        else:
            return self.DeterComp(A,n), symbol


class Mutant6(DeterMinant):
    def Determinant(self, A, n):
        f1 = f2 = f3 = f4 = True
        symbol = 0
        for i in range(n):
            for j in range(n):
                if f1 and j>i and A[i * n + j] != 0:
                    f1 = False
                if f2 and i>j and A[i * n + j] != 0:
                    f2 = False
                if f3 and i+j<n-1 and A[i * n + j] != 0:
                    f3 = False
                if f4 and i+j>n-1 and A[i * n + j] != 0:
                    f4 = False
        if f1 or f2:
            result = 1
            for i in range(n):
                result *= A[i*n+i]
            return result, symbol
        elif f3 or f4:
            result = int(math.pow(-1,n*(n-1)/2))
            for i in range(n):
                result *= A[i*n+(n-1-i)]
            return result, symbol
        else:
            return self.DeterComp(A,n)

    def DeterComp(self, A, n):
        mid = 0
        temp = []
        symbol  =0
        for i in range(n*n):
            temp.append(A[i])
        if (n == 1):
            result = A[0]
        else:
            symbol = 1
            for i in range(n):
                mid += int(math.pow(1, 2+i)) * A[i] * self.DeterComp(self.AlgComp(temp,n,i),n-1)[0]  # math.pow(-1,2+i)
            result = mid
        return result, symbol

    def AlgComp(self,x,n,i):
        array = []
        for j in range(n,n*n):
            # if (j % n < i):
            #     array[(j / n - 1) * (n - 1) + (j % n)] = x[j]
            # elif(j % n > i):
            #     array[(j / n - 1) * (n - 1) + (j % n) - 1] = x[j]
            if (j % n == i):
                pass
            else:
                array.append(x[j])
        return array

class Mutant7(DeterMinant):
    def Determinant(self, A, n):
        f1 = f2 = f3 = f4 = True
        symbol = 0
        for i in range(n):
            for j in range(n):
                if (f1 and j>i and A[i*n+j] != 0):
                    f1 = False
                if (f2 and i>j and A[i*n+j] != 0):
                    f2 = False
                if (f3 and i+j<n-1 and A[i*n+j] != 0):
                    f3 = False
                if (f4 and i+j>n-1 and A[i*n+j] != 0):
                    f4 = False
        if (f1 or f2):
            result = 1
            for i in range(n):
                result *= A[i*n+i]
            return result, symbol
        elif (f3 or f4):
            result = int(math.pow(-1,n*(n-1)/2))
            for i in range(n):
                result *= A[i*n+(n-1-i)]
            return result, symbol
        else:
            return self.DeterComp(A,n)

    def DeterComp(self, A, n):
        mid = 0
        temp = []
        symbol  =0
        for i in range(n*n):
            temp.append(A[i])
        if (n == 1):
            result = A[0]
        else:
            symbol = 1
            for i in range(n):
                mid *= int(math.pow(-1,2+i)) * A[i] * self.DeterComp(self.AlgComp(temp,n,i),n-1)[0]  # +=
            result = mid
        return result, symbol

    def AlgComp(self,x,n,i):
        array = []
        for j in range(n,n*n):
            # if (j % n < i):
            #     array[(j / n - 1) * (n - 1) + (j % n)] = x[j]
            # elif(j % n > i):
            #     array[(j / n - 1) * (n - 1) + (j % n) - 1] = x[j]
            if (j % n == i):
                pass
            else:
                array.append(x[j])
        return array

class Mutant8(DeterMinant):
    def Determinant(self, A, n):
        f1 = f2 = f3 = f4 = True
        symbol = 0
        for i in range(n):
            for j in range(n):
                if (f1 and j>i and A[i*n+j] != 0):
                    f1 = False
                if (f2 and i>j and A[i*n+j] != 0):
                    f2 = False
                if (f3 and i+j<n-1 and A[i*n+j] != 0):
                    f3 = False
                if (f4 and i+j>n-1 and A[i*n+j] != 0):
                    f4 = False
        if (f1 or f2):
            result = 1
            for i in range(n):
                result *= A[i*n+i]
            return result, symbol
        elif (f3 or f4):
            result = int(math.pow(-1,n*(n-1)/2))
            for i in range(n):
                result *= A[i*n+(n-1-i)]
            return result, symbol
        else:
            return self.DeterComp(A,n)

    def DeterComp(self, A, n):
        mid = 0
        temp = []
        symbol  =0
        for i in range(n*n):
            temp.append(A[i])
        if (n == 1):
            result = A[0]
        else:
            symbol = 1
            for i in range(n):
                mid *= int(math.pow(1, 2+i)) * A[i] * self.DeterComp(self.AlgComp(temp, n, i), n-1)[0]  # += -1
            result = mid
        return result, symbol

    def AlgComp(self, x, n, i):
        array = []
        for j in range(n,n*n):
            # if (j % n < i):
            #     array[(j / n - 1) * (n - 1) + (j % n)] = x[j]
            # elif(j % n > i):
            #     array[(j / n - 1) * (n - 1) + (j % n) - 1] = x[j]
            if (j % n == i):
                pass
            else:
                array.append(x[j])
        return array

class DeterFactory():
    def __init__(self, class_name):
        self.class_name = class_name

    def getDeter(self):
        if( self.class_name == "Mutant1"):
            return Mutant1()
        elif(self.class_name == "Mutant2"):
            return Mutant2()
        elif (self.class_name == "Mutant3"):
            return Mutant3()
        elif (self.class_name == "Mutant4"):
            return Mutant4()
        elif (self.class_name == "Mutant5"):
            return Mutant5()
        elif (self.class_name == "Mutant6"):
            return Mutant6()
        elif (self.class_name == "Mutant7"):
            return Mutant7()
        # elif (self.class_name == "Mutant8"):
        #     return Mutant8()
        else:
            return DeterMinant()

# 矩阵变换
n = 3
def ArrtoMat(mat, n):
    A = mat.copy()
    M = []
    for i in range(0, len(A), n):
        M.append(A[i:i + n])
    return M

def MattoArr(mat, n):
    A = mat
    M = []
    for i in range(len(A)):
        for j in range(len(A[0])):
            M.append((A[i][j]))
    return M

def MR1(mat, n, dynamic):
    '''
    交换行列式任意两行后所得到的新行列式与原行列式互为相反数
    '''
    A = mat.copy()
    M = ArrtoMat(mat, n)
    M_swap = M.copy()
    # k1, k2 = random.sample(range(0, n), 2)
    k1 = 1
    k2 = 2
    M_swap[k1],  M_swap[k2] = M_swap[k2], M_swap[k1]
    A_swap = MattoArr(M_swap, n)
    result_source_a = DeterMinant().Determinant(A, n)
    result_follow_a = DeterMinant().Determinant(A_swap, n)
    result_source, symbol = dynamic.Determinant(A, n)
    result_follow, symbol = dynamic.Determinant(A_swap, n)
    if abs(result_source + result_follow) < 1e-4:
        return 0, A_swap
    else:
        return 1, A_swap


def MR2(mat, n, dynamic):
    '''
    用矩阵的一行减去另一行的倍数，行列式不变
    '''
    A = mat.copy()  # source case
    M = ArrtoMat(mat, n)
    M_tran = M.copy()
    # k1, k2 = random.sample(range(0, n), 2)
    k1 = 1
    k2 = 2
    k = 3
    # k = random.randint(1, 6)
    M_tran[k1] = np.array(M_tran[k1]) - k * np.array(M_tran[k2])
    M_tran[k1] = M_tran[k1].tolist()
    A_tran = MattoArr(M_tran, n)
    result_source_a = DeterMinant().Determinant(A,n)
    result_follow_a = DeterMinant().Determinant(A_tran,n)
    result_source, symbol = dynamic.Determinant(A, n)
    result_follow, symbol = dynamic.Determinant(A_tran, n)
    if abs(result_source - result_follow) < 1e-4:
        return 0, A_tran
    else:
        return 1, A_tran


def MR3(mat, n, dynamic):
    '''
    转置矩阵的行列式不变
    '''
    A = mat.copy()  # source case
    M = ArrtoMat(mat, n)
    M_T = M.copy()
    M_T = np.transpose(M_T).tolist()
    A_T = MattoArr(M_T, n)
    result_source_a = DeterMinant().Determinant(A,n)
    result_follow_a = DeterMinant().Determinant(A_T,n)
    result_source, symbol = dynamic.Determinant(A, n)
    result_follow, symbol = dynamic.Determinant(A_T, n)
    if abs(result_source - result_follow) < 1e-4:
        return 0, A_T
    else:
        return 1, A_T


def MR4(mat, n, dynamic):
    '''
    n阶可逆方阵A与其逆矩阵A^-1的行列式互为倒数
    '''
    A = mat.copy()  # source case
    M = ArrtoMat(mat, n)
    result, symbol = DeterMinant().Determinant(A, n)
    if result == 0:
        return 0, A
    else:
        M_inv = M.copy()
        M_inv = np.linalg.inv(M_inv)
        A_inv = MattoArr(M_inv, n)
        result_source_a = DeterMinant().Determinant(A, n)
        result_follow_a = DeterMinant().Determinant(A_inv, n)
        result_source, symbol = dynamic.Determinant(A, n)
        result_follow, symbol = dynamic.Determinant(A_inv, n)
        if abs(result_source * result_follow - 1) < 1e-4:
            return 0, A_inv
        else:
            return 1, A_inv


def MR5(mat, n, dynamic):
    '''
    MR1和MR2组合，先MR1，再MR2
    '''
    # 先MR1
    A = mat.copy()
    M = ArrtoMat(mat, n)
    M_swap = M.copy()
    # k1, k2 = random.sample(range(0,n),2)
    k1 = 1
    k2 = 2
    M_swap[k1], M_swap[k2] = M_swap[k2], M_swap[k1]
    A_swap = MattoArr(M_swap, n)
    # 再MR2
    M_tran = A_swap.copy()
    M_tran = ArrtoMat(M_tran, n)
    # k1, k2 = random.sample(range(0, n), 2)
    k1 = 1
    k2 = 2
    k = 3
    # k = random.randint(1, 6)
    M_tran[k1] = np.array(M_tran[k1]) - k * np.array(M_tran[k2])
    M_tran[k1] = M_tran[k1].tolist()
    A_tran = MattoArr(M_tran, n)

    # 结果应该是什么样的呢，相反
    result_source_a = DeterMinant().Determinant(A,n)
    result_follow_a = DeterMinant().Determinant(A_tran,n)
    result_source, symbol = dynamic.Determinant(A, n)
    result_follow, symbol = dynamic.Determinant(A_tran, n)
    if abs(result_source + result_follow) < 1e-4:
        return 0, A_tran
    else:
        return 1, A_tran


def MR6(mat, n, dynamic):
    '''
    MR2和MR1组合，先MR2，再MR1
    '''
    # 先MR2
    A = mat.copy()  # source case
    M = ArrtoMat(mat, n)
    M_tran = M.copy()
    # k1, k2 = random.sample(range(0, n), 2)
    k1 = 1
    k2 = 2
    k = 3
    # k = random.randint(1,6)
    M_tran[k1] = np.array(M_tran[k1]) - k * np.array(M_tran[k2])
    M_tran[k1] = M_tran[k1].tolist()
    A_tran = MattoArr(M_tran, n)

    # 再MR1
    M_swap = A_tran.copy()
    M_swap = ArrtoMat(M_swap, n)
    # k1,k2 = random.sample(range(0,n),2)
    k1 = 1
    k2 = 2
    M_swap[k1],M_swap[k2] = M_swap[k2],M_swap[k1]
    A_swap = MattoArr(M_swap, n)

    # 结果应该是什么样的呢，相反
    result_source_a = DeterMinant().Determinant(A,n)
    result_follow_a = DeterMinant().Determinant(A_swap,n)
    result_source, symbol = dynamic.Determinant(A, n)
    result_follow, symbol = dynamic.Determinant(A_swap, n)
    if abs(result_source + result_follow) < 1e-4:
        return 0, A_swap
    else:
        return 1, A_swap


def MR7(mat, n, dynamic):
    # 先MR1
    A = mat.copy()
    M = ArrtoMat(mat, n)
    M_swap = M.copy()
    # k1,k2 = random.sample(range(0,n),2)
    k1 = 1
    k2 = 2
    M_swap[k1],M_swap[k2] = M_swap[k2],M_swap[k1]
    A_swap = MattoArr(M_swap, n)

    # 再MR3
    M_T = A_swap.copy()
    M_T = ArrtoMat(M_T, n)
    M_T = np.transpose(M_T).tolist()
    A_T = MattoArr(M_T, n)

    # 预期的结果是什么呢？相反
    result_source_a = DeterMinant().Determinant(A,n)
    result_follow_a = DeterMinant().Determinant(A_T,n)
    result_source, symbol = dynamic.Determinant(A, n)
    result_follow, symbol = dynamic.Determinant(A_T, n)
    if abs(result_source + result_follow) < 1e-4:
        return 0, A_T
    else:
        return 1, A_T


def MR8(mat, n, dynamic):
    A = mat.copy()  # source case
    M = ArrtoMat(mat, n)
    M_T = M.copy()
    M_T = np.transpose(M_T).tolist()
    A_T = MattoArr(M_T, n)

    M_swap = A_T.copy()
    M_swap = ArrtoMat(M_swap, n)
    # k1,k2 = random.sample(range(0,n),2)
    k1 = 1
    k2 = 2
    M_swap[k1], M_swap[k2] = M_swap[k2], M_swap[k1]
    A_swap = MattoArr(M_swap, n)

    # 结果应该是什么样的呢，相反
    result_source_a = DeterMinant().Determinant(A,n)
    result_follow_a = DeterMinant().Determinant(A_swap,n)
    result_source, symbol = dynamic.Determinant(A, n)
    result_follow, symbol = dynamic.Determinant(A_swap, n)
    if abs(result_source + result_follow) < 1e-4:
        return 0, A_swap
    else:
        return 1, A_swap


def MR9(mat, n, dynamic):
    # 先MR2
    A = mat.copy()  # source case
    M = ArrtoMat(mat, n)
    M_tran = M.copy()
    # k1, k2 = random.sample(range(0, 3), 2)
    k1 = 1
    k2 = 2
    k = 3
    # k = random.randint(1,6)
    M_tran[k1] = np.array(M_tran[k1]) - k * np.array(M_tran[k2])
    M_tran[k1] = M_tran[k1].tolist()
    A_tran = MattoArr(M_tran, n)
    # 再MR3
    M_T = A_tran.copy()
    M_T = ArrtoMat(M_T, n)
    M_T = np.transpose(M_T).tolist()
    A_T = MattoArr(M_T, n)
    # 预期的结果是什么呢？不变
    result_source_a = DeterMinant().Determinant(A,n)
    result_follow_a = DeterMinant().Determinant(A_T,n)
    result_source, symbol = dynamic.Determinant(A, n)
    result_follow, symbol = dynamic.Determinant(A_T, n)
    if abs(result_source - result_follow) < 1e-4:
        return 0, A_T
    else:
        return 1, A_T


def MR10(mat, n, dynamic):
    A = mat.copy()  # source case
    M = ArrtoMat(mat, n)
    M_T = M.copy()
    M_T = np.transpose(M_T).tolist()
    A_T = MattoArr(M_T, n)

    M_tran = A_T.copy()
    M_tran = ArrtoMat(M_tran, n)
    # k1, k2 = random.sample(range(0, n), 2)
    k1 = 1
    k2 = 2
    k = 3
    # k = random.randint(1,6)
    M_tran[k1] = np.array(M_tran[k1]) - k * np.array(M_tran[k2])
    M_tran[k1] = M_tran[k1].tolist()
    A_tran = MattoArr(M_tran, n)
    # 预期的结果是什么呢？不变
    result_source_a = DeterMinant().Determinant(A, n)
    result_follow_a = DeterMinant().Determinant(A_tran, n)
    result_source, symbol = dynamic.Determinant(A, n)
    result_follow, symbol = dynamic.Determinant(A_tran, n)
    if abs(result_source - result_follow) < 1e-4:
        return 0, A_tran
    else:
        return 1, A_tran


def MTG(argv, dynamic):
    source = argv.copy()
    follow_case = []
    MG = []
    current_module = sys.modules[__name__]
    for i in range(1, 11):  # MR
        result, follow = getattr(current_module, 'MR'+str(i))(source, n, dynamic)
        MG.append(result)
        follow_case.append(follow)
    return MG, follow_case
