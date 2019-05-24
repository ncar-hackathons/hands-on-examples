def unique_chars(string):
    """Determine and display the number of unique characters in a string"""
    
    # Add each character to a dictionary with a value of True
    # Once we are done the number of keys in the dictionary will be the number of unique characters in the string
    characters = {}
    for ch in string:
        characters[ch] = True
        
    print(f'{string} contains {len(characters)} unique character(s).')
unique_chars('zzz')
