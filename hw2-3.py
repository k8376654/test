# 3.	迴圏的練習-perfectNumber
# 一個數字若等於其所有因數的總和，則此數為perfect number。
# 找出100以內所有的完美數。
# 說明：6的因數為1, 2, 3，6=1+2+3，故6為完美數。




for i in range (1,101) :
    total = 0
    for j in range (1, i):
        if i%j==0 :
            total+=j
    if i==total:
        print(i)


