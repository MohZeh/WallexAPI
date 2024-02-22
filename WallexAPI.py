import requests
import socketio
import re

BASE_URL: str = "https://api.wallex.ir/"
CONTENT_TYPE: str = "application/json"

# ----- MarketInfo EndPoints -----
MARKET_EP: dict = {
    "markets": "v1/markets",
    "currencies_stats": "v1/currencies/stats",
    "order_book_symbol": "v1/depth",
    "order_book_all": "v2/depth/all",
    "latest_trades": "v1/trades",
    "market_history": "v1/udf/history",
}

# ----- AccountManage EndPoints -----
ACCOUNT_EP: dict = {
    "profile": "v1/account/profile",
    "fee": "v1/account/fee",
    "card_numbers": "v1/account/card-numbers",
    "ibans": "v1/account/ibans",
    "balances": "v1/account/balances",
    "money_deposit": "v1/account/money-deposit",
    "money_withdrawal": "v1/account/money-withdrawal",
    "crypto_deposit": "v1/account/crypto-deposit",
    "crypto_withdrawal": "v1/account/crypto-withdrawal",
    "transfers": "sub-accounts/transfers",
}

# ----- OrdersManage EndPoints -----
ORDERS_EP: dict = {
    "orders": "v1/account/orders",
    "openOrders": "v1/account/openOrders",
    "last_trades": "v1/account/trades",
}

# ----- MarketsOTC EndPoints -----
OTC_EP: dict = {
    "otc_markets": "v1/otc/markets",
    "otc_price": "v1/account/otc/price",
    "otc_orders": "v1/account/otc/orders",
}

# ----- WebSocket EVENTS -----
EVENTS: dict = {
    "marketCap": "@marketCap",
    "sellDepth": "@sellDepth",
    "buyDepth": "@buyDepth",
    "trade": "@trade",
}


class MarketInfo:
    """
    A class for interacting with the Wallex API to retrieve market-related information.

    Args:
        base_url (str, optional): The base URL of the Wallex API. Defaults to "https://api.wallex.ir/".

    Methods:
        get_markets(self): Retrieves a list of available markets.
        get_currencies(self): Retrieves currency statistics.
        get_order_book_symbol(self, symbol: str): Retrieves the order book for a specific symbol.
        get_order_book_all(self, symbol: str): Retrieves the order book for all symbols.
        get_latest_trades(self, symbol: str): Retrieves the latest trades for a specific symbol.
        get_market_history(self, symbol: str, resolution: str, time_from: int, time_to: int): Retrieves market history data for a specific symbol and time range.

    Example:
        api = MarketInfo()
        symbol = "USDTTMN"
        m00_time = int(time.time())
        h01_time = m00_time - (m00_time % (60 * 60))

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
        time_from = h01_time - 60 * 60 * 5
        time_to = h01_time
        market_history = api.get_market_history(symbol, "60", time_from, time_to)
        print("Market History Result:")
        print(market_history)
    """

    def __init__(self, base_url=BASE_URL):
        """
        Initializes a new instance of the MarketInfo class.

        Args:
            base_url (str, optional): The base URL of the Wallex API. Defaults to "https://api.wallex.ir/".
        """
        self.BASE_URL = base_url

    def _make_request(self, endpoint, params=None):
        """
        Sends an HTTP GET request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint to request.
            params (dict, optional): Query parameters to include in the request. Defaults to None.

        Returns:
            dict: The JSON response from the API.

        Raises:
            requests.exceptions.RequestException: If a network-related error occurs.
            requests.exceptions.HTTPError: If an HTTP error (4xx or 5xx) occurs.
        """
        try:
            response = requests.get(self.BASE_URL + endpoint, params=params)
            # response.raise_for_status()  # Raises an exception for 4xx and 5xx status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(f"(Request) error: {e}")
        except requests.exceptions.HTTPError as e:
            raise requests.exceptions.HTTPError(f"(HTTP) error: {e}")

    def get_markets(self, endpoint=MARKET_EP["markets"]):
        """
        Retrieves a list of available markets.

        Returns:
            dict: A dictionary containing market information.
        """
        return self._make_request(endpoint)

    def get_currencies(self, endpoint=MARKET_EP["currencies_stats"]):
        """
        Retrieves currency statistics.

        Returns:
            dict: A dictionary containing currency statistics.
        """
        return self._make_request(endpoint)

    def get_order_book_symbol(
        self, symbol: str, endpoint=MARKET_EP["order_book_symbol"]
    ):
        """
        Retrieves the order book for a specific symbol.

        Args:
            symbol (str): The symbol for which to retrieve the order book.

        Returns:
            dict: A dictionary containing the order book for the specified symbol.
        """
        params = {"symbol": symbol}
        return self._make_request(endpoint, params=params)

    def get_order_book_all(self, symbol: str, endpoint=MARKET_EP["order_book_all"]):
        """
        Retrieves the order book for all symbols.

        Args:
            symbol (str): The symbol for which to retrieve the order book.

        Returns:
            dict: A dictionary containing the order book for all symbols.
        """
        params = {"symbol": symbol}
        return self._make_request(endpoint, params=params)

    def get_latest_trades(self, symbol: str, endpoint=MARKET_EP["latest_trades"]):
        """
        Retrieves the latest trades for a specific symbol.

        Args:
            symbol (str): The symbol for which to retrieve the latest trades.

        Returns:
            dict: A dictionary containing the latest trades for the specified symbol.
        """
        params = {"symbol": symbol}
        return self._make_request(endpoint, params=params)

    def get_market_history(
        self,
        symbol: str,
        resolution: str,
        time_from: int,
        time_to: int,
        endpoint=MARKET_EP["market_history"],
    ):
        """
        Retrieves market history data for a specific symbol and time range.

        Args:
            symbol (str): The symbol for which to retrieve market history.
            resolution (str): The time interval for data (e.g., "60" for 1-hour intervals).
            time_from (int): The start time for data retrieval (Unix timestamp in seconds).
            time_to (int): The end time for data retrieval (Unix timestamp in seconds).

        Returns:
            dict: A dictionary containing market history data.
        """
        params = {
            "symbol": symbol,
            "resolution": resolution,
            "from": time_from,
            "to": time_to,
        }
        return self._make_request(endpoint, params=params)


