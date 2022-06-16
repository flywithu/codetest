import sys
from pathlib import Path
inputname = Path((sys.argv[0])).stem+"_flywithu.txt"
sys.stdin = open(inputname,'r')

n,m = map(int,input().split())
x,y,z=map(int,input().split())
#북동남서
direction = [(0,-1),(1,0),(0,1),(-1,0)]

mymap=[]

print(n,m)
for _ in range(m):
  mymap.append(list(map(int,input().split())))
  
# mydir = z  # map.append([list(map(int,input()))])
count = 1
mymap[x][y]=1
turncount = 0

while True:
  # print(f"z:{z}")
  z=z-1
  turncount+=1
  if(z<0):
    z=3
  x1 = x+direction[z][0]
  y1 = y+direction[z][1]
  
  if(mymap[x1][y1]==0 and x1>=0 and x1<n and y1>=0 and y1<m):
    x=x1
    y=y1
    count+=1
    turncount = 0
    mymap[x1][y1]=1 
    print(x1 , y1)
# 3->1
# 2->0
# 1->2
# 0->3
  
  if(turncount >=4):
    mytemp=(z-2) if z>=2 else (3-z)
    x1 = x+direction[mytemp][0]
    y1 = y+direction[mytemp][1]
    if(mymap[x1][y1]==0 and x1>=0 and x1<n and y1>=0 and y1<m):
      x=x1
      y=y1
      count+=1
      turncount = 0
      mymap[x1][y1]=1 
      print(f"back: {x1} {y1}")
    else:
      break

print(count)
  
  
    
  


  
  
