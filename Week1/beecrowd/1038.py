#!/usr/bin/env python
# coding: utf-8

# # 1038

# In[2]:


a,b=map(int,input().split())

if a==1:
    p=4.00
elif a==2:
    p=4.50
elif a==3:
    p=5.00
elif a==4:
    p=2.00
elif a==5:
    p=1.50

print(f"Total: R$ {float(b*p):.2f}")

