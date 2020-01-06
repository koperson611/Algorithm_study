# 지능형 기차
# 기차에 사람이 가장 많을 때 사람 수를 계산
# 한 줄에 하나 씩 '내린사람 탄사람'이 주어짐

train = []
remainer = 0
while True :
    takeOffer, rider = map(int, input().split())
    if(rider == 0): break
    remainer += (rider - takeOffer)
    train.append(remainer)
    # list 쓸 필요없이 각 remainer 계산마다 최대값을 구하면 됨
    # max(train, remainer)
print(max(train))