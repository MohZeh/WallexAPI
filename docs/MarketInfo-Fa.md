# <p align="center"> مستندات جامع (MarketInfo)WallexAPI

## توجه

قبل از استفاده از WallexAPI، لطفاً این توضیحات را مطالعه و درک کنید:

> **توجه**: استفاده از WallexAPI به عهده خودتان است. در حالی که تلاش‌هایی برای اطمینان از دقت و قابلیت اطمینان نرم‌افزار صورت گرفته است، نویسنده نمی‌تواند جامعیت و صحت آن را تضمین کند. نویسنده مسئولیتی در قبال هرگونه آسیب مستقیم، غیرمستقیم، اتفاقی، خاص یا ناشی از استفاده یا ناتوانی در استفاده از نرم‌افزار ندارد.

## مقدمه

فایل WallexAPI یک کتابخانه کلاینت Python است که برای تسهیل در تعامل با وب‌سرویس صرافی Wallex.ir طراحی شده است. این کلاس (WallexAPI.MarketInfo) مجموعه‌ای از متدهای مناسب را برای بازیابی اطلاعات مربوط به بازار ارائه می‌دهد، از جمله بازارهای موجود، آمار ارز، اطلاعات دفتر سفارشات، آخرین معاملات و تاریخچه بازار.

## شروع کار

برای شروع استفاده از WallexAPI، مراحل زیر را دنبال کنید:

۱. **دانلود**: Wallex API را از مخزن یا [این لینک](https://codeload.github.com/mohzeh/WallexApi/zip/refs/heads/main) دانلود کنید و آن را به محل پروژه خود منتقل کنید:

۲. **وارد کردن**: کلاس `MarketInfo` را به اسکریپت Python یا برنامه خود وارد کنید:

   ```python
   from wallexapi import MarketInfo
   ```

۳. **آماده‌سازی**: یک نمونه از کلاس `MarketInfo` را ایجاد کنید:

   ```python
   client_MarketInfo = MarketInfo()
   ```

۴. **استفاده**: میتوانید از متدهای ارائه شده توسط کلاس `MarketInfo` برای تعامل با وب‌سرویس صرافی Wallex.ir استفاده کنید.

## کلاس `MarketInfo`

کلاس `MarketInfo` به عنوان رابط اصلی برای دسترسی به داده‌های مربوط به بازار از API Wallex عمل می‌کند. این کلاس چندین متد برای بازیابی انواع مختلف اطلاعات ارائه می‌دهد:

### متدها

- **`get_markets(self)`**: دریافت لیستی از بازارهای موجود
- **`get_currencies(self)`**: دریافت اطلاعات نمادها
- **`get_order_book_symbol(self, symbol: str)`**: دریافت دفتر سفارشات برای یک نماد خاص
- **`get_order_book_all(self, symbol: str)`**: دریافت دفتر سفارشات برای همه نمادها
- **`get_latest_trades(self, symbol: str)`**: دریافت آخرین معاملات برای یک نماد خاص
- **`get_market_history(self, symbol: str, resolution: str, time_from: int, time_to: int)`**: دریافت داده‌های تاریخچه بازار برای یک نماد خاص با محدوده زمانی مشخص

### مثال

در زیر مثالی از نحوه استفاده از کلاس `MarketInfo` آمده است:

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

## نکات اضافی

- اطمینان حاصل کنید که قبل از استفاده از WallexAPI اتصال اینترنت پایدار داشته باشید.
- برای اطلاعات دقیق در مورد نقاط پایانی و پارامترهای موجود، مستندات رسمی به [صفحه رسمی WallexAPI](https://api-docs.wallex.ir/) مراجعه کنید.
- برای تطابق با نیازهای خاص خود به بررسی و سفارشی‌سازی روش‌های ارائه شده توجه داشته باشید.
