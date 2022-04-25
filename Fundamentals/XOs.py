# Check to see if a string has the same amount of 'x's and 'o's.
# The method must return a boolean and be case insensitive.
# The string can contain any char.

def xo(s):
    countx = 0
    counto = 0
    if not s:
        return True
    for char in s:
        if char == 'x' or char == 'X':
            countx += 1
        elif char == 'o' or char == 'O':
            counto += 1
    if countx == counto:
        return True
    else:
        return False