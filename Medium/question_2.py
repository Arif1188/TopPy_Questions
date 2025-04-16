# Largest & Smallest Element: Create a Python program to find the sum of the largest and the smallest elements in a list.
# Given: [5, 6, 3, 8, 9]
# Excepted Outpu: 12

from typing import List

# 1st solution
numbers = [5, 6, 3, 8, 9]

def find_sum(numbers: List[int]) -> str:
    max_num: int = numbers[0]
    min_num: int = numbers[0]
    for num in range(len(numbers)):
        if numbers[num] > max_num:
            max_num = numbers[num]
        elif numbers[num] < min_num:
            min_num = numbers[num]
    total: int = max_num + min_num
    return f"Max number: {max_num}\nMin number: {min_num}\nSum of largest and smallest: {total}"

result = find_sum(numbers)
print(result)


# 2nd solution
def find_sum2(numbers: List[int]) -> int:
    total: int = max(numbers) + min(numbers)
    return total

result = find_sum2(numbers)
print(result)