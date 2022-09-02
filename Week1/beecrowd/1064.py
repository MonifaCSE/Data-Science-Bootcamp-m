#!/usr/bin/env python
# coding: utf-8

# # 1064

# In[1]:


n=6
i=0
s=0
while n>0:
    n=n-1
    v=input()
    if v[0]!='-':
        i=i+1
        s=s+float(v)
print(f"{i} valores positivos")
print(f"{s/i:0.1f}")

        


# In[ ]:




