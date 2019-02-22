# 2.	迴圏的練習-factor
# 輸入一正整數，求其所有的因數。
# 說明：36的因數為1, 2, 3, 4, 6, 9, 12, 18, 36。

num= eval(input("輸入一個數字N求其因數 :\n"))

for n in range (1 , num+1 , 1) :
    if num%n ==0 :
        print(n,end=' ')
    else :
        pass
