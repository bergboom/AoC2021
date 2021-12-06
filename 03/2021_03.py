

import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Input/input.txt"
abs_file_path = os.path.join(script_dir, rel_path)
arrBitCnt = []
noOfLines = 0
init = 1
with open(abs_file_path) as f:
    lines = f.readlines()
    for line in lines:
        _l = line.strip()
        noOfLines += 1
        bit = 0
        if init == 1:
            print(_l)
            init = 0
            for i in _l:
                arrBitCnt.append(0)
        while bit < len(_l):
            if line[bit] == '1':
                arrBitCnt[bit] += 1
            bit += 1

result_byte = ''
for i in arrBitCnt:
    if i > (noOfLines / 2):
        result_byte += '1'
    else:
        result_byte += '0'
_inverse = ''
for i in result_byte:
    
    if i == '0':
        _inverse += '1'
          
    else:
        _inverse += '0'


print("Gamma:   ", result_byte, int(result_byte,2))
print("Epsilon: ", _inverse, int(_inverse,2))
print("Result: ",int(_inverse,2)*int(result_byte,2) )

