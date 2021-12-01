from os import read


result = 0

storedDepthSequence = 0.0
activeDepthSequence = 0.0
nextSequence = 0.0

initCounter = 1
_numberOfSequence = 3
with open('Input/01_input.txt') as f:
    lines = f.readlines()
    for depthRead in lines:
        if initCounter == 1:
            activeDepthSequence = float(depthRead)
            print("Init 01", activeDepthSequence, nextSequence)
        if initCounter < _numberOfSequence and initCounter > 1:
            activeDepthSequence = activeDepthSequence + float(depthRead)
            nextSequence = float(depthRead)
            print("Init 02", activeDepthSequence, nextSequence)


        if initCounter == _numberOfSequence:
            activeDepthSequence = activeDepthSequence + float(depthRead)
            if storedDepthSequence < activeDepthSequence:
                result = result +1
                print("Increase: ",storedDepthSequence,activeDepthSequence)
            else: print("Validate: ",storedDepthSequence,activeDepthSequence)
            storedDepthSequence = activeDepthSequence
            activeDepthSequence = nextSequence + float(depthRead)
            nextSequence = float(depthRead)
    
        if(initCounter < _numberOfSequence):
            initCounter = initCounter + 1

print("Increases: ", result-1) #removing inital result which is not correct