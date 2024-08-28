import sys


class TCAS:
    def ALIM(self):
        return self.Positive_RA_Alt_Thresh[self.Alt_Layer_Value]

    def Inhibit_Biased_Climb(self):
        if self.Climb_Inhibi:
            self.Climb_Inhibit = self.Up_Separation + self.NOZCROSS
        else:
            self.Climb_Inhibit = self.Up_Separation
        return self.Climb_Inhibit
        # return (Climb_Inhibit = Up_Separation + NOZCROSS if Climb_Inhibit else Up_Separation)

    def Own_Below_Threat(self):
        return (self.Own_Tracked_Alt < self.Other_Tracked_Alt)

    def Own_Above_Threat(self):
        return self.Other_Tracked_Alt < self.Own_Tracked_Alt

    def Non_Crossing_Biased_Climb(self):
        self.upward_preferred = self.Inhibit_Biased_Climb() > self.Down_Separation
        if self.upward_preferred:
            result = not (self.Own_Below_Threat()) or (
                    self.Own_Below_Threat() and not (self.Down_Separation >= self.ALIM()))
        else:
            result = self.Own_Above_Threat() and (self.Cur_Vertical_Sep >= self.MINSEP) and (
                        self.Up_Separation >= self.ALIM())
        return result

    def Non_Crossing_Biased_Descend(self):
        upward_preferred = self.Inhibit_Biased_Climb() > self.Down_Separation
        if upward_preferred:
            result = self.Own_Below_Threat() and (self.Cur_Vertical_Sep >= self.MINSEP) and (
                        self.Down_Separation >= self.ALIM())
        else:
            result = not (self.Own_Above_Threat()) or (
                        (self.Own_Above_Threat()) and (self.Up_Separation >= self.ALIM()))
        return result

    def Tcas(self, argv):
        self.Cur_Vertical_Sep = argv[0]
        self.High_Confidence = argv[1]
        self.Two_of_Three_Reports_Valid = argv[2]
        self.Own_Tracked_Alt = argv[3]
        self.Own_Tracked_Alt_Rate = argv[4]
        self.Other_Tracked_Alt = argv[5]
        self.Alt_Layer_Value = argv[6]
        self.Up_Separation = argv[7]
        self.Down_Separation = argv[8]
        self.Other_RAC = argv[9]
        self.Other_Capability = argv[10]
        self.Climb_Inhibi = argv[11]
        self.Positive_RA_Alt_Thresh = [400, 500, 640, 740]

        self.OLEV = 600
        self.MAXALTDIFF = 600
        self.MINSEP = 300
        self.NOZCROSS = 100
        self.TCAS_TA = 1
        self.NO_INTENT = 0
        enabled = self.High_Confidence and (self.Own_Tracked_Alt_Rate <= self.OLEV) and (
                    self.Cur_Vertical_Sep > self.MAXALTDIFF)
        tcas_equipped = self.Other_Capability == self.TCAS_TA
        intent_not_known = self.Two_of_Three_Reports_Valid and self.Other_RAC == self.NO_INTENT
        alt_sep = 'UNRESOLVED'
        if enabled and ((tcas_equipped and intent_not_known) or not tcas_equipped):
            need_upward_RA = self.Non_Crossing_Biased_Climb() and self.Own_Below_Threat()
            need_downward_RA = self.Non_Crossing_Biased_Descend() and self.Own_Above_Threat()
            if need_upward_RA and need_downward_RA:
                alt_sep = 'UNRESOLVED'
            elif need_upward_RA:
                alt_sep = 'UPWARD_RA'
            elif need_downward_RA:
                alt_sep = 'DOWNWARD_RA'
            else:
                alt_sep = 'UNRESOLVED'
        return alt_sep


class Mutant1(TCAS):
    def Non_Crossing_Biased_Climb(self):
        self.upward_preferred = self.Inhibit_Biased_Climb() < self.Down_Separation  # >  -->  <  # 与参数[7]和参数[8]有关
        if self.upward_preferred:
            result = not (self.Own_Below_Threat()) or (
                    self.Own_Below_Threat() and not (self.Down_Separation >= self.ALIM()))
        else:
            result = self.Own_Above_Threat() and (self.Cur_Vertical_Sep >= self.MINSEP) and (
                        self.Up_Separation >= self.ALIM())
        return result


