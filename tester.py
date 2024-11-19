
import os
import time
import filecmp

# Codes for veredicts
PENDING = 0
AC = 1
WA = 2
TLE = 3 
RTE = 4 

def haveSubtasks(ifile):
    return not (ifile.split('.')[1] == 'in')
       
def testAllCases(TestCasesFolder, sourceCode):
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

def testWithSubtasks(TestCasesFolder, sourceCode):
    IFolder = TestCasesFolder + '/input'
    OFolder = TestCasesFolder + '/output'

    OFiles = os.listdir(OFolder)
    IFiles = os.listdir(IFolder)

    worstTime = 0

    subtasks = 0
    subtaskPoints = [0]*15
    subtaskVeredict = [PENDING]*15

    for ifile in IFiles:
        ifile = ifile.split('.')
        subtask = int(ifile[1]) 
        subtaskValue = int(ifile[2])
        ifile = f'{ifile[0]}.{ifile[1]}.{ifile[2]}'

        if not f"{ifile}.out" in OFiles:
            continue
        if subtaskVeredict[subtask] != PENDING:
            continue

        subtasks = max(subtasks, subtask)
        subtaskPoints[subtask] = subtaskValue

        prevTime = time.time()
        returnValue = os.system(f"cat {IFolder}/{ifile}.in | timeout 1s {sourceCode}.o >| /tmp/ofiles/{ifile}.out")
        nextTime = time.time()

        if (nextTime - prevTime > 1):
            subtaskVeredict[subtask] = TLE
            continue
        if (returnValue != 0):
            subtaskVeredict[subtask] = RTE
            continue

        worstTime = max(worstTime, nextTime - prevTime)
        result = filecmp.cmp(f"/tmp/ofiles/{ifile}.out", f"{OFolder}/{ifile}.out")
        if subtask == 1:
            os.system(f'diff /tmp/ofiles/{ifile}.out {OFolder}/{ifile}.out')
        os.remove(f"/tmp/ofiles/{ifile}.out")

        if result == False:
            subtaskVeredict[subtask] = WA
    
    os.remove(f'{sourceCode}.o')
    points = 0

    for subtask in range(1, subtasks + 1):
        if subtaskVeredict[subtask] == PENDING:
            print(f'Subtask {subtask} AC, {subtaskPoints[subtask]} points')
            points += subtaskPoints[subtask]
        elif subtaskVeredict[subtask] == WA:
            print(f'Subtask {subtask} WA')
        elif subtaskVeredict[subtask] == TLE:
            print(f'Subtask {subtask} TLE')
        elif subtaskVeredict[subtask] == RTE:
            print(f'Subtask {subtask} RTE')

    print(f'Total Score: {points}')

    return [points, worstTime]

def RunTests(TestCasesFolder, sourceCode):
    IFiles = os.listdir(TestCasesFolder + '/input')
    if haveSubtasks(IFiles[0]):
        testWithSubtasks(TestCasesFolder, sourceCode)
    else:
        testAllCases(TestCasesFolder, sourceCode)    
