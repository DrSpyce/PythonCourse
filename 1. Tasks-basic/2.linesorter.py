user_input = input('Write a list of numbers with a space between them ').split()

numbers = list()

for inp in user_input:
    try:
        numbers.append(int(inp))
    except ValueError:
        print(f'That is not a valid number: {inp}')

numbers.sort()
print(numbers)