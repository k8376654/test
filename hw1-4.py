# 4.	選擇性敘述的練習-leapYear
# 輸入一西元年，如2015。判斷此年份是否為閏年。
# 提示：每四年一閏，每百年不閏，每四百年一閏，每四千年不閏。

year = eval(input("輸入西元年，我會幫你算他是不是閏年 :\n"))

if year%4000 == 0:
    print("平年")
elif year%400== 0 :
    print("閏年")
elif year%100 == 0 :
    print("平年")
elif year%4 == 0 :
    print("閏年")
else :
    print("平年")

# 大的數字寫上面給他篩





