import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "04_input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

#lanternFish = [3,4,3,1,2]
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
                    print(board)
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
for numb in lotteriSeries:
    for board in boards:
        if len(isBingo) < 1:
            for row_index,board_row in enumerate(board):
                
                if [numb,0] in board_row:
                    #print("Found:", numb, board_row)
                    isFullRow = 0
                    for columnIndex,x in enumerate(board_row):
                        if x[0] == numb:
                            x[1] = 1
                        if x[1] == 1:
                            isFullRow += 1
                            column = columnIndex
                    if isFullRow == 5:
                        print("BINGO! ROW.", row_index,columnIndex)
                        isBingo = board
                        lastNumber = numb
                    if(board[0][columnIndex][1] == 1
                        and board[1][columnIndex][1] == 1
                        and board[2][columnIndex][1] == 1
                        and board[3][columnIndex][1] == 1
                        and board[4][columnIndex][1] == 1):
                            print("Bingo. COLUMN!", row_index, columnIndex)
                            isBingo = board
                            lastNumber = numb

                
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
