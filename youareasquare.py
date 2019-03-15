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

# Alternate recommended solutions
# • No.1 :
# import math
# def is_square(n):
#     if n < 0:
#         return False
#     sqrt = math.sqrt(n)    
#     return sqrt.is_integer()

# • No.2 :
# import math
# def is_square(n):
#     return n > -1 and math.sqrt(n) % 1 == 0;
