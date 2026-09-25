arr=eval(input())
n=len(arr)
maxsum=arr[0]
for i in range(n):
    curr=0
    for j in range(i,n):
        curr+=arr[j]
        if(curr>maxsum):
            maxsum=curr
print(maxsum)
