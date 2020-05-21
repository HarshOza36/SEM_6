from sympy import symbols, diff
import math
x, y, z = symbols('x y z', real=True)
df=x**2+(2*x*y)+2*(y**2)+x
'''partial diif'''
pdx=diff(df,x)
pdy=diff(df,y)
x0=[0.50,0.50]
alpha=float(0.1)
print("Alpha:"+str(alpha))
g=[]
g.append(round(float(alpha*(pdx.evalf(subs={x: 0.5, y: 0.5}))),2))
g.append(round(float(alpha*(pdy.evalf(subs={x: 0.5, y: 0.5}))),2))
print("alpha*G0:"+str(g))
x1=[0,0]
for i in range(0,2):
    x1[i]=(x0[i]-g[i])
print("x1:"+str(x1))
c=0
while(c!=3):
    g[0]=(round(float(alpha*(pdx.evalf(subs={x: x1[0], y: x1[1]}))),2))
    g[1]=(round(float(alpha*(pdy.evalf(subs={x: x1[0], y: x1[1]}))),2))   
    print("Alpha*G1:"+str(g))
    for i in range(0,2):
        x1[i]=round((x1[i]-g[i]),2)
    print("x1:"+str(x1))
    c+=1
g[0]=round(float(g[0]/alpha),2)
g[1]=round(float(g[1]/alpha),2)
print("Last G:"+str(g))




















'''
cur_x = 3 # The algorithm starts at x=3
rate = 0.01 # Learning rate
precision = 0.000001 #This tells us when to stop the algorithm
previous_step_size = 1 #
max_iters = 10000 # maximum number of iterations
iters = 0 #iteration counter
df = lambda x: 2*(x+5) #Gradient of our function 
while previous_step_size > precision and iters < max_iters:
    prev_x = cur_x #Store current x value in prev_x
    cur_x = cur_x - rate * df(prev_x) #Grad descent
    previous_step_size = abs(cur_x - prev_x) #Change in x
    iters = iters+1 #iteration count
    print("Iteration",iters,"\nX value is",cur_x) #Print iterations
    
print("The local minimum occurs at", cur_x)
'''
