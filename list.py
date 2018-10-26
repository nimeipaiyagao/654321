def hano(n,a,b,c):
    if n == 1:
        print(a,'-->',c)
        return None
    if n == 2:
        print(a,'-->',b)
        print(a,'-->',c)
        print(b,'-->',c)
        return None

    hano(n-1,a,c,b)
    print(a,'-->',c)
    hano(n-1,b,a,c)
a="A"
b="B"
c='C'
n =10
hano(n,a,b,c)
'''



'''
s = "我今天买了一个鸡蛋，可便宜了"
替换 = s.maketrans("鸡蛋","白菜")
print(替换)
print(s.translate(替换))

help(list)



list = [5,8,227,92,4,7,9,1,8,6,312,4,89,2]
list.sort()
print(list)
list.sort(reverse=True)
print(list)

tuple = (1,2,3,4,5,6)
print(tuple.index(2))

dict={"a":1,"b":2,"c":3}
for k,v in dict.items():
    print(k,"--",v)


dict = {"d":4,"a":1,"b":2,"c":3}
dict.update({"d":2,"c":74,"e":16})
print(dict)
dict["d"]=6
print(dict)

s = "abcdefghijklmnopqrstuvwxyz"
s1 = s.find("j",10)
print(s1)


for i in range(1,10):
    for j in range(1,i+1):
        print(str(j) +"x"+ str(i)+ "=" + str(j*i)+"\t",end="")
    print()


s= {1,2,3,4,5,6,7}
s1 = frozenset(s)
print(s1)

t = tuple()
print(t)

print("在古希腊神话中，玫瑰集爱情与美丽于一身，所以人们常用玫瑰来表达爱情。")
print("但是不同朵数的玫瑰花代表的含义是不同的。")
number = input("输入您想送几朵玫瑰花，我会告诉您含义：")
if number == 1:
    print("1朵，你是我惟一")
elif number == 3:
    print("3朵， I love you!")
elif number == 10:
    print("10朵，十全十美")
elif number == 99:
    print("99朵，天长地久")
elif number == 108:
    print("108朵，求婚")
else:
    print("不知道了")


