import csv
import os
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# مسیر فایلی که دیتاها قراره توش ذخیره بشه
CSV_FILE = 'logs/market_data.csv'

# اگر فایل وجود نداره، بسازش و هدرهای جدول رو توش بنویس
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Symbol', 'Ask', 'Bid'])

class QuantHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # جواب دادن به متاتریدر (که ارتباط قطع نشه)
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"OK")
        
        # استخراج دیتا
        parsed_url = urlparse(self.path)
        params = parse_qs(parsed_url.query)
        
        if 'symbol' in params and 'ask' in params:
            symbol = params['symbol'][0]
            ask_price = params['ask'][0]
            bid_price = params['bid'][0]
            
            # ساختن مُهر زمان با دقت میلی‌ثانیه برای هوش مصنوعی
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            
            # ذخیره کردن دیتا در فایل CSV
            with open(CSV_FILE, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([now, symbol, ask_price, bid_price])
                
            # چاپ گزارش در ترمینال
            print(f"💾 [SAVED] {now} | {symbol} | Ask: {ask_price} | Bid: {bid_price}")

# روشن کردن موتور
server_address = ('127.0.0.1', 5555)
httpd = HTTPServer(server_address, QuantHandler)
print("🚀 مغز پایتون آپدیت شد! در حال ضبط و ذخیره دیتای بازار در پوشه logs...")
httpd.serve_forever()
