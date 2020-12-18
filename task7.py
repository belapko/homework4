def fact(n):
    count = 1
    for i in range(1, n + 1):
        count *= i

        yield count

for i in fact(n = int(input())):
    print(i)