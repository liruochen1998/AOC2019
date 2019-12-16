def main():
    filepath = "./day2/input1.txt"
    fp = open(filepath)
    line = fp.readline()
    tape_str = line.split(',')
    tape_num = [int(s) for s in tape_str]
    solve(tape_num)
    fp.close()



def solve(tape):
    index = 0
    opcode = tape[index]
    while opcode != 99:
        
        print(index)
        print(tape)
        pos1 = tape[index+1]
        pos2 = tape[index+2]
        out_pos = tape[index+3] 
        print(opcode)
        if opcode == 1:
            # add pos1 and pos2 and output to out_pos
            sum = tape[pos1] + tape[pos2]
            tape[out_pos] = sum
        if opcode == 2:
            # mul pos1 and pos2 and output to out_pos
            mul = tape[pos1] * tape[pos2]
            tape[out_pos] = mul
        index += 4
        opcode = tape[index]

    print(tape[0])






if __name__ == "__main__":
    main()