import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "06_input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

#lanternFish = [3,4,3,1,2]
#noOfLanterFish = [0,0,0,0,0,0,0,0,0]
#for x in lanternFish:
#    noOfLanterFish[x] = noOfLanterFish[x]+1
noOfLanterFish = [0,0,0,0,0,0,0,0,0]
with open(abs_file_path) as f:
    lines = f.readlines()
    for line in lines:
        _l = line.strip().split(",")
        for x in _l:
            val = int(x)
            noOfLanterFish[val] = noOfLanterFish[val]+1

#print(lanternFish)
iterations = 256
i = 0
while i < iterations:
    fishMovement = [0,0,0,0,0,0,0,0,0]
    i = i +1
    j = len(noOfLanterFish)-1
    while j >= 0:
        if j > 0:
            fishMovement[j-1] = noOfLanterFish[j]
        else:
            fishMovement[8] = fishMovement[8] + noOfLanterFish[0]
            fishMovement[6] = fishMovement[6] + noOfLanterFish[0]
        j = j - 1
    noOfLanterFish = fishMovement
    print("Iteration:"+ str(i))
#print(noOfLanterFish)
result = 0
for x in noOfLanterFish:
    result = result +x

print(result)