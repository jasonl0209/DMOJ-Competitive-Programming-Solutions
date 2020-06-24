from sys import *
num = int(stdin.readline())
for i in range(num):
    n = int(stdin.readline())
    list_original = list(map(int, input().split()))
    sorted_list = sorted(list_original)
    counter = 0
    for k in range(n):
        for j in range(n-k-1):
            if list_original[j] > list_original[j+1]:
                list_original[j], list_original[j+1] = list_original[j+1], list_original[j]
                counter += 1
            if list_original == sorted_list:
                break
    print("Optimal train swapping takes", counter, "swaps.")