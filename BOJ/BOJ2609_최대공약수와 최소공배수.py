def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a%b)
# gcd는 return a if b%a else gcd(b, a%b)로도 가능
def lcm(a, b):
    return a * b // gcd(a,b)

a, b = map(int,input().split())

print(gcd(a,b))
print(lcm(a,b))