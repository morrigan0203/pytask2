import fractions

num_den1 = str(input("Введите дробное число, в формате x/y: "))
num_den2 = str(input("Введите дробное число, в формате x/y: "))
num1 = num_den1.split("/")
num2 = num_den2.split("/")
f1 = fractions.Fraction(int(num1[0]), int(num1[1]))
f2 = fractions.Fraction(int(num2[0]), int(num2[1]))
print(f"Умножение дробей {num_den1} на {num_den2} , будет равно : {int(num1[0])*int(num2[0])}/{int(num1[1])*int(num2[1])}")
print(f"Проверка умножение дробей {num_den1} на {num_den2}, будет равно : {f1*f2}")
if int(num1[1]) == int(num2[1]):
    print(f"Сумма дробей {num_den1} и {num_den2}, будет : {int(num1[0])+int(num2[0])}/{int(num1[1])}")
else:
    print(f"Сумма дробей {num_den1} и {num_den2}, будет : {int(num1[0])*int(num2[1])+int(num2[0])*int(num1[1])}/{int(num1[1])*int(num2[1])}")
print(f"Проверка суммы дробей {num_den1} и {num_den2}, будет равно : {f1+f2}")


