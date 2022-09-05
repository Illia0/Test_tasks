



if __name__ == '__main__':
    print("Input positive integer:")
    try:
        num = int(input())
        sum = 0
        if num > 0 and num < 10 ** 25:
            for i in range(num + 1):
                sum += i
            print("Result:", sum)
        else:
            print("Number out of range")
    except ValueError:
        print("It`s not a number")
