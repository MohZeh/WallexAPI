### <p align="center"> English

#### <p align="center"> "This program is unofficial and not affiliated with the exchange. Use it at your own discretion."


# WallexAPI - Python Client for Wallex.ir Exchange API

Welcome to WallexAPI! This Python program provides a powerful client for interacting with the Wallex.ir Exchange API. With this client, you can seamlessly integrate the functionality of Wallex.ir Exchange into your Python applications.

## Features

- **Comprehensive API Coverage**: Implementations for all APIs offered by Wallex.ir Exchange, including account management, trading, market data retrieval, and order management.
- **Easy Integration**: Simple-to-use methods allow you to quickly incorporate Wallex.ir Exchange functionalities into your Python projects.
- **Flexibility**: Customize and extend the client according to your specific requirements and use cases.
- **Detailed Documentation**: Extensive documentation and examples are provided to help you understand and utilize the client effectively.

## Getting Started

1. **Obtain API Key**: Before using the WallexAPI client, you need to obtain an API key from Wallex.ir Exchange. Contact Wallex.ir Exchange to acquire your API key.
2. **Installation**: Clone the repository and install the required dependencies using `pip`:

   ```
   git clone https://github.com/MohZeh/WallexAPI.git
   cd WallexAPI
   pip install -r requirements.txt
   ```

3. **Usage**: Import the `WallexAPI` class into your Python script and initialize it with your API key:

   ```python
   from wallexapi import MarketInfo, AccountManage, OrdersManage, MarketsOTC, WebSocket

   api_key = "Your-API-Key-Here"
   client_MarketInfo = MarketInfo()
   client_AccountManage = AccountManage(api_key)
   client_OrdersManage = OrdersManage(api_key)
   client_MarketsOTC = MarketsOTC(api_key)
   client_WebSocket = WebSocket()
   
   ```

4. **Examples**: Utilize the methods provided by the client to interact with the Wallex.ir Exchange API. Refer to the documentation and examples for guidance on usage.

## Documentation

For detailed documentation on how to use WallexAPI and the available methods, refer to the [documentation file](./docs/).

## Disclaimer

The responsibility of using this program rests with the user, who should conduct the necessary due diligence before utilizing the program. The author of this program is not responsible for any damages or losses incurred as a result of using this program.

## Contributions

Contributions to WallexAPI are welcome! Whether you want to report a bug, suggest a feature, or contribute code, your input is appreciated. Feel free to open issues or pull requests on the GitHub repository.

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](./LICENSE.bib) file for details.

###

### 
 ###  <p align="center"> فارسی
 ###  <p align="center"> "این برنامه غیر رسمی است و به صرافی وابسته نیست. با صلاحدید خود از آن استفاده کنید."
 # کلاینت پایتون برای والکس - WallexAPI

به WallexAPI خوش آمدید! این برنامه پایتون یک کلاینت قدرتمند برای تعامل با API اکسچنج والکس است. با استفاده از این کلاینت، می‌توانید به طور بی‌درنگ قابلیت‌های اکسچنج والکس را در برنامه‌های پایتونی خود یکپارچه کنید.

## ویژگی‌ها

- **پوشش گسترده API**: پیاده‌سازی برای تمامی API‌های ارائه شده توسط اکسچنج والکس از جمله مدیریت حساب، معامله، بازیابی داده‌های بازار و مدیریت سفارشات.
- **ادغام آسان**: از روش‌های ساده برای سریع یکپارچه کردن قابلیت‌های اکسچنج والکس در پروژه‌های پایتونی خود استفاده کنید.
- **انعطاف‌پذیری**: کلاینت را بر اساس نیازها و موارد استفاده خاص خود سفارشی‌سازی و گسترش دهید.
- **مستندات دقیق**: مستندات جامع و مثال‌ها برای کمک به درک و استفاده مؤثر از کلاینت فراهم شده است.

## شروع

۱. **کلید API را دریافت کلید**: قبل از استفاده از کلاینت WallexAPI، باید یک کلید API از اکسچنج والکس دریافت کنید. با اکسچنج والکس تماس بگیرید تا کلید API خود را دریافت کنید.

۲. **نصب**: مخزن را کلون کرده و وابستگی‌های مورد نیاز را با استفاده از `pip` نصب کنید:

   ```
   git clone https://github.com/MohZeh/WallexAPI.git
   cd WallexAPI
   pip install -r requirements.txt
   ```

۳. **استفاده**: کلاس `WallexAPI` را به اسکریپت پایتونی خود وارد کنید و با استفاده از کلید API خود آن را مقداردهی کنید:

   ```python
   from wallexapi import MarketInfo, AccountManage, OrdersManage, MarketsOTC, WebSocket

   api_key = "Your-API-Key-Here"
   client_MarketInfo = MarketInfo()
   client_AccountManage = AccountManage(api_key)
   client_OrdersManage = OrdersManage(api_key)
   client_MarketsOTC = MarketsOTC(api_key)
   client_WebSocket = WebSocket()
   ```

۴. **مثال‌ها**: از روش‌های ارائه شده توسط کلاینت برای تعامل با API اکسچنج والکس استفاده کنید. برای راهنمایی در استفاده به مستندات و مثال‌ها مراجعه کنید.

## مستندات

برای مستندات جامع در مورد چگونگی استفاده از WallexAPI و متدهای موجود، به [فایل مستندات](./docs/) مراجعه کنید.

## سلب مسئولیت

مسئولیت استفاده از این برنامه با کاربر است که باید قبل از استفاده از برنامه مورد بررسی و ارزیابی لازم را انجام دهد. نویسنده این برنامه مسئولیتی در قبال هرگونه آسیب یا ضرر ناشی از استفاده از این برنامه ندارد.

## مشارکت‌ها

مشارکت‌ها در WallexAPI مورد استقبال قرار می‌گیرند! اگر می‌خواهید یک باگ را گزارش دهید، ویژگی‌ای را پیشنهاد دهید یا کدی را ارسال کنید، ورود شما قدردانی می‌شود. احساس راحت کنید که مسائل یا درخواست‌های پیشنهادی را در مخزن GitHub باز کنید.

## مجوز

این پروژه تحت مجوز GPL-3.0 است - جزئیات را در [فایل مجوز](./LICENSE.bib) ببینید.

