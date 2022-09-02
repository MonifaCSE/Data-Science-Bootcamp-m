#!/usr/bin/env python
# coding: utf-8

# In[11]:


n=float(input())

if  n>=0 and n<=400:
     b= n*0.15
     c=n+b
     d=15
elif  n>=400.01 and n<=800.00:
     b=n*0.12
     c=n+b
     d=12
elif n>=800.01 and n<=1200.00:
    b=n*0.1
    c=n+b
    d=10
elif n>=1200.01 and n<=2000.00:
     b=n*0.07
     c=n+b
     d=7
elif n>2000:
     b=n*0.04
     c=n+b
     d=4
print(f"Novo salario: {c:.2f}")
print(f"Reajuste ganho: {b:.2f}")
print(f"Em percentual: {d} %")


# In[ ]:




