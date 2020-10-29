"""Summary

Attributes:
    blockWidth (int): Description
    offset (int): Description
    win (TYPE): Description
"""
from fileReading import *
from solvingSudoku import *
from graphics import *

blockWidth = 50
offset = 10
win = GraphWin('Sudoku', offset * 4 + blockWidth * 9 + 1, 200 + blockWidth * 9 + 1)


def drawBlock(row, col, val, color):
  """Summary

  Args:
      row (TYPE): Description
      col (TYPE): Description
      val (TYPE): Description
      color (TYPE): Description
  """
  verticalOffsets = row // 3 + 1
  verticalO = verticalOffsets * offset + 50;
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
  """Summary

  Args:
      puzzle (TYPE): Description

  Returns:
      TYPE: Description
  """
  for row in range(9):
    for col in range(9):
      if puzzle[row][col] == 0:
        return (row, col)
  return None

def DrawPuzzle(puzzle: list, color):
  """Summary

  Args:
      puzzle (list): Description
      color (TYPE): Description
  """
  for row in range(9):
    for col in range(9):
      if puzzle[row][col] == 0:
        drawBlock(row, col, puzzle[row][col], 'white')
      else:
        drawBlock(row, col, puzzle[row][col], color)

def solveWithGraphics(puzzle):
  """Summary

  Args:
      puzzle (TYPE): Description

  Returns:
      TYPE: Description
  """
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
      time.sleep(0.25)
  return False

def clear(win):
    """Summary
    Clears the window of all items (undraws them)
    Args:
        win (GraphWin): Description
    """
    for item in win.items[:]:
        item.undraw()
    win.update()

def rectangleContains(rect: Rectangle, p: Point):
  """Summary

  Args:
      rect (Rectangle): Description
      p (Point): Description

  Returns:
      TYPE: Description
  """
  x = p.getX()
  y = p.getY()
  return x >= rect.getP1().getX() and x <= rect.getP2().getX() and y >= rect.getP1().getY() and y <= rect.getP2().getY()

def main():
  """Summary
  """
  while(True):
    clear(win)
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
    shouldReset = False
    blankPuzzle = getPuzzleFromFile("puzzles/" + filename)
    puzzle = getPuzzleFromFile("puzzles/" + filename)
    DrawPuzzle(blankPuzzle, "light green")
    header = Text(Point(win.getWidth() / 2, 25), "Puzzle: " + filename)
    header.setSize(24)
    header.draw(win)

    buttonWidth = 100
    buttonHeight = 40
    solveButton = Rectangle(Point((win.getWidth() / 6) - (buttonWidth / 2), win.getHeight() - 65 - buttonHeight / 2),
                          Point(win.getWidth()/6+ buttonWidth / 2, win.getHeight() - 65 + buttonHeight / 2))
    solveText = Text(Point((win.getWidth() / 6), win.getHeight() - 65), "Solve")

    solveButton.draw(win)
    solveText.draw(win)

    steps = Rectangle(Point((win.getWidth() / 2) - (buttonWidth / 2), win.getHeight() - 65 - buttonHeight / 2), Point(win.getWidth() / 2 + (buttonWidth / 2), win.getHeight() - 65 + buttonHeight / 2))
    solveText = Text(Point((win.getWidth() / 2), win.getHeight() - 65), "Steps")

    steps.draw(win)
    solveText.draw(win)

    reset = Rectangle(Point((5 * win.getWidth() / 6) - (buttonWidth / 2), win.getHeight() - 90 - buttonHeight / 2),
                          Point(5 * win.getWidth()/ 6 + buttonWidth / 2, win.getHeight() - 90 + buttonHeight / 2))
    resetText = Text(Point((5 * win.getWidth() / 6), win.getHeight() - 90), "Reset")
    reset.draw(win)
    resetText.draw(win)

    newFile = Rectangle(Point((5 * win.getWidth() / 6) - (buttonWidth / 2), win.getHeight() - 40 - buttonHeight / 2),
                          Point(5 * win.getWidth()/ 6 + buttonWidth / 2, win.getHeight() - 40 + buttonHeight / 2))
    newFileText = Text(Point((5 * win.getWidth() / 6), win.getHeight() - 40), "New File")
    newFile.draw(win)
    newFileText.draw(win)
    while not shouldReset:
      userInput = win.getMouse()
      print(userInput)
      if rectangleContains(solveButton, userInput):
        print("solve")
        solve(puzzle)
        DrawPuzzle(puzzle, color_rgb(76, 184, 46))
        buttonPressed = True
      elif rectangleContains(steps, userInput):
        print("steps")
        solveWithGraphics(puzzle)
        if solve(puzzle):
          DrawPuzzle(puzzle, color_rgb(76, 184, 46))
        else:
          DrawPuzzle(puzzle, color_rgb(247, 169, 151))
        buttonPressed = True
      elif rectangleContains(reset, userInput):
        print("reset")
        buttonPressed = True
        DrawPuzzle(blankPuzzle, "light green")
        puzzle = getPuzzleFromFile("puzzles/" + filename)
      elif rectangleContains(newFile, userInput):
        print("newFile")
        clear(win)
        buttonPressed = True
        shouldReset = True
      else:
        buttonPressed = False
  win.close()


if __name__ == '__main__':
    main()
