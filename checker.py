import os
import time
import filecmp

def compile_and_check(sourceCodePath):
    if not (os.path.isfile(sourceCodePath + '.cpp')):
        print('[-] Source file does not exist')
        exit(1)

    os.system(f"g++ {sourceCodePath}.cpp -o {sourceCodePath}.o -Wall")

    if not (os.path.isfile(sourceCodePath + '.o')):
        print('[-] Compiling error')
        exit(1)

    print('[+] Compiled Succefully')

def test_all_cases(TestCasesFolder, sourceCode):
    IFolder = TestCasesFolder + '/input'
    OFolder = TestCasesFolder + '/output'

    OFiles = os.listdir(OFolder)
    IFiles = os.listdir(IFolder)

    ac = 0
    total = 0
    worstTime = 0

    for ifile in IFiles: 
        ifile = ifile.split('.')
        ifile = ifile[0]
        if not f"{ifile}.out" in OFiles:
            continue

        prevTime = time.time()
        returnValue = os.system(f"cat {IFolder}/{ifile}.in | timeout 1s {sourceCode}.o >| /tmp/ofiles/{ifile}.out")
        nextTime = time.time()

        if (nextTime - prevTime > 1):
            print('[+] Time limit exeded')
            os.remove(f'{sourceCode}.o')
            exit(1)
        if (returnValue != 0):
            print('[-] Runtime Error')
            os.remove(f'{sourceCode}.o')
            exit(1)

        worstTime = max(worstTime, nextTime - prevTime)
        result = filecmp.cmp(f"/tmp/ofiles/{ifile}.out", f"{OFolder}/{ifile}.out")

        total += 1
        if result == True:
            ac += 1

    if ac == 0:
        print(f"[-] Wrong Answer, 0 de {total}")
    else:
        print(f"Score: {(100 / total * ac):.2f}, {ac} of {total} [{worstTime:.3f}s]")
    os.remove(f'{sourceCode}.o')

    return [total, ac, worstTime]

def Execute(Folder, SourceCode): 
    try:
        os.mkdir('/tmp/ofiles/')
    except Exception as e:
        pass

    compile_and_check(SourceCode)
    test_all_cases(Folder, SourceCode)

def AutomChecker():
    Folder = input()
    SourceCode = Folder + '/main'
    Execute(Folder, SourceCode)

def Checker(): 
    SourceCode = input('Enter the source code path without extension\n')
    Folder = input('Enter the path to the test case folder\n')
    Execute(Folder, SourceCode)
    
if __name__ == '__main__':
    Checker()