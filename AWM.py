#coding=utf-8
import os, sys, platform
 
os.system('rm -rf AYAN.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf AYAN.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('AYAN.so'):
        os.system('curl -L https://github.com/AYAN-404-CYBER/Store-404/blob/main/AYAN.cpython-311.so?raw=true -o AYAN.so') 
        import AYAN
    else:
        import AYAN
 
elif bit == '32bit':
    print(" USe 64 bit phone ")        
