import numpy as np 

x = np.array([1, 1, 2, 3, 4, 3, 4, 6, 4])
y = np.array([2, 1, 0.5, 1, 3, 3, 2, 5, 4])

summation = 0  #variable to store the summation of differences
n = len(y) #finding total number of items in list

for i in range (0,n):  #looping through each element of the list
  difference = x[i] - y[i]  #calculating the difference between observed and predicted value
  squared_difference = difference**2  #taking square of the differene 
  summation = summation + squared_difference  #taking a sum of all the differences
  
MSE = summation/n  #dividing summation by total values to obtain average
print ("The Mean Squared Error is: " , MSE)

from sklearn.metrics import mean_squared_error as mse
import numpy as np 
x = np.array([1, 1, 2, 3, 4, 3, 4, 6, 4])
y = np.array([2, 1, 0.5, 1, 3, 3, 2, 5, 4])


# Calculation of Mean Squared Error (MSE) using scikit – learn:
MSE1 = mse(x,y) 
print("The Mean Squared Error using scikit-learn is:", MSE1)

# Calculation of Mean Squared Error (MSE) using Numpy model:
MSE2 = np.square(np.subtract(x,y)).mean() 
print("The Mean Squared Error using Numpy model is:",MSE2)
