import pandas as pd
import os

# آدرس دقیق فایل روی مک شما
FILE_PATH = '/Users/alimansouri/Desktop/M1_Quant_Engine/Data/XAUUSD_History.csv'

if not os.path.exists(FILE_PATH):
    print(f"❌ برادر فایل رو پیدا نکردم! مسیر رو چک کن: {FILE_PATH}")
else:
    df = pd.read_csv(FILE_PATH)
    print("✅ موتور پانداز روشن شد. ۱۰ هزار ساعت تاریخچه طلا بارگذاری شد.")
    
    # ۱. تمیزکاری دیتا
    df['Time'] = pd.to_datetime(df['Time'])
    df['Return'] = df['Close'].diff()
    
    # ۲. تعریف الگو (۳ ساعت ریزش متوالی)
    df['Three_Red'] = (df['Return'] < 0) & (df['Return'].shift(1) < 0) & (df['Return'].shift(2) < 0)
    
    # ۳. تحلیل نتیجه
    pattern_occurrences = df[df['Three_Red'] == True]
    if len(pattern_occurrences) > 0:
        win_cases = pattern_occurrences[pattern_occurrences['Return'].shift(-1) > 0]
        win_rate = (len(win_cases) / len(pattern_occurrences)) * 100
        
        print("-" * 40)
        print(f"🔍 تحلیل الگو روی {len(df)} ساعت گذشته:")
        print(f"🔸 تعداد دفعات رخ دادن الگو: {len(pattern_occurrences)} بار")
        print(f"📈 درصد موفقیت برگشت قیمت: {win_rate:.2f}%")
        print("-" * 40)
    else:
        print("❌ دیتای کافی برای پیدا کردن این الگو پیدا نشد.")
