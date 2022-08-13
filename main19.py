# 比大小 find max

def find_max(num1, num2, num3):
    if type(num1)!= int or type(num2) !=int or type(num3) != int:
        return "請輸入整數"  # return之後下面的程式都不會執行
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3


print(find_max("10", 60, 30))
