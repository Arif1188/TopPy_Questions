# Write a function to convert a given string to Spongecase.
# Given: 'learn to code'
# Excepted Output: 'lEaRn To CoDe'

def to_spongecase(text: str) -> str:
    result: str = ''
    counter: int = 0
    
    for char in text:
        if char.isalpha():
            if counter % 2 == 0:
                result += char.lower()
            else:
                result += char.upper()
            counter += 1
        else:
            result += char
    
    return result


asa = to_spongecase('learn to code')

print(asa)