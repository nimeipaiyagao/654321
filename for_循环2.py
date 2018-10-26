for i in range(1,6):
    for m in range(1,6-i):
        print(end=" ")
    for j in range(6-i,6):
        if i == 1 or i == 3 or j == 6-i or j == 5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


for i in range(1,5):
    for k in range(6-i):
        print(end=" ")
    for j in range(6-i,6):
        print("*",end=" ")
    print()
for i in range(1,6):
    for k in range(i):
        print(end=" ")
    for j in range(6-i):
        print("*",end=" ")
    print()

height= float(input("请输入您的身高(M)："))
weight= float(input("请输入您的体重(Kg)："))
bmi = weight/(height*height) #bmi指身体质量指数
print("您的BMI指数为{},".format(bmi))
if bmi <18.5:
    print("体重过轻")
if bmi >=18.5 and bmi<24.9:
    print("正常范围,注意保持(└(^o^)┘)")
if bmi >=24.9 and bmi<29.9:
    print("体重过重")
if bmi >=29.9:
    print("肥胖")