# 比大小 find max

def find_max(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num1 and num2 > num3:
        print(num2)
    else:
        print(num3)


find_max(10, 60, 30)
