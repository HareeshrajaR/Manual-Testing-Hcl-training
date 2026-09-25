arr=eval(input())
n=len(arr)
maxprod=arr[0]
for i in range(n):
    curr_prod=1
    for j in range(i,n):
        curr_prod*=arr[j]
        if(curr_prod>maxprod):
            maxprod=curr_prod
print(maxprod)
