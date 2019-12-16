def main():
    filepath = "./day2/input1.txt"
    fp = open(filepath)
    line = fp.readline()
    tape_str = line.split(',')
    tape_num = [int(s) for s in tape_str]
    temp_tape_num = tape_num.copy()
    for noun in range(100):
        for verb in range(100):
            temp_tape_num = tape_num.copy()
            temp_tape_num[1] = noun
            temp_tape_num[2] = verb

            #print(temp_tape_num)
            #print(noun)
            #print(verb)

            ans = solve(temp_tape_num)
            #print(temp_tape_num)
            if ans == 19690720:
                print(noun)
                print(verb)
                print(noun*100 + verb)

    fp.close()



def solve(tape):
    index = 0
    opcode = tape[index]
    while opcode != 99:
        
        #print(index)
        #print(tape)
        pos1 = tape[index+1]
        pos2 = tape[index+2]
        out_pos = tape[index+3] 
        #print(opcode)
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

    return tape[0]






if __name__ == "__main__":
    main()