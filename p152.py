import sys
from pathlib import Path
inputname = Path((sys.argv[0])).stem+"_flywithu.txt"
sys.stdin = open(inputname,'r')

n,m = map(int,input().split())
graph = []
for _ in range(n):
  # print (input())
  graph.append(list(map(int,input())))

# print(graph)
# graph[n-1][m-1]=1

from collections import deque

def isPossible(x,y):
  if (x>=0 and y>=0 and x<n and y<m):
    if(graph[x][y]!=0):
      return True
  return False

dxy = ((-1,0),(1,0),(0,1),(0,-1))

# print(len(dxy))
def bfs(x,y):
  myque = deque()
  myque.append((x,y))
  
  while myque:
    x,y = myque.popleft()
    for i in range(len(dxy)):
      myx = x+dxy[i][0]
      myy = y+dxy[i][1]

      if(isPossible(myx,myy)):
         if(graph[myx][myy] == 1):
           # print(f"{myx} {myy}")
           graph[myx][myy]=graph[x][y]+1
           myque.append((myx,myy))
  
# def bfs(graph,x,y):
bfs(0,0)
print(graph)
print(graph[n-1][m-1])
