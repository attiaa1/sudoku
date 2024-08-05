# Sudoku Game with Pygame [UNFINISHED]

## Last updated 3/15/2024

High level plan for the following:

Generate a Solvable Grid with Blank Spots Randomly:
- There are algorithms available online that can generate a solved Sudoku grid.
- Once you have a solved grid, you can randomly remove numbers from it to create a puzzle. The number of numbers you remove will determine the difficulty of the puzzle. Make sure to check that the puzzle still has a unique solution after each removal.

Allow the User to Enter Numbers into Blank Spots in the Grid:
- You can use Pygame’s event handling system to listen for mouse clicks. When the user clicks on a cell, you can highlight that cell and listen for keyboard input.
- When the user presses a number key, you can update the value of the highlighted cell with that number.

Check and Time the User’s Solution:
- You can create a function that checks if the current state of the grid is a valid Sudoku solution. This function should check that each row, column, and 3x3 square contains all of the numbers from 1 to 9 exactly once.
- You can call this function whenever the user enters a number. If the grid is a valid solution, you can display a message to the user indicating that they’ve solved the puzzle.
- To time the user’s solution, you can start a timer when the puzzle is first displayed to the user, and stop the timer when the user solves the puzzle.

Allow the Computer to Solve and Time Its Solution:
- You can implement a Sudoku solving algorithm, such as backtracking, that can solve the puzzle automatically.
- To time the solution, you can start a timer just before the algorithm starts, and stop the timer when the algorithm finds a solution.

Have the Option to Do Either of the Above:
- You can add a menu to your game that allows the user to choose between solving the puzzle themselves or having the computer solve it.
- This menu can be implemented using Pygame’s drawing and event handling capabilities.