class Mutant2(TCAS):
    def Non_Crossing_Biased_Climb(self):
        self.upward_preferred = self.Inhibit_Biased_Climb() < self.Down_Separation  # >  -->  <  # 与参数[7]和参数[8]有关
        if self.upward_preferred:
            result = not (self.Own_Below_Threat()) or (
                    (self.Own_Below_Threat()) and (not (self.Down_Separation >= self.ALIM())))
        else:
            result = self.Own_Above_Threat() and (self.Cur_Vertical_Sep >= self.MINSEP) and (
                    self.Up_Separation >= self.ALIM())
        return result

    def Own_Above_Threat(self):
        return self.Other_Tracked_Alt > self.Own_Tracked_Alt  # < --> >


class Mutant3(TCAS):
    def Own_Above_Threat(self):
        return self.Other_Tracked_Alt > self.Own_Tracked_Alt  # < --> >

    def Non_Crossing_Biased_Climb(self):
        self.upward_preferred = self.Inhibit_Biased_Climb() < self.Down_Separation  # >  -->  <  # 与参数[7]和参数[8]有关
        if self.upward_preferred:
            result = not (self.Own_Below_Threat()) or (
                    (self.Own_Below_Threat()) and (not (self.Down_Separation >= self.ALIM())))
        else:
            result = self.Own_Above_Threat() and (self.Cur_Vertical_Sep >= self.MINSEP) and (
                    self.Up_Separation >= self.ALIM())
        return result

    def Non_Crossing_Biased_Descend(self):
        upward_preferred = self.Inhibit_Biased_Climb() > self.Down_Separation
        if upward_preferred:
            result = self.Own_Below_Threat() or (self.Cur_Vertical_Sep >= self.MINSEP) and (
                    self.Down_Separation >= self.ALIM())  # 第一个and --> or
        else:
            result = not (self.Own_Above_Threat()) or (
                    (self.Own_Above_Threat()) and (self.Up_Separation >= self.ALIM()))
        return result


class Mutant4(TCAS):
    def Own_Above_Threat(self):
        return self.Other_Tracked_Alt > self.Own_Tracked_Alt  # < --> >


class Mutant5(TCAS):
    def Tcas(self, argv):
        self.Cur_Vertical_Sep = argv[0]
        self.High_Confidence = argv[1]
        self.Two_of_Three_Reports_Valid = argv[2]
        self.Own_Tracked_Alt = argv[3]
        self.Own_Tracked_Alt_Rate = argv[4]
        self.Other_Tracked_Alt = argv[5]
        self.Alt_Layer_Value = argv[6]
        self.Up_Separation = argv[7]
        self.Down_Separation = argv[8]
        self.Other_RAC = argv[9]
        self.Other_Capability = argv[10]
        self.Climb_Inhibi = argv[11]
        self.Positive_RA_Alt_Thresh = [400, 500, 640, 740]

        self.OLEV = 600
        self.MAXALTDIFF = 600
        self.MINSEP = 300
        self.NOZCROSS = 100
        self.TCAS_TA = 1
        self.NO_INTENT = 0
        enabled = self.High_Confidence or (self.Own_Tracked_Alt_Rate <= self.OLEV) and (
                    self.Cur_Vertical_Sep > self.MAXALTDIFF)  # and  ---> or
        tcas_equipped = self.Other_Capability == self.TCAS_TA
        intent_not_known = self.Two_of_Three_Reports_Valid and self.Other_RAC == self.NO_INTENT
        alt_sep = 'UNRESOLVED'
        if enabled and ((tcas_equipped and intent_not_known) or not tcas_equipped):
            need_upward_RA = self.Non_Crossing_Biased_Climb() and self.Own_Below_Threat()
            need_downward_RA = self.Non_Crossing_Biased_Descend() and self.Own_Above_Threat()
            if need_upward_RA and need_downward_RA:
                alt_sep = 'UNRESOLVED'
            elif need_upward_RA:
                alt_sep = 'UPWARD_RA'
            elif need_downward_RA:
                alt_sep = 'DOWNWARD_RA'
            else:
                alt_sep = 'UNRESOLVED'
        return alt_sep


class Mutant6(TCAS):
    def Tcas(self, argv):
        self.Cur_Vertical_Sep = argv[0]
        self.High_Confidence = argv[1]
        self.Two_of_Three_Reports_Valid = argv[2]
        self.Own_Tracked_Alt = argv[3]
        self.Own_Tracked_Alt_Rate = argv[4]
        self.Other_Tracked_Alt = argv[5]
        self.Alt_Layer_Value = argv[6]
        self.Up_Separation = argv[7]
        self.Down_Separation = argv[8]
        self.Other_RAC = argv[9]
        self.Other_Capability = argv[10]
        self.Climb_Inhibi = argv[11]
        self.Positive_RA_Alt_Thresh = [400, 500, 640, 740]

        self.OLEV = 600
        self.MAXALTDIFF = 600
        self.MINSEP = 300
        self.NOZCROSS = 100
        self.TCAS_TA = 1
        self.NO_INTENT = 0
        enabled = self.High_Confidence and (self.Own_Tracked_Alt_Rate <= self.OLEV) and (
                    self.Cur_Vertical_Sep > self.MAXALTDIFF)
        tcas_equipped = self.Other_Capability == self.TCAS_TA
        intent_not_known = self.Two_of_Three_Reports_Valid and self.Other_RAC == self.NO_INTENT
        alt_sep = 'UNRESOLVED'
        if enabled or ((tcas_equipped and intent_not_known) or not tcas_equipped):  # 第一个and ---> or
            need_upward_RA = self.Non_Crossing_Biased_Climb() and self.Own_Below_Threat()
            need_downward_RA = self.Non_Crossing_Biased_Descend() and self.Own_Above_Threat()
            if need_upward_RA and need_downward_RA:
                alt_sep = 'UNRESOLVED'
            elif need_upward_RA:
                alt_sep = 'UPWARD_RA'
            elif need_downward_RA:
                alt_sep = 'DOWNWARD_RA'
            else:
                alt_sep = 'UNRESOLVED'
        return alt_sep


class Mutant7(TCAS):
    def Tcas(self, argv):
        self.Cur_Vertical_Sep = argv[0]
        self.High_Confidence = argv[1]
        self.Two_of_Three_Reports_Valid = argv[2]
        self.Own_Tracked_Alt = argv[3]
        self.Own_Tracked_Alt_Rate = argv[4]
        self.Other_Tracked_Alt = argv[5]
        self.Alt_Layer_Value = argv[6]
        self.Up_Separation = argv[7]
        self.Down_Separation = argv[8]
        self.Other_RAC = argv[9]
        self.Other_Capability = argv[10]
        self.Climb_Inhibi = argv[11]
        self.Positive_RA_Alt_Thresh = [400, 500, 640, 740]

        self.OLEV = 600
        self.MAXALTDIFF = 600
        self.MINSEP = 300
        self.NOZCROSS = 100
        self.TCAS_TA = 1
        self.NO_INTENT = 0
        enabled = self.High_Confidence and (self.Own_Tracked_Alt_Rate <= self.OLEV) and (
                    self.Cur_Vertical_Sep > self.MAXALTDIFF)
        tcas_equipped = self.Other_Capability == self.TCAS_TA
        intent_not_known = self.Two_of_Three_Reports_Valid or self.Other_RAC == self.NO_INTENT  # and --> or
        alt_sep = 'UNRESOLVED'
        if enabled and ((tcas_equipped and intent_not_known) or not (tcas_equipped)):
            need_upward_RA = self.Non_Crossing_Biased_Climb() and self.Own_Below_Threat()
            need_downward_RA = self.Non_Crossing_Biased_Descend() or self.Own_Above_Threat()  # and --> or
            if need_upward_RA and need_downward_RA:
                alt_sep = 'UNRESOLVED'
            elif need_upward_RA:
                alt_sep = 'UPWARD_RA'
            elif need_downward_RA:
                alt_sep = 'DOWNWARD_RA'
            else:
                alt_sep = 'UNRESOLVED'
        return alt_sep


class Mutant8(TCAS):
    def Inhibit_Biased_Climb(self):
        if self.Climb_Inhibi:
            self.Climb_Inhibit = self.Up_Separation + self.MINSEP  # operand mutation NOZCROSS
        else:
            self.Climb_Inhibit = self.Up_Separation
        return self.Climb_Inhibit


class Mutant9(TCAS):
    def Tcas(self, argv):
        self.Cur_Vertical_Sep = argv[0]
        self.High_Confidence = argv[1]
        self.Two_of_Three_Reports_Valid = argv[2]
        self.Own_Tracked_Alt = argv[3]
        self.Own_Tracked_Alt_Rate = argv[4]
        self.Other_Tracked_Alt = argv[5]
        self.Alt_Layer_Value = argv[6]
        self.Up_Separation = argv[7]
        self.Down_Separation = argv[8]
        self.Other_RAC = argv[9]
        self.Other_Capability = argv[10]
        self.Climb_Inhibi = argv[11]
        self.Positive_RA_Alt_Thresh = [400, 500, 640, 740]

        self.OLEV = 600
        self.MAXALTDIFF = 600
        self.MINSEP = 300
        self.NOZCROSS = 100
        self.TCAS_TA = 1
        self.NO_INTENT = 0
        enabled = self.High_Confidence and (self.Own_Tracked_Alt_Rate <= self.OLEV) and (
                    self.Cur_Vertical_Sep > self.MAXALTDIFF)
        tcas_equipped = self.Other_Capability == self.TCAS_TA
        intent_not_known = self.Two_of_Three_Reports_Valid or self.Other_RAC == self.NO_INTENT  # and --> or
        alt_sep = 'UNRESOLVED'
        if enabled and ((tcas_equipped and intent_not_known) or not tcas_equipped):
            need_upward_RA = self.Non_Crossing_Biased_Climb() and self.Own_Below_Threat()
            need_downward_RA = self.Non_Crossing_Biased_Descend() and self.Own_Above_Threat()
            if need_upward_RA and need_downward_RA:
                alt_sep = 'UNRESOLVED'
            elif need_upward_RA:
                alt_sep = 'UPWARD_RA'
            elif need_downward_RA:
                alt_sep = 'DOWNWARD_RA'
            else:
                alt_sep = 'UNRESOLVED'
        return alt_sep


class Mutant10(TCAS):
    def Non_Crossing_Biased_Climb(self):
        self.upward_preferred = self.Inhibit_Biased_Climb() > self.Down_Separation
        if self.upward_preferred:
            result = not (self.Own_Below_Threat()) or (
                    self.Own_Below_Threat() and not (self.Down_Separation >= self.ALIM()))
        else:
            result = self.Own_Above_Threat() and (self.Cur_Vertical_Sep >= self.MINSEP) or (
                        self.Up_Separation >= self.ALIM())  # and --> or
        return result


class Mutant11(TCAS):
    def Tcas(self, argv):
        self.Cur_Vertical_Sep = argv[0]
        self.High_Confidence = argv[1]
        self.Two_of_Three_Reports_Valid = argv[2]
        self.Own_Tracked_Alt = argv[3]
        self.Own_Tracked_Alt_Rate = argv[4]
        self.Other_Tracked_Alt = argv[5]
        self.Alt_Layer_Value = argv[6]
        self.Up_Separation = argv[7]
        self.Down_Separation = argv[8]
        self.Other_RAC = argv[9]
        self.Other_Capability = argv[10]
        self.Climb_Inhibi = argv[11]
        self.Positive_RA_Alt_Thresh = [400, 500, 640, 740]

        self.OLEV = 600
        self.MAXALTDIFF = 600
        self.MINSEP = 300
        self.NOZCROSS = 100
        self.TCAS_TA = 1
        self.NO_INTENT = 0
        enabled = self.High_Confidence and (
                    self.Own_Tracked_Alt_Rate <= self.OLEV)  # and (Cur_Vertical_Sep > MAXALTDIFF); missing code
        tcas_equipped = self.Other_Capability == self.TCAS_TA
        intent_not_known = self.Two_of_Three_Reports_Valid and self.Other_RAC == self.NO_INTENT
        alt_sep = 'UNRESOLVED'
        if enabled and ((tcas_equipped and intent_not_known) or not tcas_equipped):
            need_upward_RA = self.Non_Crossing_Biased_Climb() and self.Own_Below_Threat()
            need_downward_RA = self.Non_Crossing_Biased_Descend() and self.Own_Above_Threat()
            if need_upward_RA and need_downward_RA:
                alt_sep = 'UNRESOLVED'
            elif need_upward_RA:
                alt_sep = 'UPWARD_RA'
            elif need_downward_RA:
                alt_sep = 'DOWNWARD_RA'
            else:
                alt_sep = 'UNRESOLVED'
        return alt_sep


class TCASFactory():
    def __init__(self, class_name):
        self.class_name = class_name

    def getTCAS(self):
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
        elif self.class_name == "Mutant7":
            return Mutant7()
        elif self.class_name == "Mutant8":
            return Mutant8()
        elif self.class_name == "Mutant9":
            return Mutant9()
        elif self.class_name == "Mutant10":
            return Mutant10()
        elif self.class_name == "Mutant11":
            return Mutant11()
        else:
            return TCAS()


# MR定义
def MR1(argv, dynamic):
    # MR12
    o_s = TCAS().Tcas(argv)
    argv_f = argv.copy()
    result = 2
    if o_s == 'UPWARD_RA':
        argv_f[3] = ((argv[3] + argv[5]) / 2) - 1
        argv_f[5] = ((argv[3] + argv[5]) / 2) + 1
    elif o_s == 'DOWNWARD_RA':
        argv_f[3] = ((argv[3] + argv[5]) / 2) + 1
        argv_f[5] = ((argv[3] + argv[5]) / 2) - 1
    elif o_s == 'UNRESOLVED':
        argv_f[3] = ((argv[3] + argv[5]) / 2)
        argv_f[5] = ((argv[3] + argv[5]) / 2)
    r_s = dynamic.Tcas(argv)
    r_f = dynamic.Tcas(argv_f)
    if r_f == r_s:
        result = 0
    else:
        result = 1
    return result, argv_f


def MR2(argv, dynamic):
    # MR13
    o_s = TCAS().Tcas(argv)
    argv_f = argv.copy()
    result = 2
    if o_s == 'UPWARD_RA':
        argv_f[8] = argv[8] - 10
    elif o_s == 'DOWNWARD_RA':
        argv_f[7] = argv[7] + 10  # y8>x8
        if argv[11] == 1:
            argv_f[8] = argv_f[7] + 110  # y8+100<=y9
        else:
            argv_f[8] = argv_f[7] + 10  # y8<=y9
    elif o_s == 'UNRESOLVED':
        argv_f[7] = argv[7] - 10  # y8<x8
        argv_f[8] = argv[8] + 10  # y9>x9
        if argv[11] == 1:
            if argv[7] > (argv[8] - 100):  # x8>x9-100
                argv_f[8] = argv_f[7] + 90  # y8>y9-100
            elif argv[7] == (argv[8] - 100):
                return result, argv_f
            else:
                argv_f[8] = argv_f[7] + 110
        else:
            if argv[7] > argv[8]:
                argv_f[7] = argv_f[8] + 1
            elif argv[7] == argv[8]:  # 无解
                return result, argv_f
            else:
                argv_f[8] = argv_f[7] + 1
    r_s = dynamic.Tcas(argv)
    r_f = dynamic.Tcas(argv_f)
    if r_f == r_s:
        result = 0
    else:
        result = 1
    return result, argv_f


def MR3(argv, dynamic):
    # MR14
    o_s = TCAS().Tcas(argv)
    argv_f = argv.copy()
    result = 2
    if o_s == 'UPWARD_RA':
        if argv[6] == 3:
            return result, argv_f
        else:
            argv_f[6] = argv[6] + 1
    elif o_s == 'DOWNWARD_RA':
        if argv[6] == 0:
            return result, argv_f
        else:
            argv_f[6] = argv[6] - 1
    elif o_s == 'UNRESOLVED':
        if argv[3] <= argv[5]:
            if argv[6] == 0:
                return result, argv_f
            else:
                argv_f[6] = argv[6] - 1
        else:
            if argv[6] == 3:
                return result, argv_f
            else:
                argv_f[6] = argv[6] + 1
    r_s = dynamic.Tcas(argv)
    r_f = dynamic.Tcas(argv_f)
    if r_f == r_s:
        result = 0
    else:
        result = 1
    return result, argv_f


def MR4(argv, dynamic):
    o_s = TCAS().Tcas(argv)
    argv_f = argv.copy()
    argv_ff = argv_f.copy()
    result = 2
    if o_s == 'UPWARD_RA':
        argv_f[3] = ((argv[3] + argv[5]) / 2) - 1
        argv_f[5] = ((argv[3] + argv[5]) / 2) + 1
        argv_ff = argv_f.copy()
        argv_ff[8] = argv_f[8] - 10
    elif o_s == 'DOWNWARD_RA':
        argv_f[3] = ((argv[3] + argv[5]) / 2) + 1
        argv_f[5] = ((argv[3] + argv[5]) / 2) - 1
        argv_ff = argv_f.copy()
        argv_ff[7] = argv_f[7] + 10  # y8>x8
        if argv_f[11] == 1:
            argv_ff[8] = argv_ff[7] + 110  # y8+100<=y9
        else:
            argv_ff[8] = argv_ff[7] + 10  # y8<=y9
    elif o_s == 'UNRESOLVED':
        argv_f[3] = ((argv[3] + argv[5]) / 2)
        argv_f[5] = ((argv[3] + argv[5]) / 2)
        argv_ff = argv_f.copy()
        argv_ff[7] = argv_f[7] - 10  # y8<x8
        argv_ff[8] = argv_f[8] + 10  # y9>x9
        if argv_f[11] == 1:
            if argv_f[7] > (argv_f[8] - 100):  # x8>x9-100
                argv_ff[8] = argv_ff[7] + 90  # y8>y9-100
            elif argv_f[7] == (argv_f[8] - 100):
                return result, argv_ff
            else:
                argv_ff[8] = argv_ff[7] + 110
        else:
            if argv_f[7] > argv_f[8]:
                argv_ff[7] = argv_ff[8] + 1
            elif argv_f[7] == argv_f[8]:  # 无解
                return result, argv_ff
            else:
                argv_ff[8] = argv_ff[7] + 1

    r_s = dynamic.Tcas(argv)
    r_f = dynamic.Tcas(argv_ff)
    if r_f == r_s:
        result = 0
    else:
        result = 1
    return result, argv_ff


def MR5(argv, dynamic):
    o_s = TCAS().Tcas(argv)
    argv_f = argv.copy()
    argv_ff = argv_f.copy()
    result = 2
    if o_s == 'UPWARD_RA':
        argv_f[3] = ((argv[3] + argv[5]) / 2) - 1
        argv_f[5] = ((argv[3] + argv[5]) / 2) + 1
        argv_ff = argv_f.copy()
        if argv_f[6] == 3:
            return result, argv_ff
        else:
            argv_ff[6] = argv_f[6] + 1
    elif o_s == 'DOWNWARD_RA':
        argv_f[3] = ((argv[3] + argv[5]) / 2) + 1
        argv_f[5] = ((argv[3] + argv[5]) / 2) - 1
        argv_ff = argv_f.copy()
        if argv_f[6] == 0:
            return result, argv_ff
        else:
            argv_ff[6] = argv_f[6] - 1
    elif o_s == 'UNRESOLVED':
        argv_f[3] = ((argv[3] + argv[5]) / 2)
        argv_f[5] = ((argv[3] + argv[5]) / 2)
        argv_ff = argv_f.copy()
        if argv_f[3] <= argv_f[5]:
            if argv_f[6] == 0:
                return result, argv_ff
            else:
                argv_ff[6] = argv_f[6] - 1
        else:
            if argv_f[6] == 3:
                return result, argv_ff
            else:
                argv_ff[6] = argv_f[6] + 1
    r_s = dynamic.Tcas(argv)
    r_f = dynamic.Tcas(argv_ff)
    if r_f == r_s:
        result = 0
    else:
        result = 1
    return result, argv_ff


def MR6(argv, dynamic):
    o_s = TCAS().Tcas(argv)
    argv_f = argv.copy()
    argv_ff = argv_f.copy()
    result = 2
    if o_s == 'UPWARD_RA':
        argv_f[8] = argv[8] - 10
        argv_ff = argv_f.copy()
        argv_ff[3] = ((argv_f[3] + argv_f[5]) / 2) - 1
        argv_ff[5] = ((argv_f[3] + argv_f[5]) / 2) + 1
    elif o_s == 'DOWNWARD_RA':
        argv_f[7] = argv[7] + 10  # y8>x8
        if argv[11] == 1:
            argv_f[8] = argv_f[7] + 110  # y8+100<=y9
        else:
            argv_f[8] = argv_f[7] + 10  # y8<=y9
        argv_ff = argv_f.copy()
        argv_ff[3] = ((argv_f[3] + argv_f[5]) / 2) + 1
        argv_ff[5] = ((argv_f[3] + argv_f[5]) / 2) - 1
    elif o_s == 'UNRESOLVED':
        argv_f[7] = argv[7] - 10  # y8<x8
        argv_f[8] = argv[8] + 10  # y9>x9
        if argv[11] == 1:
            if argv[7] > (argv[8] - 100):  # x8>x9-100
                argv_f[8] = argv_f[7] + 90  # y8>y9-100
            elif argv[7] == (argv[8] - 100):
                return result, argv_ff
            else:
                argv_f[8] = argv_f[7] + 110
        else:
            if argv[7] > argv[8]:
                argv_f[7] = argv_f[8] + 1
            elif argv[7] == argv[8]:  # 无解
                return result, argv_ff
            else:
                argv_f[8] = argv_f[7] + 1
        argv_ff = argv_f.copy()
        argv_ff[3] = ((argv_f[3] + argv_f[5]) / 2)
        argv_ff[5] = ((argv_f[3] + argv_f[5]) / 2)

    r_s = dynamic.Tcas(argv)
    r_f = dynamic.Tcas(argv_ff)
    if r_f == r_s:
        result = 0
    else:
        result = 1
    return result, argv_ff


def MR7(argv, dynamic):
    o_s = TCAS().Tcas(argv)
    argv_f = argv.copy()
    argv_ff = argv_f.copy()
    result = 2
    if o_s == 'UPWARD_RA':
        if argv[6] == 3:
            return result, argv_f
        else:
            argv_f[6] = argv[6] + 1
        argv_ff = argv_f.copy()
        argv_ff[3] = ((argv_f[3] + argv_f[5]) / 2) - 1
        argv_ff[5] = ((argv_f[3] + argv_f[5]) / 2) + 1
    elif o_s == 'DOWNWARD_RA':
        if argv[6] == 0:
            return result, argv_ff
        else:
            argv_f[6] = argv[6] - 1
        argv_ff = argv_f.copy()
        argv_ff[3] = ((argv_f[3] + argv_f[5]) / 2) + 1
        argv_ff[5] = ((argv_f[3] + argv_f[5]) / 2) - 1
    elif o_s == 'UNRESOLVED':
        if argv[3] <= argv[5]:
            if argv[6] == 0:
                return result, argv_ff
            else:
                argv_f[6] = argv[6] - 1
        else:
            if argv[6] == 3:
                return result, argv_ff
            else:
                argv_f[6] = argv[6] + 1
        argv_ff = argv_f.copy()
        argv_ff[3] = ((argv_f[3] + argv_f[5]) / 2)
        argv_ff[5] = ((argv_f[3] + argv_f[5]) / 2)
    r_s = dynamic.Tcas(argv)
    r_f = dynamic.Tcas(argv_ff)
    if r_f == r_s:
        result = 0
    else:
        result = 1
    return result, argv_ff


def MR8(argv, dynamic):
    o_s = TCAS().Tcas(argv)
    argv_f = argv.copy()
    argv_ff = argv_f.copy()
    result = 2
    if o_s == 'UPWARD_RA':
        argv_f[8] = argv[8] - 10
        argv_ff = argv_f.copy()
        if argv_f[6] == 3:
            return result, argv_ff
        else:
            argv_ff[6] = argv_f[6] + 1
    elif o_s == 'DOWNWARD_RA':
        argv_f[7] = argv[7] + 10  # y8>x8
        if argv[11] == 1:
            argv_f[8] = argv_f[7] + 110  # y8+100<=y9
        else:
            argv_f[8] = argv_f[7] + 10  # y8<=y9
        argv_ff = argv_f.copy()
        if argv_f[6] == 0:
            return result, argv_ff
        else:
            argv_ff[6] = argv_f[6] - 1
    elif o_s == 'UNRESOLVED':
        argv_f[7] = argv[7] - 10  # y8<x8
        argv_f[8] = argv[8] + 10  # y9>x9
        if argv[11] == 1:
            if argv[7] > (argv[8] - 100):  # x8>x9-100
                argv_f[8] = argv_f[7] + 90  # y8>y9-100
            elif argv[7] == (argv[8] - 100):
                return result, argv_f
            else:
                argv_f[8] = argv_f[7] + 110
        else:
            if argv[7] > argv[8]:
                argv_f[7] = argv_f[8] + 1
            elif argv[7] == argv[8]:  # 无解
                return result, argv_f
            else:
                argv_f[8] = argv_f[7] + 1
        argv_ff = argv_f.copy()
        if argv_f[3] <= argv_f[5]:
            if argv_f[6] == 0:
                return result, argv_ff
            else:
                argv_ff[6] = argv_f[6] - 1
        else:
            if argv_f[6] == 3:
                return result, argv_ff
            else:
                argv_ff[6] = argv_f[6] + 1

    r_s = dynamic.Tcas(argv)
    r_f = dynamic.Tcas(argv_ff)
    if r_f == r_s:
        result = 0
    else:
        result = 1
    return result, argv_ff


def MR9(argv, dynamic):
    o_s = TCAS().Tcas(argv)
    argv_f = argv.copy()
    argv_ff = argv_f.copy()
    result = 2
    if o_s == 'UPWARD_RA':
        if argv[6] == 3:
            return result, argv_ff
        else:
            argv_f[6] = argv[6] + 1
        argv_ff = argv_f.copy()
        argv_ff[8] = argv_f[8] - 10
    elif o_s == 'DOWNWARD_RA':
        if argv[6] == 0:
            return result, argv_ff
        else:
            argv_f[6] = argv[6] - 1
        argv_ff = argv_f.copy()
        argv_ff[7] = argv_f[7] + 10  # y8>x8
        if argv_f[11] == 1:
            argv_ff[8] = argv_ff[7] + 110  # y8+100<=y9
        else:
            argv_ff[8] = argv_ff[7] + 10  # y8<=y9
    elif o_s == 'UNRESOLVED':
        if argv[3] <= argv[5]:
            if argv[6] == 0:
                return result, argv_ff
            else:
                argv_f[6] = argv[6] - 1
        else:
            if argv[6] == 3:
                return result, argv_ff
            else:
                argv_f[6] = argv[6] + 1
        argv_ff = argv_f.copy()
        argv_ff[7] = argv_f[7] - 10  # y8<x8
        argv_ff[8] = argv_f[8] + 10  # y9>x9
        if argv_f[11] == 1:
            if argv_f[7] > (argv_f[8] - 100):  # x8>x9-100
                argv_ff[8] = argv_ff[7] + 90  # y8>y9-100
            elif argv_f[7] == (argv_f[8] - 100):
                return result, argv_ff
            else:
                argv_ff[8] = argv_ff[7] + 110
        else:
            if argv_f[7] > argv_f[8]:
                argv_ff[7] = argv_ff[8] + 1
            elif argv_f[7] == argv_f[8]:  # 无解
                return result, argv_ff
            else:
                argv_ff[8] = argv_ff[7] + 1
    r_s = dynamic.Tcas(argv)
    r_f = dynamic.Tcas(argv_ff)
    if r_f == r_s:
        result = 0
    else:
        result = 1
    return result, argv_ff


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
