# Write a function to convert a number into a string of dashes equal to the number.
# Given: 5
# Expected Output: '-----'

def number_to_dashes(n: int) -> str:
    return '-' * n

output = number_to_dashes(5)
print(output)

