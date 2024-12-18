import numpy as np

#create 4x(4x3)
arr = np.array([
    [[1,2,3], 
     [4,5,6], 
     [6,7,8], 
     [8,9,10]],
    
    [[4,5,6],
     [7,8,9],
     [1,2,3],
     [4,5,6]],
    
    [[4,5,6],
     [7,8,9],
     [1,2,3],
     [4,5,6]],
    
    [[1,2,3], 
     [4,5,6], 
     [6,7,8], 
     [8,9,10]]
])

print(arr.shape)
#print(arr)
print()
# print(arr.shape[0])
# print(arr.shape[1])
# print(arr.shape[2])
print(arr[0][1])
print()
print("arr[0,1,2]: ",arr[0,1,2])