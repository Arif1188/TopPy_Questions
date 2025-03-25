# Write a function to check if a given number is a Pronic number or not.
# Given: 6
# Excepted Output: True

from typing import List

def is_pronic(num: List[int]) -> bool:
    if num < 0:
        return False
    
    i: int = 0
    while i*(i+1) <= num:
        if i*(i+1) == num:
            return True
        i+=1
    return False

numbers = [0,4,6,12,20,24,25,26,30,-5]
for num in numbers:
    if is_pronic(num):
        print(f"{num} is Pronic number")
    else:
        print(f"{num} is not Pronic number")
    
