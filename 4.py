import random
secert = random.randint(1,100)
times = 3
while times:
    num = input("请输入数字：")
    if num.isdigit():
        tmp =int(num)
        if tmp == secert:
            print("你猜对了！")
            break
        elif tmp < secert:
            print("你猜小了！")
            times -= 1
        else:
            print("你猜大了！")
            times -= 1
print("你的机会用完了")

