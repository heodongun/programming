#print("Hello")

#print("Hello world")

# print("Hello")

# print("world")

# print("'Hello'")

# a="C:\Download\\'hello'.py"

# print('"'+a+'"')

#print('print("Hello\\nWorld")')

# a=input()

# for i in range(3):

#     print(a)

# a=input().split()

# print(a[1])

# print(a[0])

# a=input().split()
# print(a[1])
# print(a[0])

# a=input()
# for i in range(3):
#     print(a)

# a=input()
# print(a)

# a=input()
# for i in a:
#     print(i)

# a=input().split()
# print(a[0]+a[1])

# a=input()
# b=input()
# b=float(a)+float(b)
# print(b)

# a=int(input(),16)
# print('%o'%a)

# n = ord(input())
# print(n)

# c = int(input())
# print(chr(c))

# n=int(input())
# print(-n)

# n=ord(input())
# print(chr(n+1))

# one=int(input().split())
# print(one[0]-one[1])

# a = list(map(int, input().split()))
#
# print(a[0]-a[1])

# a=input().split()
# print(int(a[1])*a[0])

# a=int(input())
# b=input()
# print(a*b)

# a=input().split()
# print(int(a[0])**int(a[1]))

# a=input().split()
# print(float(a[0])**float(a[1]))

# a=input().split()
# print(int(int(a[0])/int(a[1])))

# a=input().split()
# print(int(int(a[0])%int(a[1])))

# a=input()
# a=float(a)
# print( format(a, ".2f") )

# a=input().split()
# print(int(a[0])+int(a[1]))
# print(int(a[0])-int(a[1]))
# print(int(a[0])*int(a[1]))
# print(int(int(a[0])/int(a[1])))
# print(int(a[0])%int(a[1]))
# print(format(int(a[0])/int(a[1]),".2f"))

# a=input().split()
# sum=0
# for i in a:
#     sum+=int(i)
# avg=format(sum/len(a),".2f")
# print(str(sum)+' '+str(avg))

# a=input().split()
# if int(a[0])!=int(a[1]):
#     print("True")
# else:
#     print("False")

# a=int(input())
# if a!=0:
#     print("False")
# else:
#     print("True")

# a=input().split()
# if int(a[0])!=0 and int(a[1])!=0:
#     print("True")
# else:
#     print("False")
#
# a=input().split()
# if int(a[0])|int(a[1]):
#     print("True")
# else:
#     print("False")

# # 두 개의 정수를 입력받기
# a, b = input().split()
#
# # 정수를 bool 타입으로 변환
# c = bool(int(a))
# d = bool(int(b))
#
# # XOR 연산을 통해 서로 다른 경우에만 True 출력
# print((c and not d) or (not c and d))

# a=int(input())
# print(~a)

# a=input().split()
# print(int(a[0])&int(a[1]))

# a=input().split()
# print(int(a[0])|int(a[1]))

# a=input().split()
# print(int(a[0])^int(a[1]))

# a=input().split()
# if int(a[0])>int(a[1]):
#     print(a[0])
# else:
#     print(a[1])

# a=int(input())
# if a<0:
#     if a%2==0:
#         print('A')
#     else:
#         print('B')
# else:
#     if a%2==0:
#         print('C')
#     else:
#         print('D')

# score = int(input())
# grade = 'winter' if  score==12 or score==1 or score==2 else (
#         'spring' if  score==3 or score==4 or score==5 else (
#         'summer' if  score==6 or score==7 or score==8 else (
#         'fall' if score==9 or score==10 or score==11 else())))
#
# print(grade)

# a=int(input())
# while(a!=0):
#         print(a)
#         a=int(input())

# a=int(input())
# for i in range(a):
#         print(a)
#         a-=1

# a=int(input())
# for i in range(a):
#         print(a-1)
#         a-=1

# a=ord('a')
# b=ord(input())
# for i in range(a,b+1):
#         print(chr(i),end=' ')

a=int(input())
sum=0
for i in range(1,a+1):
        if i%2==0:
                sum=sum+i
print(sum)
