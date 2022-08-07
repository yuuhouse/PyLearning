# 拉麵點餐系統
print("welcome ramen order\n "
      "1.salt ramen 220\n "
      "2.soy sauce ramen 240\n"
      "3.tonkotsu ramen 280")
flavor = int(input("1 or 2 or 3: "))  # .upper() 變成大寫
big = input("big y or n: ")
egg = input("egg y or n: ")
chashu = input("chashu y or n: ")
price = 0
if flavor == 1:
    price += 220
elif flavor == 2:
    price += 240
else:
    price += 280

if big == "y":
    if flavor != 3:  # 不等於豚骨
        price += 30
    else:
        price += 50
else:
    price += 0

if egg == "y":
    price += 30
else:
    price += 0

if chashu == "y":
    price += 60
else:
    price += 0

if big == "y" and egg == "y" and chashu == "y":
    price -= 20
    print(f"我全都要折20, total is {price}, thanks for coming.")
else:
    print(f"total is {price}, thanks for coming.")
# if flavor == 1:
#     p_flavor = 220
# elif flavor == 2:
#     p_flavor = 240
# else:
#     p_flavor = 280
#
# if big == "Y":
#     if flavor != 3:  # 不等於豚骨
#         p_big = 30
#     else:
#         p_big = 50
# else:
#     p_big = 0
#
# if egg == "Y":
#     p_egg = 30
# else:
#     p_egg = 0
#
# if chashu == "Y":
#     p_chashu = 60
# else:
#     p_chashu = 0

# print(p_flavor)
# print(p_big)
# print(p_egg)
# print(p_chashu)
# print("total is " + str(p_flavor + p_big + p_egg + p_chashu) + ", thanks for coming.")
