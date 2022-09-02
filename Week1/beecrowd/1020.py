#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = int(input())

y=int(a/365)
a=a%365
m=int(a/30)
d=a%30
 
print(f"{y} ano(s)\n{m} mes(es)\n{d} dia(s)")

