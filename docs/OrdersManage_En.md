# <p align="center"> WallexAPI(OrdersManage) Comprehensive Documentation

## Disclaimer

Before using WallexAPI, please read and understand the following disclaimer:

> **Disclaimer**: The use of WallexAPI is at your own risk. While efforts have been made to ensure the accuracy and reliability of the software, the author cannot guarantee its correctness or completeness. The author shall not be liable for any direct, indirect, incidental, special, or consequential damages arising out of the use of or inability to use the software.

## Introduction

Wallex API provides a Python client library for interacting with the Wallex Exchange API. This documentation serves as a guide for developers to understand and utilize the functionality provided by the OrdersManage class.

## Getting Started

To begin using WallexAPI, follow these steps:

1. **Download**: Download the Wallex API from the repository or [this link](https://codeload.github.com/mohzeh/WallexApi/zip/refs/heads/main) and copy it to your project location:
   
2. **Import**: Import the `OrdersManage` class into your Python script or application:

   ```python
   from wallexapi import OrdersManage
   ```

3. **Initialization**: Create an instance of the `OrdersManage` class:

   ```python
    # Replace 'Your-API-Key-Here' with your actual API key
    api_key = "Your-API-Key-Here"
    client_OrdersManage = OrdersManage(api_key)
   ```

4. **Usage**: Utilize the methods provided by the OrdersManage class to interact with the Wallex API for managing orders and trading.


### `OrdersManage` Class

The `OrdersManage` class serves as the main interface for interacting with orders and trading through the Wallex API. It offers several methods for placing orders, retrieving order information, and managing trades.

#### Methods

- **`set_order(self, symbol, type_order, side, price, quantity, client_id=None)`**: Place an order with the Wallex API.
- **`get_order(self, clientOrderId)`**: Get information about a specific order by its clientOrderId.
- **`del_order(self, clientOrderId)`**: Cancel an order by its clientOrderId.
- **`get_open_orders(self, symbol=None)`**: Get a list of open orders.
- **`get_last_trades(self, symbol=None, side=None)`**: Get a list of the last trades.

### Example

Here's an example of how to use the `OrdersManage` class:

```python
# Import the OrdersManage class
from wallexapi import OrdersManage

# Initialize OrdersManage with your API key
api_key = "Your-API-Key-Here"
api = OrdersManage(api_key)

# Example usage of set_order function
symbol = "SHIBTMN"
type_order = "LIMIT"
side = "BUY"
price = "0.3500"
quantity = "350000"
client_id = "mohsen_zehtabchi_00001"

set_order_result = api.set_order(symbol, type_order, side, price, quantity, client_id)
print("Set Order Result:")
print(set_order_result)

# Example usage of get_order function
client_order_id_to_get = "mohsen_zehtabchi_00001"
get_order_result = api.get_order(client_order_id_to_get)
print("Get Order Result:")
print(get_order_result)

# Example usage of del_order function
client_order_id_to_cancel = "mohsen_zehtabchi_00001"
cancel_order_result = api.del_order(client_order_id_to_cancel)
print("Cancel Order Result:")
print(cancel_order_result)

# Example usage of get_open_orders function
open_orders_result = api.get_open_orders(symbol=symbol)
print("Open Orders Result:")
print(open_orders_result)

# Example usage of get_last_trades function
last_trades_result = api.get_last_trades(symbol=symbol, side="buy")
print("Last Trades Result:")
print(last_trades_result)
```

### Additional Notes

- Ensure that you have a stable internet connection before using Wallex API.
- Replace placeholders such as "Your-API-Key-Here" with your actual API key and data.
- For detailed information about available endpoints and parameters, refer to the official documentation on the [official WallexAPI page](https://api-docs.wallex.ir/).
- Feel free to explore and customize the provided methods to suit your specific requirements.
