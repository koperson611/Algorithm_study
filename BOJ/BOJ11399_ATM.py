N = int(input())

P = list(map(int,input().split()))
P.sort()
sum = 0
t = 0
for i in P:
    t += i
    sum += t
print(sum)