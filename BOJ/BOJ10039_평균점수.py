# 5명의 평균 점수, 40점 미만은 40점으로 계산
sum = 0
for i in range(0,5):
    score = int(input())
    sum += score if score >= 40 else +40
print(int(sum/5)) # 답 제출시에는 float이면 틀릴 수 있다