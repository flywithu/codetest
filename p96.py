import sys

from pathlib import Path

inputname = Path((sys.argv[0])).stem+"_input.txt"

sys.stdin = open(inputname,'r')
print ("inputname:"+inputname)
# Using fileinput.input() method

n,m=map(int,input().split())
result = []
for _ in range(n):
  row = sorted(list(map(int,input().split())))
  
  result.append(row[0])
result.sort(reverse=True)
print(result[0])