# elif # nested if(巢狀) #邏輯運算

score = int(input("score:"))
if score >= 90:
    print("甲")
    if score == 100:
        print("最頂的")
    else:
        print("你怎麼沒有考100")
elif score >= 80:
    print("乙")
elif score >= 70:
    print("丙")
elif score >= 60:
    print("丁")
else:
    print("不及格")
