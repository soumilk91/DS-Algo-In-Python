"""
Author: Soumil Ramesh Kulkarni
Date: 01/15/2024

Question: Find the Factorial of a given number:
Eg:
fact(5) = 5*4*3*2*1 = 120

 We will use the decrease and conquer approach for this module

"""

def fact(number):
    if number == 1:
        #print("Base Case: fact(1)")
        return 1
    else:
        #print("{0} * fact({0} - 1)".format(number))
        return number * fact(number-1)


def power(n, k):
    """
    return the computation of n to the power k
    eg: n = 4 and k = 2
    return: 4**2 = 16
    Again we use decrease and conquer technique here
    """
    if k == 1:
        return n
    else:
        return n * power(n, (k-1))


def fibo(number):
    """
    Fibo Series: 0 1 1 2 3 5 8 13 21 .....
    """
    if number <= 1:
        return number
    else:
        return fibo(number - 1 ) + fibo(number - 2 )


print(fact(5))
print(power(25, 2))
print(fibo(7))