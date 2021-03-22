l = []
for _ in range(int(input())):
   l.append(int(input()))
l.sort()

count = len(l)
for i in range(len(l)):
   l[i] = l[i]*count
   
   count -= 1
print(max(l))

