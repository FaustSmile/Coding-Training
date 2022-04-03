# 密碼重試程式
# password = "a123456"
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果正確 就印出 "登入成功"
# 如果不正確 就印出"密碼錯誤! 還有_次機會!"
password = "a12345"
chance = 2
while chance > -1:
    pwd = input ("請輸入密碼:")
    if pwd == password :
        print("登入成功!!")
        break
    elif chance == 0 :
        print("超過輸入次數限制!!")
    else:
        print("密碼錯誤! 還有", chance, "次機會")
    chance = chance - 1