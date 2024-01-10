import random
import string


def generate_strong_password(length):
    if length < 5:
        raise ValueError("Password length must be at least 5 characters.")

    uppercase_letter = random.choice(string.ascii_uppercase)
    lowercase_letter = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    symbol = random.choice(string.punctuation)

    all_characters = (
        string.ascii_letters + string.digits + string.punctuation
    )
    remaining_length = length - 4
    random_characters = ''.join(random.choice(all_characters) for _ in range(remaining_length))

    password_characters = [uppercase_letter, lowercase_letter, digit, symbol, random_characters]
    random.shuffle(password_characters)
    return ''.join(password_characters)


if __name__ == "__main__":
    try:
        password_length = int(input("Enter the desired password length (at least 5): "))
        strong_password = generate_strong_password(password_length)
        print(f"Generated Strong Password: {strong_password}")

    except ValueError as ve:
        print(f"Error: {ve}")
