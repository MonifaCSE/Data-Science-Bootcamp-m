#!/usr/bin/env python
# coding: utf-8

# In[5]:


a,b,c=map(int,input().split())

if (a<=b and a<=c):
    l1=a
    if b<=c:
        l2=b
        l3=c
    else:
        l2=c
        l3=b
        
elif b<=a and b<=c:
    l1=b
    if a<=c:
        l2=a
        l3=c
    else:
        l2=c
        l3=a
else:
    l1=c
    if b<=a:
        l2=b
        l3=a
    else:
        l2=a
        l3=b
        
print(f"{l1}\n{l2}\n{l3}")
 

print(f"\n{a}\n{b}\n{c}")
    

