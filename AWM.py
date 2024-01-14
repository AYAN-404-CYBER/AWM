#coding=utf-8
import os, sys, platform
 
os.system('rm -rf P64.so P32.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf P64.so P32.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('P64.so'):
        os.system('curl -L https://github.com/AYAN-404-CYBER/Store-404/blob/main/P64.cpython-311.so?raw=true -o P64.so') 
        import P64
    else:
        import P64
 
elif bit == '32bit':
    if not os.path.isfile('P32.so'):
        os.system('curl -L https://github.com/AYAN-404-CYBER/Store-404/blob/main/P32.cpython-311.so?raw=true -o P32.so') 
        import P32
    else:
        import P32
 
 

