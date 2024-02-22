# <p align="center"> WallexAPI(MarketInfo) Comprehensive Documentation

## Disclaimer

Before using WallexAPI, please read and understand the following disclaimer:

> **Disclaimer**: The use of WallexAPI is at your own risk. While efforts have been made to ensure the accuracy and reliability of the software, the author cannot guarantee its correctness or completeness. The author shall not be liable for any direct, indirect, incidental, special, or consequential damages arising out of the use of or inability to use the software.

## Introduction

WallexAPI is a Python client library designed to facilitate interactions with the Wallex.ir Exchange API. It provides a set of convenient methods for retrieving market-related data such as available markets, currency statistics, order book information, latest trades, and market history.

## Getting Started

To begin using WallexAPI, follow these steps:

1. **Download**: Download the Wallex API from the repository or [this link](https://codeload.github.com/mohzeh/WallexApi/zip/refs/heads/main) and copy it to your project location:
   
2. **Import**: Import the `MarketInfo` class into your Python script or application:

   ```python
   from wallexapi import MarketInfo
   ```

3. **Initialization**: Create an instance of the `MarketInfo` class:

   ```python
   client_MarketInfo = MarketInfo()
   ```

4. **Usage**: Utilize the methods provided by the `MarketInfo` class to interact with the Wallex.ir Exchange API.

## `MarketInfo` Class

The `MarketInfo` class serves as the main interface for accessing market-related data from the Wallex API. It offers several methods for retrieving different types of information:

### Methods

- **`get_markets(self)`**: Retrieves a list of available markets.
- **`get_currencies(self)`**: Retrieves currency statistics.
- **`get_order_book_symbol(self, symbol: str)`**: Retrieves the order book for a specific symbol.
- **`get_order_book_all(self, symbol: str)`**: Retrieves the order book for all symbols.
- **`get_latest_trades(self, symbol: str)`**: Retrieves the latest trades for a specific symbol.
- **`get_market_history(self, symbol: str, resolution: str, time_from: int, time_to: int)`**: Retrieves market history data for a specific symbol and time range.

### Example

Here's an example of how to use the `MarketInfo` class:

```python
# Import the MarketInfo class
from wallexapi import MarketInfo
import time

# Initialize MarketInfo
api = MarketInfo()
symbol = "USDTTMN"

# Retrieve a list of available markets
markets = api.get_markets()
print("Markets Result:")
print(markets)

# Retrieve currency statistics
currencies = api.get_currencies()
print("Currencies Result:")
print(currencies)

# Retrieve the order book for a specific symbol
order_book_symbol = api.get_order_book_symbol(symbol)
print("Order Book for Symbol Result:")
print(order_book_symbol)

# Retrieve the order book for all symbols
order_book_all = api.get_order_book_all(symbol)
print("Order Book for All Symbols Result:")
print(order_book_all)

# Retrieve the latest trades for a specific symbol
latest_trades = api.get_latest_trades(symbol)
print("Latest Trades Result:")
print(latest_trades)

# Retrieve market history data for a specific symbol and time range
time_from = int(time.time()) - 60 * 60 * 5
time_to = int(time.time())
market_history = api.get_market_history(symbol, "60", time_from, time_to)
print("Market History Result:")
print(market_history)
```

## Additional Notes

- Ensure that you have a stable internet connection before using WallexAPI.
- For detailed information about available endpoints and parameters, refer to the official documentation on the [official WallexAPI page](https://api-docs.wallex.ir/).
- Feel free to explore and customize the provided methods to suit your specific requirements.


