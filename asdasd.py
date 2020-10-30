num = int(input())
height = 123123123
last_height = 0
way = 0
for i in range(num):
    x = int(input())
    for j in range(x):
        f = int(input())
        if f < height:
            height = f  # минимальная высота грузовика на ЭТОЙ дороге
        else:
            pass
    if last_height < height:
        last_height = height
        way = i + 1
    height = 123123123
print(way, last_height)
            
        