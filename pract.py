import numpy as np 

height = 200
width = 290

print(height//2)

arr = np.zeros((2,3,3))
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        for k in range(arr.shape[2]):
            arr[i,j,k] = int(np.random.randint(0,256))
            
print(arr[0,0])
print(arr[0][0])
print(arr[0,0,2])
print(arr)
print(arr[0,1,2])
print(arr[0][1][2])

print()
print(np.random.randint(0, 255, size=3))