# Write a function to merge two sorted lists into a single sorted list.
# Given: [1, 3, 5] [2, 4, 6]
# Excepted Output: [1, 2, 3, 4, 5, 6]

from typing import List

def merge_list(list1: List[int], list2: List[int]) -> List[int]:
    combined_list: List[int] = list1 + list2
    sorted_list = sorted(combined_list)
    return sorted_list


asa = merge_list([1,3,5,7,9,10], [2,4,6,8,11,12])
print(asa)



