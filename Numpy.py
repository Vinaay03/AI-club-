#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


#simplest way to create an array is to use python list
mypythonlist = [123,345,567]
print(mypythonlist)


# In[4]:


#to convert python list to an array by using the obeject np.array
numpy_array_from_list = np.array(mypythonlist)
numpy_array_from_list


# In[5]:


a = np.array([1,6,7,5,3])
print(a)


# In[6]:


y=numpy_array_from_list +10
print(y)


# In[7]:


a = np.array([1,2,3,4])
print(a.shape)
print(a.dtype)


# In[10]:


### different type
b= np.array([1.2,2.3,3.4,5.6])
print(b.dtype)


# In[11]:


## 2dimension
c = np.array([(1,2,3),
              (4,5,6)])
print(c)


# In[16]:


# 3 dimension
d = np.array([
    [[1,2,3],
       [4,5,6]],
    [[7,8,9],
       [10,11,12]]
     
])
print(d.shape)
(2,2,3)
print(d)


# In[20]:


import numpy as np
x=np.zeros((2,2), dtype=np.int16)
print(x)


# In[21]:


import numpy as np
y=np.ones((1,2,3), dtype=np.int16)
print(y.shape)
print(y)


# In[22]:


#reshape data
import numpy as np
e = np.array([(1,2,3),(4,5,6)])
print(e)
e.reshape(3,2)


# In[23]:


e.flatten()


# In[24]:


#horizontal stack
import numpy as np
f = np.array([1,2,3])
g = np.array([4,5,6])

print('Horizontal append:',np.hstack((f,g)))


# In[25]:


##vertical stack
import numpy as np
f = np.array([1,2,3])
g = np.array([4,5,6])

print('Vertical Append:', np.vstack((f,g)))


# In[26]:


##generating random numbers
normal_array = np.random.normal(6,0.6,12)
print(normal_array)


# In[27]:


A = np.matrix(np.ones((4,4)))
print(A)


# In[28]:


np.asarray(A)[2]=2
print(A)


# In[30]:


np.arange(1,11)


# In[31]:


np.arange(1,14,4)


# In[ ]:




