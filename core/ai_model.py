import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import os

FILE_PATH = '/Users/alimansouri/Desktop/M1_Quant_Engine/Data/XAUUSD_History.csv'

if not os.path.exists(FILE_PATH):
    print("❌ فایل دیتا یافت نشد!")
else:
    df = pd.read_csv(FILE_PATH)
    
    # --- مهندسی ویژگی‌ها (Feature Engineering) ---
    # ما به هوش مصنوعی می‌گیم این‌ها رو ببین:
    df['Return'] = df['Close'].diff()
    df['Range'] = df['High'] - df['Low']
    df['Vol_Change'] = df['TickVolume'].diff()
    
    # هدف (Target): آیا ساعت بعد قیمت بالا میره؟ (1 برای بله، 0 برای خیر)
    df['Target'] = (df['Return'].shift(-1) > 0).astype(int)
    
    # پاک کردن ردیف‌های خالی
    df = df.dropna()
    
    # انتخاب ویژگی‌ها برای آموزش
    features = ['Return', 'Range', 'TickVolume', 'Vol_Change']
    X = df[features]
    y = df['Target']
    
    # جدا کردن دیتای آموزش و تست (۸۰٪ آموزش، ۲۰٪ تست)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    
    # ساخت مدل جنگل تصادفی (Random Forest)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # تست مدل
    accuracy = model.score(X_test, y_test)
    
    print("🤖 هوش مصنوعی آموزش دید!")
    print(f"🎯 دقت پیش‌بینی مدل روی دیتای تست: {accuracy*100:.2f}%")
    print("-" * 30)
    print("💡 نکته: اگر دقت بالای 52% باشه، یعنی ما لبه معاملاتی (Edge) پیدا کردیم!")
