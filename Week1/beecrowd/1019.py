#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())

h=int(n/3600)
n=n%3600
m=int(n/60)
s=n%60

print(f"{h}:{m}:{s}")

