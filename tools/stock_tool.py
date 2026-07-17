import requests
from config import STOCK_API_URL, STOCK_SEARCH_URL


def _resolve_symbol(query):
    """
    Turn a company name like 'microsoft' into a ticker symbol like 'MSFT'.
    If the query is already a valid ticker, this still finds it.
    """
    response = requests.get(
        STOCK_SEARCH_URL,
        params={"q": query, "quotesCount": 1, "newsCount": 0},
        timeout=5,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    response.raise_for_status()

    quotes = response.json().get("quotes", [])

    if not quotes:
        return None

    return quotes[0].get("symbol")


def execute(arguments: dict):
    """
    Stock Price Tool
    Returns the latest price for a stock ticker symbol or company name.
    """

    query = arguments.get("symbol")

    if not query:
        return "Stock Error: Symbol not provided."

    query = query.strip()

    try:
        symbol = _resolve_symbol(query) or query.upper().replace(" ", "")

        response = requests.get(
            STOCK_API_URL + symbol,
            timeout=5,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        response.raise_for_status()

        data = response.json()

        result = data["chart"]["result"]

        if not result:
            return f"No stock data found for '{query}'."

        meta = result[0]["meta"]

        price = meta.get("regularMarketPrice")
        currency = meta.get("currency", "")
        exchange = meta.get("exchangeName", "")

        if price is None:
            return f"No price data found for '{query}'."

        return (
            f"Stock: {symbol}\n"
            f"Price: {price} {currency}\n"
            f"Exchange: {exchange}"
        )

    except Exception as e:
        return f"Stock Error: {e}"


if __name__ == "__main__":

    print("=" * 50)
    print("Stock Tool Test")
    print("=" * 50)

    print(execute({"symbol": "microsoft"}))
