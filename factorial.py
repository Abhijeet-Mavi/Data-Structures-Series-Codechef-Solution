def fun(n):
    count = 0
    while n >= 5:
        count += n//5
        n = n//5
    return count

for _ in range(int(input())):
    n = int(input())
    print(fun(n))