import math
def is_square(n):
    if n<0:
        return False
    elif n==0:
        return True
    elif (int(math.sqrt(n))*int(math.sqrt(n))) == n:
        return True
    else:
        return False
