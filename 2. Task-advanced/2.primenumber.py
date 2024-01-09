def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_primes(up_to):
    primes = list()
    for num in range(2, up_to + 1):
        if is_prime(num):
            primes.append(num)
    return primes


if __name__ == "__main__":
    try:
        limit = int(input("Enter a number to find all prime numbers up to that limit: "))
        prime_numbers = find_primes(limit)
        print(f"Prime numbers up to {limit}: {prime_numbers}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")