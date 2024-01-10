import string


def check_password_criteria(password):
    criteria = {
        'uppercase': any(char.isupper() for char in password),
        'lowercase': any(char.islower() for char in password),
        'digit': any(char.isdigit() for char in password),
        'symbol': any(char in string.punctuation for char in password),
        'length': len(password) >= 5
    }

    return criteria


def main():
    user_password = input("Enter your password: ")
    criteria_results = check_password_criteria(user_password)

    print("\nPassword Criteria Check:")
    for criterion, meets_requirement in criteria_results.items():
        if meets_requirement:
            print(f"{criterion.capitalize()}: Passed")
        else:
            print(f"{criterion.capitalize()}: Failed")

    if all(criteria_results.values()):
        print("\nCongratulations! Your password meets all criteria.")
    else:
        print("\nPassword does not meet all criteria. Please review the feedback above.")


if __name__ == "__main__":
    main()