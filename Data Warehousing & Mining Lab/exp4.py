import matplotlib.pyplot as plt  
n=int(input("Enter the number of inputs>>"))
x=[]
y=[]
xx=[]
xy=[]
for i in range (0,n):
    x.append(float(input("Enter x{}>>".format(i+1))))
    y.append(float(input("Enter y{}>>".format(i+1))))

print(x)
print(y)

xbar=sum(x)/len(x)
ybar=sum(y)/len(y)
print("X-mean>>",xbar)
print("Y-mean>>",ybar)

for i in range(0,n):
    xy.append((x[i]-xbar)*(y[i]-ybar))
    xx.append((x[i]-xbar)*(x[i]-xbar))

xym=sum(xy)/len(xy)
xxm=sum(xx)/len(xx)
b1=(xym)/(xxm)
print("m>>",b1)
b0=ybar-(b1*xbar)
print("c>>",b0)
yn=[]
for i in range(len(x)):
    yn.append((float(b1)*float(x[i]))+float(b0))


sx=sum(x)
sy=sum(y)
xy=[]
sqx=[]
sqy=[]
for i in range(len(x)):
    xy.append(x[i]*y[i])
    sqx.append(x[i]**2)
    sqy.append(y[i]**2)
sxy=sum(xy)
ssqx=sum(sqx)
ssqy=sum(sqy)
n=len(x)
num=(n*sxy)-(sx*sy)
den=((n*ssqx-(sx**2))*(n*ssqy-(sy**2)))**(1/2)
r=num/den
print("Correlation coefficient of regression line>>",r)
print('--------------------------------------------------')
sq_error_y=[]
for i in range(len(y)):
    sq_error_y.append(y[i]-yn[i])
sq_error=0.0
for i in range(len(y)):
    sq_error = float(sq_error) + float(sq_error_y[i]**2)
print("Square error>>",sq_error)
print("Mean Square error>>",float(sq_error)/float(len(y)))
print('----------------------------------------------------')
plt.scatter(x,y,label='xy',color='grey',marker='o')
plt.plot(x,yn,label='y=mx+c')
plt.title('Regression Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()




