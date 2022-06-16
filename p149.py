import sys
from pathlib import Path
inputname = Path((sys.argv[0])).stem+"_flywithu.txt"
sys.stdin = open(inputname,'r')
graph = []

n,m = map(int,input().split())

for i in range(n):
  graph.append(list(map(int,input())))

dxy=[(-1,0),(1,0),(0,1),(0,-1)]
def isOutArea(x,y):
  global n,m
  if (x>=0 and x<n and y>=0 and y<m):
    return False
  else:
    return True

def fillarea(x,y):
  graph[x][y]=1
  for dx,dy in dxy:
    myx = x+dx
    myy = y+dy
    if(isOutArea(myx,myy) == False and graph[myx][myy] == 0):
      fillarea(x+dx,y+dy);
count = 0      
# print(graph)
for i in range(n):
  for j in range(m):
    if graph[i][j]==0:
      count +=1
      # print(graph)
      fillarea(i,j)

# print(graph)
print (count)