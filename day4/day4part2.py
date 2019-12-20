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

    # may improve this part in the future, simply it's just a task to check whether
    # there is consecutive numbers of the same value of only length 2, but...
    i = 0
    while i < 5:
        count_same_number = 1
        while i < 5 and num[i+1] == num[i]:
            count_same_number += 1
            i += 1
        if count_same_number == 2:
            check_same = True
        i += 1
           
    return check_same
    

if __name__ == "__main__":

    print(check(111122))
    main()