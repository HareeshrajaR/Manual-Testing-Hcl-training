arr=eval(input())
n=len(arr)
longest=0
set_fun=set()
for i in range(n):
    set_fun.add(arr[i])
for i in set_fun:
    count=0
    if((i-1) not in set_fun):
        j=i
        while j in set_fun:
            j+=1
            count+=1
        longest=max(count,longest)
print(longest)
        
    
