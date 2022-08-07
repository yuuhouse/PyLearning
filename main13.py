# if 語句 #True T大寫 F大寫
# > < >= <= == not

is_rainy = True

if is_rainy:
    print("y")
else:
    print("n")

score = 60
if score >= 60:
    print("y")
else:
    print("n")

name = "林鮭魚"
print(name == "林鮭魚")  # 可以偵測Ture False

print(True or True)
print(True or False)
print(False or True)
print(False and False)
if name == "" and "":
    print()
score = 100
if score != 100:
    print("你好爛")
else:
    print("best")

if not score == 100:
    print("你好爛")
else:
    print("best")