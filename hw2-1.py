# 1.	迴圏的練習-expression
# 利用for迴圏計算12-22+32-42+…+492-502的值。

totaln =0
totalm =0


for n in range (1,51,2):
    totaln+=n**2
for m in range (2,51,2):
    totalm+=m**2

print(totaln-totalm)


