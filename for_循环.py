for tow in range(1,10):
    for col in range(1,1+tow):
        print(tow*col,end=" ")
    print()


for i in range(0,4):
    print("* * * * *")


for i in range(0,4):
    if i == 0 or i == 3:
        print("* " * 5)
    if i == 1 or i== 2:
        for j in range(0,5):
            if j == 0 or j == 4:
                print("* ",end="")
            else:
                print("  ",end="")
        print()


for i in range(5):
    for j in range(i+1):
        print("* ",end="")
    print()


for i   in range(5):
    for j in range(i+1):
        if i == 4:
            print("* ",end="")
            continue
        if j == 0 or j == i:
            print("* ",end="")
        else:
            print("  ",end="")
    print()


for i in range(5):
    for j in range(5-i):
        print("* ",end="")
    print()


for i in range(5):
    for j in range(5):
        if i == 0:
            print("* ",end="")
            continue
        if j == 0 or j == 5-i-1:
            print("* ",end="")
        else:
            print("  ",end="")
    print()

for i in range(5):
    for j in range(5-i):
        print("* ",end="")
    print()


#i-for 控制行
#j-for 控制列

for i in range(0,5):
    for j in range(5-i):
        print(" ",end="")
    for m in range(i+1):
        print("* ",end="")
    print()


for i in range(5):
    for j in range(5):
        if i == 0:
            print("* ",end="")
            continue
        if j == 0 or j == 5-i-1:
            print("* ",end="")
        else:
            print("  ",end="")
    print()



def stu( **kwargs):
    print("hello,大家好，我先自我介绍一下:")
    print(type(kwargs))

    for k,v in kwargs.items():
        print(k, "---", v)
stu(name="yaoyuan", age=18, addr="辽宁省", work="程序员")
print("*" * 50)
stu(name="XXX")

