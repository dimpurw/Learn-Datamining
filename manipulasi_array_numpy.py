# Nama  : Dimas Pratama Purwadinata
# Nim   : 182410101127
# Kelas : Datamining B

# Kode 1 
# F
import numpy as np
arr = np.array([[4,4,5],[7,6,4],[9,7,4],[6,3,7]])
print(arr)

# G
import numpy as np
arr = np.array([[[7,8,5],[4,7,7],[7,1,9],[5,4,10]],
				[[2,1,2],[9,8,5],[3,7,3],[4,9,9]],
    			[[2,9,3],[2,4,8],[1,6,6],[8,1,3]]])
print(arr)


# KODE 2
# D
import numpy as np
arr = np.array([[1,8,8,2],[8,2,1,2],[10,1,4,7],[1,4,7,8],[8,2,3,4]])
arr[1::2] +=1
arr[:,0::2] +=2
print(arr)

# E
import numpy as np
arr = np.array([[[7,8,5],[4,7,7],[7,1,9],[5,4,10]],
				[[2,1,2],[9,8,5],[3,7,3],[4,9,9]],
    			[[2,9,3],[2,4,8],[1,6,6],[8,1,3]]])
print(arr[::-1])


# F
import numpy as np
arr = np.array([[[7,8,5],[4,7,7],[7,1,9],[5,4,10]],
				  [[2,1,2],[9,8,5],[3,7,3],[4,9,9]],
				  [[2,9,3],[2,4,8],[1,6,6],[8,1,3]]])
print(arr.reshape(6,6))


# KODE 3
# E
import numpy as np
arr = np.array([[5, 10, 10, 7], [7, 8, 4, 10], [9, 10, 2, 5], [1, 8, 9, 3], [6, 10, 5, 2], [4, 6, 9, 4]])
print(arr)
print('--------------')
arr2 = np.copy(arr[:3,:])
arr[:3,:] = arr[3:,:]
arr[3:,:] = arr2

arr2 = np.copy(arr[:,:2])
arr[:,:2] = arr[:,2:]
arr[:,2:] = arr2
print (arr)

