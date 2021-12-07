import os
import math
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
            highWeight = highWeight + item[1]
        else:
            lowWeight = lowWeight + item[1]
    if( highWeight > lowWeight): return ["high",highWeight,lowWeight]
    else:   
        if (lowWeight > highWeight): return ["low",highWeight,lowWeight]
        else: return ["same",highWeight,lowWeight]
     
    
def calcFuelConsumption(toPosition: int):
    consumption = 0
    for item in positionDict.items():
        consumption += abs(item[0]-toPosition)*item[1]
        #print("Cons",consumption, item[0], item[1])
    return consumption



highPosition = 0
lowPosition = 100000
numberOfPositions = 0
middleValue = 0

previousHighWeight = 0
previousLowWeight = 0
previousMiddle = 0
found = False
isHigh = False

positions = readFile("test_input.txt")
for currentPosition in positions:
    
    addPositionToDictionary(int(currentPosition))
    numberOfPositions += 1
    if int(currentPosition) > highPosition:
        highPosition = int(currentPosition)
    if int(currentPosition) < lowPosition:
        lowPosition = int(currentPosition)
middleValue = math.floor((highPosition-lowPosition)/2)



while not(found):
    print("middle:",middleValue)
    sort = isHigherSplit(middleValue)
    print(sort)
    if (sort[1] == previousHighWeight and sort[2] == previousLowWeight) or middleValue == previousMiddle or abs(highPosition-lowPosition) <= 2:
        print("high", highPosition)
        print("low", lowPosition)
        print("middle:",middleValue)
        found = True
        #(isHigh and sort[0] == "low") or (not isHigh and sort[0] == "high") or
    if not found:
        previousHighWeight = sort[1]
        previousLowWeight = sort[2]
        previousMiddle = middleValue
    if sort[0] == "high" and not found:
        lowPosition = middleValue
        middleValue = math.floor((highPosition-((highPosition-lowPosition)/2)))
        isHigh = True
    if sort[0] == "low" and not found:
        highPosition = middleValue
        middleValue = math.floor((highPosition-lowPosition)/2)
    if sort[0] == "same":
        found = True
    
x = lowPosition
smallestConsumption = calcFuelConsumption(previousMiddle)
while x <= highPosition:
    _consumption = calcFuelConsumption(x)
    if _consumption < smallestConsumption:
        smallestConsumption = _consumption
        previousMiddle = x
    print(_consumption, x)
    x += 1

print("Found", previousMiddle)
print("Consumption Found:", smallestConsumption)

