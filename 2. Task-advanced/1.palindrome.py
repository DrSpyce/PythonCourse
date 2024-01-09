def is_palindrome(s):
    cleaned_s = ''.join(char.lower() for char in s)
    return cleaned_s == cleaned_s[::-1]


if __name__ == "__main__":
    user_input = input("Enter a word or phrase: ")

    if is_palindrome(user_input):
        print(f"{user_input} is a palindrome!")
    else:
        print(f"{user_input} is not a palindrome.")