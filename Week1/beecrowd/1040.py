#!/usr/bin/env python
# coding: utf-8

# # 1040

# In[3]:


a,b,c,d=map(float,input().split())

a = (a*2+b*3+c*4+d*1)/10

print(f"Media: {a:.1f}")
      
if  a>=7.0:
    print("Aluno aprovado.")
elif a<5.0:
    print("Aluno reprovado.")
elif a>=5.0 and a<7.0:
    print("Aluno em exame.")
    n= float(input())
    print(f"Nota do exame: {n:.1f}")
    n= (a+n)/2
    if n>=5.0:
        print("Aluno aprovado.")
        print(f'Media final: {n:.1f}')
    else:
        print("Aluno reprovado.")
        print(f"Media final: {n:.1f}")


# In[ ]:




