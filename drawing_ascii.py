n = int(input())
m = int(input())
symb = input()
for i in range(1, n + 1):
    if i == 1 or i == n:
        print(symb * m)
    else:
        print(symb + ' ' * (m - 2) + symb)
        
