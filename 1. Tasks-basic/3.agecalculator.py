from datetime import datetime

age = int(input('Write you age of birth: '))

current_year = datetime.now().year

print(f'User age: {current_year - age}')