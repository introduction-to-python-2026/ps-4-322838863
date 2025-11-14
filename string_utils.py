def split_before_each_uppercases(input):    
    if not input:
        return []

    parts = []
    current = input[0]

    for ch in input[1:]:
        if ch.isupper():
            parts.append(current)
            current = ch
        else:
            current += ch

    parts.append(current)
    return parts

def split_at_first_digit(s):    
    for i, ch in enumerate(s):
        if ch.isdigit():
            # First digit found
            prefix = s[:i]
            number = int(s[i:])
            return prefix, number

    # No digit found
    return s, 1
            
            
       
            
            
        
            
            
            
            
            
  
