# Find Majority Element in List
# Give: [1, 7, 8, 7, 7, 7]
# Excepted Output: 7



numbers = [1, 3,4,5,6,7,2,2,7,7,7]

# 1st solution
def find_majority_number(numbers):
    my_dict = {}
    majority_num = None
    for number in numbers:
        if number in my_dict:
            my_dict[number] += 1
        else:
            my_dict[number] = 1
    max_num = 0
    for num in my_dict:
        if my_dict[num] > max_num:
            max_num  = my_dict[num]
            majority_num = num
    return f"Majority number: {majority_num}, repeted {max_num} times"
            
result = find_majority_number(numbers)
print(result)   


# 2nd solution
majority_number = None

for num in numbers:
    count = numbers.count(num)
    majority_number = num
    
print(f"Majority number: {majority_number}, repeted {count} times")