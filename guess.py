import random
r = random.randint(1,100)
count = 0
while True:
    count += 1 # count = count + 1一樣意思
    num = input("請猜數字: ")
    num = int(num)
    if num == r:
        print("恭喜您!猜中了")
        print("恭喜您!!第", count, "次猜中了!!")
        break
    elif num > r:
        print("猜小一點")
    elif num < r:
        print("猜大一點")
    print("猜數字第", count, "次")