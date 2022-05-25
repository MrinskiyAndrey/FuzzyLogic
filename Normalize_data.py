from sklearn import preprocessing
import numpy as np

x_array = np.array([2,3,5,6,7,4,8,7,6])


def normalize_data(data):
    
    normalized_arr = preprocessing.normalize([data])
    i=0
    result = []
    while i < len(normalized_arr[0]):
        result.append(normalized_arr[0][i]*10)
        i+=1
    return result

print(normalize_data(x_array))
