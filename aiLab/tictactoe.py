def printboard(board):
    for i in range(0,9,3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i<6 :
            print("_"*11)
    
def win(board,player):
    wincombo = [[0,1,2],[0,3,6],[0,4,8],[1,4,7],[3,4,5],[6,7,8],[2,5,8],[2,4,6]]
    
    for i in wincombo:
        if board[i[0]] == board[i[1]] == board[i[2]] == player :
            return True
    return False

def full(board):
    return " " not in board
def game():
    board = [" " for _ in range(9)]
    players =["X","O"]
    current = 0
    
    while True :
        printboard(board)
        player = players[current]
        
        move = int(input(f"Player {player} Enter your move (1-9):"))
        
        if 0<=move<=8 and board[move]==" " :
            board[move] = player
             
        else :
            print("Invalid move")

        if win(board,player):
            printboard(board)
            print(f"Player {player} wins")
            break
        elif full(board) :
            printboard(board)
            print("Its a draw")
            break  
        else :
            current = 1- current
if __name__ == "__main__"  : 
    game()