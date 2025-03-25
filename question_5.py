# Write a function to generate a list of palindrome numbers within a given range.
# Given: 10 to 100
# Excepted Output: [11, 22, 33, 44, 55, 66, 77, 88, 99]

# 1st solution with for cycle
def palindrome_numbers(start: int,end: int) ->list:
    my_list: list = []
    for i in range(start,end):
        num_str: str = str(i)
        if num_str == num_str[::-1]:
            my_list.append(int(num_str))
    return my_list

palindrome = palindrome_numbers(10,100)
print(palindrome)
        
# 2nd solution with while cycle      
def palindrome_numbers2(start: int, end: int) -> list:
    my_list: list = []
    while start <= end:
        num_str: str = str(start)
        if num_str == num_str[::-1]:
            my_list.append(num_str)
        start +=1
    return my_list

palindrome2 = palindrome_numbers(100,200)
print(palindrome2)