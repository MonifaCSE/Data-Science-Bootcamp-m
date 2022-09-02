#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a,b,c=map(float,input().split())

TRIANGULO=.5 * a * c
CIRCULO=3.14159 * c * c
TRAPEZIO=0.5 * (a+b) * c
QUADRADO= b * b
RETANGULO=a * b

print(f"TRIANGULO: {TRIANGULO:0.3f}")
print(f"CIRCULO: {CIRCULO:0.3f}")
print(f"TRAPEZIO: {TRAPEZIO:0.3f}")
print(f"QUADRADO: {QUADRADO:0.3f}")
print(f"RETANGULO: {RETANGULO:0.3f}")