class AccountManage:
    """
    A Python client for interacting with the Wallex API to manage user accounts and perform financial operations.

    Args:
        api_key (str): Your Wallex API key.
        base_url (str, optional): The base URL of the Wallex API. Defaults to "https://api.wallex.ir/".

    Methods:
        get_profile(): Get the user's profile information.
        get_fee(): Get user level and fee information related to the user's account.
        get_card_numbers(): Get bank card numbers associated with the user's account.
        get_ibans(): Get IBANs associated with the user's account.
        get_balances(): Get wallet assets balances for the user's account.
        get_money_deposit(): Get information related to money (Toman) deposits in the user's account.
        get_money_withdrawal(): Get information related to money (Toman) withdrawal in the user's account.
        get_crypto_deposit(): Get information related to cryptocurrency deposits in the user's account.
        get_crypto_withdrawal(): Get information related to cryptocurrency withdrawal in the user's account.
        get_transfer(): Get information related to transfers in the user's account.
        set_money_withdrawal(iban, value): Initiate a money (Toman) withdrawal from the user's account to a specified IBAN.
        set_crypto_withdrawal(coin, network, value, wallet_address, memo=None): Initiate a cryptocurrency withdrawal from the user's account.

    Example:
        api_key = "Your API Key"
        api = AccountManage(api_key)

        # Get the user's profile information
        profile_info = api.get_profile()
        print("User Profile:")
        print(profile_info)

        # Get user level and fee information
        fee_info = api.get_fee()
        print("User Fee Information:")
        print(fee_info)

        # Get bank card numbers
        card_numbers = api.get_card_numbers()
        print("Bank Card Numbers:")
        print(card_numbers)

        # Get IBANs
        ibans = api.get_ibans()
        print("IBANs:")
        print(ibans)

        # Get wallet balances
        balances = api.get_balances()
        print("Wallet Balances:")
        print(balances)

        # Get money deposit information
        money_deposit_info = api.get_money_deposit()
        print("Money Deposit Information:")
        print(money_deposit_info)

        # Get money withdrawal information
        money_withdrawal_info = api.get_money_withdrawal()
        print("Money Withdrawal Information:")
        print(money_withdrawal_info)

        # Get cryptocurrency deposit information
        crypto_deposit_info = api.get_crypto_deposit()
        print("Crypto Deposit Information:")
        print(crypto_deposit_info)

        # Get cryptocurrency withdrawal information
        crypto_withdrawal_info = api.get_crypto_withdrawal()
        print("Crypto Withdrawal Information:")
        print(crypto_withdrawal_info)

        # Get transfer information
        transfer_info = api.get_transfer()
        print("Transfer Information:")
        print(transfer_info)

        # Initiate a money withdrawal
        iban_to_withdraw_to = "Your IBAN"
        amount_to_withdraw = 100.0  # Replace with the amount you want to withdraw
        money_withdrawal_result = api.set_money_withdrawal(iban_to_withdraw_to, amount_to_withdraw)
        print("Money Withdrawal Result:")
        print(money_withdrawal_result)

        # Initiate a cryptocurrency withdrawal
        coin = "USDT"
        network = "TRC20"
        value = 100.0  # Replace with the amount you want to withdraw
        wallet_address = "Your wallet address"  # Replace with your wallet address
        crypto_withdrawal_result = api.set_crypto_withdrawal(coin, network, value, wallet_address)
        print("Crypto Withdrawal Result:")
        print(crypto_withdrawal_result)
    """

    def __init__(self, api_key, base_url=BASE_URL):
        """
        Initialize the Wallex Account API client with the provided API key.

        Args:
            api_key (str): Your Wallex API key.
            base_url (str, optional): The base URL of the Wallex API. Defaults to "https://api.wallex.ir/".
        """
        self.api_key = api_key
        self.BASE_URL = base_url
        self.CONTENT_TYPE = CONTENT_TYPE

    def _make_request(self, endpoint, method="GET", params=None, json_payload=None):
        """
        Make an HTTP request to the Wallex API.

        Args:
            endpoint (str): The API endpoint.
            method (str): The HTTP method (GET or POST).
            params (dict): Query parameters (for GET requests).
            json_payload (dict): JSON payload (for POST requests).

        Returns:
            dict: JSON response from the API or an error message.
        """
        url = self.BASE_URL + endpoint
        headers = {
            "Content-Type": self.CONTENT_TYPE,
            "x-api-key": self.api_key,
        }
        try:
            response = requests.request(
                method, url, headers=headers, params=params, json=json_payload
            )
            return response.json()

        except requests.exceptions.RequestException as e:
            return f"(Request) error: {e}"
        except requests.exceptions.HTTPError as e:
            return f"(HTTP) error: {e}"

    def get_profile(self, endpoint=ACCOUNT_EP["profile"]):
        """
        Get the user's profile information.

        Returns:
            dict: User profile information.
        """
        return self._make_request(endpoint)

    def get_fee(self, endpoint=ACCOUNT_EP["fee"]):
        """
        Get User level and fee information related to the user's account.

        Returns:
            dict: User level and fee information.
        """
        return self._make_request(endpoint)

    def get_card_numbers(self, endpoint=ACCOUNT_EP["card_numbers"]):
        """
        Get bank card numbers with the user's account.

        Returns:
            dict: Bank card numbers information.
        """
        return self._make_request(endpoint)

    def get_ibans(self, endpoint=ACCOUNT_EP["ibans"]):
        """
        Get IBANs associated with the user's account.

        Returns:
            dict: IBANs information.
        """
        return self._make_request(endpoint)

    def get_balances(self, endpoint=ACCOUNT_EP["balances"]):
        """
        Get Wallet assets balances for the user's account.

        Returns:
            dict: Account balances.
        """
        return self._make_request(endpoint)

    def get_money_deposit(self, endpoint=ACCOUNT_EP["money_deposit"]):
        """
        Get information related to money (Toman) deposits in the user's account.

        Returns:
            dict: Money (Toman) deposit information.
        """
        return self._make_request(endpoint)

    def get_money_withdrawal(self, endpoint=ACCOUNT_EP["money_withdrawal"]):
        """
        Get information related to money (Toman) withdrawal in the user's account.

        Returns:
            dict: Money (Toman) withdrawal information.
        """
        return self._make_request(endpoint)

    def get_crypto_deposit(self, endpoint=ACCOUNT_EP["crypto_deposit"]):
        """
        Get information related to cryptocurrency deposits in the user's account.

        Returns:
            dict: Cryptocurrency deposit information.
        """
        return self._make_request(endpoint)

    def get_crypto_withdrawal(self, endpoint=ACCOUNT_EP["crypto_withdrawal"]):
        """
        Get information related to cryptocurrency withdrawal in the user's account.

        Returns:
            dict: Cryptocurrency withdrawal information.
        """
        return self._make_request(endpoint)

    def get_transfer(self, endpoint=ACCOUNT_EP["transfers"]):
        """
        Get information related to transfer in the user's account.

        Returns:
            dict: Transfer information.
        """
        return self._make_request(endpoint)

    def set_money_withdrawal(
        self, iban: int, value: float, endpoint=ACCOUNT_EP["money_withdrawal"]
    ):
        """
        Initiate a money (Toman) withdrawal from the user's account to a specified IBAN.

        Args:
            iban (int): The IBAN (Shaba) to which money will be withdrawn.
            value (float): The amount of money (Toman) to withdraw.

        Returns:
            dict: Withdrawal request result or an error message.
        """
        payload_money_withdrawal: dict = {"iban": iban, "value": value}
        return self._make_request(
            endpoint, method="POST", json_payload=payload_money_withdrawal
        )

    def set_crypto_withdrawal(
        self,
        coin: str,
        network: str,
        value: float,
        wallet_address: str,
        memo=None,
        endpoint=ACCOUNT_EP["crypto_withdrawal"],
    ):
        """
        Initiate a cryptocurrency withdrawal from the user's account.

        Args:
            coin (str): The cryptocurrency coin symbol (e.g., "BTC").
            network (str): The network or blockchain (e.g., "Bitcoin").
            value (float): The amount of cryptocurrency to withdraw.
            wallet_address (str): The recipient's cryptocurrency wallet address.
            memo (str, optional): Additional address memo; If the network needs.

        Returns:
            dict: Withdrawal request result or an error message.
        """
        payload_crypto_withdrawal: dict = {
            "coin": coin,
            "network": network,
            "value": value,
            "wallet_address": wallet_address,
            "memo": memo,
        }
        return self._make_request(
            endpoint, method="POST", json_payload=payload_crypto_withdrawal
        )


