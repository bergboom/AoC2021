class subMarine:
    depth = 0
    horizontal = 0
    aim = 0

    def __init__(self,depth,horizontalMovement, aim):
        self.depth = depth
        self.horizontal = int(horizontalMovement)
        aim = int(aim)
    def move(self,direction, movement):
        
        if direction == "forward":
           self.horizontal += movement
           self.depth += (movement * self.aim)
        if direction == "up":
            self.aim -= movement
        if direction == "down":
            self.aim +=movement


sub = subMarine(0,0,0)
import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Input/02_input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    lines = f.readlines()
    for line in lines:
        instruction = line.split()
        direction = instruction[0]
        movement = int(instruction[1])
        sub.move(direction,movement)
        print(sub.horizontal, sub.depth, sub.aim)
        

print("Movement: ", sub.horizontal, sub.depth)
print("Answer: ",sub.horizontal*sub.depth)