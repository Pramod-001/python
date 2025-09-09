def add(a,b) :
    return a+b
def sub(a,b) :
    return a-b
def mult(a,b) :
    return a*b
def div(a,b) :
    return a/b
def mod(a,b) :
    return a%b


cont = True
op = { 
    "+" :"add",
    "-" :"sub",
    "*" :"mult",
    "/" :"div",
    "%" :"mod",
}

while cont == True :
    
    num1 = int(input("Enter 1st number : "))
    for i in op :
        print(i)
    operation = input("Pick an Operation : ") 
    num2 = int(input("Enter 2nd number : "))
    if operation == "+" :
        result = add(num1,num2)
        print(result)
    
    elif operation == "-" :
        result = sub(num1,num2)
        print(result)
    
    elif operation == "*" :
        result = mult(num1,num2)
        print(result)
    
    elif operation == "/" :
        result = div(num1,num2)
        print(result)
    
    elif operation == "%" :
        result = mod(num1,num2)
        print(result)
    
    ct = input("Do you want to continue (y/n) : ").lower()
    if ct == "n":
        print("Process Completed")
        cont = False 

       
    