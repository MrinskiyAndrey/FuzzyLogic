import func
import openpyxl


#Входные данные 1
book = openpyxl.open('yen.xlsx', read_only=True)
sheet = book.active
x_1 = []
for row in range(2, 52):
    x_1.append(sheet[row][2].value)
norm_x1 = func.normalize_data(x_1)


#Входные данные 2
book = openpyxl.open('tenge.xlsx', read_only=True)
sheet = book.active
x_2 = []
for row in range(2, 52):
    x_2.append(sheet[row][2].value)
norm_x2 = func.normalize_data(x_2)


#Входные данные 3
book = openpyxl.open('tugrik.xlsx', read_only=True)
sheet = book.active
x_3 = []
for row in range(2, 52):
    x_3.append(sheet[row][2].value)
norm_x3 = func.normalize_data(x_3)

print('\n---------------------------------------------------------\n')
print('Нормализированые данные х1: \n',norm_x1)
print('Нормализированые данные х2: \n',norm_x2)
print('Нормализированые данные х3: \n',norm_x3)
print('\n---------------------------------------------------------\n')
#-----------------------------------------------------------------------

# x1 малое:
x1_S = func.small(norm_x1)
print('Икс один малое: \n', x1_S)

# x1 средне-малое
x1_MS = func.medium_small(norm_x1)
print('Икс один средне малое: \n', x1_MS)

# x1 средне-большое
x1_MB = func.medium_big(norm_x1)
print('Икс один средне большое: \n', x1_MB)

# x1 большое
x1_B = func.big(norm_x1)
print('Икс один большое: \n', x1_B)

print('-----------------------------------------------------------')

# x2 малое
x2_S = func.small(norm_x2)
print('Икс два малое: \n', x2_S)

# x2 средне-малое
x2_MS = func.medium_small(norm_x2)
print('Икс два малое: \n', x2_S)

# x2 средне-большое
x2_MB = func.medium_big(norm_x2)
print('Икс два средне большое: \n', x2_MB)

# x2 большое
x2_B = func.big(norm_x2)
print('Икс два большое: \n', x2_B)

print('-----------------------------------------------------------')


# x3 малое
x3_S = func.small(norm_x3)
print('Икс три малое: \n', x3_S)

# x2 средне-малое
x3_MS = func.medium_small(norm_x3)
print('Икс три малое: \n', x3_S)

# x2 средне-большое
x3_MB = func.medium_big(norm_x3)
print('Икс три средне большое: \n', x3_MB)

# x2 большое
x3_B = func.big(norm_x3)
print('Икс три большое: \n', x3_B)

print('\n---------------------------------------------------------\n')
#-----------------------------------------------------------------------

    
