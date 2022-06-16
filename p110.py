import sys
from pathlib import Path
inputname = Path((sys.argv[0])).stem+"_input.txt"
sys.stdin = open(inputname,'r')


mydic = {'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}

N=int(input())
data = input().split()
x,y = 1,1
for d in data:
  my=mydic[d]
  # print (my[0] , my[1])
  if(x+my[0]>0 and y+my[1]>0):
    x+=my[0]
    y+=my[1]

print(x,y)

