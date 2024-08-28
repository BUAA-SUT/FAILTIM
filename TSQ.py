import math
import sys


class Trisquare:

    def trisquare(self, argv):
        symbol = 0  # 检查测试用例是否经过了错误语句
        a = argv[0]
        b = argv[1]
        c = argv[2]
        if a <= 0 or b <= 0 or c <= 0 or a >= b + c or b >= a + c or c >= a + b:
            print('Not a triangle')
            return 0
        Sum = a + b + c
        Max = max(a, b, c)
        Min = min(a, b, c)
        mid = Sum - Max - Min
        if pow(Max, 2) < pow(mid, 2) + pow(Min, 2):
            # 锐角三角形
            if Max == mid:
                # 顶角小于或等于60度的等腰三角形
                h = math.sqrt(pow(Max, 2) - pow(Min / 2, 2))
                return Min * h / 2, symbol
            elif Min == mid:
                # 顶角大于60度的等腰三角形
                h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
                return Max * h / 2, symbol
            else:
                # 不规则的锐角三角形，海伦公式计算
                p = (Max + mid + Min) / 2
                return math.sqrt(p * (p - Max) * (p - mid) * (p - Min)), symbol
        if pow(Max, 2) == pow(mid, 2) + pow(Min, 2):
            return mid * Min / 2, symbol
        if Min == mid:
            # 钝角等腰三角形
            h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
            return Max * h / 2, symbol
        else:
            # 不规则钝角三角形，Max乘以高除以2
            x = (pow(Max, 2) + pow(mid, 2) - pow(Min, 2)) / (2 * Max)
            h = math.sqrt(pow(mid, 2) - pow(x, 2))
            return Max * h / 2, symbol


class Mutant1:
    def trisquare(self, argv):
        symbol = 0  # 检查测试用例是否经过了错误语句
        area = 0
        a = argv[0]
        b = argv[1]
        c = argv[2]
        if a <= 0 or b <= 0 or c <= 0 or a >= b + c or b >= a + c or c >= a + b:
            print('Not a triangle')
            return area, symbol
        Sum = a + b + c
        Max = max(a, b, c)
        Min = min(a, b, c)
        mid = Sum - Max - Min
        if pow(Max, 2) < pow(mid, 2) + pow(Min, 2):  # 锐角三角形
            # print('Acute triangle')
            if Max == mid:  # 顶角小于或等于60度的等腰三角形  e.g. [5, 5, 4]
                h = math.sqrt(pow(Max, 2) - pow(mid / 2, 2))  # h = math.sqrt(pow(Max,2)-pow(Min/2,2))
                symbol = 1
                area = Min * h / 2
                return area, symbol
            elif Min == mid:  # 顶角大于60度的等腰三角形
                h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
                area = Max * h / 2
                return area, symbol
            else:  # 不规则的锐角三角形, 海伦公式计算
                p = (Max + mid + Min) / 2
                area = math.sqrt(p * (p - Max) * (p - mid) * (p - Min))
                return area, symbol
        if (pow(Max, 2) == pow(mid, 2) + pow(Min, 2)):
            # print('Right-angled triangle') #直角三角形
            area = mid * Min / 2
            return area, symbol
        # print('Obtuse triangle')
        if (Min == mid):  # 等腰三角形
            h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
            area = Max * h / 2
            return area, symbol
        else:  # 不规则钝角三角形，Max乘以高除以2
            x = (pow(Max, 2) + pow(mid, 2) - pow(Min, 2)) / (2 * Max)
            h = math.sqrt(pow(mid, 2) - pow(x, 2))
            area = Max * h / 2
            return area, symbol


