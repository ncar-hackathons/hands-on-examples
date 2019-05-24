import math
def compute_square_root(num):
    """Compute and display approximate square root of a number using Newton's method
    
    Parameters
    ----------
    num : int, float
         Non-negative number
         
    """
    
    
    # Use assert statement to guarantee that no matter what
    # num is a non-negative number 
    
    assert 0 <= num 
    
    
    x = num 
    # initialize guess to x/2
    guess = x / 2 
    
    
    while abs((guess * guess) - x) > 1e-12:
        
        print(f'Current guess is: {guess}')
        
        # Update guess
        guess = 0.5 * (guess + (x / guess))
    
    print(f'The approximate square root of {num} is: {guess}')
    print(f'Using the built-in math module, it is: {math.sqrt(num)}')
    
compute_square_root(2)