class OrdersManage:
    """
    A Python client for interacting with the Wallex API to place orders and manage trading.

    Args:
        api_key (str): Your Wallex API key.
        base_url (str, optional): The base URL of the Wallex API. Defaults to "https://api.wallex.ir/".

    Methods:
        set_order(self, symbol: str, type_order: str, side: str, price: str, quantity: str, client_id: str = None) -> dict
            Place an order with the Wallex API.

        get_order(self, clientOrderId: str) -> dict
            Get information about a specific order by its clientOrderId.

        del_order(self, clientOrderId: str) -> dict
            Cancel an order by its clientOrderId.

        get_open_orders(self, symbol: str = None) -> dict
            Get a list of open orders.

        get_last_trades(self, symbol: str = None, side: str = None) -> dict
            Get a list of the last trades.

    Example:
        # Replace with your actual API key
        api_key: str = "Your-API-Key-Here"
        api: OrdersManage = OrdersManage(api_key)

        # Example usage of set_order function
        symbol: str = "USDTTMN"
        type_order: str = "LIMIT"
        side: str = "BUY"
        price: str = "50000"
        quantity: str = "10"
        client_id: str = "mohsen_zehtabchi_00001"

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
        open_orders_result = api.get_open_orders(symbol="USDTTMN")
        print("Open Orders Result:")
        print(open_orders_result)

        # Example usage of get_last_trades function
        last_trades_result = api.get_last_trades(symbol="USDTTMN", side="buy")
        print("Last Trades Result:")
        print(last_trades_result)
    """

    def __init__(self, api_key: str, base_url=BASE_URL):
        """
        Initialize the API client with the provided API key.

        Args:
            api_key (str): Your Wallex API key.
            base_url (str, optional): The base URL of the Wallex API. Defaults to "https://api.wallex.ir/".
        """
        self.api_key: str = api_key
        self.BASE_URL = base_url
        self.CONTENT_TYPE = CONTENT_TYPE

    def _make_request(
        self,
        endpoint: str,
        method: str = "GET",
        params: dict = None,
        json_payload: dict = None,
    ) -> dict:
        """
        Make an HTTP request to the Wallex API.

        :param endpoint(str): The API endpoint.
        :param method(str): The HTTP method (GET or POST or DELETE).
        :param params(dict): Query parameters (for GET requests).
        :param json_payload(dict): JSON payload (for POST requests).
        :return: (dict) JSON response or an error message.
        """
        url: str = self.BASE_URL + endpoint
        headers: dict = {
            "Content-Type": self.CONTENT_TYPE,
            "x-api-key": self.api_key,
        }
        try:
            response = requests.request(
                method, url, headers=headers, params=params, json=json_payload
            )
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"(Request) error: {e}"}
        except requests.exceptions.HTTPError as e:
            return {"error": f"(HTTP) error: {e}"}

    def _validate_client_id(self, client_id: str) -> bool:
        """
        Validate the client ID string.

        :param client_id(str): The client ID string to validate.
        :return: (bool) True if valid, False otherwise.
        """
        pattern = re.compile(r"^[\w.:-]+$")
        # Allow letters, numbers, '.', ':', '-' and '_'
        return bool(pattern.match(client_id))

    def set_order(
        self,
        symbol: str,
        type_order: str,
        side: str,
        price: str,
        quantity: str,
        client_id: str = None,
        endpoint=ORDERS_EP["orders"],
    ) -> dict:
        """
        Place an order with the Wallex API.

        :param symbol(str): The trading symbol.
        :param type_order(str): Order type (LIMIT or MARKET).
        :param side(str): Order side (BUY or SELL).
        :param price(str): Order price (for LIMIT orders).
        :param quantity(str): Order quantity.
        :param client_id(str): Unique client identifier (optional).
        :return: (dict) JSON response or an error message.
        """

        payload: dict = {
            "symbol": symbol,
            "type": type_order,
            "side": side,
            "price": price,
            "quantity": quantity,
        }

        if client_id:
            if not self._validate_client_id(client_id):
                return {
                    "error": "Invalid client ID. Only letters, numbers, '.', ':', '-' and '_' are allowed."
                }
            payload["client_id"] = client_id

        return self._make_request(endpoint, method="POST", json_payload=payload)

    def get_order(self, clientOrderId: str, endpoint=ORDERS_EP["orders"]) -> dict:
        """
        Get information about a specific order by its clientOrderId.

        :param clientOrderId(str): The unique client identifier of the order.
        :return: (dict) JSON response or an error message.
        """
        endpoint = f"{endpoint}/{clientOrderId}"
        return self._make_request(endpoint)

    def del_order(self, clientOrderId: str, endpoint=ORDERS_EP["orders"]) -> dict:
        """
        Cancel an order by its clientOrderId.

        :param clientOrderId(str): The unique client identifier of the order to cancel.
        :return: (dict) JSON response or an error message.
        """
        endpoint = f"{endpoint}/{clientOrderId}"
        return self._make_request(endpoint, method="DELETE")

    def get_open_orders(
        self, symbol: str = None, endpoint=ORDERS_EP["openOrders"]
    ) -> dict:
        """
        Get a list of open orders.

        :param symbol(str): The trading symbol (optional).
        :return: (dict) JSON response or an error message.
        """
        # params = {"symbol": symbol} if symbol else None
        params = {"symbol": symbol}
        return self._make_request(endpoint, params=params)

    def get_last_trades(
        self, symbol: str = None, side: str = None, endpoint=ORDERS_EP["last_trades"]
    ) -> dict:
        """
        Get a list of the last trades.

        :param symbol(str): The trading symbol (optional).
        :param side(str): Order side ("buy" or "sell") (optional).
        :return: (dict) JSON response or an error message.
        """
        # params = {"symbol": symbol, "side": side} if symbol and side else None
        params = {"symbol": symbol, "side": side}
        return self._make_request(endpoint, params=params)


