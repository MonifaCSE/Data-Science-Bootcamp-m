#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a,b,c=map(int,input().split())



ab=(a+b+abs(a-b))/2
ABC=int((ab+c+abs(ab-c))/2)

print(f"{ABC} eh o maior")

