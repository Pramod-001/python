bidding = {}
auct = True
def maxbid(bidding) :
    
    win = ""
    
    max(bidding)
    for i in bidding:
        highest =0
        if bidding[i] > highest  :
            highest = bidding[i]
            win = i
    print(f"Highest bidder is {i} and amount is ${highest}")
 
while auct == True :
    name = input("Enter name of the Person : ")
    bid = int(input("Enter the bid amount : "))
    bidding[name] = bid
    choice = input("Any other bidders left (yes or no) : ").lower()
    
    if choice == "no" :
        auct = False
        maxbid(bidding)
    elif choice == "yes" :
        print("\n" *50)
        
            
            
    