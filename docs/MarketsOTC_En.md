# <p align="center"> WallexAPI(MarketsOTC) Comprehensive Documentation

## Disclaimer

Before using WallexAPI, please read and understand the following disclaimer:

> **Disclaimer**: The use of WallexAPI is at your own risk. While efforts have been made to ensure the accuracy and reliability of the software, the author cannot guarantee its correctness or completeness. The author shall not be liable for any direct, indirect, incidental, special, or consequential damages arising out of the use of or inability to use the software.

## Introduction

Wallex API provides a Python client library for interacting with the Wallex Exchange API. This documentation serves as a guide for developers to understand and utilize the functionality provided by the OrdersManage class.

## Getting Started

To begin using WallexAPI, follow these steps:

1. **Download**: Download the Wallex API from the repository or [this link](https://codeload.github.com/mohzeh/WallexApi/zip/refs/heads/main) and copy it to your project location:
   
2. **Import**: Import the `MarketsOTC` class into your Python script or application:

   ```python
   from wallexapi import MarketsOTC
   ```

3. **Initialization**: Create an instance of the `MarketsOTC` class:

   ```python
    client_MarketsOTC = MarketsOTC(api_key)
    ```

- `api_key`: Your Wallex API key.
- `base_url` (optional): The base URL of the Wallex API. Defaults to `"https://api.wallex.ir/"`.
   

4. **Usage**: Utilize the methods provided by the MarketsOTC class to interact with the Wallex API for managing orders and trading by OTC way.


##### Methods:

1. **`get_otc_markets()`**:
   - Get OTC markets.

2. **`get_otc_price(symbol: str, side: str)`**:
   - Get the OTC price for a specific symbol and side.
   - Parameters:
     - `symbol`: The trading symbol.
     - `side`: OTC side (BUY or SELL).

3. **`get_otc_orders(symbol: str, side: str, amount: float)`**:
   - Get OTC orders for a specific symbol, side, and amount.
   - Parameters:
     - `symbol`: The trading symbol.
     - `side`: OTC side (BUY or SELL).
     - `amount`: The amount of the OTC order.

#### Example Usage:

```python
api = MarketsOTC(api_key)

symbol = "SHIBTMN"
side = "SELL"
amount = 100.0  # Replace with your desired amount

# Example usage: get_otc_markets
otc_markets_result = api.get_otc_markets()

# Example usage: get_otc_price
otc_price_result = api.get_otc_price(symbol, side)

# Example usage: get_otc_orders
otc_orders_result = api.get_otc_orders(symbol, side, amount)
```

### Additional Notes:

- Ensure that you have a stable internet connection before using Wallex API.
- Replace placeholders such as `"Your-API-Key-Here"` with your actual API key.
- For detailed information about available endpoints and parameters, refer to the official documentation on the [official WallexAPI page](https://api-docs.wallex.ir/).
- Feel free to explore and customize the provided methods to suit your specific requirements.
- Remember to handle errors and exceptions appropriately in your application to ensure robustness and reliability.
