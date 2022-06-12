open=[]
closed=[]
path = []
parent = {}
graph = {'A':['B','C'],
         'B':['D','E'],
         'C':['F','G'],
         'D':[],
         'E':[],
         'F':[],'G':[]}

def findpath(tar):
  global open,path
  while tar!='':
    path.append(tar)
    tar = parent[tar]

def BFS(tar, ptr):
  global open, closed, graph
  print('open : ',open[ptr:],'\nclosed : ',closed, "\n")
  if ptr >= len(open):
    return -1
  closed.append(open[ptr])
  if open[ptr]==tar:
    findpath(tar)
    return 1
  for child in graph[open[ptr]]:
    open.append(child)
    parent[child]=open[ptr]
  return BFS(tar,ptr+1)

open.append('A')
parent['A']=''
tar = input('Enter goal node : ')
BFS(tar,0)

if path==[]:
  print("Goal node not found")
else:
  path.reverse()
  BFSpath = '->'.join(path)
  print('Path : ',BFSpath)
