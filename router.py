import re

def detect_tool(user_input):
    text = user_input.lower()

    # Calculator
    if re.search(r"\d+\s*[\+\-\*/]\s*\d+", text):
        return "calculator", {"expression": user_input}

    # Time
    if "time" in text or "date" in text:
        return "time", {}

    # Weather
    if "weather" in text or "temperature" in text:
        city = text.replace("weather", "").replace("in", "").strip()
        return "weather", {"city": city}

    # Currency Converter
    match = re.search(r"convert\s+([\d.]+)\s+([a-zA-Z]{3})\s+to\s+([a-zA-Z]{3})", text)
    if match:
        amount, from_currency, to_currency = match.groups()
        return "currency", {
            "amount": float(amount),
            "from_currency": from_currency,
            "to_currency": to_currency
        }

    # Stock
    if "stock price" in text or "share price" in text or "stock of" in text:
        symbol = (
            text.replace("stock price of", "")
            .replace("share price of", "")
            .replace("stock price", "")
            .replace("share price", "")
            .replace("stock of", "")
            .replace("stock", "")
            .strip()
        )
        return "stock", {"symbol": symbol}

    return None, None