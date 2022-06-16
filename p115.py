import sys
from pathlib import Path
inputname = Path((sys.argv[0])).stem+"_flywithu.txt"
sys.stdin = open(inputname,'r')

pos = list(input())
# print (pos)
x = ord(pos[0])-ord('a')+1
y= int(pos[1])
moves= [(2,-1),(2,1),(-2,-1),(-2,1),(1,-2),(1,2),(-1,-2),(-1,2)]

count = 0
for dx,dy in moves:
  if(8>(x+dx)>0 and 8>(y+dy)>0):
    count+=1

print(count)

# print(x,y)
