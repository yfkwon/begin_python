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
s = '가나다'
ss = "가나다"

sss = """아리랑
 아리아
 아리아
 아라리오
 """

print(s, ss, sss)

s = '아리아\n아리랑\n아라이요'
print(s)

# 문자열 포맷팅

p = "이름: %s 나이: %d" % ("김유신", 65)
print(p)

p = "X = %0.3f, Y = %10.2f" % (3.141592, 3.141592)
print(p)


path = r'c:\Temp\test.csv'
print(path)

s = ','.join(['가나', '다라', '마바'])
print(s)

s = ''.join(['가나', '다라', '마바'])
print(s)

items = '가나,다라,마바'.split(',')
print(items)

departure, _, arrival = "Seattle-Seoul".partition('-')
print(departure)

s = "Name: {0}, Age: {1}".format("강정수", 30)
print(s)

s = "Name: {name}, Age: {age}".format(name="강정수", age=30)
print(s)

area = (10, 20)
s = "width: {x[0]}, height: {x[1]}".format(x = area)
print(s)

text = b"hello"
for c in text:
    print(c)

s1 = "hello"
b1 = s1.encode('utf-8')
print(b1)
for c in b1:
    print(c)

s2 = b1.decode('utf-8')
print(s2)

# 조건문
x = 10
if x < 10:
    print(x)
    print("한자리수")

if x < 100: print(x)

if x < 10:
    print("한자리수")
elif x < 100:
    print("두자리수")
else:
    print("세자리수")

# 반복문
i = 1
while i <= 10:
    print(i)
    i += 1

sums = 0
for i in range(11):
    sums += i
print(sums)
