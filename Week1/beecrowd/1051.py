#!/usr/bin/env python
# coding: utf-8

# # 1051

# In[11]:


c=float(input())
 
if c>=0 and c<=2000:
    print("Isento")
elif c>=2000.01 and c<=3000:
    c=c-2000
    b= c*.08
    print(f"R$ {b:0.2f}")
elif c>=3000.01 and c<=4500:
    c=c-3000
    b=c*.18+80
    print(f"R$ {b:.2f}")
else:
       c=c-4500
       b= c*.28+350
       print(f"R$ {b:0.2f}")


# In[ ]:




