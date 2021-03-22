import sys
import os
import sys
from io import BytesIO, IOBase
from collections import defaultdict as dt
import collections
import math 
import itertools


BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")



def multi(k,d0,d1):
    
    if k==2:
        if (d0+d1)%3==0:
            return 'YES'
            
        return 'NO'
        
    if k==3:
        if ((d0+d1)+(d0+d1)%10)%3==0:
            return 'YES'
            
        return 'NO'
        
    y=(d0+d1)%10
    
    if (k-3)%2==0 and (k-3)%4!=0 :
        t=(k-3)//4
        
        sum_=((2*y)%10+(4*y)%10+(8*y)%10+(6*y)%10)*t
        sum_+=(2*y)%10+(4*y)%10+y%10
                
    elif (k-3)%4==0:
        t=(k-3)//4
        
        sum_=((2*y)%10+(4*y)%10+(8*y)%10+(6*y)%10)*t
        sum_+=y%10
        
    elif (k-2)%2==0 and (k-2)%4!=0:
        t=(k-3)//4
        sum_=((2*y)%10+(4*y)%10+(8*y)%10+(6*y)%10)*t
        sum_+=(2*y)%10+y%10
        
    else:
        # print(1)
        t=(k-3)//4
        # print(t)
        sum_=((2*y)%10+(4*y)%10+(8*y)%10+(6*y)%10)*t
        sum_+=(2*y)%10+((4*y)%10)+(y%10)+((8*y)%10)
    
    sum_+=d0+d1
    
    # print(sum_)
    
    if (sum_)%3==0:
        return 'YES'
    else:
        return 'NO'

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        k,d0,d1=list(map(int,input().split()))
        print(multi(k,d0,d1))
        
    
        
        
