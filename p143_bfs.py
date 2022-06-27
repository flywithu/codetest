from collections import deque



def bfs(graph,v,visited):
  myque = deque([v])
  visited[v]=True
  while myque:
    myv = myque.popleft()
    print(myv,end=",")

    
    for i in graph[myv]:
      if visited[i]==False:
        visited[i]=True
        myque.append(i)
        


#1,2,3,8,7,4,5,6,
        
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

bfs(graph,1,visited)

  # myque = deque([v])
  # visited[v]=True
  # while myque:
  #   myv = myque.popleft()
  #   print(myv,end=",")
  #   for i in graph[myv]:
  #     if not visited[i]:
  #       myque.append(i)
  #       visited[i]=True