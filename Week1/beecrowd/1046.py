#!/usr/bin/env python
# coding: utf-8

# In[9]:


a,b=map(int,input().split())

if a>b:
    d=(24-a)+b
elif a<b:
    d=b-a
elif a==b:
    d=24
print(f"O JOGO DUROU {d} HORA(S)")


# In[ ]:




