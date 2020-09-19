import math
import sys

def getNumber (): 
    while type:
        print ('Введите число:', end = '')
        getTempNumber=input ()
        try:
            getTempNumber=float(getTempNumber)
        except ValueError:
            print ('"'+  getTempNumber + '"' + ' - не является числом')
        else:
            break
    return getTempNumber

print("Забелина Варвара ИУ5-51Б")
print("Нахождение корней квадратного уравнения")

if len(sys.argv) == 4:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    try:
        getTempNumberA=float(a)
        getTempNumberB=float(b)
        getTempNumberC=float(c)
    except ValueError:
        print ('Введенное не является числом')
    else:
        a = getNumber()
elif len(sys.argv) == 1:
    try:
        a = float(input("a = "))
    except ValueError:
        print ("Не является числом")
        a = getNumber()
    
    try:
        b = float(input("b = "))
    except ValueError:
        print ('Не является числом')
        b = getNumber()
    
    try:
        c = float(input("c = "))
    except ValueError:
        print ('Не является числом')
        c = getNumber()
else:
    print("Неправильное количество параметров командной строки")
    sys.exit()

print("a = {0}, b = {1}, c = {2}".format(a, b, c))
d = b ** 2 - 4 * a * c

if a == 0 and b == 0 and c == 0:
    print("Корень уравнения: любое число")
elif (a == 0 and b == 0 and c != 0):
    print("Нет решений")
elif d < 0:
    print("Уравнение не имеет действительных корней")
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)

    if x1 < 0 and x2 < 0:
        print("Нет решений")
    elif x1 == x2:
        print("x1 = {0}, x2 = {1}".format(math.sqrt(x1), -math.sqrt(x2)))
    elif x1 < 0:
        print("x1 = {0}, x2 = {1}".format(math.sqrt(x2), -math.sqrt(x2)))
    elif x2 < 0:
        print("x1 = {0}, x2 = {1}".format(math.sqrt(x1), -math.sqrt(x1)))
    else:
        if x1 == 0:
            print("x1 = {0}, x2 = {1}, x3= {2}".format(0, math.sqrt(x2), -math.sqrt(x2)))
        elif x2 == 0:
            print("x1 = {0}, x2 = {1}, x3= {2}".format(0, math.sqrt(x1), -math.sqrt(x1)))
        else:
            print("x1 = {0}, x2 = {1}, x3 = {2}, x4 = {3}".format(math.sqrt(x1), -math.sqrt(x1), math.sqrt(x2), -math.sqrt(x2)))
