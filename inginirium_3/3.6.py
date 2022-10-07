#Создаём список с именами
visitors = ['Andrey', 'Sanek', 'Harry Potter']

#Поочерёдно выводим имена
print('Список приглашённых на обед:')
print(visitors[0])
print(visitors[1])
print(visitors[2])

#Выводим имя гостя который не придёт
print(f'К сожалению, {visitors[2]} придти не сможет.')

#Заменяем имя приглашенного на другое
visitors.pop(2)
visitors.insert(2, 'Putin')

#Создаём вспомогательную переменную
a = 0
#Создаем цикл выводящий приглашения поочерёдно для каждого приглашенного
while a != 3:
    print(f'Привет, {visitors[a]}, приглашаю тебя на обед!')
    a += 1

print('Я купил новый стол! Пригласим еще троих гостей!')

#Добавляем людей в список
visitors.insert(0, 'Vasya')
visitors.insert(2, 'Leha')
visitors.append('Timofei')

b = 0
#
while b != len(visitors):
    print(f'Привет, {visitors[b]}, приглашаю тебя на обед!')
    b += 1