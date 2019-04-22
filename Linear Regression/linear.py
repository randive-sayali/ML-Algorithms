import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Salary_Data.csv')

# print(data)

X = data['YearsExperience'].values
Y = data['Salary'].values
print('\nIndependent Variable (Years of Experience) X=', X)
print('\n\nDependent Variable Y (Salary) =', Y)

# Scatter Plot for Points

plt.scatter(X, Y, c='#ef5423', label='Scatter Plot')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()

# Finding correlation between x and y

corr = data.corr()
print('\n\nCorelation Matrix is as follows: \n\n', corr)

# Finding Mean

mean_x = sum(X)/len(X)
mean_y = sum(Y)/len(Y)
print('\n\nMean of X = ', mean_x)
print('Mean of Y = ', mean_y)


# Finding Coefficients
num = 0
den = 0
for i in range(len(X)):
    num += (X[i]-mean_x) * (Y[i]-mean_y)
    den += (X[i]-mean_x)**2

b1 = num/den
b0 = mean_y - (mean_x * b1)

print('\n\nSlope of Line (b1) =', b1)
print('Intercept of Line (b0) =', b0)

# Plot line of regression

yp = X * b1 + b0

plt.scatter(X, Y, color = '#ef5423', label = 'Scatter Plot')
plt.axhline(mean_y, color = '#000000', label = 'Mean Regression Line')
plt.plot(X, yp, color = 'green', label = 'Linear Regression Line')
plt.xlabel('Years Of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()

# Finding Accuracy of Linear Regression Line using RMS

sst = 0
sse = 0
for i in range (len(X)):
    yp = b0 + b1 * X[i]

    sst += (Y[i] - mean_y) ** 2
    sse += (Y[i] - yp) ** 2

r2 = 1 - (sse/sst)
print('\n\n\nSum of Squared Error Value of Linear Regression Line = ', sse)
print('Accuracy of Linear Regression Line given by RMSE = ', r2)

# Finding Accuracy of MEan Regression Line

sstm = 0
ssem = 0

for i in range (len(X)):

    ssem += (Y[i] - mean_y) ** 2

print('\n\n\nSum of Squared Error Value of Mean Regression Line = ', ssem)
print('Error value of Mean Regression is more than Linear Regression by ', (ssem - sse))
'''
# Error Value
sum_of_error = 0
ypred = 0
e= 0

for i in range(len(X)):
    ypred = b1 * X[i] + b0
    e = Y[i] - ypred
    sum_of_error = sum_of_error + e

    print('Error value = ', sum_of_error)
'''

# Know difference between actual and predicted values of Salary

print('\n\nEnter the value of X (Years of Experience) : ')
x = float(input())
y = 0.0
for i in range(len(X)):
    if x == X[i]:
        y = Y[i]
        print('\n\nActual Value of Salary for ', x, ' Years of Experience is ', y )
yp = b1 * x + b0
print('Predicted Value of Salary for ', x, ' Years of Experience is ', yp)

print('Difference between actual and predicted values = ', abs(yp-y))

