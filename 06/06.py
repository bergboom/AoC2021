import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "06_input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

#lanternFish = [3,4,3,1,2]
lanternFish = []
with open(abs_file_path) as f:
    lines = f.readlines()
    for line in lines:
        _l = line.strip().split(",")
        for x in _l:
            lanternFish.append(int(x))

#print(lanternFish)
iterations = 18
i = 0
while i < iterations:
    i = i +1
    j = 0
    #print(lanternFish)
    noOfFish = len(lanternFish)
    while j < noOfFish:
        lanternFish[j] = lanternFish[j] -1
        if  lanternFish[j] < 0:
            lanternFish[j] = 6
            lanternFish.append(8)
        j = j + 1
    print("Iteration:"+ str(i))
print(len(lanternFish))