import requests
from config import CURRENCY_API_URL


def execute(arguments: dict):
    """
    Currency Converter Tool
    Converts an amount from one currency to another using live rates.
    """

    amount = arguments.get("amount", 1)
    from_currency = arguments.get("from_currency")
    to_currency = arguments.get("to_currency")

    if not from_currency or not to_currency:
        return "Currency Error: Please specify both currencies (e.g. 'convert 100 USD to INR')."

    from_currency = from_currency.strip().upper()
    to_currency = to_currency.strip().upper()

    try:
        response = requests.get(
            CURRENCY_API_URL,
            params={
                "amount": amount,
                "from": from_currency,
                "to": to_currency
            },
            timeout=5
        )

        response.raise_for_status()

        data = response.json()

        rates = data.get("rates", {})
        converted = rates.get(to_currency)

        if converted is None:
            return f"Currency Error: Could not convert {from_currency} to {to_currency}."

        return f"{amount} {from_currency} = {converted} {to_currency}"

    except Exception as e:
        return f"Currency Error: {e}"


if __name__ == "__main__":

    print("=" * 50)
    print("Currency Converter Tool Test")
    print("=" * 50)

    print(execute({"amount": 100, "from_currency": "USD", "to_currency": "INR"}))