class MarketsOTC:
    """
    A Python client for interacting with the Wallex OTC Markets API.

    Args:
        api_key (str): Your Wallex API key.
        base_url (str, optional): The base URL of the Wallex API. Defaults to "https://api.wallex.ir/".

    Methods:
        get_otc_markets():
            Get OTC markets.

            Returns:
                dict: JSON response or an error message.

        get_otc_price(symbol: str, side: str):
            Get the OTC price for a specific symbol and side.

            Args:
                symbol (str): The trading symbol.
                side (str): OTC side (BUY or SELL).

            Returns:
                dict: JSON response or an error message.

        get_otc_orders(symbol: str, side: str, amount: float):
            Get OTC orders for a specific symbol, side, and amount.

            Args:
                symbol (str): The trading symbol.
                side (str): OTC side (BUY or SELL).
                amount (float): The amount of the OTC order.

            Returns:
                dict: JSON response or an error message.
    """

    def __init__(self, api_key, base_url=BASE_URL):
        """
        Initialize the API client with the provided API key.

        Args:
            api_key (str): Your Wallex API key.
            base_url (str, optional): The base URL of the Wallex API. Defaults to "https://api.wallex.ir/".
        """
        self.api_key = api_key
        self.BASE_URL = base_url
        self.CONTENT_TYPE = CONTENT_TYPE

    def _make_request(self, endpoint, method="GET", params=None, json_payload=None):
        """
        Make an HTTP request to the Wallex API.

        :param endpoint(str): The API endpoint.
        :param method(str): The HTTP method (GET or POST or DELETE).
        :param params(dict): Query parameters (for GET requests).
        :param json_payload(dict): JSON payload (for POST requests).
        :return: (dict) JSON response or an error message.
        """
        url = self.BASE_URL + endpoint
        headers = {
            "Content-Type": self.CONTENT_TYPE,
            "x-api-key": self.api_key,
        }
        try:
            response = requests.request(
                method, url, headers=headers, params=params, json=json_payload
            )
            # response.raise_for_status()  # Raise an error if the response status code is not in the 200s.
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"(Request) error: {e}"}
        except requests.exceptions.HTTPError as e:
            return {"error": f"(HTTP) error: {e}"}

    def get_otc_markets(self, endpoint=OTC_EP["otc_markets"]):
        """
        Get a list of OTC markets.

        :return: (dict) JSON response or an error message.
        """
        return self._make_request(endpoint)

    def get_otc_price(self, symbol: str, side: str, endpoint=OTC_EP["otc_price"]):
        """
        Get the OTC price for a specific symbol and side.

        :param symbol(str): The trading symbol.
        :param side(str): OTC side (BUY or SELL).
        :return: (dict) JSON response or an error message.
        """
        if side not in {"BUY", "SELL"}:
            return {"error": "Invalid OTC side"}

        params = {"symbol": symbol, "side": side}
        return self._make_request(endpoint, params=params)

    def get_otc_orders(
        self, symbol: str, side: str, amount: float, endpoint=OTC_EP["otc_orders"]
    ):
        """
        Get OTC orders for a specific symbol, side, and amount.

        :param symbol(str): The trading symbol.
        :param side(str): OTC side (BUY or SELL).
        :param amount(float): The amount of the OTC order.
        :return: (dict) JSON response or an error message.
        """
        if side not in {"BUY", "SELL"}:
            return {"error": "Invalid OTC side"}

        payload = {"symbol": symbol, "side": side, "amount": amount}
        return self._make_request(endpoint, method="POST", json_payload=payload)


