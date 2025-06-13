# The function takes in the credit card number as an argument.
# Inside the function replace all the digits of the card number with asterisks ("*"), except for the last four digits.
# Return the new credit card number.
# Given: 4444444444444444
# Excepted Output: ************4444

def replacde_digits(card_number: int) -> str:
    num_str: str = str(card_number)
    return "*" * (len(num_str)-4) + num_str[-4:]
    
            
result = replacde_digits(4444444444444444)
print(result)