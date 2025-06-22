import numpy as np

random_array = np.random.randint (1, 101, size=(5, 5))
print("original array: ")
print(random_array)

random_array[random_array % 2 == 0] = 0
print("\narray after replacing all even numbers with 0: ")
print(random_array)