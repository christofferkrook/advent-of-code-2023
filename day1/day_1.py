
# load the input data
with open('input.txt', 'r') as f:
    data = f.read().splitlines()

for i, element in enumerate(data):
    data[i] = [x for x in element if x.isdigit()]


values = []

for element in data:
    if len(element) == 1:
        values.append(int(element[0] + element[0]))
    else:
        values.append(int(element[0] + element[-1]))

answer_part_1 = sum(values)
print("Answer to part one: " + str(answer_part_1))

# ---------------------------- part 2

# load the input data
with open('input.txt', 'r') as f:
    data = f.read().splitlines()


def replace_text_numbers(strings):
    # Dictionary mapping text numbers to numeric values
    text_number_mapping = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine': 'n9e'
    }

    # Function to replace text numbers in a string
    def replace_numbers_in_string(s):
        for text_number, numeric_value in text_number_mapping.items():
            s = s.replace(text_number, numeric_value)
        return s

    # Replace text numbers in each string in the list
    replaced_strings = [replace_numbers_in_string(s) for s in strings]

    return replaced_strings

# Replace text numbers in the list
result_strings = replace_text_numbers(data)
for i, element in enumerate(result_strings):
    result_strings[i] = [x for x in element if x.isdigit()]
values = []

for element in result_strings:
    if len(element) == 1:
        values.append(int(element[0] + element[0]))
    else:
        values.append(int(element[0] + element[-1]))

answer_part_2 = sum(values)
print("Answer to part two: " + str(answer_part_2))