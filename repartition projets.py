d=[[3,5,7,18],[17,15,16,11,13]]
t=[[1,2,6,7],[16,15,17,12,18]]
z=[[6,7,14,19],[8,9,10,15,17]]
l=[[1,5,7,18],[13,17,10,12,15]]
m=[[7,10,18,19],[5,4,8,9,15]]
f=[[10,12,13,19],[7,6,2,3,11]]
ma=[[4,5,9,10],[1,6,8,15,18]]
b=[[3,4,5,18],[8,9,10,11,13,15]]
p=[[4,5,6,18],[3,9,14,16,17]]
lo=[[3,7,19],[1,4,5,10,13,18]]
a=[[7,10,18,19],[1,11,13,8,15]]
c=[[8,13,18,19],[1,9,11,14,17]]
la=[[3,4,7,14],[1,2,6,8,18]]
w=[[4,5,12,19],[1,2,8,9,15]]
pe=[[3,15,18,19],[1,6,7,9,11]]
h=[[1,6,7,18],[2,11,12,14,15]]
fo=[[4,5,8],[10,13,14,16,17]]
mi=[[6,7,19],[15,8,10,13,14,16,18]]
fa=[[3,4,18,19],[2,1,8,9,16]]

binomes = [d,t,z,l,m,f,ma,b,p,lo,a,c,la,w,pe,h,fo,mi,fa]
repartition=[i for i in range(19)]
choice=[[]]

from random import *
from math import *


def initialisation(popsize,dimension):
    p0=[]
    for k in range(popsize):
        i=[-1 for i in range(dimension)]
        indexes=[j for j in range(20)]
        l=19
        for j in range(dimension):
            r=randrange(0,l)
            e=indexes.pop(r)
            l-=1
            i[e]=j+1
        p0.append(i)
    return p0

def index(liste,x):
    l=len(liste)
    for i in range(l):
        if x==liste[i]:
            return l-i

def function_i(ind):
    l=len(ind)
    s=0
    for i in range(0,l):
        subject=ind[i]
        pair=pairs[i]
        if subject in pair[0]:
            s+=150
        elif subject in pair[1]:
            s-=(100+index(pair[1],subject))
        else:
            s-=10
    return s

def evaluation(p):
    e=[]
    l=len(p)
    for i in range(l):
        e.append(function_i(p[i]))
    return e

def reproduction(p):
    l=len(p)
    i=randrange(0,l)
    j=randrange(0,l)
    while i==j:
        j=randrange(0,l)
    return p[i],p[j]

def crossing_over(p1,p2,pc):
    p=random()
    if pc<p:
        return p1,p2
    l=len(p1)
    e1=[]
    e2=[]
    for i in range(l):
        if randrange(0,2)<1:
            e1.append(p1[i])
            e2.append(p2[i])
        else:
            e1.append(p2[i])
            e2.append(p1[i])
    return e1,e2

def mutation(e,pm):
    l=len(e)
    for i in range(l):
        if random()<pm:
            i=randrange(0,l)
            j=randrange(0,l)
            e[i],e[j]=e[j],e[i]
    return e

def selection(gen0,gen1,e0,e1,popsize):
    #to sort people by evaluations
    tri0e=[e0[0]]
    tri0g=[gen0[0]]
    tri1e=[e1[1]]
    tri1g=[gen1[0]]
    l0=len(e0)
    l1=len(e1)
    for i in range(1,l0):
        j=0
        while j<i and e0[i]>tri0e[j]:
            j+=1
        tri0e=tri0e[:j]+[e0[i]]+tri0e[j:]
        tri0g=tri0g[:j]+[gen0[i]]+tri0g[j:]
    for i in range(1,l1):
        j=0
        while j<i and e1[i]>tri1e[j]:
            j+=1
        tri1e=tri1e[:j]+[e1[i]]+tri1e[j:]
        tri1g=tri1g[:j]+[gen1[i]]+tri1g[j:]
    #print(tri1e,tri0e)
    gens=[]
    es=[]
    c0=0
    c1=0
    for i in range(popsize):
        if tri0e[c0]<=tri1e[c1]:
            gens.append(tri0g[c0])
            es.append(tri0e[c0])
            #print(tri0e[c0])
            c0+=1
        else:
            gens.append(tri1g[c1])
            es.append(tri1e[c1])
            #print(tri1e[c1])
            c1+=1
    return gens,es
        
    
    

def genetic(pm,pc,popsize,dimension,maxgen):
    gen0=initialisation(popsize,dimension)
    e0=evaluation(gen0)
    for iter in range(maxgen):
        gen1=[]#initialisation(popsize,dimension)
        for j in range(0,popsize,4):
            p1,p2=reproduction(gen0)
            e1,e2=crossing_over(p1,p2,pc)
            e1=mutation(e1,pm)
            e2=mutation(e2,pm)
            e3,e4=reproduction(gen0)
            e3=mutation(e3,pm)
            e4=initialisation(1,dimension)[0]
            gen1.append(e1)
            gen1.append(e2)
            gen1.append(e3)
            gen1.append(e4)
        e1=evaluation(gen1)
        gen0,e0=selection(gen0,gen1,e0,e1,popsize)
        """print(e0)
        e0=evaluation(gen0)
        print(e0)"""
    return gen0,e0

pm=0.45
pc=0
popsize=20
dimension=19
maxgen=1000#0000
print(genetic(pm,pc,popsize,dimension,maxgen))