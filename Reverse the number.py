t = int(input())

for i in range(t):
    n = input()
    rev = n[::-1]
    ans = ""
    for c in rev:
        if c == '0':
            rev = rev[1:]
        else: break
    print(rev)