import random
def game () :
    num = [1,2,3,4,5,6,7,8,9,10]
    print("Welcome to Number Guessing Game \n")
    print("Computer is thinking of a number guess it !")
    mode = input("How do you want to play the level(Easy or Hard) : ").lower()

    if mode =="easy" :
        turns =10
    elif mode =="hard" :
        turns = 5
    comp = random.choice(num)

    def check (guess,num) :
        if guess > num :
            print("Too High")
            turns-=1
            print(f"Remaining turns left are {turns}")
        elif guess < num :
            print("Too Low")
            turns-=1
            print(f"Remaining turns left are {turns}")
        else :
            print("Tou have guessed the correct number")
    uchoice = 0
    while uchoice != comp  :        
        uchoice = int(input("Enter ur choice of number from 1 to 10  : "))
        check(uchoice , comp)
        if turns ==0 :
            return()
game()