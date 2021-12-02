class subMarine:
    depth = 0
    horizontal = 0

    def __init__(self,depth,horizontalMovement):
        self.depth = depth
        self.horizontal = int(horizontalMovement)
    def move(self,depth, horizontalMovement):
        self.depth += int(depth)
        self.horizontal += int(horizontalMovement)

sub = subMarine(0,0)
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
        if direction == "forward":
           sub.move(0,movement)
        if direction == "up":
            movement = -int(movement)
            sub.move( movement,0)
        if direction == "down":
            sub.move(movement,0)
        if direction == "backwards":
            movement = -movement
            sub.move( 0,movement)

print("Movement: ", sub.horizontal, sub.depth)
print("Answer: ",sub.horizontal*sub.depth)