n=int(input("Enter the number of points>>>"))
x=[]
y=[]
cx=[]
cy=[]
k1=[]
kc1=[]
for i in range(0,n):
    print("Enter Coordinates of point{}>>>".format(i+1))
    x.append(int(input("Enter X>>>")))
    y.append(int(input("Enter Y>>>")))

k=int(input("Enter the number of clusters>>>"))
for i in range(0,k):
    z=[0]
    k1.append(z)
    c1x=[]
    c1y=[]
    print("Enter Centre Point {}>>>".format(i+1));
    c1x.append(int(input()))
    c1y.append(int(input()))
    cx.append(c1x)
    cy.append(c1y)
      

while (True):
    kc1=k1.copy()
    k1=[[],[],[]]
    r=[]
    print("\n")
    for j in range(0,k):
        r1=[]  
        for i in range(0,n):
            a=round((((x[i]-cx[j][0])**2)+((y[i]-cy[j][0])**2))**(1/2),3)
            r1.append(a)
        r.append(r1)
        print(r[j])
    for i in range(0,n):
       temp=r[0][i]
       for j in range(0,k):
           if(r[j][i]<=temp):
               temp=r[j][i]
               t=j
           else:
               continue
       k1[t].append(i+1)
       
    cx=[[],[],[]]
    cy=[[],[],[]]
    for i in range(0,k):
        for p in k1[i]:
            p=p-1
            cx[i].append(x[p])
            cy[i].append(y[p])

        cx[i][0]=sum(cx[i])/len(cx[i])
        cy[i][0]=sum(cy[i])/len(cy[i])
        print("Cluster {}>>>".format(i+1),k1[i])
        print("Centre {}>>>(".format(i+1),cx[i][0],",",cy[i][0],")")
    if k1==kc1:
        break
    else:
        kc1=[[],[],[]]
        
   
      
