def dfs(graph,v,visited):
  print(v,end=",")
  visited[v]=True
  for l in graph[v]:
    if visited[l] == False:
      dfs(graph,l,visited)
# 1,2,7,6,8,3,4,5

graph=[
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False]*9

dfs(graph,1,visited)



  # mystack = []
  # mystack.append(v)
  # myv = mystack.pop()
  # print(myv,end=",")
  # visited[myv]=True
  # for l in graph[myv]:
  #   if visited[l]==False:
  #     dfs(graph,l,visited)