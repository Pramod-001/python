graph = {'A' : ['B','C'],
         'B' : ['A','C','D'],
         'C' : ['A','C','E'],
         'D' : ['B','E'], 
         'E' : ['D','C'],}

vis = list()
def dfs(vis,graph,snode):
    if snode not in vis:
        print(snode,end="")
        vis.append(snode)
        
        for i in graph[snode]:
            dfs(vis,graph,i)

snode = input("Enter :")
dfs(vis,graph,snode)