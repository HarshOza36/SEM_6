print("Database is:")
print("1 3 4")
print("2 3 5") 
print("1 2 3 5") 
print("2 5")
def Apriori_gen(Itemset, lenght):
    canditate = []
    canditate_index = 0
    for i in range (0,lenght):
        element = str(Itemset[i])
        for j in range (i+1,lenght):
            element1 = str(Itemset[j])
            if element[0:(len(element)-1)] == element1[0:(len(element1)-1)]:
                    unionset = element[0:(len(element)-1)]+element1[len(element1)-1]+element[len(element)-1] #Combine (k-1)-Itemset to k-Itemset 
                    unionset = ''.join(sorted(unionset))  #Sort itemset by dict order
                    canditate.append(unionset)
    return canditate


def Apriori_prune(Ck,MinSupport):
    L = []
    sup=[]
    print("Candidate")
    for i in Ck:
        print(i,":",Ck[i])
    #print("Candidate",cc,":",Ck)
    for i in Ck:
        if Ck[i] >= minsupport:
            L.append(i)
            sup.append(Ck[i])
    return sorted(L),sup
    
def Apriori_count_subset(Canditate,Canditate_len):
    """ Use bool to know is subset or not """
    Lk = dict()
    file = open('example.txt')
    for l in file:
        l = str(l.split())
        count = 0
        for i in range (0,Canditate_len):
            key = str(Canditate[i])
            if key not in Lk:
                Lk[key] = 0
            flag = True
            for k in key:
                if k not in l:
                    flag = False
            if flag:
                Lk[key] += 1
    file.close()
    return Lk
minsupport =2 
mincon=0.50
cc=0
C1={} 
file = open('example.txt')
"""Count one canditate"""
for line in file:
    for item in line.split():
        if item in C1:
            C1[item] +=1
        else:
            C1[item] = 1
file.close()

#C1.keys().sort()
sorted(C1)

L = []
L1,supp = Apriori_prune(C1,minsupport)
L = Apriori_gen(L1,len(L1))
print ('====================================')
#print ('L1:',L1,supp)
print("L1")
print("Itemset:Support count")
for i in range(len(L1)):
	print(L1[i],":",supp[i])
print ('====================================')
k=2
while L != []:
    C = dict()
    C = Apriori_count_subset(L,len(L))
    fruquent_itemset = []
    fruquent_itemset,suppp = Apriori_prune(C,minsupport)
    print ('====================================')
    #print ('L',k,':',fruquent_itemset,suppp)
    print("L",k)
    print("Itemset:Support count")
    for i in range(len(fruquent_itemset)):
            print(fruquent_itemset[i],":",suppp[i])
    print ('====================================')
    L = Apriori_gen(fruquent_itemset,len(fruquent_itemset))
    k += 1

#########################################################
from collections import Counter, OrderedDict
import itertools
from pprint import pprint

MIN_SUPPORT_COUNT = 2
MIN_CONFIDENCE = 0.70
debug_print = print
'''print([
        ['I1', 'I3', 'I4'], 
        ['I2', 'I3', 'I5'], 
        ['I1', 'I2', 'I3', 'I5'], 
        ['I2', 'I5']
    ])
'''
def load_dataset():
    return [
        ['1', '3', '4'], 
        ['2', '3', '5'], 
        ['1', '2', '3', '5'], 
        ['2', '5']
    ]


def print_dict(d):
    for k, v in d.items():
        print(k, ':', v)
    return len(k)


def support_count(item):
    return sum(1 for row in load_dataset() if item.issubset( row ))


def confidence(rule):
    # rule: 2-tuple
    # where rule[0] = set of items
    #       rule[1] = set of items
    return support_count(rule[0] | rule[1]) / support_count(rule[1])


def apriori(data, min_sup=MIN_SUPPORT_COUNT, min_conf=MIN_CONFIDENCE):
    d = [item for sublist in data for item in sublist]
    freq = OrderedDict(Counter(d).items())
    comb = 2
    while True:
        c = {}
        for perm in itertools.combinations(freq.keys(), comb):
            count = 0
            for row in data:
                if set(perm).issubset(row):
                    count += 1
                if count >= min_sup:
                    c[perm] = count   
        if len(c.keys()) <= 2:
            break
        comb += 1
    debug_print("Final Candidate: ")
    k_size = print_dict(c) # final candidate table

    debug_print('Association rules:')
    rules = []
	
    for itemset in c:
        for i in range(1, k_size):
            for item in itertools.combinations(itemset, r=i):
                lhs, rhs = set(item), set(itemset) - set(item)
                rules.append( (lhs, rhs) )

    for rule in rules:
        debug_print(rule[0], '->', rule[1], end=' ')
        debug_print('Confidence:', '{:5.2f}'.format( confidence(rule) ))

    debug_print('Chosen rules:')
    chosen_rules = [rule for rule in rules if confidence(rule) >= min_conf]
    for rule in chosen_rules:
        debug_print(rule[0], '->', rule[1], end=' ')
        debug_print('Confidence:', '{:5.2f}'.format( confidence(rule) ))

		 

if __name__ == '__main__':
    c = apriori(data=load_dataset())