class Mutant2:
    def trisquare(self, argv):
        symbol = 0  # 检查测试用例是否经过了错误语句
        area = 0
        a = argv[0]
        b = argv[1]
        c = argv[2]
        if (a <= 0 or b <= 0 or c <= 0 or a >= b + c or b >= a + c or c >= a + b):
            print('Not a triangle')
            return area, symbol
        Sum = a + b + c
        Max = max(a, b, c)
        Min = min(a, b, c)
        mid = Sum - Max - Min
        if (pow(Max, 2) < pow(mid, 2) + pow(Min, 2)):  # 锐角三角形
            # print('Acute triangle')
            if (Max == mid):  # 顶角小于或等于60度的等腰三角形
                h = math.sqrt(pow(Max, 2) - pow(Min / 2, 2))

                area = Min * h / 2
                return area, symbol
            elif (Min == mid):  # 顶角大于60度的等腰三角形 [4, 4, 5]
                h = math.sqrt(pow(Min, 2) - pow(mid / 2, 2))  # h = math.sqrt(pow(Min,2)-pow(Max/2,2))
                symbol = 1
                area = Max * h / 2
                return area, symbol
            else:  # 不规则的锐角三角形，海伦公式计算
                p = (Max + mid + Min) / 2
                area = math.sqrt(p * (p - Max) * (p - mid) * (p - Min))
                return area, symbol
        if (pow(Max, 2) == pow(mid, 2) + pow(Min, 2)):
            # print('Right-angled triangle') #直角三角形
            area = mid * Min / 2
            return area, symbol
        # print('Obtuse triangle')
        if (Min == mid):  # 等腰三角形
            h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
            area = Max * h / 2
            return area, symbol
        else:  # 不规则钝角三角形，Max乘以高除以2
            x = (pow(Max, 2) + pow(mid, 2) - pow(Min, 2)) / (2 * Max)
            h = math.sqrt(pow(mid, 2) - pow(x, 2))
            area = Max * h / 2
            return area, symbol


class Mutant3:
    def trisquare(self, argv):
        symbol = 0  # 检查测试用例是否经过了错误语句
        area = 0
        a = argv[0]
        b = argv[1]
        c = argv[2]
        if (a <= 0 or b <= 0 or c <= 0 or a >= b + c or b >= a + c or c >= a + b):
            print('Not a triangle')
            return area, symbol
        Sum = a + b + c
        Max = max(a, b, c)
        Min = min(a, b, c)
        mid = Sum - Max - Min
        if (pow(Max, 2) < pow(mid, 2) + pow(Min, 2)):  # 锐角三角形
            # print('Acute triangle')
            if (Max == mid):  # 顶角小于或等于60度的等腰三角形
                h = math.sqrt(pow(Max, 2) - pow(Min / 2, 2))

                area = Min * h / 2
                return area, symbol
            elif (Min == mid):  # 顶角大于60度的等腰三角形
                h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
                area = Max * h / 2
                return area, symbol
            else:  # 不规则的锐角三角形，海伦公式计算
                p = (Max + mid + Min) * 2  # p = (Max + mid + Min)/2
                symbol = 1
                area = math.sqrt(p * (p - Max) * (p - mid) * (p - Min))
                return area, symbol
        if (pow(Max, 2) == pow(mid, 2) + pow(Min, 2)):
            # print('Right-angled triangle') #直角三角形
            area = mid * Min / 2
            return area, symbol
        # print('Obtuse triangle')
        if (Min == mid):  # 等腰三角形
            h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
            area = Max * h / 2
            return area, symbol
        else:  # 不规则钝角三角形，Max乘以高除以2
            x = (pow(Max, 2) + pow(mid, 2) - pow(Min, 2)) / (2 * Max)
            h = math.sqrt(pow(mid, 2) - pow(x, 2))
            area = Max * h / 2
            return area, symbol


