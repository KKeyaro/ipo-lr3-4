p = str(12345) #Задаем правильный пароль в виде строки
n = str(input("Введите пароль: ")) #Просим пользователя ввести пароль
if p == n: #Используем оператор ветвления if и задаем условие
    print("Доступ разрешен") #Выведется если условие верно
else:  #Оператор else будет выполнен, если условие будет ложно
    print("Доступ запрещен")  #Выведется если условие ложно