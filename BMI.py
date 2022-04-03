# BMI值計算公式:    BMI = 體重(公斤) / 身高2(公尺2)
height = input("請輸入您的身高(cm): ")
weight = input("請輸入您的體重(kg): ")
height = int(height)
weight = int(weight)
height = height / 100 # 轉換成公尺
bmi = weight / (height ** 2)
if bmi < 15 or bmi > 40 :
    print("輸入錯誤，請重新輸入")
elif bmi < 18.5 :
    print("您的BMI為: ", bmi, "屬於體重過輕!!")
elif bmi >= 18.5 and bmi < 24 :
    print("您的BMI為: ", bmi, "屬於正常範圍!!")
elif bmi >= 24 and bmi < 27 :
    print("您的BMI為: ", bmi, "屬於體重過重!!")
elif bmi >= 27 and bmi < 30 :
    print("您的BMI為: ", bmi, "屬於輕度肥胖!!")
elif bmi >= 30 and bmi < 35 :
    print("您的BMI為: ", bmi, "屬於中度肥胖!!")
elif bmi >= 35 :
    print("您的BMI為: ", bmi, "屬於重度肥胖!!")