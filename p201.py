import autoload
import sys
sys.setrecursionlimit(9)
N,M = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort(reverse=True)

print(arr)


for i in range(arr[0]):
  # print(i)
  newarr =[x-i if x>i else 0 for x in arr]
  # print (newarr)
  mysum = sum(newarr)
  
  if(mysum == M):
    print (i)
    break
  # print(mysum)

start = 0
end = arr[0]

result = 0 
while (start<=end):
  mid = (start+end)//2
  newarr =[x-mid if x>mid else 0 for x in arr]
  print (newarr)
  mysum = sum(newarr)
  
  if(mysum == M):
    print("Found")
    print (mid)
    break
  elif mysum>M:
    start = mid+1
  elif mysum<M:
    end=mid-1
  