class Mutant4:
    def trisquare(self, argv):
        symbol = 0  # 检查测试用例是否经过了错误语句
        area = 0
        a = argv[0]
        b = argv[1]
        c = argv[2]
        if (a <= 0 or b <= 0 or c <= 0 or a >= b + c or b >= a + c or c >= a + b):
            print('Not a triangle')
            return area, symbol
        Sum = a + b + c
        Max = max(a, b, c)
        Min = min(a, b, c)
        mid = Sum - Max - Min
        if (pow(Max, 2) < pow(mid, 2) + pow(Min, 2)):  # 锐角三角形
            # print('Acute triangle')
            if (Max == mid):  # 顶角小于或等于60度的等腰三角形
                h = math.sqrt(pow(Max, 2) - pow(Min / 2, 2))
                area = Min * h / 2
                return area, symbol
            elif (Min == mid):  # 顶角大于60度的等腰三角形
                h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
                area = Max * h / 2
                return area, symbol
            else:  # 不规则的锐角三角形，海伦公式计算
                p = (Max + mid + Min) / 2
                area = math.sqrt(p * (p - Max) * (p - mid) * (p - Min))
                return area, symbol
        if (pow(Max, 2) == pow(mid, 2) + pow(Min, 2)):  # 直角三角形
            # print('Right-angled triangle')
            area = mid * Min  # mid*Min/2
            symbol = 1
            return area, symbol
        # print('Obtuse triangle')
        if (Min == mid):  # 钝角等腰三角形
            h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
            area = Max * h / 2
            return area, symbol
        else:  # 不规则钝角三角形，Max乘以高除以2
            x = (pow(Max, 2) + pow(mid, 2) - pow(Min, 2)) / (2 * Max)
            h = math.sqrt(pow(mid, 2) - pow(x, 2))
            area = Max * h / 2
            return area, symbol


class Mutant5:
    def trisquare(self, argv):
        symbol = 0  # 检查测试用例是否经过了错误语句
        area = 0
        a = argv[0]
        b = argv[1]
        c = argv[2]
        if (a <= 0 or b <= 0 or c <= 0 or a >= b + c or b >= a + c or c >= a + b):
            print('Not a triangle')
            return area, symbol
        Sum = a + b + c
        Max = max(a, b, c)
        Min = min(a, b, c)
        mid = Sum - Max - Min
        if (pow(Max, 2) < pow(mid, 2) + pow(Min, 2)):  # 锐角三角形
            # print('Acute triangle')
            if (Max == mid):  # 顶角小于或等于60度的等腰三角形
                h = math.sqrt(pow(Max, 2) - pow(Min / 2, 2))

                area = Min * h / 2
                return area, symbol
            elif (Min == mid):  # 顶角大于60度的等腰三角形
                h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
                area = Max * h / 2
                return area, symbol
            else:  # 不规则的锐角三角形，海伦公式计算
                p = (Max + mid + Min) / 2
                area = math.sqrt(p * (p - Max) * (p - mid) * (p - Min))
                return area, symbol
        if (pow(Max, 2) == pow(mid, 2) + pow(Min, 2)):
            # print('Right-angled triangle') #直角三角形
            area = mid * Min / 2
            return area, symbol
        # print('Obtuse triangle')
        if (Min == mid):  # 等腰三角形
            h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
            area = Max * h  # Max*h/2
            symbol = 1
            return area, symbol
        else:  # 不规则钝角三角形，Max乘以高除以2
            x = (pow(Max, 2) + pow(mid, 2) - pow(Min, 2)) / (2 * Max)
            h = math.sqrt(pow(mid, 2) - pow(x, 2))
            area = Max * h / 2
            return area, symbol


class Mutant6:
    def trisquare(self, argv):
        symbol = 0  # 检查测试用例是否经过了错误语句
        area = 0
        a = argv[0]
        b = argv[1]
        c = argv[2]
        if (a <= 0 or b <= 0 or c <= 0 or a >= b + c or b >= a + c or c >= a + b):
            print('Not a triangle')
            return area, symbol
        Sum = a + b + c
        Max = max(a, b, c)
        Min = min(a, b, c)
        mid = Sum - Max - Min
        if (pow(Max, 2) < pow(mid, 2) + pow(Min, 2)):  # 锐角三角形
            # print('Acute triangle')
            if (Max == mid):  # 顶角小于或等于60度的等腰三角形
                h = math.sqrt(pow(Max, 2) - pow(Min / 2, 2))
                area = Min * h / 2
                return area, symbol
            elif (Min == mid):  # 顶角大于60度的等腰三角形
                h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
                area = Max * h / 2
                return area, symbol
            else:  # 不规则的锐角三角形，海伦公式计算
                p = (Max + mid + Min) / 2
                area = math.sqrt(p * (p - Max) * (p - mid) * (p - Min))
                return area, symbol
        if (pow(Max, 2) == pow(mid, 2) + pow(Min, 2)):
            # print('Right-angled triangle') #直角三角形
            area = mid * Min / 2
            return area, symbol
        # print('Obtuse triangle')
        if (Min == mid):  # 等腰三角形
            h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
            area = Max * h / 2
            return area, symbol
        else:  # 不规则钝角三角形，Max乘以高除以2
            x = (pow(Max, 2) + pow(Min, 2) - pow(mid, 2)) / (2 * Max)  # x = (pow(Max,2)+pow(mid,2)-pow(Min,2))/(2*Max)
            h = math.sqrt(pow(mid, 2) - pow(x, 2))
            area = Max * h / 2
            symbol = 1
            return area, symbol


