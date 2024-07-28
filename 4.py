name1 = input("Enter name 1: ")#گرفتن ام اول
name2 = input("Enter name 2: ")#گرفتن اسم دوم
name3 = input("Enter name 3: ")#گرفتن اسم سوم
name4 = input("Enter name 4: ")#گرفتن اسم چهارم
name5 = input("Enter name 5: ")#گرفتن اسم پنجم
inputs = (name1, name2, name3, name4, name5)#قرار دادن انها در متغیر ها
(A, B, *C) = inputs#قرار دادن انها در متغیر ها
print(A)#چاپ اولین متغیر
print(B)#چاپ دومین متغیر
print(*C)#چاپ سومین متغیر به صورت ساده
#پایان