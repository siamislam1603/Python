n,m=map(int,input().split())
arr=list(map(int,input().split()))
a=set((map(int, input().split())))
b=set((map(int, input().split())))
output=0
for val in arr:
    if(val in a):
        output+=1
    if(val in b):
        output-=1
print(output)

