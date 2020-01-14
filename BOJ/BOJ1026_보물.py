N = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A = sorted(A, reverse= True)
B = sorted(B)

S = 0
for i in range(0,N):
    S += A[i]*B[i]

print(S)


'''
6번 줄 부터
S = 0
while A:
    S += A.pop(A.index(min(A))) * B.pop(B.index(min(B)))
print(S)
pop은 index를 인자로 받음. index는 값의 위치를 반환. min은 리스트의 최소값을 돌려줌.
> 리스트에서 최소값찾고 그의 위치를 알아내어 리스트에서 꺼냄. 그렇게 리스트가 빌때까지 반복
'''