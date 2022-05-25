from sklearn import preprocessing

x_array = str(input("Введите строку данных:\n"))
y_array = x_array.replace(',','.').split()


def normalize_data(data : list):
    
    
    normalized_arr = preprocessing.normalize([data])
    i=0
    result = []
    while i < len(normalized_arr[0]):
        result.append(normalized_arr[0][i]*10)
        i+=1
    return result
    #return normalized_arr
print("Нормализованные данные:\n", normalize_data(y_array))
