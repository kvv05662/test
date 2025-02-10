import random

def generateList (length):
     x = []
     for i in range(length):
          y = random.randrange(-100, 100)
          x.append (y)
     return (x)



def otherCode():
     a = generateList(10)
     a = []
     print("Задане натуральне число n — ")
     n = int(input("n = "))
     if n <= 0:
          print("Завдання не виконується")
     for i in range(1, 1+n):
          if (n % i == 0): 
               a.append(i) #тут заносимо число, на яке ділиться n (дільник) в список

     print(a) # тут виводимо список дільників в консоль
