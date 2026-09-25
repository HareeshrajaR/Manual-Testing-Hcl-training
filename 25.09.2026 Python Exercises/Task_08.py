arr=eval(input())
n=len(arr)
dict={}

for i in range(n):
    val=sorted(arr[i])
    str=""
    for j in range(len(val)):
        str+=val[j]
    if str not in dict:
        dict[str]=[]
        dict[str].append(arr[i])
    else:
        dict[str].append(arr[i])


print(list(dict.values()))


    
