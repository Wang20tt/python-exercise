lst=list(range(3,1000,2))
m=int(1000**0.5)
for index in range(m):
    current =lst[index]
    if current>m:
        break
    lst[index+1:]=list(
        filter(
            lambda x: 0 if not x%current else x,
            lst[index+1:]
        )
    )
print ([2]+lst)