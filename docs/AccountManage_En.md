# <p align="center"> WallexAPI(AccountManage) Comprehensive Documentation

## Disclaimer

Before using WallexAPI, please read and understand the following disclaimer:

> **Disclaimer**: The use of WallexAPI is at your own risk. While efforts have been made to ensure the accuracy and reliability of the software, the author cannot guarantee its correctness or completeness. The author shall not be liable for any direct, indirect, incidental, special, or consequential damages arising out of the use of or inability to use the software.

## Introduction

WallexAPI is a Python client library designed to facilitate interactions with the Wallex.ir Exchange API. It provides a set of convenient methods for managing user accounts and performing financial operations.

## Getting Started

To begin using WallexAPI, follow these steps:

1. **Download**: Download the Wallex API from the repository or [this link](https://codeload.github.com/mohzeh/WallexApi/zip/refs/heads/main) and copy it to your project location:

2. **Import**: Import the `AccountManage` class into your Python script or application:

   ```python
   from wallexapi import AccountManage
   ```

3. **Initialization**: Create an instance of the `AccountManage` class with your Wallex API key:

   ```python
   api_key = "Your-API-Key-Here"
   client_AccountManage = AccountManage(api_key)
   ```

4. **Usage**: Utilize the methods provided by the `AccountManage` class to manage user accounts and perform financial operations.

## `AccountManage` Class

The `AccountManage` class serves as the main interface for interacting with user accounts and performing financial operations through the Wallex API. It offers several methods for retrieving account information and initiating financial transactions.

### Methods

- **`get_profile(self)`**: Retrieves the user's profile information.
- **`get_fee(self)`**: Retrieves user level and fee information related to the user's account.
- **`get_card_numbers(self)`**: Retrieves bank card numbers associated with the user's account.
- **`get_ibans(self)`**: Retrieves IBANs associated with the user's account.
- **`get_balances(self)`**: Retrieves wallet asset balances for the user's account.
- **`get_money_deposit(self)`**: Retrieves information related to money (Toman) deposits in the user's account.
- **`get_money_withdrawal(self)`**: Retrieves information related to money (Toman) withdrawals in the user's account.
- **`get_crypto_deposit(self)`**: Retrieves information related to cryptocurrency deposits in the user's account.
- **`get_crypto_withdrawal(self)`**: Retrieves information related to cryptocurrency withdrawals in the user's account.
- **`get_transfer(self)`**: Retrieves information related to transfers in the user's account.
- **`set_money_withdrawal(self, iban, value)`**: Initiates a money (Toman) withdrawal from the user's account to a specified IBAN.
- **`set_crypto_withdrawal(self, coin, network, value, wallet_address, memo=None)`**: Initiates a cryptocurrency withdrawal from the user's account.

### Example

Here's an example of how to use the `AccountManage` class:

```python
# Import the AccountManage class
from wallexapi import AccountManage

# Initialize AccountManage with your API key
api_key = "Your-API-Key-Here"
api = AccountManage(api_key)

# Retrieve the user's profile information
profile_info = api.get_profile()
print("User Profile:")
print(profile_info)

# Retrieve user level and fee information
fee_info = api.get_fee()
print("User Fee Information:")
print(fee_info)

# Retrieve bank card numbers
card_numbers = api.get_card_numbers()
print("Bank Card Numbers:")
print(card_numbers)

# Retrieve IBANs
ibans = api.get_ibans()
print("IBANs:")
print(ibans)

# Retrieve wallet balances
balances = api.get_balances()
print("Wallet Balances:")
print(balances)

# Retrieve money deposit information
money_deposit_info = api.get_money_deposit()
print("Money Deposit Information:")
print(money_deposit_info)

# Retrieve money withdrawal information
money_withdrawal_info = api.get_money_withdrawal()
print("Money Withdrawal Information:")
print(money_withdrawal_info)

# Retrieve cryptocurrency deposit information
crypto_deposit_info = api.get_crypto_deposit()
print("Crypto Deposit Information:")
print(crypto_deposit_info)

# Retrieve cryptocurrency withdrawal information
crypto_withdrawal_info = api.get_crypto_withdrawal()
print("Crypto Withdrawal Information:")
print(crypto_withdrawal_info)

# Retrieve transfer information
transfer_info = api.get_transfer()
print("Transfer Information:")
print(transfer_info)

# Initiate a money withdrawal
iban_to_withdraw_to = "Your-IBAN"
amount_to_withdraw = 100.0  # Replace with the amount you want to withdraw
money_withdrawal_result = api.set_money_withdrawal(iban_to_withdraw_to, amount_to_withdraw)
print("Money Withdrawal Result:")
print(money_withdrawal_result)

# Initiate a cryptocurrency withdrawal
coin = "USDT"
network = "TRC20"
value = 100.0  # Replace with the amount you want to withdraw
wallet_address = "Your-wallet-address"  # Replace with your wallet address
crypto_withdrawal_result = api.set_crypto_withdrawal(coin, network, value, wallet_address)
print("Crypto Withdrawal Result:")
print(crypto_withdrawal_result)
```

## Additional Notes

- Ensure that you have a stable internet connection before using WallexAPI.
- Replace placeholders such as "Your-API-Key-Here" and "Your-IBAN" with your actual API key and data.
- For detailed information about available endpoints and parameters, refer to the official documentation on the [official WallexAPI page](https://api-docs.wallex.ir/).
- Feel free to explore and customize the provided methods to suit your specific requirements.

