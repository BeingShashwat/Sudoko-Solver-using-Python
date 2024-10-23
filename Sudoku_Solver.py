#Input Function
def get_sudoku_input():
    
    board = []
    print("Enter the Sudoku puzzle row by row (use 0 for empty cells):")
    
    for i in range(9):
        while True:
            try:
                row = input(f"Row {i + 1}: ")
                #Checking of INput
                if len(row) == 9 and all(c.isdigit() for c in row):
                    board.append([int(c) for c in row])
                    break
                else:
                    print("Invalid input. Please enter exactly 9 digits (0-9).")
            except ValueError:
                print("Please enter valid integers.")
                
    return board

#Board Print Function
def display(board):
    
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

#Checking if it is safe to put a number in empty cell
def is_safe(board, row, col, num):
    
    #Checking the row
    for x in range(9):
        if board[row][x] == num:
            return False

    #Checking the column
    for x in range(9):
        if board[x][col] == num:
            return False

    #Checking the 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

#Solving by backtracking method
def solve_sudoku(board):
    
    empty = find_empty_location(board)
    if not empty:
        return True  #Puzzle solved
    row, col = empty

    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  #Reset

    return False

#Finding empty locations
def find_empty_location(board):

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j) 
    return None

#Main function
if __name__ == "__main__":
    board = get_sudoku_input()

    print("\nInitial Sudoku board:")
    display(board)

    if solve_sudoku(board):
        print("\nSolved Sudoku board:")
        display(board)
    else:
        print("No solution exists.")