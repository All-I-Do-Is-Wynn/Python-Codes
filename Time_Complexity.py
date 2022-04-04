# Here we show differing time complexities of operations

def choice(option):
    if option == 1:
        constant(list)
    elif option == 2:
        linear(list)
    elif option == 3:
        quadratic(list2)
    elif option == 4:
        exponentiation(40)

    elif option == 8:
        print("Exiting...\n")
    else:
        print("Invalid Input")

def constant(list):
    print("First element : ", list[0])
    print("Last element : ", list[-1],"\n")

def linear(list):
    sum = 0
    for l in list:
        sum += l
    print("The linear sum is : ",sum,"\n")


def quadratic(list):
    sum = 0
    for row in list:
        for element in row:
            sum += element
    print("The 2D quadratic sum is : ", sum,"\n")


def exponentiation(num):
    tmp = num
    # Fibonacci Sequence
    if num <= 1:
        return num
    return exponentiation(num - 1) + exponentiation(num - 2)



if __name__ == "__main__":
    # 1D list
    list = [1, 4, 7, 5, 9, 8]
    # 2D List
    list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Choose
    option = 0
    while option != 8:
        option = int(input("Choose from the following:\n1.) Constant\n2.) Linear"
                           "\n3.) Quadratic\n4.) Exponentiation\n5.) Logarithmic"
                           "\n6.) Quasilinear\n7.) Factorial\n8.) Exit\n\n"))

        choice(option)