class TriFactory:
    def __init__(self, class_name):
        self.class_name = class_name

    def getTri(self):
        if self.class_name == "Mutant1":
            return Mutant1()
        elif self.class_name == "Mutant2":
            return Mutant2()
        elif self.class_name == "Mutant3":
            return Mutant3()
        elif self.class_name == "Mutant4":
            return Mutant4()
        elif self.class_name == "Mutant5":
            return Mutant5()
        elif self.class_name == "Mutant6":
            return Mutant6()
        else:
            return Trisquare()


def MR1(argv, dynamic):
    a = argv[0]
    b = argv[1]
    c = argv[2]
    zs, symbol = Trisquare().trisquare(argv)
    s, symbol = dynamic.trisquare(argv)
    if zs == 0:
        return 2
    a1 = math.sqrt(2 * pow(b, 2) + 2 * pow(c, 2) - pow(a, 2))
    b1 = b
    c1 = c
    edge = [a1, b1, c1]
    s1, symbol = dynamic.trisquare(edge)
    s = float('%.4f' % s)
    s1 = float('%.4f' % s1)
    if abs(s1 - s) < 1e-4:
        return 0, edge
    else:
        return 1, edge


def MR2(argv, dynamic):
    a = argv[0]
    b = argv[1]
    c = argv[2]
    zs, symbol = Trisquare().trisquare(argv)
    s, symbol = dynamic.trisquare(argv)
    if zs == 0:
        return 2
    a1 = a
    b1 = math.sqrt(2 * pow(a, 2) + 2 * pow(c, 2) - pow(b, 2))
    c1 = c
    edge = [a1, b1, c1]
    s1, symbol = dynamic.trisquare(edge)
    s = float('%.4f' % s)
    s1 = float('%.4f' % s1)
    if abs(s1 - s) < 1e-4:
        return 0, edge
    else:
        return 1, edge


def MR3(argv, dynamic):
    a = argv[0]
    b = argv[1]
    c = argv[2]
    zs, symbol = Trisquare().trisquare(argv)
    s, symbol = dynamic.trisquare(argv)
    if zs == 0:
        return 2
    a1 = a
    b1 = b
    c1 = math.sqrt(2 * pow(a, 2) + 2 * pow(b, 2) - pow(c, 2))
    edge = [a1, b1, c1]
    s1, symbol = dynamic.trisquare(edge)
    s = float('%.4f' % s)
    s1 = float('%.4f' % s1)
    if abs(s1 - s) < 1e-4:
        return 0, edge
    else:
        return 1, edge


def MR4(argv, dynamic):
    a = argv[0]
    b = argv[1]
    c = argv[2]
    zs, symbol = Trisquare().trisquare(argv)
    s, symbol = dynamic.trisquare(argv)
    if zs == 0:
        return 2
    a1 = math.sqrt(2 * pow(b, 2) + 2 * pow(c, 2) - pow(a, 2))
    b1 = math.sqrt(3 * pow(b, 2) + 6 * pow(c, 2) - 2 * pow(a, 2))
    c1 = c
    edge = [a1, b1, c1]
    s1, symbol = dynamic.trisquare(edge)
    s = float('%.4f' % s)
    s1 = float('%.4f' % s1)
    if abs(s1 - s) < 1e-4:
        return 0, edge
    else:
        return 1, edge


