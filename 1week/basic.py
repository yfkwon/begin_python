import math

# 시작하기
str = "Hello World"
print(str)

# 간단한 프로그램 작성
a = 1
b = 2
c = a+b

print(c)

# 코딩의 기초
n = math.sqrt(9.0)

print(n)

# 기본 데이타 타입
i = int(3.5)
exp = 2e3
f1 = float("1.6")
f2 = float("inf")
f3 = float("-inf")
b1 = bool(0)
b2 = bool(-1)
b3 = bool("False")
n1 = None
n2 = n1 is None

print(i, exp, f1, f2, f3, b1, b2, b3, n1, n2)

# 산술연산자
a1 = 5 % 2
a2 = 5 // 2

print(a1, a2)

# 비교연산자
if a != 1:
    print("1이 아님")
else:
    print("1이 맞음")


# 할당연산자
a = a * 10
a *= 10

print(a)

# 논리연산자
x = True
y = False

if x and y:
    print("Yes")
else:
    print("No")

# Bitwise 연산자

a = 8
b = 11
c = a & b
d = a ^ b

print(c)
print(d)

# 멤버쉽 연산자

a = [1, 2, 3, 4]
b = 3 in a          # True

print(b)

# Identity 연산자

a = "ABC"
b = a

print(a is b)

# 문자열