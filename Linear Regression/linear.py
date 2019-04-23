import pandas as pd
import matplotlib.pyplot as plt

def correlation(corr_data):
    print(corr_data.corr())

def cal_mean(x,y):
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    return(mean_x,mean_y)

def calc_coff(x, y,mean_x, mean_y):
    num = 0
    den = 0
    for i in range(len(x)):
        num += (x[i] - mean_x) * (y[i] - mean_y)
        den += (x[i] - mean_x) ** 2

    b1 = num/den
    b0 = mean_y - b1 * mean_x

    return (b1,b0)

def acc_by_res(x, y, mean_x, mean_y, b1, b0):
    sst = 0
    sse = 0
    for i in range(len(x)):
        yp = b0 + b1 * x[i]

        sst += (y[i] - mean_y) ** 2
        sse += (y[i] - yp) ** 2

    r2 = 1 - (sse / sst)
    return r2

def main():
    print('\n****************************************************')
    print('\n\nFirst Linear Regression Line :')
    data = pd.read_csv('Salary_Data.csv')
    X = data['YearsExperience'].values
    Y = data['Salary'].values

    data1 = data.sample(frac=0.75)
    X1 = data1['YearsExperience'].values
    Y1 = data1['Salary'].values
    print('For first linear regression line :')
    print('Corelation matrix is as follows:')
    correlation(data1)
    m_x1, m_y1 = cal_mean(X1, Y1)
    b1, b0 = calc_coff(X1, Y1, m_x1, m_y1)
    print('\nCoefficeints are: ', b1, b0)
    print('\nEquation of line is: y = ', b0, ' + ', b1, ' * x')
    r21 = acc_by_res(X, Y, m_x1, m_y1, b1, b0)
    print('\nAccuracy of the line is : ', r21 * 100)
    print('\n****************************************************')

    print('\n****************************************************')
    print('\n\nSecond Linear Regression Line :')
    data2 = data.sample(frac=0.85)
    X2 = data2['YearsExperience'].values
    Y2 = data2['Salary'].values
    print('For second linear regression line :')
    print('Corelation matrix is as follows:')
    correlation(data2)
    m_x2, m_y2 = cal_mean(X2, Y2)
    b1_2, b0_2 = calc_coff(X2, Y2, m_x2, m_y2)
    print('\nCoefficeints are: ', b1_2, b0_2)
    print('\nEquation of line is: y = ', b0_2, ' + ', b1_2, ' * x')
    r22 = acc_by_res(X, Y, m_x2, m_y2, b1_2, b0_2)
    print('\nAccuracy of the line is : ', r22 * 100)
    print('\n****************************************************')

    print('\n****************************************************')
    print('\n\nThird Linear Regression line :')
    print('Corelation matrix is as follows:')
    correlation(data)
    m_x3, m_y3 = cal_mean(X, Y)
    b1_3, b0_3 = calc_coff(X, Y, m_x3, m_y3)
    print('\nCoefficeints are: ', b1_3, b0_3)
    print('\nEquation of line is: y = ', b0_3, ' + ', b1_3, ' * x')
    r2_3 = acc_by_res(X, Y, m_x3, m_y3, b1_3, b0_3)
    print('\nAccuracy of the line is : ', r2_3 * 100)
    print('\n****************************************************')

    if r21 > r22:
        if r21 > r2_3:
            print('The First linear Regression line i.e. the green line is the best fit.')
        else:
            print('The Third linear Regression line i.e. the black line is the best fit.')
    else:
        if r22 > r2_3:
            print('The Second linear Regression line i.e. the yellow line is the best fit.')
        else:
            print('The Third linear Regression line i.e. the black line is the best fit.')

    plt.scatter(X, Y, color='orange', label='Scatter Plot')
    yp = b0 + b1 * X1
    yp_2 = b0_2 + b1_2 * X2
    yp_3 = b0_3 + b1_3 * X
    plt.plot(X1, yp, color='green', label='First Linear Regg Line')
    plt.plot(X2, yp_2, color='yellow', label='Second Linear Regg Line')
    plt.plot(X, yp_3, color='black', label='Best Fit Linear Regg Line')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.legend()
    plt.show()

main()
