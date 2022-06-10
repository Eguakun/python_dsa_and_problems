def getPyTrip(a=0, b=0, c=0):
    max = a

    if b > max:
        max = b
    if c > max:
        max = c

    if max == a:
        flag = (a * a) == ((b * b) + (c*c))
        return flag
    elif max == b:
        flag = (b * b) == ((a * a) + (c*c))
        return flag
    else:
        flag = (c * c) == ((a * a) + (b * b))
        return flag

print(getPyTrip(3,4,51))