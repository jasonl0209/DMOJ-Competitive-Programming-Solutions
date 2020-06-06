n, k = map(int, input().split(" "))
lst = list(map(int, input().split()))
counter = 0
i = 0
while counter < k and i < n-1:
    element = max(lst[i+1:n])
    if lst[i] < element:
        index = lst.index(element)
        h = lst[i]
        lst[i] = element 
        lst[index] = h
        counter+=1
    i+=1
print(*lst)