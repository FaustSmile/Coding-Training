driving = input("請問您有開過車嗎?")
if driving != "有" and driving != "沒有":
    print("只能輸入 有/沒有")
    raise SystemExit #程式 在這裡終止

age = input("請問您的年齡?")
age = int(age)
if driving == "有" :
    if age >= 18:
        print("請注意安全、小心開車!")
    else:
        print("不可以開車喔!你還沒有駕照!")
elif driving == "沒有":
    if age >= 18:
        print("趕快去考駕照!就可以開車囉!")
    else:
        print("在等等，成年考完駕照就可以開車了!")
else:
    print("請輸入: 有/沒有")