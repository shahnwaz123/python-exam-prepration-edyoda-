#!/usr/bin/env python
# coding: utf-8

# # variables in python

# In[7]:


# VAriable is nothing but a container that contain data.


# In[8]:


# Example:


# In[9]:


var1="hello world"
print(var1)

# here var1 is a variable which contain string data thet is hello world.


# # Data type in python

# In[12]:


var1=6
var2=7.5
var3='hello'
var4=True


# In[13]:


print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))


# In[14]:


# Contatinate of two data type.


# In[15]:


var1+var2


# In[17]:


var3+var1


# In[18]:


# we cant concatiante string with int or float value.thats why we can use type casting.


# # Data typecasting

# In[19]:


# it is a process of changing one data type two another data type.
# Example:


# In[31]:


a="32"
b="95"
print(a,b)


# In[32]:


# after typecasting


# In[33]:


print(int(a)+int(b))


# In[34]:


# we have various type of typecastint function.

#1. str()
#2. float()
#3. int()


# In[35]:


# how to print an object in 10 time.


# In[40]:


print("hello world\n"*10)


# In[41]:


#If we want to print 10 times with a integer value then we have to convert it first into string.
# example-


# In[49]:


c=10
d=5
print(10*str(c+d))


# In[50]:


# How to take input from user by using input function:


# In[57]:


# Lets creat an input which add 10 automatically


# In[58]:


"entered your number"
a=(input())
print("your number is",int(a)+10)


# In[59]:


# quiz- make  a simple calculator which multiply two numbers:


# In[61]:


"enter your first number"
a=input()
"entered your second number"
b=input()
print("your answer is ",int(a)*int(b))


# In[ ]:




