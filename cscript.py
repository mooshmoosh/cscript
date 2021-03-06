#!/usr/bin/python3

import os, sys, random, re

def isFunctionDeclaration(line):
    return re.compile("\s*[\(\w\*\)]+\s+[^=\(]+\([^;\)]*\)").match(line)

def isIncludeLine(line):
    return re.compile("\s*#include").match(line)

def isTypedef(line):
    return re.compile("[\s]*typedef").match(line)

def fileIsNewerThan(filename1, filename2):
    if not os.path.exists(filename1):
        return False
    if os.path.exists(filename2):
        return False
    return os.stat(filename1).st_mtime >= os.stat(filename2).st_mtime 

def shouldBeMovedToTop(line):
    if isFunctionDeclaration(line):
        return True
    if isTypedef(line):
        return True
    if isIncludeLine(line):
        return True
    return False
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print ("usage: %s {script}" % sys.argv[0])
        exit()

    compileArguments = ""
    for index,a in enumerate(sys.argv):
        if a.startswith('--compiler-arguments="'):
            compileArguments = a[a.find('=') + 2:a.rfind('"')]
            sys.argv.pop(index)

    sourceFileName = sys.argv[1]
    commandLineArguments = " ".join(sys.argv[2:])

    (sourceDirectory, sourceFile) = os.path.split(sourceFileName)
    executableFileName = sourceDirectory + '/' + "." + sourceFile+ ".bin"

    if fileIsNewerThan(executableFileName, sourceFileName):
        os.system(executableFileName + " " + commandLineArguments)
        exit()
    
    with open(sourceFileName, "r") as file:
        scriptContents = file.read().splitlines()

    mode = "Normal"
    preMainLines = []
    processedLines = []
    braceFoldLevel = 0

    # remove the shebang
    if scriptContents[0].startswith('#!'):
        scriptContents = scriptContents[1:]

    for l in scriptContents:
        if mode == "Normal":
            if shouldBeMovedToTop(l):
                preMainLines.append(l)
                mode = "PRE_MAIN"
                braceFoldLevel = l.count("{") - l.count("}")
            else:
                processedLines.append(l)
        elif mode == "PRE_MAIN":
            preMainLines.append(l)
            braceFoldLevel += l.count("{") - l.count("}")
            if braceFoldLevel < 0:
                print("Error, mismatched {}")
                exit()
            if braceFoldLevel == 0:
                mode = "Normal"

    cfile = """//created with cscript
#include "stdio.h"
#include "stdlib.h"

"""
    cfile += "\n".join(preMainLines)
    cfile += """
int main(int argc, char** argv)
{
    """    

    cfile += "\n".join(processedLines)

    cfile += """
}
"""

    tmpfile = sourceDirectory + "/" + "." + sourceFile + ".c"

    with open (tmpfile, "w") as file:
        file.write(cfile)

    statusCode = os.system("gcc " + tmpfile + " " + compileArguments + " -o " + executableFileName)
    
    if not statusCode:
        os.system(executableFileName + " " + commandLineArguments)
