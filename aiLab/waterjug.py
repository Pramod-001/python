def water(cap1,cap2,target):
    vis = set()
    path = []

    def dfs(j1,j2):
        if(j1,j2) in vis :
            return False
        vis.add((j1,j2))
        path.append((j1,j2))
        
        if j1==target or j2 == target :
            return True
        
        if dfs(3,j2):
            return True
        if dfs(j1,5):
            return True
        if dfs(0,j2):
            return True
        if dfs(j1,0):
            return True
        if dfs(max(0,j1-(5-j2)),min(5,j1+j2)):
            return True
        if dfs ((min(3,j1+j2)),max(0,j2-(3-j1))):
            return True
        
        path.pop()
        return False
    dfs(0,0)
    
    return path

cap1=3
cap2=5
target =4

sol = water(cap1,cap2,target)
if sol :
    print("Solution :")
    for i in sol :
        print(i)
else :
    print("Solution Not found")