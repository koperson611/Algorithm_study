N = int(input())
ans = []
while N:
    ans.append(N%10)
    N = N//10
ans = sorted(ans, reverse= True)
for i in range(0,len(ans)):
    print(ans[i],end='')

# 다른 사람 답
# print(sorted(list(map(int,input())), reverse=True), sep='')
# print(''.join(reversed(sorted(input()))))