# <p align="center"> Wallex WebSocket API

## Disclaimer

Before using Wallex WebSocket API, please read and understand the following disclaimer:

> **Disclaimer**: The use of Wallex WebSocket API is at your own risk. While efforts have been made to ensure the accuracy and reliability of the software, the author cannot guarantee its correctness or completeness. The author shall not be liable for any direct, indirect, incidental, special, or consequential damages arising out of the use of or inability to use the software.

## Introduction

The Wallex WebSocket API provides a way to receive live market data from the Wallex exchange. This documentation serves as a comprehensive guide for developers to interact with the WebSocket API using the provided Python client library.

## Getting Started

To begin using the Wallex WebSocket API, follow these steps:

1. **Download**: Download the WebSocket API from the repository or [this link](https://codeload.github.com/mohzeh/WallexApi/zip/refs/heads/main) and copy it to your project location.

2. **Import**: Import the `WebSocket` class into your Python script or application:

   ```python
   from wallexapi import WebSocket
   ```

3. **Initialization**: Create an instance of the `WebSocket` class:

   ```python
   client_WebSocket = WebSocket()
   ```

4. **Usage**: Utilize the methods provided by the WebSocket class to subscribe to market events and receive live data.

### WebSocket Class

The `WebSocket` class is designed to interact with the Wallex WebSocket API and subscribe to various market events. It offers several methods for subscribing to events and retrieving live market data.

#### Methods

- **`__init__(self, once: bool = True, base_url: str = BASE_URL)`**: Initialize the WebSocket class.
- **`subscribe(self, symbol: str, event: str, callback: callable)`**: Subscribe to a market event.
- **`disconnect(self)`**: Disconnect from the Socket.IO server.
- **`get_market_cap(self, symbol, event=EVENTS["marketCap"])`**: Get market capitalization data.
- **`get_buy_depth(self, symbol, event=EVENTS["buyDepth"])`**: Get buy depth data.
- **`get_sell_depth(self, symbol, event=EVENTS["sellDepth"])`**: Get sell depth data.
- **`get_trade(self, symbol, event=EVENTS["trade"])`**: Get trade data.

#### Example Usage

```python
# Create an instance of the WebSocket class
client = WebSocket()

# Define a symbol to subscribe to (e.g., "USDTTMN")
symbol = "USDTTMN"

# Subscribe to the "marketCap" event and provide a callback function
client.subscribe(symbol, EVENTS["marketCap"], client.handle_received_data)

# Subscribe to the "sellDepth" event and provide a callback function
client.subscribe(symbol, EVENTS["sellDepth"], client.handle_received_data)

# Subscribe to the "buyDepth" event and provide a callback function
client.subscribe(symbol, EVENTS["buyDepth"], client.handle_received_data)

# Subscribe to the "trade" event and provide a callback function
client.subscribe(symbol, EVENTS["trade"], client.handle_received_data)
```

### Additional Notes

- Ensure that you have a stable internet connection before using the Wallex WebSocket API.
- For detailed information about available events and parameters, refer to the official documentation on the [official Wallex API page](https://api-docs.wallex.ir/).
- Remember to handle errors and exceptions appropriately in your application to ensure robustness and reliability.