class WebSocket:
    """
    A class for interacting with the Wallex WebSocket API to receive live market data.

    Args:
        base_url (str, optional): The base URL of the Wallex API. Defaults to "https://api.wallex.ir/".

    Methods:
        __init__(self, once: bool = True, base_url: str = BASE_URL): Initialize the WebSocket class.
        subscribe(self, symbol: str, event: str, callback: callable): Subscribe to a market event.
        handle_received_data(self, data: dict): Handle received data.
        disconnect(self): Disconnect from the Socket.IO server.
        get_market_cap(self, symbol, event=EVENTS["marketCap"]): Get market capitalization data.
        get_buy_depth(self, symbol, event=EVENTS["buyDepth"]): Get buy depth data.
        get_sell_depth(self, symbol, event=EVENTS["sellDepth"]): Get sell depth data.
        get_trade(self, symbol, event=EVENTS["trade"]): Get trade data.

    Example:
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
    """

    def __init__(self, once: bool = True, base_url=BASE_URL):
        """
        Initialize the WebSocket class.

        Args:
            once (bool, optional): Whether to disconnect after receiving data once. Defaults to True.
            base_url (str, optional): The base URL of the Wallex API. Defaults to "https://api.wallex.ir/".
        """
        self.once = once
        self.sio = socketio.Client()
        self.latest_data = None  # Initialize instance variable to store latest data
        self.BASE_URL = base_url
        self.TRANSPORT = "websocket"

    def _on_broadcaster(self, channel: str, data: dict):
        """
        Internal event handler for "Broadcaster" events.

        :param channel: The channel name.
        :type channel: str

        :param data: The data received.
        :type data: dict

        """
        try:
            if self.callback:
                self.callback(data)
        except Exception as e:
            print(f"Error in callback: {e}")

    def _connect(self):
        """
        Connect to the Socket.IO server and subscribe to the specified channel.
        """
        try:
            # Define the "connect" event handler
            @self.sio.event
            def connect():
                # Emit the "subscribe" event with the desired channel
                self.sio.emit("subscribe", {"channel": self.channel})
                print(f"Connected to {self.BASE_URL}")

            # Define the "disconnect" event handler
            @self.sio.event
            def disconnect():
                print("Disconnected from the server")

            # Register the "Broadcaster" event handler
            self.sio.on("Broadcaster", self._on_broadcaster)

            # Connect to the Socket.IO server with the specified transport
            self.sio.connect(self.BASE_URL, transports=[self.TRANSPORT])

            # Keep the client running
            self.sio.wait()

        except Exception as e:
            print(f"Error: {e}")

    def disconnect(self):
        """
        Disconnect from the Socket.IO server.
        """
        self.sio.disconnect()

    def subscribe(self, symbol: str, event: str, callback: callable):
        """
        Subscribe to a specific channel and set the callback function to handle received data.

        :param symbol: The symbol or market identifier.
        :type symbol: str

        :param event: The event type to subscribe to (e.g.,EVENTS["marketCap"]).
        :type event: str

        :param callback: The callback function to handle received data.
        :type callback: callable

        """
        self.channel = symbol + event
        self.callback = callback
        self._connect()

    def handle_received_data(self, data: dict):
        """
        Handle received data.

        :param data: The received data.
        :type data: dict
        """

        # print(f"{self.channel} - Received message:\n", data)

        # Store received data in instance variable
        self.latest_data = data

        # Disconnect after receiving data once
        if self.once:
            self.disconnect()

    def get_market_cap(self, symbol, event=EVENTS["marketCap"]) -> dict:
        """
        Get market capitalization data for a symbol.

        :param symbol: The symbol or market identifier.
        :type symbol: str

        :param event: The event type (default: marketCap).
        :type event: str

        :return: The latest market capitalization data.
        :rtype: dict
        """
        self.subscribe(symbol=symbol, event=event, callback=self.handle_received_data)
        return self.latest_data

    def get_buy_depth(self, symbol, event=EVENTS["buyDepth"]) -> dict:
        """
        Get buy depth data for a symbol.

        :param symbol: The symbol or market identifier.
        :type symbol: str

        :param event: The event type (default: buyDepth).
        :type event: str

        :return: The latest buy depth data.
        :rtype: dict
        """
        self.subscribe(symbol=symbol, event=event, callback=self.handle_received_data)
        return self.latest_data

    def get_sell_depth(self, symbol, event=EVENTS["sellDepth"]) -> dict:
        """
        Get sell depth data for a symbol.

        :param symbol: The symbol or market identifier.
        :type symbol: str

        :param event: The event type (default: sellDepth).
        :type event: str

        :return: The latest sell depth data.
        :rtype: dict
        """
        self.subscribe(symbol=symbol, event=event, callback=self.handle_received_data)
        return self.latest_data

    def get_trade(self, symbol, event=EVENTS["trade"]) -> dict:
        """
        Get trade data for a symbol.

        :param symbol: The symbol or market identifier.
        :type symbol: str

        :param event: The event type (default: trade).
        :type event: str

        :return: The latest trade data.
        :rtype: dict
        """
        self.subscribe(symbol=symbol, event=event, callback=self.handle_received_data)
        return self.latest_data


