#!/usr/bin/env python
# coding: utf-8

# # FOR LOOP & WHILE LOOP

# In[8]:


# Example:Lets try iterating for loop with list-


# In[9]:


list1= ['harry','marry','larry']
for item in list1:
    print(item)


# In[ ]:


# Lets try to iteratting for loopwith tuple-


# In[10]:


list2= ('harry','marry','larry')
for item in list2:
    print(item)


# In[11]:


# but we cannot iterate all data type like list and tuple.


# In[12]:


# Lets have a another iteration with list.


# In[14]:


list3= [['harry',15],['marry',45],['larry',35]]
for item ,lollypop in list3:
    print(item,'number of lollypop',lollypop)


# In[16]:


# lets typecaste with dictonary and use for loop in it- 


# In[17]:


list3= [['harry',15],['marry',45],['larry',35]]
dict1=dict(list3)
print(dict1)


# In[ ]:


# in dict you have to use [.items()] fuction to iterate for loop:
# example-


# In[33]:


dict2={'harry': 15, 'marry': 45, 'larry': 35}
for item in dict2:
    print(item)


# In[30]:


dict2={'harry': 15, 'marry': 45, 'larry': 35}
for item,lollypop in dict2.items():
    print(item,'number of lollypop',lollypop)


# In[ ]:


# make a list with random name and numeric value and should print numeric value graeter than 6.


# In[58]:


list6=['harry',22,33,'rohan',78,5,4,'manoj']
for item in list6:
    if str(item).isnumeric() and item>=6:
     print(item)


# # WHILE LOOP

# In[59]:


# while loop run untile condition is satisfied-


# In[60]:


# Example-


# In[66]:


i=0
while (i<=20):
    print(i)
    i=i+1


# In[ ]:




