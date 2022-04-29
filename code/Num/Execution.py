import re
import os
import re

class MyEnv():
    def __init__(self):
        self.workspace_dir = "."
        self.inputs_dir = self.workspace_dir + "/input"
        self.outputs_dir = self.workspace_dir + "/output"
        self.results_dir = self.workspace_dir + "/result"

    def CreateWorkingDirs(self):
        self.checkDir(self.inputs_dir)
        self.checkDir(self.outputs_dir)
        self.checkDir(self.results_dir)

    def checkDir(self, dir):
        if not os.path.exists(dir):
            os.makedirs(dir)
            print("created dir of {}".format(dir))

class Input():
    def __init__(self, infile):
        self.setInfile(infile)

    def parseInfile(self):
        self.lines = self.getLines()

    def check_charset(self, file_path):
        import chardet
        with open(file_path, 'rb') as f:
            data = f.read()
        charset = chardet.detect(data)['encoding']
        return charset

    def getLines(self):
        file = open(self.infile, "r", encoding=self.check_charset(self.infile))
        lines = file.readlines()
        for i in range(len(lines)):
            lines[i] = str(lines[i])
        return lines

    def getInfile(self):
        return self.infile

    def setInfile(self, infile):
        env = MyEnv()
        self.infile = env.inputs_dir+"/{}".format(infile)

    def writeInfile(self):
        temp_file = open(self.infile, "w")
        temp_file.writelines(self.lines)
        temp_file.close()


class Output:
    def __init__(self, output):
        env = MyEnv()
        self.output_name = env.outputs_dir + "/{}".format(output)

    def parse(self):
        self.lines = self.getLines()

    def setResults(self, lines):
        self.lines = lines

    def check_charset(self, file_path):
        import chardet
        with open(file_path, 'rb') as f:
            data = f.read()
        charset = chardet.detect(data)['encoding']
        return charset

    def getLines(self):
        file = open(self.output_name, 'r', encoding=self.check_charset(self.output_name))
        lines = file.readlines()
        return lines

    def setInfile(self, infile):
        env = MyEnv()
        self.infile = env.inputs_dir+"/{}".format(infile)

    def writeInfile(self):
        temp_file = open(self.infile, "w")
        temp_file.writelines(self.lines)
        temp_file.close()

