import random
import os

def initialize_board():
    return [[0] * 4 for _ in range(4)]

def add_new_tile(board):
    empty_tiles = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if not empty_tiles:
        return
    i, j = random.choice(empty_tiles)
    board[i][j] = 2 if random.random() < 0.9 else 4

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in board:
        print("\t".join(str(num) if num != 0 else '.' for num in row))
    print()

def can_merge(a, b):
    return a == b

def slide_and_merge_row_left(row):
    new_row = [num for num in row if num != 0]
    new_row += [0] * (4 - len(new_row))

    for i in range(3):
        if can_merge(new_row[i], new_row[i + 1]):
            new_row[i] *= 2
            new_row[i + 1] = 0

    new_row = [num for num in new_row if num != 0]
    new_row += [0] * (4 - len(new_row))
    return new_row

def move_left(board):
    new_board = [slide_and_merge_row_left(row) for row in board]
    return new_board

def move_right(board):
    reversed_board = [list(reversed(row)) for row in board]
    new_board = [slide_and_merge_row_left(row) for row in reversed_board]
    return [list(reversed(row)) for row in new_board]

def move_up(board):
    transposed = list(zip(*board))
    new_board = [slide_and_merge_row_left(list(row)) for row in transposed]
    return [list(row) for row in zip(*new_board)]

def move_down(board):
    transposed = list(zip(*board))
    reversed_board = [list(reversed(row)) for row in transposed]
    new_board = [slide_and_merge_row_left(row) for row in reversed_board]
    return [list(row) for row in zip(*[list(reversed(row)) for row in new_board])]

def has_valid_moves(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return True
            if i < 3 and can_merge(board[i][j], board[i + 1][j]):
                return True
            if j < 3 and can_merge(board[i][j], board[i][j + 1]):
                return True
    return False

def check_win(board):
    for row in board:
        if 2048 in row:
            return True
    return False

def main():
    board = initialize_board()
    add_new_tile(board)
    add_new_tile(board)

    while True:
        print_board(board)
        
        if check_win(board):
            print("Congratulations! You have reached 2048!")
            break
        
        if not has_valid_moves(board):
            print("Game Over! No more valid moves.")
            break

        move = input("Enter move (w/a/s/d): ").strip().lower()
        
        if move == 'w':
            new_board = move_up(board)
        elif move == 'a':
            new_board = move_left(board)
        elif move == 's':
            new_board = move_down(board)
        elif move == 'd':
            new_board = move_right(board)
        else:
            print("Invalid move! Use 'w', 'a', 's', or 'd'.")
            continue
        
        if new_board != board:
            board = new_board
            add_new_tile(board)

if __name__ == "__main__":
    main()
