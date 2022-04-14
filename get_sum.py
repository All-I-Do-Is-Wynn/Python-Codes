# Given two integers a and b, which can be positive or negative,
# find the sum of all the integers between and including them and return it.
# If the two numbers are equal return a or b.

# Note: a and b are not ordered!
def get_sum(a,b):
    sum = 0
    if a < b:
        for x in range(a,b+1):
            sum += x
    else:
        for x in range(b,a+1):
            sum += x
    return sum

# Shortened
def get_sum2(a,b):
    return sum(range(min(a,b),max(a,b)+1))

if __name__ == '__main__':
    print(get_sum(0,2))
    print(get_sum2(0,-2))