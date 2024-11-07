import pandas as pd

# بارگذاری داده‌ها از فایل CSV
file_path = 'WLD_RTFP_country_2024-11-04.csv'
data = pd.read_csv(file_path)

# تبدیل ستون تاریخ به فرمت زمانی و استخراج سال و ماه
data['date'] = pd.to_datetime(data['date'])
data['Year'] = data['date'].dt.year
data['Month'] = data['date'].dt.month

# ایجاد جدول محوری برای مقایسه قیمت‌های Close در هر ماه از سال‌های مختلف
pivot_table = data.pivot_table(values='Close', index='Year', columns='Month')

# تغییر نام ستون‌ها به نام ماه‌ها
pivot_table.columns = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# نمایش جدول
print(pivot_table)
