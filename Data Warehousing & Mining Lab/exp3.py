#NAiVE BAYES CLASSIFICATION
def calcCount(x, y):
    count = 0
    for element in d:
        if(set([x, y]).issubset(set(element))):
            count += 1
    return count
d=[['<=30','high','STno','fair','no'],
         ['<=30','high','STno','excellent','no'],
         ['31..40','high','STno','fair','yes'],
         ['>40','medium','STno','fair','yes'],
         ['>40','low','STyes','fair','yes'],
         ['>40','low','STyes','excellent','no'],
         ['31..40','low','STyes','excellent','yes'],
         ['<=30','medium','STno','fair','no'],
         ['<=30','low','STyes','fair','yes'],
         ['>40','medium','STyes','fair','yes'],
         ['<=30','medium','STyes','excellent','yes'],
         ['31..40','medium','STno','excellent','yes'],
         ['31..40','high','STyes','fair','yes'],
         ['>40','medium','STno','excellent','no']
        ]
y=0
n=0
for i in range(len(d)):
   if(d[i][4]=='yes'):
       y+=1
   else:
       n+=1
py=y/len(d)
pn=n/len(d)
print("P(Yes)="+str(py)+"\nP(No)="+str(pn))
print("--------------------------------")
p_ay=calcCount('<=30','yes')
print("P(age<=30|Yes)="+str(p_ay/y))
p_atfy=calcCount('31..40','yes')
print("P(age 31..40|Yes)="+str(p_atfy/y))
p_agfy=calcCount('>40','yes')
print("P(age>40|Yes)="+str(p_agfy/y))
print("--------------------------------")
p_an=calcCount('<=30','no')
print("P(age<=30|No)="+str(p_an/n))
p_atfn=calcCount('31..40','no')
print("P(age 31..40|No)="+str(p_atfn/n))
p_agfn=calcCount('>40','no')
print("P(age>40|No)="+str(p_agfn/n))
print("--------------------------------")
p_ihy=calcCount('high','yes')
print("P(income high|Yes)="+str(p_ihy/y))
p_imy=calcCount('medium','yes')
print("P(income medium|Yes)="+str(p_imy/y))
p_ily=calcCount('low','yes')
print("P(income low|Yes)="+str(p_ily/y))
print("--------------------------------")
p_ihn=calcCount('high','no')
print("P(income high|no)="+str(p_ihn/n))
p_imn=calcCount('medium','no')
print("P(income medium|no)="+str(p_imn/n))
p_iln=calcCount('low','no')
print("P(income low|no)="+str(p_iln/n))
print("--------------------------------")
p_syy=calcCount('STyes','yes')
print("P(student yes|yes)="+str(p_syy/y))
p_sny=calcCount('STno','yes')
print("P(student no|yes)="+str(p_sny/y))
print("--------------------------------")
p_syn=calcCount('STyes','no')
print("P(student yes|no)="+str(p_syn/n))
p_snn=calcCount('STno','no')
print("P(student no|no)="+str(p_snn/n))
print("--------------------------------")
p_crfy=calcCount('fair','yes')
print("P(credit_rating fair|Yes)="+str(p_crfy/y))
p_crey=calcCount('excellent','yes')
print("P(credit_rating excellent|Yes)="+str(p_crey/y))
print("--------------------------------")
p_crfn=calcCount('fair','no')
print("P(credit_rating fair|no)="+str(p_crfn/n))
p_cren=calcCount('excellent','no')
print("P(credit_rating excellent|no)="+str(p_cren/n))

data = '<=30,medium,Yes,fair'
newData = data.split(',')
print('')
print(newData)
p_newyes=(p_ay)*(p_imy)*(p_syy)*(p_crfy)*(py)
p_newno=(p_an)*(p_imn)*(p_syn)*(p_crfn)*(pn)
print('New data is ',end="")
if(p_newyes>p_newno):
    print('Buy computer')
else:
    print('Do not buy computer')


