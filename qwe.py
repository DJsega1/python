k = int(input())
count = 0
strs = 0
amount = 0
while True:
    count += 1
    for i in range(1, count + 1):
        print(amount + i, sep='', end=' ')
        if amount + i == k:
            exit()        
    print()
    amount += i
