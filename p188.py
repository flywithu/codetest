import sys
from pathlib import Path
inputname = Path((sys.argv[0])).stem+"_flywithu.txt"
sys.stdin = open(inputname,'r')


def bi_search(arr,target,start,end):
  # print (f"{start}  {end}")
  mid = (start+end)//2
  # print(f"{mid}")
  if  (end-start)<=1:
    return -1
  elif target < arr[mid]:
    return bi_search(arr,target,start,mid)
  elif target > arr[mid]:
    return bi_search(arr,target,mid,end)
  else:
    return mid



tc_count = int(input())
for _ in range(tc_count):
  n,m = map(int,input().split())
  myarr = []
  myarr.extend(list(map(int,input().split())))
  result = int(input())
  
  # print(myarr)
  if (result == (bi_search(myarr,m,0,n))):
    print ("PASS")
  else:
    print("Fail")
    