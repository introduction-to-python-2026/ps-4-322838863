def split_at_first_digit(formula):
    for i,  digit in enumerate(formula):
        if digit.isdigit():
            prefix = formula[0:i:1]
            number = formula[i::]
            return prefix,int(number)
            
    return formula, 1




def split_before_each_uppercase(formula):
  current = _
  new_formula = []
  for let in formula:
    if let.isupper():
      new_formula.append(current)
      current = _ 
    current += let
new_formula.append(current)
return new_formula
    
            
            
       
            
            
        
            
            
            
            
            
  
