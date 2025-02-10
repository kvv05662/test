class Person:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def age(self, current_year):
        return current_year-self.year


tom = Person("Tom", 1992)
this_year2 = (2024)
print(tom.age(this_year2))

from datetime import datetime
from dateutil.relativedelta import relativedelta

class PersonA:
    name = ""
    birthday = datetime

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = datetime.strptime(birthday, "%d.%m.%Y")

    def getAge(self):
        difference_in_years = relativedelta(datetime.now(), self.birthday).years
        # return datetime.now() - self.birthday
        return difference_in_years
    
    def say_hi(self):
        return 'Hi, my name is ' + self.name + '. I`m ' + str(self.getAge())


person = PersonA('Jon', '29.06.1993')

print(person.say_hi())
print(person.getAge())



#цю функцію потрібно буде написати згідно з інструкціями в завданні. тут вона лише для демонстрації принципу роботи коду.
def collats(num): 
    if(num % 2 == 0):
        return num/2
    else:
        return 3*num + 1
    # return num-1


x = int(input())

curentNum = x # початкове значення аргументу функції вводить користувач
# нижче написано те, про що йдеться в другому абзаці. 
while(curentNum != 1): #виконуємо код, поки curentNum не стане рівним 1. != означає "не дорівнює". 
    a = collats(curentNum)  # перший виклик функції. функція повертає якесь значення.
    print(a) # друкуємо це значення
    curentNum = a # присвоюємо нове значення змінній, яка в наступній ітерації стане аргументом функції, що викликається в рядку 12









def collats(num): 
    if(num % 2 == 0):
        return num/2
    else:
        return 3*num + 1


x = int(input())
curentNum = x
while (curentNum != 1):
    a = collats(curentNum)
    print(a)
    curentNum = a




def funcName(list):
    string = ''

    for i in range(len(list)):

        string = string + list[i]
        
        if(i+2 == len(list)):
            string = string + " and "
        elif(i+1 < len(list)):
            string = string  + ", "

    return string


spam = ["apples", "bananas", "tofu", "cats"]

print(funcName(spam))




# from function import *
import graphics

class Vector:
    def __init__(self, x, y):
        try:
            self.x = float (x)
            self.y = float (y)
        except ValueError:
            self.x = 0.0
            self.y = 0.0


    def norm(self):
        return (self.x**2 + self.y**2) ** 0.5


    def __add__(self, other):
        newx = self.x + other.x
        newy = self.y + other.y
        return Vector (newx, newy)


    def __str__(self):
        return "(%f, %f)" %(self.x, self.y)
u = Vector (3, 4)
v = Vector (3, 6)
print (u + v)

