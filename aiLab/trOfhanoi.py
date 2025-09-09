def tower(n,s,aux,des):
    if n==1 :
        print(f"Move from {s} to {des}")
        return 
    
    tower(n-1,s,des,aux)
    
    print(f"Move from {s} to {des}")
    
    tower(n-1,aux,s,des)

n = 3
tower(n,'A','B','C')