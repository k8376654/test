# 3.	選擇性敘述的練習-electricity
# 輸入何種用電和度數，計算出需繳之電費。
# 電力公司使用累計方式來計算電費，分工業用電及家庭用電。
#                      家庭用電        工業用電
#   240度(含)以下		0.15元			0.45元
#   240~540(含)度   		0.25元			0.45元
#   540度以上          	0.45元			0.45元

kind = eval(input("輸入您是何種用電戶,家庭用電=1,工業用電=2 :\n"))

if kind ==1 :
    house = eval(input("輸入您的家庭用電度數 :\n"))
    if house >540 :
        print('您的家庭用電繳費總共是{}元'.format(house*0.45))
    elif 540 >= house >= 240 :
        print('您的家庭用電繳費總共是{}元'.format(house * 0.25))
    elif 0 <= house < 240 :
        print('您的家庭用電繳費總共是{}元'.format(house * 0.15))
    else :
        print("輸入錯誤")

elif kind ==2 :
    industry = eval(input("輸入您的工業用電度數 :\n"))
    print('您的工業用電繳費總共是{}元'.format(industry*0.45))

else :
    print("你打錯囉")

