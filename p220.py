import autoload
N=int(input())
data = list(map(int,input().split()))

dp=[0]*101
dp[1]=data[0]
dp[2]=max(data[0],data[1])
for i in range(3,N):
  print(i)
  dp[i]=max(data[i]+data[i-2],data[i-1])
  

print(data)
print(dp[N-1])