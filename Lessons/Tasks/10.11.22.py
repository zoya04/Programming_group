import random 
###1
# Найти сумму всех чисел от 1 до 100 и вывести полученное значение на экран
sum = 0
for doc_num in range(0,101):
     sum = sum + doc_num
     print(sum)
     



   
###2 Вывести на экран все чётные значения в диапазоне от 1 до 497
for sum in range(1,498):
    if sum% 2 == 0:
     print(sum)





###3  
# Дан список чисел:
list1 = [1,2,5,12,14,48,256,17]
for elem1 in list1:
    print(elem1)
    
list1.append('list over')
print(list1)



# А) Необходимо вывести на экран каждый элемент цикла, используя for
# B) Необходимо по завершению цикла добавить в конец списка строку "List over"

### 4 
# Необходимо создать пустой список. В этот список, используя функцию input(), 
# пользователю необходимо будет ввести имя человека. Необходимо добавлять
# имена, записанные пользователем, в наш список, и выводить весь список на экран после
# каждого добавленного имени. Как только количество имен в списке
# станет равным четырем, вывести на экран "Список имен заполнен"
# list1 = []
# list1 = (input("Zoya"))
# print =(list1)
# list1 = (input("Alex"))
# print = (list1)
# list1 = (input("Teo"))
# print = (list1)
# list1 = (input("Shelbe"))
# print = (list1)
# list1 = (input("список имен завершен"))
# print = (list1)

# Names = []

# for num1 in r





### 5
# Дано уравнение: 


# result = (int1*117 + 87)//13 * (21**int1)

# Где int1 - переменная, объявляемая при создании цикла
# Необходимо решить это уравнение для каждого числа в диапазоне от 0 до 5
for int1 in range(0,6):
    result = (int1*117 + 87)//13 * (21**int1)
    print(result) 




###Раздел 2 

###1
# В программе генерируется случайное целое число от 0 до 100. 
# Пользователь должен его отгадать не более чем за 10 попыток. 
# После каждой неудачной попытки должно сообщаться больше или меньше 
# введенное пользователем число, чем то, что загадано. 
# Если за 10 попыток число не отгадано, то вывести загаданное число.

# для выполнение этой задачи вам потребуется импортировать модуль random:

# import random наверху первой строчкой

random_int = random.randint(1,100)
print(random_int)

try_num = 10 



# while try_num > 0:
#     user_num = int(input("Введите число:"))
#     if user_num == random_int:
#         pass
#     elif user_num < random_int:
#         pass
#     elif user_num > random_int:
#         pass
#     try_num = try_num - 1
#     print(try_num)
# else:
#     print('игра закончена!')

# while try_num > 0:
#     user_num = int(input("Введите число:"))
#     if user_num == random_int:
#         print("вы угадали! загаданное число было", random_int, f"Осталось{try_num} попыток")
#         break
#     elif user_num < random_int:
#         print("Введенное число меньше загаданного")
#     elif user_num > random_int:
#         print("Введенное число больше загаданного")
#     try_num = try_num - 1
#     print(try_num)
# else:
#     print("У вас не осталось попыток!")
# print('игра закончена!')

while try_num > 0:
     user_num = int(input("Введите число:"))
     if user_num <1 or user_num > 100: 
        print("Вы ввели неверное число! Введите число от 1 до 100")
        continue 
     if user_num == random_int:
         print("вы угадали! загаданное число! В", random_int, f"Осталось{try_num} попыток")
         break
     elif user_num < random_int:
         print("Введенное число меньше загаданного")
     elif user_num > random_int:
         print("Введенное число больше загаданного")
     try_num = try_num - 1
     print(try_num)
     
else:
     print("У вас не осталось попыток!")
print('игра закончена!')

