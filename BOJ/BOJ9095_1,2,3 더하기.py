def solve(n):
    if(n<4) :
        return ans[n]
    else:
        ans.insert(n,solve(n-1)+solve(n-2)+solve(n-3))
        return ans[n]

T = int(input())

ans = [0,1,2,4]

for i in range(0,T):
    n = int(input())
    print(solve(n))