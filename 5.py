x = 0
while x < 1000:
    if (x % 2 == 1)  \
    and (x % 3 == 2) \
    and (x % 5 == 4) \
    and (x % 6 == 5) \
    and (x % 7 == 0) :
        print(x)
        x = x + 1
    else:
        x = x + 1

for i in range(0,101):
    if i % 2 == 0:
        print("{0}是偶数".format(i))

l = range(101)
if 100 not in l:
    print(True)
else:
    print(False)

i = 0
string = "ILOVETULING"
leng = len(string)
while i < leng:
    print(i)
    i += 1



password = "123456"
times = 3
while times:
    input_password = input("请输入用户密码：")
    if "*" in input_password:
        print("密码中不能包含*号。")
    elif input_password == password:
        print("密码正确。")
        break
    else:
        print("密码错误")
        times = times - 1