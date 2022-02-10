import math

def nth_root(x, n):
    '''Source: https://riptutorial.com/python/example/8751/computing-large-integer-roots'''
    # Start with some reasonable bounds around the nth root.
    upper_bound = 1
    while upper_bound ** n <= x:
        upper_bound *= 2
    lower_bound = upper_bound // 2
    # Keep searching for a better result as long as the bounds make sense.
    while lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2
        mid_nth = mid ** n
        if lower_bound < mid and mid_nth < x:
            lower_bound = mid
        elif upper_bound > mid and mid_nth > x:
            upper_bound = mid
        else:
            # Found perfect nth root.
            return mid
    return mid + 1

def int_to_string(i):
    length = math.ceil(i.bit_length() / 8)
    return i.to_bytes(length, byteorder='big')

file = open("Crypto/encrypted-messages.txt", "r")
for line in file.readlines():
    if line[0] == 'c':
        x = int(line[3:])
        m = nth_root(x,3)
        if b'd4rkc0de' in int_to_string(m):
            print(int_to_string(m))
