# Simple Checker for Linux

This Checker takes a cpp source file, compile it and run against some test cases.
The test cases must be specified as the folder that contains them, separated into subfolders 'input' ans 'output' in lowercase.

As example: 

```
|- /my-pc/home/my-user/ProblemTestCases
|   |- input
|   |   |- 001.in
|   |   |- 002.in
|   |   |- 003.in
|   |- output 
|   |   |- 001.out
|   |   |- 002.out
|   |   |- 003.out

```

The folder you must pass as parameter is ```/my-pc/home/my-user/ProblemTestCases```

## How to use

Just execute it as other python file: 

```python3 checker.py```

Then follow the CLI instructions.

## Features? 
Probably I will take time to make easy to mount as web service, just like an API (IDK). 