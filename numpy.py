

import numpy as np

arr_linspace = np.linspace(0, 1, 15)

arr1 = [1.1, 2.1, 3.1]
arr2 = [4.1, 5.1, 6.1]
arr3 = [7.1, 8.1, 9.1]
arr4 = [10.1, 11.1, 12.1]
arr_3d = np.array([[arr1, arr2], [arr3, arr4]])

print("Type:", type(arr_3d))
print("Datatype:", arr_3d.dtype)
print("Shape:", arr_3d.shape)
print("Size:", arr_3d.size)
print("Dimension:", arr_3d.ndim)

arr_4d = arr_3d.reshape(1, 2, 2, 3)
print("4D Dimension:", arr_4d.ndim)
print("4D Shape:", arr_4d.shape)

arr_int = arr_3d.astype(int)

for x in np.nditer(arr_int):
    print(x, end=" ")
print()

print("8th element:", arr_int.flatten()[7])

print("5th element:", arr_int.flatten()[4])
print("6th element:", arr_int.flatten()[5])

print("Indices of element 8:", np.where(arr_int == 8))

arr_reshaped = arr_int.reshape(2, 3, 2)
print("Reshaped array:\n", arr_reshaped)

a1 = np.array([["A", "B"], ["E", "F"]])
a2 = np.array([["C", "D"], ["G", "H"]])
merged_default = np.concatenate((a1, a2))

merged_axis1 = np.concatenate((a1, a2), axis=1)

split_arr = np.array_split(merged_axis1, 2, axis=1)
print("Split Array 1:\n", split_arr[0])
print("Split Array 2:\n", split_arr[1])
