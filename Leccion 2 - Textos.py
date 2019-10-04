#!/usr/bin/env python
# coding: utf-8

# In[86]:




#Devuelve el número ordenado de mayor a menor
def devolver_num(a):
    return int("".join(sorted(str(num), reverse=True)))

print(devolver_num(1425))


# In[88]:


#Devuelve el sumatorio de cada uno de los numeros intermedios incluyendo el mayor
def get_sum(a,b):
    return sum(range(min(a,b), max(a,b)+1))
print(get_sum(1,6))


# In[165]:


#Devuelve una piramide de asteriscos
def tower(n_floors):
    pir=[]
    for a in range(0,n_floors*2):
        if a%2==1:
            pir.append("{:^{}}".format("*"*(a), n_floors*2-1))
        
    return pir
print(tower(7))

def tower_builder(n):
    length = n * 2 - 1
    return ['{:^{}}'.format('*' * a, length) for a in range(1, length + 1, 2)]
print(tower_builder(7))


# In[ ]:


#Recibe un valor y tiene que hacer una secuencia de 1+1/4+1/7, tantas sumas segun marque el valor
def cadenaserie(n):   
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))


def series_sum(n):
    a=0
    for p in range(0,n):
        if p==0:
            pass
        a+=1/(4+(p-1)*3)
    return "{:.2f}".format(a)

