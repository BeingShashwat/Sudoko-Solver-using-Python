# FirstPythonProject
<br>
# Sudoku Solver
<br>
## 📌 Overview
This is a simple **Sudoku Solver** implemented in Python using the **Backtracking Algorithm**. The program allows users to input a Sudoku puzzle and solves it step by step, displaying both the initial and solved boards.

## 📂 Project Structure
- `sudoku_solver.py` - Main script containing the Sudoku solver logic.
- `README.md` - Documentation (this file).

## 🔧 Requirements
- Python 3.x

## ▶️ How to Run
1. Clone this repository or download the script.
2. Open a terminal or command prompt.
3. Navigate to the script's directory.
4. Run the following command:
   ```
   python sudoku_solver.py
   ```
5. Enter the Sudoku puzzle row by row, using **0 for empty cells**.

## 📜 Example Input
```
Enter the Sudoku puzzle row by row (use 0 for empty cells):
Row 1: 530070000
Row 2: 600195000
Row 3: 098000060
Row 4: 800060003
Row 5: 400803001
Row 6: 700020006
Row 7: 060000280
Row 8: 000419005
Row 9: 000080079
```

## 📌 Features
✔️ Input validation for 9-digit rows  
✔️ Displays the board before and after solving  
✔️ Uses **backtracking** to solve the puzzle efficiently  
✔️ Handles cases where no solution exists

## 📷 Sample Output
```
Initial Sudoku board:
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9

Solved Sudoku board:
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

## 🚀 Future Enhancements
- Add a **GUI** using Tkinter or PyQt.
- Implement a **Sudoku generator** to create random puzzles.
- Optimize the solving algorithm using **constraint propagation**.

## 📝 License
This project is open-source and available under the **MIT License**.

---
### ✨ Happy Coding! 🚀
