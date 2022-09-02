#!/usr/bin/env python
# coding: utf-8

# # 1070

# In[7]:


n=int(input())
j=0
for i in range(n,100):
    if j==6:
        break
    if i%2!=0:
        j=j+1
        print(i)
    
        


# In[ ]:




