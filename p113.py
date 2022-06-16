import sys
from pathlib import Path
inputname = Path((sys.argv[0])).stem+"_flywithu.txt"
sys.stdin = open(inputname,'r')

N=int(input())
count = 0
for hour in range(N+1):
  for minute in range(60):
    for second in range(60):
      time=f"{hour:00d}{minute:0}{second:0}"
      if '3' in time:
        # print(time)

        count +=1
print(count)