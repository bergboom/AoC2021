import os
script_dir = os.path.dirname(__file__) #<-- abso
rel_path = "05_input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

pointList = {}  #Dictonary with visited points

def addPoint(xCoord, yCoord):
    if (xCoord,yCoord) not in pointList:
        pointList[(xCoord,yCoord)] = 1
    else:
        _value = pointList[(xCoord,yCoord)]
        _value = _value +1
        pointList[(xCoord,yCoord)] = _value

def StoreLines(startPoint, endPoint):
    
    startXCoordinate = int(startPoint[0])
    startYCoordinate = int(startPoint[1])
    currentX = startXCoordinate
    currentY = startYCoordinate
    endXCoordinate = int(endPoint[0])
    endYCoordinate = int(endPoint[1])
    #if(startXCoordinate == endXCoordinate or startYCoordinate == endYCoordinate): #ADD THIS LINE FOR PART1
    addPoint(startXCoordinate,startYCoordinate)
    while (True):
        if(endXCoordinate > currentX):
            currentX += 1
        elif(endXCoordinate < currentX):
            currentX -=1
        if(endYCoordinate > currentY):
            currentY +=1
        elif(endYCoordinate < currentY):
            currentY -= 1
        addPoint(currentX, currentY)
        if(currentX == endXCoordinate and currentY == endYCoordinate):
            break

def parseInput(line: str):
    _l = line.strip().split(" -> ")
    #print(_l)
    return[_l[0].split(","),_l[1].split(",")]

with open(abs_file_path) as f:
    lines = f.readlines()
    for line in lines:
        #Parse Input and retrieve input coordinate-points
        coordinates = parseInput(line)
        startPoint = coordinates[0]
        endPoint = coordinates[1]
        StoreLines(startPoint,endPoint)

intersections = pointList.values()
#print(pointList)
cntIntersect = 0
for v in intersections:
    if v >= 2:
        cntIntersect += 1
print("Result: ",cntIntersect)
        

