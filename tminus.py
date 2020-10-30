num = int(input())
count = 0
for i in range(num):
    count += 1
    for i in range(count):
        print('Осталось секунд:', (count - 1) - i)
    print('Пуск', count)