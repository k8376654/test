# 4.	迴圏的練習-amstrong
# Amstrong數是指一個三位數的整數，其各位數之立方和等於該數本身。
# 找出所有的Amstrong數。
# 說明：153=13+53+33，故153為Amstrong數。

for i in range (100 , 999 , 1) :
    if ((i//100)**3 + ((i%100)//10)**3 +(i%10)**3) == i :
        print(i)