# Example usage of the API methods (replace with your actual API key and data)
if __name__ == "__main__":
    import time

    api_key = "Your-API-Key-Here"  # Replace with your actual API key

    TestAccountManage = False
    TestMarketInfo = False
    TestOrdersManage = False
    TestMarketsOTC = False
    TestWebSocket = False

    # Example usage of the methods here...

    # ----------------------------*******----------------------------
    if TestAccountManage:
        api = AccountManage(api_key)

        ### Example usage: (get_profile)
        get_profile_result = api.get_profile()
        print("Profile Result:")
        print(get_profile_result)

        ### Example usage: (get_fee)
        get_fee_result = api.get_fee()
        print("Fee Result:")
        print(get_fee_result)

        ### Example usage: (get_card_numbers)
        get_card_numbers_result = api.get_card_numbers()
        print("Card Numbers Result:")
        print(get_card_numbers_result)

        ### Example usage: (get_ibans)
        get_ibans_result = api.get_ibans()
        print("IBANs Result:")
        print(get_ibans_result)

        ### Example usage: (get_balances)
        get_balances_result = api.get_balances()
        print("Balances Result:")
        print(get_balances_result)

        ### Example usage: (get_money_deposit)
        get_money_deposit_result = api.get_money_deposit()
        print("money Deposit Result:")
        print(get_money_deposit_result)

        ### Example usage: (get_money_withdrawal)
        get_money_withdrawal_result = api.get_money_withdrawal()
        print("money withdrawal Result:")
        print(get_money_withdrawal_result)

        ### Example usage: (get_crypto_deposit)
        get_crypto_deposit_result = api.get_crypto_deposit()
        print("Crypto Deposit Result:")
        print(get_crypto_deposit_result)

        ### Example usage: (get_crypto_withdrawal)
        get_crypto_withdrawal_result = api.get_crypto_withdrawal()
        print("Crypto withdrawal Result:")
        print(get_crypto_deposit_result)

        ### Example usage: (get_transfer)
        get_transfer_result = api.get_transfer()
        print("Transfer Result:")
        print(get_transfer_result)

        ### Example usage: (set_money_withdrawal)
        iban_to_withdraw_to = int("0100")  # Replace with Your IBAN(Shaba) (int)
        amount_to_withdraw = (
            100.0  # Replace with the amount you want to withdraw (float)
        )
        money_withdrawal_result = api.set_money_withdrawal(
            iban_to_withdraw_to, amount_to_withdraw
        )
        print("Money Withdrawal Result:")
        print(money_withdrawal_result)

        ### Example usage: (set_crypto_withdrawal)
        coin = "USDT"
        network = "TRC20"
        value = 100.0  # Replace with the amount you want to withdraw (float)
        wallet_address = "Your wallet address"  # Replace with Your wallet address (str)
        crypto_withdrawal_result = api.set_crypto_withdrawal(
            coin, network, value, wallet_address
        )
        print("crypto Withdrawal Result:")
        print(crypto_withdrawal_result)

    # ----------------------------*******----------------------------
    if TestMarketInfo:
        ### Example usage:
        api = MarketInfo()
        symbol = "USDTTMN"
        m00_time = int(time.time())
        h01_time = m00_time - (m00_time % (60 * 60))

        ### Retrieve a list of available markets
        markets = api.get_markets()
        print("Markets Result:")
        print(markets)

        ### Retrieve currency statistics
        currencies = api.get_currencies()
        print("Currencies Result:")
        print(currencies)

        ### Retrieve the order book for a specific symbol
        order_book_symbol = api.get_order_book_symbol(symbol)
        print("Order Book for Symbol Result:")
        print(order_book_symbol)

        ### Retrieve the order book for all symbols
        order_book_all = api.get_order_book_all(symbol)
        print("Order Book for All Symbols Result:")
        print(order_book_all)

        ### Retrieve the latest trades for a specific symbol
        latest_trades = api.get_latest_trades(symbol)
        print("Latest Trades Result:")
        print(latest_trades)

        ### Retrieve market history data for a specific symbol and time range
        time_from = h01_time - 60 * 60 * 5
        time_to = h01_time
        market_history = api.get_market_history(symbol, "60", time_from, time_to)
        print("Market History Result:")
        print(market_history)

    # ----------------------------*******----------------------------
    if TestOrdersManage:
        api = OrdersManage(api_key)

        symbol: str = "SHIBTMN"
        type_order: str = "LIMIT"
        side: str = "BUY"
        price: str = "0.3500"
        quantity: str = "350000"
        time_id = str(time.time())

        client_id: str = (
            f"MohZeh_{symbol}_{side}_{type_order}_Price:{price}_Quantity:{quantity}_Time:{time_id}"
        )

        ### Example usage of set_order function
        set_order_result = api.set_order(
            symbol, type_order, side, price, quantity, client_id
        )
        print("Set Order Result:")
        print(set_order_result)

        # time.sleep(0.5)
        # print("\n")
        # order = api.get_order(clientOrderId=client_id)
        # print("Set Order Result:")
        # print(order)
        # if order["result"]["side"] != "SELL":
        #     print(order["result"]["side"])
        #     api.del_order(clientOrderId=client_id)

        # print("\n")
        # order = api.get_order(clientOrderId=client_id)
        # print("Set Order Result:")
        # print(order["result"]["status"])

        ### Example usage of get_order function
        # client_order_id_to_get = "LIMIT:SELL_Mohsen_Zehtabchi_Price:0.3650_Quantity:299100"
        # get_order_result = api.get_order(client_order_id_to_get)
        # print("Get Order Result:")
        # print(get_order_result)

        ### Example usage of del_order function
        # client_order_id_to_cancel = (
        #     "MohZeh_LIMIT-SHIBTMN-Price:0.3500-Quantity:350000-Time:1708508442.0160692"
        # )
        # cancel_order_result = api.del_order(client_order_id_to_cancel)
        # print("Cancel Order Result:")
        # print(cancel_order_result)

        ### Example usage of get_open_orders function
        # open_orders_result = api.get_open_orders(symbol=symbol)
        # print("Open Orders Result:", open_orders_result)
        # len_dic = len(open_orders_result["result"]["orders"])
        # for i in range(len_dic):
        #     client_id_for = open_orders_result["result"]["orders"][i]["clientOrderId"]
        #     side_for = open_orders_result["result"]["orders"][i]["side"]
        #     print("i:", i)
        #     print("client_id_for:", client_id_for)
        #     print("seide_for:", side_for)
        #     if client_id_for.startswith("MohZeh") and side_for != "SELL":
        #         api.del_order(clientOrderId=client_id_for)

        # client_id = open_orders_result["result"]["orders"][0]["clientOrderId"]
        # print("client_id:", client_id)

        ### Example usage of get_last_trades function
        # last_trades_result = api.get_last_trades(symbol=symbol, side="sell")
        # print("Last Trades Result:")
        # print(last_trades_result)

    # ----------------------------*******----------------------------
    if TestMarketsOTC:
        api = MarketsOTC(api_key)

        symbol = "SHIBTMN"
        side = "SELL"
        amount = 100.0  # Replace with your desired amount

        ### Example usage: (get_otc_markets)
        otc_markets_result = api.get_otc_markets()
        print("OTC Markets Result:")
        print(otc_markets_result)

        ### Example usage: (get_otc_price)
        otc_price_result = api.get_otc_price(symbol, side)
        print("OTC Price Result:")
        print(otc_price_result)

        ### Example usage: (get_otc_orders)
        otc_orders_result = api.get_otc_orders(symbol, side, amount)
        print("OTC Orders Result:")
        print(otc_orders_result)

    # ----------------------------*******----------------------------
    if TestWebSocket:
        ### Define a symbol to subscribe to (e.g., "USDTTMN")
        symbol = "USDTTMN"

        ### Create an instance of the WebSocket class
        client = WebSocket()
        market_cap = client.get_market_cap(symbol=symbol)
        print("marketCap Data :\n", market_cap)
        buy_depth = client.get_buy_depth(symbol=symbol)
        print("buyDepth Data :\n", buy_depth)
        sell_depth = client.get_sell_depth(symbol=symbol)
        print("sellDepth Data :\n", sell_depth)
        trade = client.get_trade(symbol=symbol)
        print("Trade Data :\n", trade)

        ### Create instances of the WebSocket class
        # client1 = WebSocket()
        # client2 = WebSocket()
        # client3 = WebSocket()
        # client4 = WebSocket()

        ### Subscribe to the "marketCap" event and provide a callback function
        # client1.subscribe(symbol, EVENTS["marketCap"], client1.handle_received_data)
        # print("Data Client1 :", client1.latest_data)

        ### Subscribe to the "sellDepth" event and provide a callback function
        # client2.subscribe(symbol, EVENTS["sellDepth"], client2.handle_received_data)
        # print("Data Client2 :", client2.latest_data)

        ### Subscribe to the "buyDepth" event and provide a callback function
        # print(client3.subscribe(symbol, EVENTS["buyDepth"], client3.handle_received_data))
        # print("Data Client3 :", client3.latest_data)

        ### Subscribe to the "trade" event and provide a callback function
        # client4.subscribe(symbol, EVENTS["trade"], client4.handle_received_data)
        # print("Data Client4 :\n", client4.latest_data)
        # print(f"{client4.channel} - Received message :\n", client4.latest_data)
