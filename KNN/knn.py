import pandas as pd
import matplotlib.pyplot as plt
import math

class dis:
    dist = 0
    x = 0
    y = 0
    p = 0

k=int(input("Enter value of k:"))
x=int(input("Enter value of x:"))
y=int(input("Enter value of y:"))

data = pd.read_csv('tshirt.csv')
X = data['Height (in cms)'].values
Y = data['Weight (in kgs)'].values
label = data['Class'].values
m_x = []
m_y = []
l_x = []
l_y = []

for i in range(len(X)):
    if label[i] == 0:
        m_x.append(X[i])
        m_y.append(Y[i])
    else:
        l_x.append(X[i])
        l_y.append(Y[i])

print(len(m_x), len(l_x))
plt.scatter(m_x, m_y, color='r')
plt.scatter(l_x, l_y, color='b')
plt.scatter(x, y , color = 'black')
plt.xlabel('Height (in cms)')
plt.ylabel('Weight (in kgs)')
plt.show()

i=0
distance=[]

for i in range(len(data)):
    d = dis()
    d.dist=math.sqrt(math.pow((x-data.iloc[i,0]),2) + math.pow((y-data.iloc[i,1]),2) )
    d.x=data.iloc[i,0]
    d.y=data.iloc[i,1]
    d.p=data.iloc[i,2]
    distance.append(d)

distance = sorted(distance, key=lambda dis: dis.dist)
n=0
y=0
for i in range(k):
    if distance[i].p==0:
        n=n+1
    else:
        y=y+1

if y>n:
    print("predicted Class:","large")
elif y<n: 
    print("predicted class:", "medium")
else:
    print("point lies on boreder")

