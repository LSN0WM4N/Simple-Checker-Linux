import os

def Compile(sourceCodePath):
    if not (os.path.isfile(sourceCodePath + '.cpp')):
        print('[-] Source file does not exist')
        exit(1)

    os.system(f"g++ {sourceCodePath}.cpp -o {sourceCodePath}.o -Wall")

    if not (os.path.isfile(sourceCodePath + '.o')):
        print('[-] Compiling error')
        exit(1)

    print('[+] Compiled Succefully')