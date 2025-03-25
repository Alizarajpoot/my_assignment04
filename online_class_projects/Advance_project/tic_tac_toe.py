#project 4 tic tac toe

import random
# Tic-Tac-Toe Board
board = [" " for _ in range(9)]

def print_board():
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print("|".join(row))
        print("-" * 5)

# Check if someone has won
def check_winner(player):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

# Minimax Algorithm for AI
def minimax(is_maximizing):
    if check_winner("O"): return 1
    if check_winner("X"): return -1
    if " " not in board: return 0

    scores = []
    for i in range(9):
        if board[i] == " ":
            board[i] = "O" if is_maximizing else "X"
            scores.append(minimax(not is_maximizing))
            board[i] = " "
    
    return max(scores) if is_maximizing else min(scores)

# AI Move
def best_move():
    best_score, move = -float("inf"), None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score, move = score, i
    board[move] = "O"

# Game Loop
def play():
    print("Welcome to Tic-Tac-Toe! You are 'X', AI is 'O'.")
    print_board()
    
    while " " in board:
        try:
            user_move = int(input("Enter position (1-9): ")) - 1
            if board[user_move] == " ":
                board[user_move] = "X"
            else:
                print("Invalid move! Try again.")
                continue
        except:
            print("Enter a valid number!")
            continue
        
        if check_winner("X"):
            print_board()
            print("🎉 You win!")
            return
        
        print("AI is thinking...")
        best_move()
        print_board()
        
        if check_winner("O"):
            print("😢 AI wins! Better luck next time.")
            return
    
    print("It's a draw! 🤝")

play()
