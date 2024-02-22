# <p align="center"> مستند جامع WallexAPI(MarketsOTC)

## توجه

قبل از استفاده از WallexAPI، لطفاً این توضیحات را مطالعه و درک کنید:

> **توجه**: استفاده از WallexAPI به عهده خودتان است. در حالی که تلاش‌هایی برای اطمینان از دقت و قابلیت اطمینان نرم‌افزار صورت گرفته است، نویسنده نمی‌تواند جامعیت و صحت آن را تضمین کند. نویسنده مسئولیتی در قبال هرگونه آسیب مستقیم، غیرمستقیم، اتفاقی، خاص یا ناشی از استفاده یا ناتوانی در استفاده از نرم‌افزار ندارد.

## مقدمه

فایل WallexAPI یک کتابخانه کلاینت Python است که برای تسهیل در تعامل با وب‌سرویس صرافی Wallex.ir طراحی شده است. این مستند به عنوان راهنمایی برای توسعه دهندگان برای درک و استفاده از قابلیت های ارائه شده توسط کلاس MarketsOTC عرضه شده است.

## شروع کار

برای شروع استفاده از WallexAPI، این مراحل را دنبال کنید:

۱. **دانلود**: کتابخانه Wallex را از مخزن یا [این لینک](https://codeload.github.com/mohzeh/WallexApi/zip/refs/heads/main) دانلود کرده و آن را به مکان پروژه خود کپی کنید.

۲. **وارد کردن**: کلاس `MarketsOTC` را به اسکریپت Python یا برنامه خود وارد کنید.

   ```python
   from wallexapi import MarketsOTC
   ```

۳. **مقدمه**: یک نمونه از کلاس `MarketsOTC` را ایجاد کنید:

    ```python
    client_MarketsOTC = MarketsOTC(api_key)
    ```

- `api_key`: Your Wallex API key.
- `base_url` (optional): The base URL of the Wallex API. Defaults to `"https://api.wallex.ir/"`.

۴. **استفاده**: از روش‌های ارائه شده توسط کلاس MarketsOTC برای تعامل با API ولکس برای مدیریت سفارشات و معاملات از طریق OTC استفاده کنید.

#### متدها:

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


#### مثال استفاده:

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
### یادداشت‌های اضافی:

- اطمینان حاصل کنید که قبل از استفاده از WallexAPI اتصال اینترنت پایدار داشته باشید.
- برای اطلاعات دقیق در مورد نقاط پایانی و پارامترهای موجود، مستندات رسمی به [صفحه رسمی WallexAPI](https://api-docs.wallex.ir/) مراجعه کنید.
- برای تطابق با نیازهای خاص خود به بررسی و سفارشی‌سازی روش‌های ارائه شده توجه داشته باشید.
