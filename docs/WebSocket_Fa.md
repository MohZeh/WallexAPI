# <p align="center"> مستندات جامع (WebSocket)WallexAPI

## اخطار

قبل از استفاده از والکس‌API، لطفا این اخطار را مطالعه و درک کنید:

> **توجه**: استفاده از WallexAPI به عهده خودتان است. در حالی که تلاش‌هایی برای اطمینان از دقت و قابلیت اطمینان نرم‌افزار صورت گرفته است، نویسنده نمی‌تواند جامعیت و صحت آن را تضمین کند. نویسنده مسئولیتی در قبال هرگونه آسیب مستقیم، غیرمستقیم، اتفاقی، خاص یا ناشی از استفاده یا ناتوانی در استفاده از نرم‌افزار ندارد.

## مقدمه

فایل WallexAPI یک کتابخانه کلاینت Python است که برای تسهیل در تعامل با وب‌سرویس صرافی Wallex.ir طراحی شده است. این کلاس چندین متد برای اشتراک گذاری رویدادها و دریافت داده‌های زنده و لحظه‌ای بازار را ارائه می‌دهد.


## شروع کار

برای شروع استفاده از وب‌سوکت والکس، این مراحل را دنبال کنید:

۱. **دانلود**: وب‌سوکت والکس را از مخزن یا [این پیوند](https://codeload.github.com/mohzeh/WallexApi/zip/refs/heads/main) دانلود کرده و آن را به مکان پروژه خود کپی کنید.

۲. **وارد کردن**: کلاس `WebSocket` را در اسکریپت یا برنامه پایتون خود وارد کنید:

   ```python
   from wallexapi import WebSocket
   ```

۳. **مقدماتی**: یک نمونه از کلاس `WebSocket` ایجاد کنید:

   ```python
   client_WebSocket = WebSocket()
   ```

۴. **استفاده**: از متدهای ارائه شده توسط کلاس WebSocket برای اشتراک‌گذاری رویدادهای بازار و دریافت داده‌های زنده استفاده کنید.

### کلاس `WebSocket`

کلاس `WebSocket` برای ارتباط با وب‌سوکت والکس و اشتراک‌گذاری رویدادهای مختلف بازار طراحی شده است. این کلاس چندین متد برای اشتراک گذاری رویدادها و دریافت داده‌های بازار زنده ارائه می‌دهد.

#### متدها

- **`__init__(self, once: bool = True, base_url: str = BASE_URL)`**: مقدماتی کلاس WebSocket.
- **`subscribe(self, symbol: str, event: str, callback: callable)`**: اشتراک‌گذاری در یک رویداد بازار.
- **`disconnect(self)`**: قطع ارتباط از سرور Socket.IO.
- **`get_market_cap(self, symbol, event=EVENTS["marketCap"])`**: دریافت داده‌های سرمایه بازار.
- **`get_buy_depth(self, symbol, event=EVENTS["buyDepth"])`**: دریافت داده‌های عمق خرید.
- **`get_sell_depth(self, symbol, event=EVENTS["sellDepth"])`**: دریافت داده‌های عمق فروش.
- **`get_trade(self, symbol, event=EVENTS["trade"])`**: دریافت داده‌های معامله.

#### نمونه استفاده

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

### نکات اضافی

- مطمئن شوید که قبل از استفاده از والکس‌API اتصال اینترنت پایداری دارید.
- جایگزین کردن نشانه‌گذارهای مانند "کلید-API-شما" و "Your-IBAN" با کلید API و داده‌های درست و واقعی‌ خود.
- برای اطلاعات دقیق در مورد نقاط پایانی و پارامترهای موجود، به مستندات رسمی به [صفحه رسمی والکس‌API](https://api-docs.wallex.ir/) مراجعه کنید.
- برای تطابق با نیازهای خاص خود به بررسی و سفارشی‌سازی روش‌های ارائه شده توجه داشته باشید.
