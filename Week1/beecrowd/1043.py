#!/usr/bin/env python
# coding: utf-8

# In[6]:


a,b,c=map(float,input().split())

if (a+b)>c and (a+c)>b and (b+c)>a:
    p = (a+b+c)
    print(f"Perimetro = {p:0.1f}")
else:
    a= 0.5*(a+b)*c
    print(f"Area = {a:0.1f}")


# In[ ]:




