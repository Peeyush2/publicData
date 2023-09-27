# leap year

def leapyear( year ):
    #2100
    #2400
    #2024
    divhunder = year % 100
    if divhunder == 0:
        year = year / 100
    remFinal = year % 4 

    if remFinal == 0:
        return True
    return False

# 0 1 1 2 3 5 
obj = {}
def fibo( n ):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    ans = fibo( n-1 ) + fibo( n-2 ) 

    return ans

#4 -> 3, 2 
# 3 - > 2, 1
# 2-> 1

#   5 -> 3, 4
# 3 -> 2 1
# 4 -> 3 2 

#       5
# 4                3
# 3 2             2  1
#
# 2 ^ n
# O (n )

print( fibo( 5 ) )


