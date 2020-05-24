n=int(input("Enter A Large Prime Number for n:"))
g=int(input("Enter Another Large Prime Number for g:"))
x=int(input("Enter Value of x:"))
y=int(input("Enter Value of y:"))

A=(g**x)%n
B=(g**y)%n

k1=(B**x)%n
k2=(A**y)%n

print(k1)
print(k2)
