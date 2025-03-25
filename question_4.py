# Write a function to swap keys and values in a dictionary.
# Given: {'a': 1, 'b': 2, 'c': 3}
# Excepted Output: {1: 'a', 2: 'b', 3: 'c'}


original_dict = {'a': 1, 'b': 2, 'c': 3}

def swap_keys(example_dict: dict) ->dict:
    return {value: key for key,value in example_dict.items()}

swapped_dict = swap_keys(original_dict)
print(swapped_dict)

