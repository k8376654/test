# 6.	選擇性敘述的練習-equation
# 一元二次方程式ax2+bx+c=0。輸入a, b, c三值，並計算方程式的根。
# b2-4ac > 0，有兩個不相等的實根。
# b2-4ac = 0，有兩個相等的實根。
# b2-4ac < 0，則印出”沒有實根”。

import math

a,b,c = eval(input("列出一元二次方程式ax2+bx+c=0。輸入a, b, c三值\n分別用逗號隔開，並計算方程式的根。 :\n"))


if b**2-4*a*c > 0 :
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    print("有兩個不相等的實根")
    print(x1,x2)
elif b**2-4*a*c == 0 :
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    print("有兩個相等的實根")
    print(x1, x2)
else:
    print("沒有實根")


