menu = {
        "espresso" : { "ing" : {
                                    "water" : 50,
                                    "coffee" : 18,
                            },
                      "cost" : 15,
                    },
        
        "latte" : { "ing" : {
                                "water" : 200,
                                "milk" : 150,
                                "coffee" : 24,
                            },
                      "cost" : 25,
                    },
        
        "cappucino" : { "ing" : {
                                "water" : 250,
                                "milk" : 100,
                                "coffee" : 24,
                            },
                      "cost" : 30,
                    },
}
resources = {
    "water" : 400,
    "milk" : 200,
    "coffee" : 150,
}

def rsuff(ingredients) :
    for i in ingredients :
        if ingredients[i] >= resources[i] :
            print(f"Sorry! Not enough {i}")
            return False
    return True

def coins() :
    print("Insert coins ")
    one = int(input("Enter No.of One Rupee Coins : "))*1.0    
    two = int(input("Enter No.of Two Rupee Coins : "))*2.0
    five = int(input("Enter No.of Five Rupee Coins : "))*5.0
    ten = int(input("Enter No.of Ten Rupee Coins : "))*10.0   
    
    total = one +two + five + ten  
    return total
print("Welcome to Coffee Machine!")
off = True 
profit = 0
while off == True : 
    rmilk = resources["milk"]
    rwater = resources["water"]
    rcoffee = resources["coffee"]
    uchoice = input("Please enter your choice of coffee\nEspresso / Latte / Cappuccino : ").lower()

    if uchoice == "report" :
        print(f"Resources : \nMilk : {rmilk}ml\nWater : {rwater}ml\nCoffee : {rcoffee}gm \n Money : {profit}")

    elif uchoice =="off" :
        print("Coffee Machine is turned off")
        off = False 
    else :
        drink = menu[uchoice]
        if rsuff(drink["ing"]) :
            pay = coins()
            amount = drink["cost"]
            if pay > amount :
                print("Transaction Successfull ")
                change = pay - amount
                profit+=amount
                print(f"Here is your Order : {uchoice} Enjoy!!\n which is Rs {amount}")
                print(f"And Here is your Change of Rs {change}")
                for i in drink["ing"] :
                    resources[i] -= (drink["ing"])[i]
                
            elif pay == amount :
                print("Transaction Successfull ")
                profit+=amount
                print(f"Here is your Order : {drink} Enjoy !!\nwhich is Rs {amount}")
                for i in drink["ing"] :
                    resources[i] -= (drink["ing"])[i]
                    
            elif pay < amount :
                print("Transaction UnSuccessfull! Not Enough Money ")
                
                