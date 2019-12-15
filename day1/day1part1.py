import math
filepath = "./day1/input1.txt"
sum_fuel = 0
with open(filepath) as fp:
    
    line  = fp.readline()
    while line:
        mass = int(line)
        curr_fuel = math.floor(mass/3) - 2
        sum_fuel += curr_fuel
        line = fp.readline()

print(sum_fuel)