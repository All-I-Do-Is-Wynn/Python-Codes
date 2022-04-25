# Input
# Input will consist of a list of pairs. Each pair contains information for a single potential member.
# Information consists of an integer for the person's age and an integer for the person's handicap.
#
# Output
# Output will consist of a list of string values (in Haskell: Open or Senior)
# stating whether the respective member is to be placed in the senior or open category.

# Functional
def open_or_senior(data):
    result = []
    for x in data:
        if x[0] >= 55 and x[1] > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result

# List comprehenstion
def open_or_senior2(data):
    return ['Senior' if x[0] >= 55 and x[1] > 7 else 'Open' for x in data]



if __name__ == '__main__':
    test = [(45, 12),(55,21),(19, -2),(104, 20)]
    print(open_or_senior(test))
    print(open_or_senior2(test))