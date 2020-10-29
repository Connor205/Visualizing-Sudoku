# Visualizing-Sudoku
The goal of this project was to implement a recursive backtracking implementation to solve any sudoku puzzle.  
In addition I wanted to create a visual interface to show how recursive backtracking works. 
The video below is an example of a simple sudoku puzzle being solved by my alorithm. 
![Demo Video (s01b.gif)](https://github.com/Connor205/Visualizing-Sudoku/blob/main/videos/s01b.gif)

# My Proccess
## Step 1: Getting the Puzzles
I started this project by developing a way to read sudokus in from a file into a 2D matrix. This would allow me to test my code on any sudoku scraped from the web.  
I then scraped a multitude of sudokus from the web into 9 by 9 text files where 0s represented empty squares. These puzzles can be found in [puzzles](/puzzles). 
## Step 2: Solving the puzzles
The second part of the project was implementing the recursive backtracking algorithm to solve any puzzle.  
Simple enough, first find an empty square and check if it is 0. If it is 0 then check if 1 works. If it does then place 1 in the position and then recur. If one does not work, or the algorithm is unable to solve with a 1 in that position then try 2. Then try 3. If none work then return false and backtrack. 
Once the algorithm is finished check to see if it returned true. If it did then print the new solved puzzle to the console, otherwise print that the puzzle was unsolveable.
## Step 3: Basic Graphics
As I had not worked with graphics much as part of my previous python experiences I choose a fairly simple graphics libarary, [graphics.py](graphics.py).  
This was good enough for my purposes as I did not want to draw any animations or do complex shapes. Sudoku is a fairly easy game to draw with simple shapes.   
Once I had tested the graphics libarary some [(here)](graphicsTesting.py) and learned how the user interaction functioned I got to work drawing the board. My first iteration consisted of a simple 9x9 grid where each box had an outline and there was nothing but the board itself. I created a drawBlock function that would take in the row, col, val and color which was supposed to be drawn there. Once that drew the boxes and the text in the correct space drawing the board consisted of me iterating through the grid and drawing each value with its row and col value.  
I then made the whole display look more appealing by adding in some offsets and making the whole board look more like sudoku. I also added a header where it shows the current file name. 
## Step 4: Animation
The next step was to show the algorithms progress visually. I could display the board before and after the solution, but I had to create a way to show the algorithms progress. I implemented this step by redrawing the block every time the algorithm guessed a value for a given spot on the board. Then every time the algorithm had to backtrack I had it paint the spot as red. 
## Step 5: UI
The final step was adding the UI for the different buttons. I started off by making a title screen where the user can input the file name they would like to test. Clicking anywhere on the screen then brought you to the setup where you could see the original board displayed. I then implemented a contains method which took in a rectangle and a point, both objects from graphics.py, and told me if that point was inside the given rectangle. This method was then used in combination with a while loop to wait for the user to press a button. The functions solve, steps, reset and newfile were all added. 
Solve: Solves the puzzle asap and displays the solution.
Steps: Shows the steps the algorithm took to make it to the solution and then the final solution. 
Reset: Clears board back to original state. 
Newfile: Clears the board of everything and returns to the original menu.\
