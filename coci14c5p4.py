n = input()
int_n = int(n)
length = len(n)
lst_n = []
for g in range(length):
    ind = int(n[g])
    lst_n.append(ind)
    
bln_done = False
counter = 1
digit = int(n[0])
if digit % 2 == 0:
    bln_even = True
else:
    bln_even = False
  
while bln_done == False:
    digit = lst_n[counter]
    if (bln_even):
        if (counter % 2 == 1 and digit % 2 == 0) or (counter % 2 == 0 and digit % 2 == 1):
            bln_done = True 
    else:
        if (counter % 2 == 1 and digit % 2 == 1) or (counter % 2 == 0 and digit % 2 == 0):
            bln_done = True 
    counter += 1
    
last_digit = lst_n[counter-1]
if last_digit == 0:
    lst_n[counter-1] = 1 
    count = 0
    for j in range(counter, length):
        if count % 2 == 0:
            lst_n[j] = 0
        else:
            lst_n[j] = 1
        count += 1
    out = ""
    for k in range(length):
        out += str(lst_n[k])
    print(out)
    
elif last_digit == 9:
    lst_n[counter-1] = 8
    count = 0
    for j in range(counter, length):
        if count % 2 == 0:
            lst_n[j] = 9
        else:
            lst_n[j] = 8
        count += 1
    out = ""
    for k in range(length):
        out += str(lst_n[k])
    print(out)
    
else:
    lst_upper = lst_n
    num = lst_upper[counter-1]
    lst_upper[counter-1] = num + 1
    count = 0
    if lst_upper[counter-1] % 2 == 0:
        for j in range(counter, length):
            if count % 2 == 0:
                lst_upper[j] = 1
            else:
                lst_upper[j] = 0
            count += 1
    else:
        for j in range(counter, length):
            if count % 2 == 0:
                lst_upper[j] = 0
            else:
                lst_upper[j] = 1
            count += 1
        
    upper = ""    
    for k in range(length):
        upper += str(lst_upper[k])
    
    lst_lower = lst_n
    num = lst_lower[counter-1]
    lst_lower[counter-1] = num - 2
    count = 0
    if lst_lower[counter-1] % 2 == 0:
        for j in range(counter, length):
            if count % 2 == 0:
                lst_lower[j] = 9
            else:
                lst_lower[j] = 8
            count += 1
    else:
        for j in range(counter, length):
            if count % 2 == 0:
                lst_lower[j] = 8
            else:
                lst_lower[j] = 9
            count += 1
            
    lower = ""
    for w in range(length):
        lower += str(lst_lower[w])
        
    upper = int(upper)
    lower = int(lower)
    
    if upper - int_n > int_n - lower:
        print(lower)
    elif upper - int_n < int_n - lower:
        print(upper)
    else:
        print(lower, upper)