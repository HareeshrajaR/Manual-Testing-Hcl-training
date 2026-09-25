arr=eval(input())
arr.sort()
first=arr[0]
res=[]
for i in range(1,len(arr)):
    prev=arr[i]
    if(prev[0]<=first[1]):
        first[1]=max(prev[1],first[1])
    else:
        res.append(first)
        first=prev
res.append(first)
print(res)
