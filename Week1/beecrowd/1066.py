#!/usr/bin/env python
# coding: utf-8

# # 1066

# In[3]:


n=5
e=0
o=0
p=0
ne=0

while n>0:
    n=n-1
    v=int(input())
    if v%2==0:
        e=e+1
    if v%2!=0:
        o=o+1
    if v>0:
        p=p+1
    if v<0:
        ne=ne+1
        

print(f"{e} valor(es) par(es)")
print(f"{o} valor(es) impar(es)")
print(f"{p} valor(es) positivo(s)")
print(f"{ne} valor(es) negativo(s)")

        


# In[ ]:




