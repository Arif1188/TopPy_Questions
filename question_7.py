# Write a function to check if a given string can be typed using a broken keyboard.
# Return True if the word can be typed with the existing keys, otherwise, return False
# Given: "abcdefg", "bag"
# Excepted Output: True


# 1st solution
def can_type(keys: str, word: str) -> bool:
    for i in word:
        if i not in keys:
            return False
    return True
        
result = can_type("abcdefg", "bag")
print(result)

# 2nd solution
def can_type2(keys, word):
    return set(word).issubset(keys)


result = can_type2("adsertg", "set")
print(result)