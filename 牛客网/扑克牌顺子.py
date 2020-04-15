def IsContinuous(numbers):
    # write code here
    new_numbers = sorted(numbers)

    numbers = new_numbers
    count_0 = numbers.count(0)
    start = count_0
    pre = numbers[start]

    while count_0 >= 0 and start < len(numbers)-1:
        start += 1
        cur = numbers[start]
        if cur > pre:
            count_0 -= cur - pre - 1
            pre = cur
        else:
            return False
        if count_0 < 0:
            return False
    return True

if __name__=='__main__':
    print(IsContinuous([1,2,8,0,0]))