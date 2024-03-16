from sklearn import datasets, linear_model 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

diabetes=datasets.load_diabetes()
diabetes_x=diabetes.data#ye second number vale feature ko column me dalke array bnyega
# print(diabetes_x)    #bohot jyada value hai to hum sirf 30 train krne ke liye....

diabetes_x_train=diabetes_x[:-30]
diabetes_x_test=diabetes_x[-30:]

diabetes_y_train=diabetes.target[:-30]
diabetes_y_test=diabetes.target[-30:]

model=linear_model.LinearRegression()

model.fit(diabetes_x_train,diabetes_y_train)

diabetes_y_predicted=model.predict(diabetes_x_test)
print("Predicted values are:",diabetes_y_predicted)
print("Mean squared error is: ",mean_squared_error(diabetes_y_test,diabetes_y_predicted))
# to print a dataset 
# print(diabetes.keys())    #isko print krte samay upar vali ko comment krna hai otherwise error raise hoga

# (['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])
# print(diabetes.DESCR)

print("Weights: ",model.coef_)       #weights ke liye model.coef_
print("Intercept: ",model.intercept_)  #intercept ke liye model.intercept_

# plt.scatter(diabetes_x_test, diabetes_y_test, )   # .scatter se sirf dots ayenge
# plt.plot(diabetes_x_test,diabetes_y_predicted)    # .plot se line ayegi
# plt.show()

# Mean squared error is:  3035.060115291269
# Weights:  [941.43097333]
# Intercept:  153.39713623331644


# New values:-

# Mean squared error is:  1826.4841712795044
# Weights:  [  -1.16678648 -237.18123633  518.31283524  309.04204042 -763.10835067
#   458.88378916   80.61107395  174.31796962  721.48087773   79.1952801 ] 
# Intercept:  153.05824267739402