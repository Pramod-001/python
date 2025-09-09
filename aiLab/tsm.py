import itertools

dist = [[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
def tsp(dist):
    n =len(dist)
    city = list(range(n))
    minpath = None
    mincost = float('inf')
    
    for i in itertools.permutations(city[1:]):
        path = [0]+list(i)+[0]
        cost = 0
        for i in range(len(path)-1):
            cost +=dist[path[i]][path[i+1]]
        
        if cost<mincost:
            mincost = cost
            minpath = path
    return mincost,minpath
cost , path = tsp(dist)
print("Best route : ")

print(f"->",path)
print("Minimum cost : ",cost)