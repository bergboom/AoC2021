import os
import math
script_dir = os.path.dirname(__file__)
fileName = "input.txt"
abs_file_path = os.path.join(script_dir, fileName)




with open(abs_file_path) as f:
    inputData = []
    for line in f:
        inputData.append(line.strip().split(','))
    inputData = [int(position) for position in inputData[0]]
    #print(inputData)

maxPosition = max(inputData)
minPosition = min(inputData)

consumption = []
for endPosition in range(minPosition,maxPosition):
    fuelUsage = 0
    for startPosition in inputData:
        fuelUsage += abs(startPosition-endPosition)
    consumption.append(fuelUsage)

print("Part 1:", min(consumption))

consumptionPart2 = []
for endPosition in range(minPosition,maxPosition):
    fuelUsage = 0
    for startPosition in inputData:
        noOfSteps = abs(startPosition-endPosition)
        fuelUsage += sum(range(1,noOfSteps+1))
    consumptionPart2.append(fuelUsage)

print("Part 2:",min(consumptionPart2))