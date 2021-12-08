from enum import unique
import os
import re
script_dir = os.path.dirname(__file__)
fileName = "input.txt"

abs_file_path = os.path.join(script_dir, fileName)

#Get the numbers and return resulting numbers of that row
def sumResult(inputData, outputNumbers):
    inputDataSeries = inputData.split(' ')
    outputDataSeries = outputNumbers.split(' ')
    #Sort the input in alpabetic order
    sortedInputData = []
    for x in inputDataSeries:
        sorted_characters = sorted(x)
        a_string = "".join(sorted_characters)
        sortedInputData.append(a_string)
    
    sortedOutputDataSeries = []
    for x in outputDataSeries:
        sorted_characters = sorted(x)
        a_string = "".join(sorted_characters)
        sortedOutputDataSeries.append(a_string)

    #Get primary unique numbers
    uniqueNumbers = {}
    for numberGroup in sortedInputData:
        if len(numberGroup) == 2: # 1
            uniqueNumbers[1] = numberGroup
        if len(numberGroup) == 3: # 7
            uniqueNumbers[7] = numberGroup
        if len(numberGroup) == 4: # 4
            uniqueNumbers[4] = numberGroup
        if len(numberGroup) == 7 : # 8
            uniqueNumbers[8] = numberGroup
    

    #Get the other numbers based on known numbers.
    for numberGroup in sortedInputData:
        if len(numberGroup) == 5 : #5 in length, compare against number 4
            cnt = 0
            for pos,char in enumerate(uniqueNumbers.get(4)):
                if(numberGroup.find(char) != -1):
                    cnt += 1
            if cnt  == 2:
                uniqueNumbers[2] = numberGroup #2
            #Three equal numbers, can be both 3 and 5. Compare against number 1
            if cnt == 3:
                _cnt2 = 0
                for pos,char in enumerate(uniqueNumbers.get(1)):
                    if(numberGroup.find(char) != -1):
                        _cnt2 += 1
                if _cnt2 == 2:
                    uniqueNumbers[3] = numberGroup #3
                if _cnt2 == 1:
                    uniqueNumbers[5] = numberGroup #5
        if len(numberGroup) == 6:
            cnt = 0
            for pos,char in enumerate(uniqueNumbers.get(4)):
                if(numberGroup.find(char) != -1):
                    cnt += 1
            if cnt == 4:
                uniqueNumbers[9] = numberGroup #9
            else:
                #Can be number 0 or 6, compare to number 1
                _cnt = 0
                for pos,char in enumerate(uniqueNumbers.get(1)):
                    if(numberGroup.find(char) != -1):
                        _cnt += 1
                if _cnt == 2:
                    uniqueNumbers[0] = numberGroup #0
                else: 
                    uniqueNumbers[6] = numberGroup #6
    returnResult = ''
    for res in sortedOutputDataSeries:
        for item in uniqueNumbers.items():
            if(res == item[1]):
                returnResult = returnResult+ str(item[0])
    return returnResult


result = 0
with open(abs_file_path) as f:
    inputData = []
    outputNumbers = []
    for line in f.readlines():
        _l = line.strip()
        splitLine = _l.split('|')
        result += int(sumResult(splitLine[0],splitLine[1]))
        #inputData.append(splitLine[0])
        #outputNumbers.append(splitLine[1])
print("Result: ", result)
