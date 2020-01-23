# int -> booelan
# Given integer n, returns True or False based on reachabilty of goal
def bears(n):
    by_2 = n % 2
    by_3 = n % 3
    by_4 = n % 4
    by_5 = n % 5
    if n < 42:
        return False
    elif n == 42:
        return True
    if by_2 == 0:
        test = bears(n - n/2)
        if test == True:
            return True
    if by_3 == 0 or by_4 == 0:
        last = n % 10
        second_last = (((n % 100) - last)/10)
        if last == 0 or second_last == 0:
            return False
        test = bears(n - (last*second_last))
        if test == True:
            return True
    if by_5 == 0:
        test = bears(n - 42)
        if test == True:
            return True
    else:
        return False
