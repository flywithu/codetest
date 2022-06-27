import autoload
import sys
sys.setrecursionlimit(9)
N=int(input())

STOCKS=list(map(int,(input().split())))
STOCKS.sort()
M=int(input())
FINDS = map(int,input().split())

def find_bisect(arr,t,start,end):
  mid = (start+end)//2
  print(f"start {start} end {end}")
  print(mid)
  print(arr[mid])
  
  if arr[mid]==t:
    return mid
  elif end<=start:
    return -1
  elif t<arr[mid]:
    return find_bisect(arr,t,start,mid-1)
  elif t>arr[mid]:
    return find_bisect(arr,t,mid+1,end)
  else:
    return -1

result=[]
for i in FINDS:
  print(STOCKS)
  print(f"try: {i}")
  result.append(find_bisect(STOCKS,i,0,N))
print(result)