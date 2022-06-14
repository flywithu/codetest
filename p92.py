
# import fileinput
import os
import sys
sys.stdin = open('p92_input.txt','r')
  
# Using fileinput.input() method

n,m,k=map(int,input().split())
data =sorted(list(map(int,input().split())),reverse=True)
n1 = data[0]
n2 = data[1]
result = 0
count = 0
while(count<m):
  count+=1
  if(count%k == 0):
    result +=n2
  else:
    result +=n1

print(result)

  
  