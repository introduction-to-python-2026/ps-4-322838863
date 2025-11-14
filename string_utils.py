def split_before_each_uppercases(formual):    
    if not formual:
        return []

    parts = []
    current = formual[0]

    for ch in formual[1:]:
        if ch.isupper():
            parts.append(current)
            current = ch
        else:
            current += ch

    parts.append(current)
    return parts

def split_at_first_digit(formual):    
    for i, ch in enumerate(formual):
        if ch.isdigit():
            # First digit found
            prefix = formual[:i]
            number = formual[i:]
            return prefix, int(number)

    # No digit found
    return s, 1
            
            
       
            
            
        
            
            
            
            
            
  
