num1, num2 = input().split()

#파이썬의 배열에서 ::은 A:B:C 일 경우, A부터 B까지 C간격만큼의 배열을 나타내라다.
# C가 양수면 끝까지, 음수면 처음까지...

print(max(num1[::-1],num2[::-1]))