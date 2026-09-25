arr=eval(input())
target=int(input())
n=len(arr)
count=0
for i in range(n):
    Currsum=0
    for j in range(i,n):
        Currsum+=arr[j]
        if(Currsum==target):
            count+=1
print(count)
