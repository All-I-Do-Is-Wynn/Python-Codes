# Write a function that returns a string in which firstname is swapped with last name.

# This is when given arr [first, last]

def name_shuffler(str_):
    arr = str_.split()
    tmp = arr[0]
    arr[0] = arr[1]
    arr[1] = tmp
    return ' '.join(arr)