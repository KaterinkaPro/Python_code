# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

a = str(input("Введите трехзначное число: "))
if len(str(a)) < 3 or len(str(a)) > 3:
  print("Число не трехзначное! Введите число, состоящее из 3 цифр: ")
else: 
  a = int(a)
  b = 0
  b = a % 10
  a = a // 10
  c = a % 10
  a = a // 10
  d = a % 10
  print(b + c + d)
  
