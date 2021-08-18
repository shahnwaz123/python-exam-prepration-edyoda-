#!/usr/bin/env python
# coding: utf-8

# In[1]:


# there are two type of function-
# 1. builtin function
# 2. user define function


# In[2]:


# example of builtin function-


# In[7]:


a=15
b=20
c=sum((a,b))
print(c)


# In[8]:


# Example of user define function-


# In[4]:


def function_example():
    print('hello world')

function_example()


# In[5]:


# lets try to add two values with fumction:


# In[12]:


def add(a,b):
    c=a+b
    print(c)

add(7,5)


# In[13]:


# Example of return function:


# In[16]:


def add(a,b):
    c=a+b
    return c

result=add(5,7)
print(result)


# In[17]:


# examlle of running two fuction at a time:


# In[19]:


def add_sub(a,b):
    x=a+b
    y=a-b
    return x,y

result1,result2=add_sub(6,5)
print(result1,result2)


# In[ ]:




