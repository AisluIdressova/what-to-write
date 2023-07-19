first=int(input("Введите первое число: "))
second=int(input("Введите второе число: "))
action=input("Введите действие: ")

if action=="+":
 print(first+second)
elif action=="-":
 print(first-second)
elif action=="*":
 print(first*second)
elif action=="/":
 print(first/second)
else:
 print("Вы ввели неправильное действие! ")