import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Input/input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

def GetRemains(bit, arrToCheck, isMostSignificant):
    _bitCnt = 0
    _noOfLines = 0
    _arrWith1 = []
    _arrWith0 = []
    if(len(arrToCheck) == 1):
        return arrToCheck
    for line in arrToCheck:
        _noOfLines += 1
        if line[bit] == '1':
            _arrWith1.append(line)
            _bitCnt += 1
        else:
            _arrWith0.append(line)
    
    if isMostSignificant:
        if (len(_arrWith1) >= len(_arrWith0) ):
            return _arrWith1
        else:
            return _arrWith0
    else:
        if (len(_arrWith0) <= len(_arrWith1)):
            return _arrWith0
        else:
            return _arrWith1

arrBitCnt = []
arrMostSignificat = []
arrLeastSignificant = []
noOfLines = 0
bitCnt = 0
noOfBits = 1
with open(abs_file_path) as f:
    lines = f.readlines()
firstLine = lines[0].strip()
print(len(firstLine))
arrMostSignificat = lines
arrLeastSignificant = lines
while bitCnt < len(firstLine):
    arrMostSignificat = GetRemains(bitCnt,arrMostSignificat,True)
    arrLeastSignificant = GetRemains(bitCnt, arrLeastSignificant, False)
    #print("Most: " + str(arrMostSignificat))
    #print("least: "+ str(arrLeastSignificant))
    bitCnt = bitCnt +1

result_Most = 0
result_Least = 0
for i in arrMostSignificat:
    result_Most = int(i,2) + result_Most
for i in arrLeastSignificant:
    result_Least = int(i,2) + result_Least
print("Result",result_Least*result_Most)
