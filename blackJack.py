import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
def draw():
    c = random.choice(cards)
    return c  
def add(cards) :
    if sum(cards) == 21 and len==2 :
        return 0
    elif 11 in cards and sum(cards)>21 :
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(uscore,cscore) :
    if uscore == cscore :
        print("Game is Drawn")
    elif cscore ==0 :
        print("You Lose , Computer won with BlackJack")
    elif uscore ==0 :
        print("You Win with a BlackJack")
    elif uscore>21:
        print("Your Score went over 21 , You Lose ")
    elif cscore>21:
        print("Computer Score went over 21 , You Win ")
    elif uscore>cscore :
        print("You Win ")
    else :
        print("You Lose")
        
game = True
user = []
comp = []
play = input("Do you want to play The BlackJack Game \n(Y/N) : ").lower()
if play == "y" :
    game =True 
else :
    game = False
for i in range(2):
    new = draw()
    user.append(new)
    comp.append(draw()) 
while game ==True :
    uscore = add(user)
    cscore = add(comp)

    print(f"Your cards are :{user}\nCurrent Score is : {uscore}")
    print(f"Computer first card is :{comp[0]}")

    ch = input("Do you want to draw a new card (y/n) : ").lower()
    if ch == "y" :
        user.append(draw())
    else:
        game=False

while cscore!=0 and cscore < 17 :
    comp.append(draw())
    cscore = add(comp)

print(compare(uscore,cscore))

