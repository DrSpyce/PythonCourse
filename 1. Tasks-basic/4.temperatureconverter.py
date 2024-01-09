def to_celsius(num):
    return (num * 9 / 5) + 32


def to_fahrenheit(num):
    return (num - 32) * 5/9


print(f'Celsius: {to_celsius(17)}')
print(f'Fahrenheit: {to_fahrenheit(80)}')
