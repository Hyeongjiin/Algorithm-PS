n=int(input())

for j in range (n - 1,0,-1):
    b='*'*(n-j)+' '*((2*j)-1)
    d=('*'*(n-j)).rjust(j-n)
    print(b,d)

print('*'*(2*n))

for i in range (1,n):
    a='*'*(n-i)+' '*((2*i)-1)
    c=('*'*(n-i)).rjust(i-n)
    print(a,c)