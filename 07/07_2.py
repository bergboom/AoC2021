import os
import math
from itertools import chain
from posixpath import split
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
positionDict = {}

def readFile(fileName: str):
    abs_file_path = os.path.join(script_dir, fileName)
    lines = []
    with open(abs_file_path) as f:
        inputLine = f.readlines()
        for line in inputLine:
            positions = line.strip().split(',')
            for pos in positions:
                lines.append(pos)
    return lines


def addPositionToDictionary(position: int):
    if position not in positionDict:
        positionDict[position] = 1
    else:
        _value = positionDict[position]
        _value = _value +1
        positionDict[position] = _value


def isHigherSplit(splitValue: int):
    highWeight = 0
    lowWeight = 0
    for item in positionDict.items():
        if item[0] > splitValue:
            x = 0
            while x <= abs(int(item[0])-splitValue):
                highWeight = highWeight + (x*item[1])
                x += 1
        else:
            x = 0
            while x <= abs(int(item[0])- splitValue):
                lowWeight = lowWeight + (x*item[1])
                x += 1
    return [highWeight+lowWeight]
   



highPosition = 0
lowPosition = 100000
numberOfPositions = 0
middleValue = 0

previousHighWeight = 0
previousLowWeight = 0
previousMiddle = 0
found = False
isHigh = False

positions = readFile("input.txt")
for currentPosition in positions:    
    addPositionToDictionary(int(currentPosition))
    numberOfPositions += 1
    if int(currentPosition) > highPosition:
        highPosition = int(currentPosition)
    if int(currentPosition) < lowPosition:
        lowPosition = int(currentPosition)



middleValue = math.floor((highPosition-lowPosition)/2)
topValue = highPosition #math.floor((highPosition-(highPosition-middleValue))/2)
lowValue = lowPosition #math.floor((middleValue-lowPosition)/2)
lowestConsumption = 0
while not(found):
    #print("Values:",topValue,middleValue,lowValue)
    sortMid = isHigherSplit(middleValue)
    sortTop = isHigherSplit(topValue)
    sortLow = isHigherSplit(lowValue)

    #print("Results:",sortTop[0], sortMid[0], sortLow[0])
    lowestConsumption = min(chain(sortMid,sortTop, sortLow))
    if(abs(topValue-middleValue) <= 1 and abs(lowValue-middleValue) <= 1):
        #print("FOUND!: ",sortTop[0], sortMid[0], sortLow[0])
        #print("Found Values:",topValue,middleValue,lowValue)
        break

    if abs(sortMid[0] - sortTop[0]) < abs(sortMid[0] - sortLow[0]):
        if sortTop[0] < sortMid[0]:
            lowValue = middleValue
            middleValue = topValue-math.floor((topValue-middleValue)/2)
            #topValue = topValue 
        else:
            topValue = topValue-math.floor(((topValue-middleValue))/2)
            lowValue = lowValue+math.floor((middleValue-lowValue)/2)
    else:
        if sortLow[0] < sortMid[0]:
            topValue = middleValue
            #lowValue = math.floor((middleValue-lowValue)/2)
            middleValue = middleValue-math.floor((middleValue-lowValue)/2)
        else:
            lowValue = lowValue+ math.floor((middleValue-lowValue)/2)
            topValue = topValue - math.floor((topValue-middleValue)/2)
print("Consumption Found:", lowestConsumption)
