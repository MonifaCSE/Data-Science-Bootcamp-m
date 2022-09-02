#!/usr/bin/env python
# coding: utf-8

# In[10]:


sh,sm,eh,em=map(int,input().split())

d=((eh*60)+em)-((sh*60)+sm)
if(d<=0):
    d+=24*60
    
h=d//60
m=d%60
 
print(f"O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)")

