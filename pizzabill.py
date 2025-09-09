print("Welcome to Pizza Counter ")
size = input("Enter size of ur pizza (S or M or L) :  ")
pep = input("Want to add extra Pepperoni(Y or N) :  ")
cheese =  input("Want to add extra Cheese(Y or N) :  ")
bill=0
if size == "S" :
    bill += 10
    print(f"Bill for pizza : ${bill}")
    if pep =="Y" :
        bill +=2
    if cheese =="Y" :
        bill +=1
    print(f"Total bill = ${bill}") 
    
if size == "M" :
    bill += 15
    print(f"Bill for pizza : ${bill}")
    if pep =="Y" :
        bill +=3
    if cheese =="Y" :
        bill +=1
    print(f"Total bill = ${bill}") 
    
if size == "L" :
    bill += 20
    print(f"Bill for pizza : ${bill}")
    if pep =="Y" :
        bill +=3
    if cheese =="Y" :
        bill +=1
    print(f"Total bill = ${bill}") 
    
