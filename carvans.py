def max_speed(arr, n):
   count = 1
   for i in range(n-1):
      if arr[i]<arr[i+1]:
         arr[i+1] = arr[i]
      else:
         count+=1
   return count

for _ in range(int(input())):
   n = int(input())
   speed = list(map(int, input().split()))

   print(max_speed(speed, n))
