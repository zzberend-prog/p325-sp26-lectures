# Functions that approximate an integral to varying levels of precision

from math import sqrt, ceil

def trapezint(func, a, b, n=4):
    """
    Approximate an integral of func() over the range [a,b] using n trapezoids

    Args:
        func (Callable): the function to integrate
        a (float): lower limit of integration
        b (float): upper limit of integration
        n (int): number of trapezoids
    
    Returns:
        The approximation of the integral (float)
    """

    base = (b-a)/n  # all trapezoids have equal base

    sum = 0
    for i in range(n): # loop over n trapezoids
        x1 = a + i*base                     # lower side of trapezoid
        x2 = a + (i+1)*base                 # upper side of trapezoid
        sum += base*(func(x1) + func(x2))/2 # area of trapezoid = base * average height

    return sum
