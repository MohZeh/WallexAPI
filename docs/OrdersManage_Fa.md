# <p align="center"> مستند جامع WallexAPI(OrdersManage)

## اخطار

قبل از استفاده از WallexAPI، لطفا این اخطار را بخوانید و درک کنید:

> **توجه**: استفاده از WallexAPI به عهده خودتان است. در حالی که تلاش‌هایی برای اطمینان از دقت و قابلیت اطمینان نرم‌افزار صورت گرفته است، نویسنده نمی‌تواند جامعیت و صحت آن را تضمین کند. نویسنده مسئولیتی در قبال هرگونه آسیب مستقیم، غیرمستقیم، اتفاقی، خاص یا ناشی از استفاده یا ناتوانی در استفاده از نرم‌افزار ندارد.

## مقدمه

فایل WallexAPI یک کتابخانه کلاینت Python است که برای تسهیل در تعامل با وب‌سرویس صرافی Wallex.ir طراحی شده است. این مستند به عنوان راهنمایی برای توسعه‌دهندگان برای درک و استفاده از قابلیت‌های ارائه شده توسط کلاس OrdersManage عرضه شده است.

## شروع کار

برای شروع استفاده از WallexAPI، این مراحل را دنبال کنید:

۱. **دانلود**: کتابخانه Wallex API را از مخزن یا [این لینک](https://codeload.github.com/mohzeh/WallexApi/zip/refs/heads/main) دانلود کرده و آن را در محل پروژه‌ی خود کپی کنید.
   
۲. **وارد کردن**: کلاس `OrdersManage` را در اسکریپت یا برنامه Python خود وارد کنید:

   ```python
   from wallexapi import OrdersManage
   ```

۳. **آماده‌سازی**: یک نمونه از کلاس `OrdersManage` را ایجاد کنید:

   ```python
    # Replace 'Your-API-Key-Here' with your actual API key
    api_key = "Your-API-Key-Here"
    client_OrdersManage = OrdersManage(api_key)
   ```

۴. **استفاده**: از روش‌های ارائه شده توسط کلاس OrdersManage برای تعامل با API والکس برای مدیریت سفارشات و معاملات استفاده کنید.


### کلاس `OrdersManage`

کلاس `OrdersManage` به عنوان رابط اصلی برای تعامل با سفارشات و معاملات از طریق API والکس عمل می‌کند. این کلاس چندین روش برای قرار دادن سفارشات، بازیابی اطلاعات سفارش و مدیریت معاملات ارائه می‌دهد.

#### روش‌ها

- **`set_order(self, symbol, type_order, side, price, quantity, client_id=None)`**: ایجاد یک سفارش .
- **`get_order(self, clientOrderId)`**: دریافت اطلاعات در مورد یک سفارش خاص با استفاده از کلاینت آیدی آن.
- **`del_order(self, clientOrderId)`**: لغو یک سفارش با استفاده از کلاینت آیدی آن.
- **`get_open_orders(self, symbol=None)`**: دریافت لیستی از سفارشات باز.
- **`get_last_trades(self, symbol=None, side=None)`**: دریافت لیستی از آخرین معاملات.

### مثال

در ادامه یک مثال از نحوه استفاده از کلاس `OrdersManage` آورده شده است:

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

### توجهات اضافی

- قبل از استفاده از API والکس، اطمینان حاصل کنید که اتصال اینترنت پایداری دارید.
- مقادیری مانند "Your-API-Key-Here" را با کلید API و داده‌های واقعی خود جایگزین کنید.
- برای اطلاعات دقیق در مورد نقاط پایانی و پارامترهای موجود، به مستندات رسمی در [صفحه رسمی والکسAPI](https://api-docs.wallex.ir/) مراجعه کنید.
- برای تطابق با نیازهای خاص خود به بررسی و سفارشی‌سازی روش‌های ارائه شده توجه داشته باشید.
