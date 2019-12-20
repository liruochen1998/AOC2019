def main():
    start_index = 231832
    end_index = 767346
    count = 0
    for num in range(start_index, end_index):
        if check(num):
            count += 1
    print(count) 

def check(num):
    num = str(num)
    check_same = False
    for i in range(len(num)-1):
        if num[i+1] < num[i]:
            return False
        if num[i+1] == num[i]:
            check_same = True
    return check_same
    

if __name__ == "__main__":

    #rint(check('123789'))
    main()