import math
t=int(input())
for i in range(t):
  n,k=input().split()
  a = math.ceil(int(k)/(int(n)-1))-1
  print(int(k)+a)