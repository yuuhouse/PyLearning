# while #猜數字遊戲

i = 1
a = 0
while i <= 5:
    print(i)
    i += 1  # 1 2 3 4 5

secret_num = 77
guess = None

while secret_num != guess:
    guess = int(input("input num:"))
    if guess < secret_num:
        print("bigger")
    elif guess > secret_num:
        print("smaller")
    else:
        print("right number")
