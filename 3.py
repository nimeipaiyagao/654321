class Student():
    name = "xxx"
    age = 18
yueyue = Student()
print(yueyue.name)


class A():
    name = "xx"
    age = 18
    def say(self):
        self.name = "xxxx"
        self.age = "11"
print(A.name)
print(A.age)

a = A()
print(a.name)
print(a.age)
a.name = "qqq"
a.age = 12
print(a.name)
print(a.age)

class Teacher():
    name = "yuwen"
    age = 45
    def say(self):
        self.name = "shuxue"
        self.age = 50
        print('My name is {0}'.format(self.name))
        print('I am {0}'.format(__class__.age))
    def sayAgain(self):
        self.name = "yingyu"
        self.age = 55
        print('My name is {0}'.format(__class__.name))
        print('I am {0}'.format(self.age))
t = Teacher()
t.say()
t.sayAgain()







