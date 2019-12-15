import math

def calculate_fuel(mass):
    return math.floor(mass/3) - 2

def main():
    filepath = "./day1/input2.txt"
    with open(filepath) as fp:
        line = fp.readline()
        total_fuel = 0
        while line:

            mass = int(line)
            curr_total_fuel= 0
            curr_fuel = calculate_fuel(mass)
            while curr_fuel >= 0:
                curr_total_fuel += curr_fuel
                curr_fuel = calculate_fuel(curr_fuel)
            total_fuel += curr_total_fuel
            line = fp.readline()
        print(total_fuel)


if __name__ == "__main__":
    main()
