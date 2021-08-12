#!/usr/bin/env python
# coding: utf-8

# # Operators in python

# In[1]:


# 1. Arithmetic operators
# 2. Assignments operators
# 3. Comparison operators
# 4. Logical operators
# 5. Identity operators
# 6. Membership opertors
# 7. Bitwise operators


# # Arithmetic operators

# In[23]:


#Arithmetic operators are used with numeric values to perform common mathematical operations:

print(5+6)
print(5-6)
print(5*6)
print(15//6)#floor divison gives integer value,not decimal value
print(2**6)#Exponential gives us multiple value
print(7%6) #modules operator gives us reminder


# # Assignments operators

# In[24]:


#Assignment operators are used to assign values to variables:

#Operator       #	Example         #	Same As
# =               	x = 5           	x = 5 
# +=              	x += 3          	x = x + 3 
# -=              	x -= 3          	x = x - 3 
# *=              	x *= 3          	x = x * 3
# /=              	x /= 3          	x = x / 3 
# %=              	x %= 3          	x = x % 3
# //=             	x //= 3         	x = x // 3 
# **=             	x **= 3         	x = x ** 3 
# &=              	x &= 3          	x = x & 3 
# |=              	x |= 3          	x = x | 3 
# ^=              	x ^= 3          	x = x ^ 3 
# >>=             	x >>= 3         	x = x >> 3 
# <<=             	x <<= 3         	x = x << 3


# In[25]:


# Example


# # Comparison operators

# In[26]:


#Comparison operators are used to compare two values:

# Operator      	Name                        	Example
# ==            	Equal                       	x == y 
# !=            	Not equal                   	x != y 
# >             	Greater than                	x > y 
# <             	Less than                   	x < y 
# >=            	Greater than or equal to    	x >= y 
# <=            	Less than or equal to       	x <= y


# # Logical operators (output will be in boolean value i.e, True & False)

# In[27]:


#Logical operators are used to combine conditional statements:

# Operator    	Description                                             	Example
# and         	Returns True if both statements are true                	x < 5 and  x < 10 
# or          	Returns True if one of the statements is true           	x < 5 or x < 4 
# not         	Reverse the result, returns False if the result is true 	not(x < 5 and x < 10)


# # Python Identity Operators

# In[28]:


#Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# Operator      	Description                                                 	Example 

# is            	Returns True if both variables are the same object          	x is y 
#is not         	Returns True if both variables are not the same object      	x is not y


# # Python Membership Operators

# In[30]:


#Membership operators are used to test if a sequence is presented in an object:

# Operator      	Description                                                                         	Example 
# in            	Returns True if a sequence with the specified value is present in the object        	x in y 
# not in        	Returns True if a sequence with the specified value is not present in the object    	x not in y


# # Python Bitwise Operators

# In[31]:


# Bitwise operators are used to compare (binary) numbers:

# Operator      	Name                    	Description
# &             	AND                     	Sets each bit to 1 if both bits are 1
# |             	OR                      	Sets each bit to 1 if one of two bits is 1
# ^             	XOR                     	Sets each bit to 1 if only one of two bits is 1
# ~             	NOT                     	Inverts all the bits
# <<            	Zero fill left shift    	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>            	Signed right shift      	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off


# In[ ]:




