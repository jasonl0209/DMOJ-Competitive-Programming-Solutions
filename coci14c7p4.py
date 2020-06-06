from sys import *
pic, colour = map(int, stdin.readline().split())
lst = [[1, 1572858], [0, 96], [1, 18], [1, 24570], [0, 12], [0, 6], [0, 96], [1, 1073741820]]
mul = colour * (colour-1)
out = lst[pic-1][0] + (colour-2) * lst[pic-1][1] // 6
out *= mul
print(out)