#!/usr/bin/env python
# coding: utf-8

# # 1072

# In[18]:


t=int(input())
i=0
o=0
while t>0:
    t=t-1
    n=int(input())
    if n>=10 and n<=20:
        i=i+1
    else:
        o=o+1
print(f"{i} in")
print(f"{o} out")
    
        


# In[ ]:




