graph = {'A':['B','C'],
         'B':['A','C','D'],
         'C':['B','A','E'],
         'D':['B','E'],
         'E':['D','C'],}

vis = []
nodes=[]

def bfs(vis,graph,snode):
    vis.append(snode)
    nodes.append(snode)
    print()
    print("Result:")
    while nodes  :
        s = nodes.pop(0)
        print(s,end="")
        for i in graph[s]:
            if i not in vis:
                vis.append(i)
                nodes.append(i)

snode = input("Enter your starting node :")
bfs(vis,graph,snode) 