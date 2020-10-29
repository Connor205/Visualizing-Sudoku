from fileReading import *
from solvingSudoku import *
from graphics import *

blockWidth = 50
offset = 10
win = GraphWin('Sudoku', offset * 4 + blockWidth * 9 + 1, 200 + blockWidth * 9 + 1)

def drawBlock(row, col, val, color):
  verticalOffsets = row // 3 + 1
  verticalO = verticalOffsets * offset;
  horizontalOffsets = col // 3 + 1
  horizontalO = horizontalOffsets * offset
  upperLeft = Point(col * blockWidth, row * blockWidth)
  upperLeft.move(horizontalO, verticalO)
  bottomRight = Point((col + 1) * blockWidth, (row + 1) * blockWidth)
  bottomRight.move(horizontalO, verticalO)
  block = Rectangle(upperLeft, bottomRight)
  block.setFill(color)
  block.draw(win)
  if val != 0:
    textPoint = Point(col * blockWidth + blockWidth/2, row * blockWidth + blockWidth/2)
    textPoint.move(horizontalO, verticalO)
    numberImage = Text(textPoint, str(val))
    numberImage.draw(win)

def findNextEmptyGraphics(puzzle):
  for row in range(9):
    for col in range(9):
      if puzzle[row][col] == 0:
        return (row, col)
  return None

def DrawPuzzle(puzzle: list, color):
  for row in range(9):
    for col in range(9):
      if puzzle[row][col] == 0:
        drawBlock(row, col, puzzle[row][col], 'white')
      else:
        drawBlock(row, col, puzzle[row][col], color)

def solveWithGraphics(puzzle):
  time.sleep(0.25)
  """Summary

  Args:
      puzzle (matrix): The puzzle to solve

  Returns:
      TYPE: Description
  """
  firstEmpty = findNextEmptyGraphics(puzzle)
  if not firstEmpty: # If there are no empty spots left
    return True
  row, col = firstEmpty
  for val in range(1, 10):
    if canPlace(puzzle, row, col, val):
      puzzle[row][col] = val
      drawBlock(row, col, val, "light gray")

      if solveWithGraphics(puzzle):
        return True

      puzzle[row][col] = 0
      drawBlock(row, col, 0, color_rgb(247, 169, 151))
  return False

def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

def main():
  while(1):
    name = Text(Point(win.getWidth()/2, 40), "Welcome to the Sudoku Solver \n By Connor Nelson")
    instructions = Text(Point(win.getWidth()/2, win.getHeight()/2), "Then click anywhere on the screen")
    entry1 = Entry(Point(win.getWidth()/2, 200),10)
    filenamePrompt = Text(Point(win.getWidth()/2, 150),'Please type in a filename and extension to begin') # label for the Entry
    beginning = [name, instructions, entry1, filenamePrompt]
    for item in beginning:
      item.draw(win)
    win.getMouse()  # To know the user is finished with the text.
    filename = entry1.getText()

    clear(win)

    puzzle = getPuzzleFromFile("puzzles/" + filename)
    DrawPuzzle(puzzle, "light green")


    solveWithGraphics(puzzle)
    printSudoku(puzzle)
    DrawPuzzle(puzzle, color_rgb(76, 184, 46))
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
