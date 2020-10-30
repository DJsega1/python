num = int(input())
count = 0
while num != 0:
    if num > 99:
        num -= 3
    elif num > 9:
        num -= 2
    else:
        num -= 1
    count += 1
print(count)
