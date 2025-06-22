l = [10, 20, 30, 40, 50]
x = len(l)
mid = x // 2
if x % 2 == 0:
      del l[mid - 1 : mid + 1]
else:
      del l[mid]


print(l)