from sklearn import preprocessing
import numpy as np

x_array = np.array([2,3,5,6,7,4,8,7,6])
normalized_arr = preprocessing.normalize([x_array])
#result = [normalized_arr[0][i]*10 for i in len(normalized_arr)]
i=0
result = []
while i < len(normalized_arr[0]):
    result.append(normalized_arr[0][i]*10)
    i+=1
#print(normalized_arr[0][3])
#print(normalized_arr)
print(result)
