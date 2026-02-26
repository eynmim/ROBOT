from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class QuantHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # اول به متاتریدر میگیم دیتا رسید، مرسی!
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"OK")
        
        # استخراج دیتای قیمت از آدرس ارسالی
        parsed_url = urlparse(self.path)
        params = parse_qs(parsed_url.query)
        
        if 'symbol' in params and 'ask' in params:
            symbol = params['symbol'][0]
            ask_price = params['ask'][0]
            bid_price = params['bid'][0]
            print(f"🟢 [DATA BAZAR] Nemad: {symbol} | Kharid(Ask): {ask_price} | Forosh(Bid): {bid_price}")
        else:
            # این برای درخواست‌های خالیه که نادیده‌اش می‌گیریم
            pass

# روشن کردن موتور
server_address = ('127.0.0.1', 5555)
httpd = HTTPServer(server_address, QuantHandler)
print("🚀 مغز پایتون آپدیت شد! در حال دریافت زنده قیمت بازار...")
httpd.serve_forever()from http.server import BaseHTTPRequestHandler, HTTPServer

class QuantHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # وقتی متاتریدر سوال می‌پرسه، این جواب رو بهش می‌دیم:
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        
        # دستور فرمانده به سرباز
        message = "Salam az Mac M1! Hame chi ok e. Amadeye Trade!"
        self.wfile.write(message.encode('utf-8'))
        
        print("یک درخواست از متاتریدر دریافت شد و جواب داده شد.")

# روشن کردن سرور روی پورت 5555
server_address = ('127.0.0.1', 5555)
httpd = HTTPServer(server_address, QuantHandler)
print("فرمانده (پایتون) بیدار شد! منتظر تماس سرباز (متاتریدر) هستم...")
httpd.serve_forever()

