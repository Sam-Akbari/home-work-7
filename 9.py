start = int(input("Start: "))#شروع بازه
end = int(input("End: "))#اخر بازه
l1 = []#ساختن یک لیست
while start <= end:#تا وقتی که شروع از پایان کوچک تر است دستور را انجام میدهد
    if start % 15 == 0:#اگر بر 15 بخش پذیر بود
        l1.append(start)#ان را به لیست اضافه کن
    start += 1#یکی اضافه کن
print(l1)#اعداد را نشان بده
print(len(l1))#تعداد کاراکتر هارا نشان میدهد
#پایان