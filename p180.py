import sys
from pathlib import Path
inputname = Path((sys.argv[0])).stem+"_flywithu.txt"
sys.stdin = open(inputname,'r')

N=int(input())
array = []
for _ in range(N):
  line = input().split()
  
  array.append((line[0],line[1]))

array = sorted(array,key=lambda studend:studend[1])

print(array)