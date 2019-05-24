
def median_solution_1(a, b, c):
    """
    compute the median of three values using if statements
    
    Parameters
    ----------
    a : float, int
      the first value
    b : float, int
       the second value
    c : float, int
       the third value 
       
    Returns
    -------
    the median of values a, b, and c
       
    """
    
    if a < b and b < c or a > b and b > c:
        return b 
    if b < a and a < c or b > a and a > c:
        return a
    if c < a and b < c or c > a and b > c:
        return c
    
    
def median_solution_2(a, b, c):
    """
    compute the median of three values using built-in min and max functions
    and a little bit of arithmetic. 
    
    Notes
    -----
    
    The median of three values is the sum of the values minus the smallest minus the largest
    
    Parameters
    ----------
    a : float, int
      the first value
    b : float, int
       the second value
    c : float, int
       the third value 
       
    Returns
    -------
    the median of values a, b, and c
       
    """
    
    return a + b + c - min(a, b, c) - max(a, b, c)


def compute_median(x, y, z):
    """Display the median of 3 values."""
    
    print(f'The first value: {x}, the second value: {y}, the thrid value: {z}')
    median_1 = median_solution_1(x, y, z)
    median_2 = median_solution_2(x, y, z)
    print(f'The median value is: {median_1}')
    print(f'Using the alternative method, it is: {median_2}')
    
compute_median(-3, 3, 2)
