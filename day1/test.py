def replace_text_numbers(strings):
    # Dictionary mapping text numbers to numeric values
    text_number_mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    # Function to replace text numbers in a string
    def replace_numbers_in_string(s):
        for text_number, numeric_value in text_number_mapping.items():
            s = s.replace(text_number, numeric_value)
        return s

    # Replace text numbers in each string in the list
    replaced_strings = [replace_numbers_in_string(s) for s in strings]

    return replaced_strings

# Example list of strings
input_strings = ["one apple", "two oranges", "three bananas"]

# Replace text numbers in the list
result_strings = replace_text_numbers(input_strings)

# Print the result
print(result_strings)