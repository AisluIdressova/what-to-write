operand=int(input("Сколько операндов?  "))
for number in range(1,operand+1)
 



first=int(input("Введите первое число: "))
second=int(input("Введите третье число: "))

action=input("Введите действие: ")

if action=="+":
 print(first+second)
elif action=="*":
 print(first*second)

else:
 print("Вы ввели неправильное действие! ")