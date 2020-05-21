n=int(input("Enter the number of inputs>>>>"))
x=[]
y=[]
xx=[]
xy=[]
for i in range (0,n):
    x.append(int(input("Enter x{}>>>>".format(i+1))))
    y.append(int(input("Enter y{}>>>>".format(i+1))))

print(x)
print(y)

xbar=sum(x)/len(x)
ybar=sum(y)/len(y)
print("Xmean>>>>",xbar)
print("Ymean>>>>",ybar)

for i in range(0,n):
    xy.append((x[i]-xbar)*(y[i]-ybar))
    xx.append((x[i]-xbar)*(x[i]-xbar))

xym=sum(xy)/len(xy)
xxm=sum(xx)/len(xx)
b1=(xym)/(xxm)
print("b1:",b1)
b0=ybar-(b1*xbar)
print("b0:",b0)
