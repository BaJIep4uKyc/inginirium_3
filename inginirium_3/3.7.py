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

#Создаём вспомогательную переменную
b = 0

#Создаём цикл
while b != len(visitors):
    print(f'Привет, {visitors[b]}, приглашаю тебя на обед!')
    b += 1

print('Обеденный стол вовремя не привезут! Приглашаются только два человека! :(')

#Поочерёдно удаляем гостей из списка
f = 0
while f != 4:
    print(f'Извини,{visitors[0]}, но мест больше нет. :(')
    visitors.pop(0)
    f += 1
print(f'Привет, {visitors[0]}, для тебя всё в силе!')
print(f'Привет, {visitors[1]}, для тебя всё в силе!')
visitors.clear()
print(visitors)