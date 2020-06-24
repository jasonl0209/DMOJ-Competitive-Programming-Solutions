from sys import *
import math
n = int(stdin.readline())
lst = []
for j in range(n):
    att, angle = map(str, stdin.readline().split())
    lst.append(float(angle))
lst.sort()
diff_lst = []
for k in range(n-1):
    val = lst[k+1] - lst[k] 
    diff_lst.append(val)
add_val = (360 - max(lst)) + min(lst)
diff_lst.append(add_val)
max_val = max(diff_lst)
out = 360 - max_val 
out = (out/360) * 4320 
print(math.ceil(out))