import math as m
mg=input("Enter the message for product cipher encryption>>>")
msg=mg.upper().replace(" ","")
a=list(msg)
k=int(input("Enter the key>>>"))
print("NOW ENCRYPTING>>>>>>>>>>>>>>>>>>>")
c1=[]
b=0
b1=0
for i in range(0,len(a)):
    b=(ord(a[i])+k)
    if(b>90):
        b=b-90 
        b1=chr(64+b)
    else:
        b1=chr(b)
    c1.append(b1)
ci1=str(c1)
print("Substitution Cipher :"+ci1)
e=[]
o=[]
for i in range(0,len(c1)):
    if(i%2==0):
        e.append(c1[i])
    else:
        o.append(c1[i])
'''print(e)
print(o)'''
c2=e+o
le=len(e)
lo=len(o)
ci2=str(c2)
print("Transposition Cipher :"+ci2)
print("NOW DECRYPTING>>>>>>>>>>>>>>>>>>")
dc2=[]
dc1=[]
l=m.ceil(len(c2)/2)
for i in range(0,l):
    dc2.append(e[i])
    if(i<lo):
        dc2.append(o[i])
dci2=str(dc2)
print("Transposition decrypt:"+dci2)
for i in range(0,len(dc2)):
    b=(ord(a[i])-k)
    if(b<65):
        b=b+90 
        b1=chr(64-b)
    else:
        b1=chr(b+1)
    dc1.append(b1)
dci1=str(dc1)
print("Substitution Decrypt :"+dci1)
