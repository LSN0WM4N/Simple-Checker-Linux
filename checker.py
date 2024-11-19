import os
import compiler
import tester

def Execute(Folder, SourceCode): 
    try:
        os.mkdir('/tmp/ofiles/')
    except Exception as e:
        pass

    compiler.Compile(SourceCode)
    tester.RunTests(Folder, SourceCode)

def AutomChecker(Folder):
    SourceCode = Folder + '/main'
    Execute(Folder, SourceCode)

def Checker(): 
    SourceCode = input('Enter the source code path without extension\n')
    Folder = input('Enter the path to the test case folder\n')
    Execute(Folder, SourceCode)
    
if __name__ == '__main__':
    Checker()