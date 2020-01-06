# N이 주어졌을 때, 높이 2N-1 너비최대 2N-1 별 찍기

N = int(input())

# for i in range(1,2*N): # 1 ~ 2*N-1랑 0 ~ 2*N-1이랑 큰 차이가 있다
#     if(i < N):
#         for j in range(i, N):
#             print(' ', end='')
#         for k in range(0, 2*i-1):
#             print('*', end='')
#     else: # i >= N
#         for j in range(2*N-i,N):
#             print(' ', end='')
#         for k in range(0,4*N-2*i-1):
#             print('*', end='')
#     print()

for i in range(1,N+1):
    print(' '*(N-i),end='')
    print('*'*(2*i-1))
for i in range(N,0, -1):
    print(' '*(N-i), end='')
    print('*'*(2*i-1))