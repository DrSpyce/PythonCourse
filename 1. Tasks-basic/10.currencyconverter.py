from forex_python.converter import CurrencyRates


def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()

    try:
        exchange_rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * exchange_rate
        return converted_amount
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    try:
        amount = float(input("Enter the amount to convert: "))
        from_currency = input("Enter the source currency code (e.g., USD): ").upper()
        to_currency = input("Enter the target currency code (e.g., EUR): ").upper()

        result = convert_currency(amount, from_currency, to_currency)

        if isinstance(result, str):
            print(result)
        else:
            print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")