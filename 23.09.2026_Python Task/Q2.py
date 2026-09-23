str="hello world! 123"
alpha=0
digits=0
for i in range (len(str)):
  if(str[i].isalpha()):
    alpha+=1
  
  elif(str[i].isnumeric()):
    digits+=1
  
print("Letters:",alpha)
print("Digits:",digits)
