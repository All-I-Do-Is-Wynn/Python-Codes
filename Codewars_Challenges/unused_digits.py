# Given a varying number of integer arguments, return the digits that are not present in any of them.

def unused_digits(*arr):
    dict = []
    for x in arr:
        arr1 = [arg for arg in str(x)]
        dict += arr1
    set1 = set(dict)
    set2 = {'0','1','2','3','4','5','6','7','8','9'}
    return ''.join(sorted(set2 - set1))