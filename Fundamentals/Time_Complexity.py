# Here we show differing time complexities of operations

def choice(opt):
    if opt == 1:
        constant(list)
    elif opt == 2:
        linear(list)
    elif opt == 3:
        quadratic(list2)
    elif opt == 4:
        print("The fibonacci of ", 10, " is ", exponentiation(10), "\n")
    elif opt == 5:
        print("The index of ", 9, " is ", logarithmic(list, 9),"\n")
    elif opt == 6:
        quasilinear(list2, 9)
    elif opt == 7:
        print("The factorial of ", 9, " is ", factorial(9),"\n")
    elif opt == 8:
        print("Exiting...\n")
    else:
        print("Invalid Input")


# O(1)
def constant(listConst):
    print("First element : ", listConst[0])
    print("Last element : ", listConst[-1], "\n")


# O(n)
# As operational time increases linearly for traversing a 1D list (addition), we obtain a linear complexity
def linear(listLinear):
    sum = 0
    for l in listLinear:
        sum += l
    print("The linear sum is : ", sum, "\n")


# O(n^(2))
# Nested loops and lists traversed twice will have Quadratic complexity
def quadratic(listQuadratic):
    sum = 0
    for row in listQuadratic:
        for element in row:
            sum += element
    print("The 2D quadratic sum is : ", sum, "\n")


# O(2^(n))
# When the input increases and the operational time increases in exponentiation
def exponentiation(num):
    tmp = num
    # Fibonacci Sequence
    if num <= 1:
        return num
    return exponentiation(num - 1) + exponentiation(num - 2)


# O(Log(n))
# Every iteration has Logarithmic complexity
def logarithmic(listLog, value):
    left_index = 0
    right_index = len(listLog) - 1
    search_try = 0
    while left_index <= right_index:
        search_try += 1
        mid_index = (left_index + right_index)//2
        if listLog[mid_index] == value:
            return mid_index
        elif listLog[left_index] == value:
            return left_index
        elif listLog[right_index] == value:
            return right_index
        elif listLog[mid_index] < value:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1


# O(n(Log(n)))
# Every iteration (n) further has Logarithmic complexity
def quasilinear(listQuasi, value):
    for list in listQuasi:
        left_index = 0
        right_index = len(listQuasi) - 1
        search_try = 0
        while left_index <= right_index:
            search_try += 1
            mid_index = (left_index + right_index)//2
            if list[mid_index] == value:
                print("Value found at", mid_index, "st/nd/rd index")
                break
            elif list[left_index] == value:
                print("Value found at", left_index, "st/nd/rd index")
                break
            elif list[right_index] == value:
                print("Value found at", right_index, "st/nd/rd index")
                break
            elif list[mid_index] < value:
                left_index = mid_index + 1
            else:
                right_index = mid_index - 1


# O(n!)
# Factorially increasing complexity
def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num-1)


if __name__ == "__main__":
    # 1D list
    list = [1, 4, 7, 5, 9, 8]
    # 2D List
    list2 = [[1, 2, 4, 7, 9, 12], [4, 5, 6, 7, 9, 11, 13], [7, 8, 9]]

    # Choose
    option = 0
    while option != 8:
        option = int(input("Choose from the following:\n1.) Constant\n2.) Linear"
                           "\n3.) Quadratic\n4.) Exponentiation\n5.) Logarithmic"
                           "\n6.) Quasilinear\n7.) Factorial\n8.) Exit\n\n"))
        choice(option)
