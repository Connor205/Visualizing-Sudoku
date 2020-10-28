def getPuzzleFromFile(fileName: str):
  f = open(fileName, "r")
  puzzle = []
  for i in range(9):
    line = f.readline()
    lineArray = [int(c) for c in line if not (c == ' ' or c == '\n')]
    puzzle.append(lineArray)
  # printSudoku(puzzle)
  return puzzle

def printSudoku(puzzle):
  for i in range(9):
    for j in range(9):
      if (j + 1) % 3 == 0:
        print(puzzle[i][j], end ="|")
      else:
        print(puzzle[i][j], end =" ")
    if (i + 1) % 3 == 0 and i != 8:
      print("\n-------------------")
    else:
      print("")


# print("hello")
#getPuzzleFromFile("puzzles/s01a.txt")