def MR5(argv, dynamic):
    a = argv[0]
    b = argv[1]
    c = argv[2]
    zs, symbol = Trisquare().trisquare(argv)
    s, symbol = dynamic.trisquare(argv)
    if zs == 0:
        return 2
    a1 = math.sqrt(2 * pow(b, 2) + 2 * pow(c, 2) - pow(a, 2))
    b1 = b
    c1 = math.sqrt(6 * pow(b, 2) + 3 * pow(c, 2) - 2 * pow(a, 2))
    edge = [a1, b1, c1]
    s1, symbol = dynamic.trisquare(edge)
    s = float('%.4f' % s)
    s1 = float('%.4f' % s1)
    if abs(s1 - s) < 1e-4:
        return 0, edge
    else:
        return 1, edge


def MR6(argv, dynamic):
    a = argv[0]
    b = argv[1]
    c = argv[2]
    s, symbol = dynamic.trisquare(argv)
    zs, symbol = Trisquare().trisquare(argv)
    if zs == 0:
        return 2
    a1 = math.sqrt(3 * pow(a, 2) + 6 * pow(c, 2) - 2 * pow(b, 2))
    b1 = math.sqrt(2 * pow(a, 2) + 2 * pow(c, 2) - pow(b, 2))
    c1 = c
    edge = [a1, b1, c1]
    s1, symbol = dynamic.trisquare(edge)
    s = float('%.4f' % s)
    s1 = float('%.4f' % s1)
    if abs(s1 - s) < 1e-4:
        return 0, edge
    else:
        return 1, edge


def MR7(argv, dynamic):
    a = argv[0]
    b = argv[1]
    c = argv[2]
    s, symbol = dynamic.trisquare(argv)
    zs, symbol = Trisquare().trisquare(argv)
    if zs == 0:
        return 2
    a1 = math.sqrt(3 * pow(a, 2) + 6 * pow(b, 2) - 2 * pow(c, 2))
    b1 = b
    c1 = math.sqrt(2 * pow(a, 2) + 2 * pow(b, 2) - pow(c, 2))
    edge = [a1, b1, c1]
    s1, symbol = dynamic.trisquare(edge)
    s = float('%.4f' % s)
    s1 = float('%.4f' % s1)
    if abs(s1 - s) < 1e-4:
        return 0, edge
    else:
        return 1, edge


def MR8(argv, dynamic):
    a = argv[0]
    b = argv[1]
    c = argv[2]
    s, symbol = dynamic.trisquare(argv)
    zs, symbol = Trisquare().trisquare(argv)
    if zs == 0:
        return 2
    a1 = a
    b1 = math.sqrt(2 * pow(a, 2) + 2 * pow(c, 2) - pow(b, 2))
    c1 = math.sqrt(6 * pow(a, 2) + 3 * pow(c, 2) - 2 * pow(b, 2))
    edge = [a1, b1, c1]
    s1, symbol = dynamic.trisquare(edge)
    s = float('%.4f' % s)
    s1 = float('%.4f' % s1)
    if abs(s1 - s) < 1e-4:
        return 0, edge
    else:
        return 1, edge


def MR9(argv, dynamic):
    a = argv[0]
    b = argv[1]
    c = argv[2]
    s, symbol = dynamic.trisquare(argv)
    zs, symbol = Trisquare().trisquare(argv)
    if zs == 0:
        return 2
    a1 = a
    b1 = math.sqrt(6 * pow(a, 2) + 3 * pow(b, 2) - 2 * pow(c, 2))
    c1 = math.sqrt(2 * pow(a, 2) + 2 * pow(b, 2) - pow(c, 2))
    edge = [a1, b1, c1]
    s1, symbol = dynamic.trisquare(edge)
    s = float('%.4f' % s)
    s1 = float('%.4f' % s1)
    if abs(s1 - s) < 1e-4:
        return 0, edge
    else:
        return 1, edge


def MTG(argv, dynamic):
    source = argv.copy()
    follow_case = []
    MG = []
    current_module = sys.modules[__name__]
    for i in range(1, 10):  # MR
        result, follow = getattr(current_module, 'MR' + str(i))(source, dynamic)
        MG.append(result)
        follow_case.append(follow)
    return MG, follow_case
