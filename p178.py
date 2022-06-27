import sys
from pathlib import Path
inputname = Path((sys.argv[0])).stem+"_flywithu.txt"
sys.stdin = open(inputname,'r')

N = int(input())
list=[]
for _ in range(N):
  list.append(int(input()))

print(sorted(list,reverse = True))