import numpy as np
import math as m
import pandas as pd

matrix = np.loadtxt(r'',  delimiter=',',encoding='utf-8-sig')#file path (.csv)
i = int()
j = int()
for i in range(len(matrix)):
    x_1=matrix[i][0]
    y_1=matrix[i][1]
    for j in range(len(matrix)):
        if i == j:
            continue
        x_2=matrix[j][0]
        y_2=matrix[j][1]
        distance = m.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
        sigma= #Input sigma value
        #print(i,j,x_1,y_1,x_2,y_2)
        if (distance < sigma):
            #print(distance)
            gauss = 1/(2*np.pi*(sigma**2))*np.exp(-((x_2-x_1)**2+(y_2-y_1)**2)/(2*sigma**2))
            new = matrix[i][2]*gauss
            matrix[j][2] += new
        else:
            #print(distance)
            pass
new_matrix_df = pd.DataFrame(matrix)
writer = pd.ExcelWriter(r'')#file path (.xlsx)
new_matrix_df.to_excel(writer,'page_1',float_format='%.10f')
writer.save()
