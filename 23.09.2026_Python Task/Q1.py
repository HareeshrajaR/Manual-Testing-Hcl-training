str="0100!0011.1010,1001/1010"
str=str.replace("!",",").replace(".",",").replace("/",",")
str=str.split(",")
print(str)
res=[]
for i in range(len(str)):
    value=str[i]
    value1=int(value,2)
    if(value1%5==0):
        res.append(value)
print(",".join(res))
