# <p align="center"> مستندات جامع (AccountManage)WallexAPI

## اخطار

قبل از استفاده از والکس‌API، لطفا این اخطار را مطالعه و درک کنید:

> **توجه**: استفاده از WallexAPI به عهده خودتان است. در حالی که تلاش‌هایی برای اطمینان از دقت و قابلیت اطمینان نرم‌افزار صورت گرفته است، نویسنده نمی‌تواند جامعیت و صحت آن را تضمین کند. نویسنده مسئولیتی در قبال هرگونه آسیب مستقیم، غیرمستقیم، اتفاقی، خاص یا ناشی از استفاده یا ناتوانی در استفاده از نرم‌افزار ندارد.

## مقدمه

فایل WallexAPI یک کتابخانه کلاینت Python است که برای تسهیل در تعامل با وب‌سرویس صرافی Wallex.ir طراحی شده است. این کتابخانه یک مجموعه از متدهای مناسب را برای مدیریت حساب کاربر و انجام عملیات مالی فراهم می‌کند.

## شروع کار

برای شروع استفاده از والکس‌API، این مراحل را دنبال کنید:

۱. **دانلود**: والکس‌API را از مخزن دانلود کرده و آن را به محل پروژه خود کپی کنید یا از [این پیوند](https://codeload.github.com/mohzeh/WallexApi/zip/refs/heads/main) استفاده کنید:

۲. **وارد کردن**: کلاس `AccountManage` را به اسکریپت یا برنامه پایتونی خود وارد کنید:

   ```python
   from wallexapi import AccountManage
   ```

۳. **آماده‌سازی**: نمونه‌ای از کلاس `AccountManage` را با کلید API والکس خود ایجاد کنید:

   ```python
   api_key = "Your-API-Key-Here"
   client_AccountManage = AccountManage(api_key)
   ```

۴. **استفاده**: از متدهای ارائه شده توسط کلاس `AccountManage` برای مدیریت حساب کاربر و انجام عملیات مالی استفاده کنید.

## کلاس `AccountManage`

کلاس `AccountManage` به عنوان رابط اصلی برای تعامل با حساب‌های کاربری و انجام عملیات مالی از طریق والکس API عمل می‌کند. این کلاس چندین متد برای بازیابی اطلاعات حساب و شروع تراکنش‌های مالی ارائه می‌دهد.

### متدها

- **`get_profile(self)`**: اطلاعات پروفایل کاربر را بازیابی می‌کند.
- **`get_fee(self)`**: اطلاعات سطح کاربر و هزینه مرتبط با حساب کاربری را بازیابی می‌کند.
- **`get_card_numbers(self)`**: شماره‌های کارت بانکی مرتبط با حساب کاربری را بازیابی می‌کند.
- **`get_ibans(self)`**: شماره شبا مرتبط با حساب کاربری را بازیابی می‌کند.
- **`get_balances(self)`**: موجودی‌های دارایی کیف پول را برای حساب کاربری بازیابی می‌کند.
- **`get_money_deposit(self)`**: اطلاعات مربوط به واریز پول (تومان) در حساب کاربری را بازیابی می‌کند.
- **`get_money_withdrawal(self)`**: اطلاعات مربوط به برداشت پول (تومان) از حساب کاربری را بازیابی می‌کند.
- **`get_crypto_deposit(self)`**: اطلاعات مربوط به واریز ارز دیجیتال در حساب کاربری را بازیابی می‌کند.
- **`get_crypto_withdrawal(self)`**: اطلاعات مربوط به برداشت ارز دیجیتال از حساب کاربری را بازیابی می‌کند.
- **`get_transfer(self)`**: اطلاعات مربوط به انتقال در حساب کاربری را بازیابی می‌کند.
- **`set_money_withdrawal(self, iban, value)`**: یک برداشت پول (تومان) از حساب کاربری به یک شبا مشخص را آغاز می‌کند.
- **`set_crypto_withdrawal(self, coin, network, value, wallet_address, memo=None)`**: یک برداشت ارز دیجیتال از حساب کاربری را آغاز می‌کند.

### مثال

در ادامه مثالی از نحوه استفاده از کلاس `AccountManage` آورده شده است:

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

## نکات اضافی

- مطمئن شوید که قبل از استفاده از والکس‌API اتصال اینترنت پایداری دارید.
- جایگزین کردن نشانه‌گذارهای مانند "کلید-API-شما" و "Your-IBAN" با کلید API و داده‌های درست و واقعی‌ خود.
- برای اطلاعات دقیق در مورد نقاط پایانی و پارامترهای موجود، به مستندات رسمی به [صفحه رسمی والکس‌API](https://api-docs.wallex.ir/) مراجعه کنید.
- برای تطابق با نیازهای خاص خود به بررسی و سفارشی‌سازی روش‌های ارائه شده توجه داشته باشید.
