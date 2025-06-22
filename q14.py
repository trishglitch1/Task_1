import numpy as np

array_1 = np.random.randint (0, 10, size=(3, 3))
array_2 = np.random.randint (0, 10, size=(3, 3))

print("array 1: ", 
print(array_1)
print("array 2: ")
print(array_2)

equal_array = array_1 == array_2

print("\nelement-wise equality: ")
print(equal_array)