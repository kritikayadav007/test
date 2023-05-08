import cv2 
import numpy as np
import pandas as pd

a = pd.read_csv('train.csv')
ser_aggRows=pd.Series(a.values.tolist())
b=ser_aggRows[10]
c=b[1:]
tem=[]
for i in range(28):
	tem.append(c[i*28:(i+1)*28])

ab = np.array(tem,dtype = np.uint8)
cv2.imshow("black", ab)
cv2.waitKey(0)