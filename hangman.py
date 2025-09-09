import random

words = ["hello","world","python"]
blank =""
final = []
lives = 6
rdchoice = random.choice(words)
print(rdchoice)
for i in rdchoice :
    blank += "_"
print(blank)
game = False
while not game:
    user = input("Guess a letter : ").lower()
    print(user)
    disp = ""
    
    for i in rdchoice :
        if i == user :
            disp += i
            final.append(i)
        elif i in final :
            disp += i
        else :
            disp += "_"
    print(disp)
    if user not in rdchoice :
        lives -=1
        if lives ==0 :
            game = True
            print("Game Over : You Lose ")

    if "_" not in disp :
        print("Game Over ")
        game = True
