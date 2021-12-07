import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "04_input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

lotteriSeries = []
boards = []
readSeries = 1
with open(abs_file_path) as f:
    lines = f.readlines()
    board = []
    for line in lines:
        if(readSeries == 1):
            _l = line.strip().split(",")
            for x in _l:
                lotteriSeries.append(x)
            readSeries = 0
        else:
            if(len(line) <= 1 ): #Board ending
                if len(board) > 1:
                    boards.append(board)
                    board = []
            else:
                _l = line.strip().split(" ")
                row = []
                for x in _l:
                    if(x.isnumeric()):
                        rowValue = [x,0]
                        row.append(rowValue)
                board.append(row)
    boards.append(board)

#print(lotteriSeries)      

isBingo = []
lastNumber = 0
hasWon = []
for numb in lotteriSeries:
        if len(isBingo) < 1: 
            for board_index,board in enumerate(boards):
                if board_index not in hasWon:
                    for row_index,board_row in enumerate(board):
                        if [numb,0] in board_row:
                            #print("Found:", numb, board_row)
                            isFullRow = 0
                            isFound = False
                            column = 0
                            for columnIndex,x in enumerate(board_row):
                                if x[0] == numb:
                                    x[1] = 1
                                    column = columnIndex
                                    isFound = True
                                if x[1] == 1:
                                    isFullRow += 1
                            if isFullRow == 5:
                                print("BINGO! ROW.", row_index,column, board_index)
                                if board_index not in hasWon and len(hasWon) < len(boards)-1:
                                    hasWon.append(board_index)
                                else:
                                    if board_index not in hasWon:
                                        print("LAST Bingo. ROW!", row_index, column, board_index)
                                        isBingo = board
                                        lastNumber = numb
                            if (board[0][column][1] == 1
                                and board[1][column][1] == 1
                                and board[2][column][1] == 1
                                and board[3][column][1] == 1
                                and board[4][column][1] == 1
                                and isFound == True):
                                    print("Bingo. COLUMN!", row_index, columnIndex, board_index)
                                    if board_index not in hasWon and len(hasWon) < len(boards)-1:
                                        hasWon.append(board_index)
                                    else:
                                        if board_index not in hasWon:
                                            print("LAST Bingo. COLUMN!", row_index, column, board_index)
                                            isBingo =board
                                            lastNumber = numb

#for board_index,board in enumerate(boards):
#    if board_index not in hasWon:
#        print("Last board: ",board_index)
#        isBingo = board
#        break
print(isBingo[0])
print(isBingo[1])
print(isBingo[2])
print(isBingo[3])
print(isBingo[4])
sumMarked = 0
sumNonMarked = 0
for row in isBingo:
    for cell in row:
        if cell[1] == 1:
            sumMarked += int(cell[0])
        else:
            sumNonMarked += int(cell[0])
print("Marked:",sumMarked)
print("NonMarked:",sumNonMarked)
print("LastNumber drawn:",lastNumber)
print("Result:", sumNonMarked*int(lastNumber))
