d1=0.85
x=int(input("Enter the number of interations you want>>>"))
y=int(input("Enter the number of nodes>>>"))
pr=[]
for i in range (0,y):
    pr.append(1)
print(pr)
mo=[]
print("Enter the elements for outgoing method>>>")
for i in range(0,y):
    a=[]
    for j in range(0,y):
        a.append(int(input()))
    mo.append(a)
for i in range(y):
    for j in range(y): 
        print(mo[i][j], end = " ") 
    print()   
print(mo)
mi=[]
print("Enter the elements for incoming method>>>")
for i in range(0,y):
    a=[]
    for j in range(0,y):
        a.append(int(input()))
    mi.append(a)
for i in range(y):
    for j in range(y): 
        print(mi[i][j], end = " ") 
    print()   
print(mi)
op=[]
inco=[]
def check(mat,outputmatrix):
    for i in range(y):
        o=0
        for j in range(y):
            if(mat[i][j]==1):
                o=o+1
        outputmatrix.append(o)
check(mo,op)
check(mi,inco)
#print("outgoing")
#print(op)
#print("incoming")
#print(inco)

#for r in range(x):
def p_rank(y,mi,pr,op):
    prv=[]
    v=[]
    s=0
    for i in range(y):
        cc=0
        #print(str(r)+"<<in ith loop>>")
        #print(i)
        #print(pr)
        #print("------")
        for j in range(y):
            if(mi[i][j]==1):
                cc=cc+1
                v.append(float(pr[j]/op[j]))
        if(cc==2):        
            s=(1-d1)+(d1*(v[i]+v[i+1]))
            #prv.append(s)
        else:
            s=(1-d1)+(d1*(v[i]))
            #prv.append(s)
        pr[i]=s
        #pr[i]=prv[i]
    #print(r)
    op=[]
    op.append([s])
    print(pr)
for i in range(x):
    print("Iteration"+str(i+1))
    p_rank(y,mi,pr,op)
#print(op)











