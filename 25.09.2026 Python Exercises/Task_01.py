arr = list(map(int, input().split()))
Set_fun = set()
left = 0
maxlen = 0
for right in range(len(arr)):
    while arr[right] in Set_fun:
        Set_fun.remove(arr[left])
        left += 1
    Set_fun.add(arr[right])
    current_len = right - left + 1
    if current_len > maxlen:
        maxlen = current_len
print(maxlen)
