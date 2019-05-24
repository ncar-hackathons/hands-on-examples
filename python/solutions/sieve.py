def sieve(limit):
    """
    Find and display all of the prime numbers between 2 and some limit. 
    """
    nums = list(range(0, limit+1))
    
    # cross out 1 by replacing it with a 0
    nums[1] = 0
    
    # Cross out all the multiples of each prime number that we discover
    p = 2
    while p < limit:
        # Cross out all multiples of p (but not p itself)
        for i in range(p*2, limit+1, p):
            nums[i] = 0
            
        # Find the next number that is not crossed out
        p = p + 1
        while p < limit and nums[p] == 0:
            p = p + 1
            
            
    # Display the result
    print(f'The prime numbers up to {limit} are: ')
    for i in nums:
        if nums[i] != 0:
            print(i)
            
sieve(limit=10)
