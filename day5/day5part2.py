def main():
    filepath = './day5/input1.txt'
    fp = open(filepath)
    line = fp.readline()
    tape_str = line.split(',')
    tape_num = [int(x) for x in tape_str]

    machine(tape_num)

def machine(tape):
    #start on the tape
    index = 0
    count = 0
    while True:
        print(count)
        count += 1
        
        digits_str = tape[index]
        digits = [int(x) for x in str(digits_str)]
        opcode = decode_op(digits)
        digits = digits[:-2] # exclued the opcode part

        # opcode == 1: add
        if opcode == 1:
            decode_args(tape, index, digits, opcode)
            index += 4
        # opcode == 2: mul
        if opcode == 2:
            decode_args(tape, index, digits, opcode)
            index += 4
        # opcode == 3: scan
        if opcode == 3:
            #special input 1
            pos1 = tape[index+1]
            tape[pos1] = 5 
            index += 2
        # opcode == 4: print
        if opcode == 4:
            pos1 = tape[index+1]
            print(tape[pos1])
            index += 2
        # opcode == 5: jump if true
        if opcode == 5:
            index = decode_jump(tape, index, digits, 5)
            

        # opcode == 6: jump if false
        if opcode == 6:
            index = decode_jump(tape, index, digits, 6)

        # opcdde == 7: less than
        if opcode == 7:
            decode_compare(tape, index, digits, 7)
            index += 4

        # opcode == 8: equals:
        if opcode == 8:
            decode_compare(tape, index, digits, 8)
            index += 4


        if opcode == 99:
            break


def decode_args(tape, index, digits, option):
    while len(digits) < 3:
        digits = [0] + digits
    pos1, pos2, pos3 = tape[index+1], tape[index+2], tape[index+3]
    if option == 1:
        tape[pos3] = (pos1 if digits[2] == 1 else tape[pos1]) + (pos2 if digits[1] == 1 else tape[pos2])
    if option == 2:
        tape[pos3] = (pos1 if digits[2] == 1 else tape[pos1]) * (pos2 if digits[1] == 1 else tape[pos2])


def decode_jump(tape, index, digits, option):
    while len(digits) < 2:
        digits = [0] + digits
    pos1, pos2 = tape[index+1], tape[index+2]
    arg1 = pos1 if digits[1] == 1 else tape[pos1]
    arg2 = pos2 if digits[0] == 1 else tape[pos2]
    
    if arg1 != 0:
        return arg2 if option == 5 else index + 3
    else :
        return arg2 if option == 6 else index + 3


def decode_compare(tape, index, digits, option):
    while len(digits) < 3:
        digits = [0] + digits
    pos1, pos2, pos3 = tape[index+1], tape[index+2], tape[index+3]
    arg1 = pos1 if digits[2] == 1 else tape[pos1]
    arg2 = pos2 if digits[1] == 1 else tape[pos2]
    if arg1 < arg2 and option == 7:
        tape[pos3] = 1
    elif arg1 == arg2 and option == 8:
        tape[pos3] = 1
    else:
        tape[pos3] = 0
    
    




        
def decode_op(digits):
    # one line parse opcode
    #!! make digits array of ints
    opcode = (0 if len(digits) == 1 else digits[-2])*10 + digits[-1]
    return opcode



if __name__ == "__main__":
    main()