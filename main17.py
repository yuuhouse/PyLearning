# 函式(函數) function #傳送參數

def print_info():
    print("小白今年245歲")
    print("小白身高200公分")


def print_name(namegg):
    print(f"{namegg}今年245歲")
    print(f"{namegg}身高200公分")


print_info()  # 呼叫函數
print_name("小黑")


def print_bmi(name, age, height):
    print(f"{name} 今年{age}歲")
    print(f"{name} 身高{height}公分")


print_bmi("小藍", 24, 160)
print_bmi(height=160, name="小藍", age=24)  # 可以用名稱指定的方式防出錯


def add(num1, num2):
    print(num1 + num2)
    return 10  # 回傳值 #不會像print一樣顯示但是有回傳


# add(2, 3)
value = add(2, 3)
print(add(2, 3))  # 得到10
