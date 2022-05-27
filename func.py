from sklearn import preprocessing
import pandas as pd

#-------------------------Normalization-----------------------------------------
#Нормализация
def normalize_data(data):

    normalized_arr = preprocessing.normalize([data])
    i=0
    result = []
    while i < len(normalized_arr[0]):
        result.append(round((normalized_arr[0][i]*10), 3))
        i+=1

    return result



#--------------------------Dimension------------------------------------------------
#малое
def small(data):
    S = []
    i=0
    while i < len(data): 
        S.append(round((5 - data[i]) / 5, 3))
        i+=1
    return S

#средне малый
def medium_small(data):
    MS = []
    i=0
    while i < len(data): 
        MS.append(round(data[i] / 5, 3))
        i+=1
    return MS

#средне большое
def medium_big(data):
    MB = []
    i=0
    while i < len(data): 
        MB.append(round((10 - data[i]) / 5, 3))
        i+=1
    return MB

#большое
def big(data):
    B = []
    i=0
    while i < len(data): 
        B.append(round((data[i] - 5) / 5, 3))
        i+=1
    return B


#---------------------------------------------------------------------------

