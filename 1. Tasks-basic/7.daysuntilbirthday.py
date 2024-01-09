from datetime import datetime


def days_until_next_birthday(birthdate):
    today = datetime.today()
    next_birthday = datetime(today.year, birthdate.month, birthdate.day)

    if today > next_birthday:
        next_birthday = datetime(today.year + 1, birthdate.month, birthdate.day)

    days_left = (next_birthday - today).days
    return days_left


birthday_str = input("Enter your birthday (YYYY-MM-DD): ")
user_birthday = datetime.strptime(birthday_str, "%Y-%m-%d")

print(f"Days left until your next birthday: {days_until_next_birthday(user_birthday)} days.")