def decimal_to_binary(num):
    # Number to convert
    q = num
    result = ""
    NEW_BASE = 2
    
    # Perform the body of the loop once
    r = q % NEW_BASE
    result = str(r) + result 
    q = q // NEW_BASE
    
    
    # Keep on looping until q == 0
    while q > 0:
        r = q % NEW_BASE
        result = str(r) + result 
        q = q // NEW_BASE

    # Display the result 
    final_res = f'{num} in Decimal is {result} in Binary'
    print(final_res)
    
decimal_to_binary(10)
