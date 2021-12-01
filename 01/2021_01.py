result = 0
lastDepth = 0.0
init = 1
with open('Input/01_input.txt') as f:
    lines = f.readlines()
    for line in lines:
        if init == 1:
            lastDepth = float(line)
            init = 0
        if float(line) > lastDepth :
            result = result +1
        lastDepth = float(line)
    
print("Increases: ", result)