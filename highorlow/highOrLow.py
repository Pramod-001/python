import random
from data import data

data2 = random.choice(data)
print("Welcome to Higher or Lower Guessing Game ")
game = True
while game ==True :
    data1 = data2
    data2 = random.choice(data)

    if data1 == data2 :
        data2 = random.choice(data)
    
    name1 = data1["name"]
    j1 = data1["job"]
    p1 = data1["place"]
    f1 = data1["follow"]

    name2 = data2["name"]
    j2 = data2["job"]
    p2 = data2["place"]
    f2 = data2["follow"]
    cont = 0

    print(f"Comparing \n A : {name1} , {j1} from {p1} \n VS \n B : {name2} , {j2} from {p2}")

    uchoice = input("Enter your choice (A or B) : ").lower()

    if uchoice == 'a' and f1 > f2 :
        print("You have guessed right")
        cont +=1
        
    elif uchoice == 'b' and f2 > f1 :
        print("You have guessed right")
        cont+=1
        
    else :
        print("You have guessed wrong!") 
        print(f"Your Score is {cont}")
        game = False
