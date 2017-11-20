
# coding: utf-8

# In[1]:


import numpy
numpy.__version__


# In[2]:


import numpy as np


# In[4]:


L = list(range(10))
L


# In[5]:


type(L[0])


# In[6]:


L2 = [str(c) for c in L]
L2


# In[7]:


type(L2[0])


# In[8]:


L3 = [True, "2", 3.0, 4]
[type(item) for item in L3]


# In[9]:


import array
L = list(range(10))
A = array.array('i', L)
A


# In[10]:


np.array([1,4,2,5,3])


# In[11]:


np.array([ 3.14, 4, 2, 3])


# In[12]:


np.array([1, 2, 3, 4], dtype='float32')


# In[13]:


# nested lists result in multidimensional arrays
np.array([range(i, i + 3) for i in [2, 4, 6]])


# In[14]:


# create a length-10 integer array filled with zeros
np.zeros(10, dtype=int)


# In[15]:


# create a 3x5 floating-point array filled with 1s
np.ones((3,5), dtype=float)


# In[16]:


# create a 3x5 array filled with 3.14
np.full((3,5), 3.14)


# In[18]:


# create an array filled with a linear sequence
# starting at 0, ending at 20, stepping by 2
# (this is similar to the built-in range() function)
np.arange(0, 20, 2)


# In[19]:


# create an array of five values evenly spaced between 0 and 1
np.linspace(0, 1, 5)


# In[20]:


# create a 3x3 array of uniformly distributed
# random values between 0 and 1
np.random.random((3,3))


# In[21]:


# create a 3x3 array of normally distributed random values
# with mean 0 and std dev 1
np.random.normal(0, 1, (3, 3))


# In[23]:


# create a 3x3 array of random integers in the interval (0, 10)
np.random.randint(0, 10, (3, 3))


# In[24]:


# create a 3x3 identity matrix
np.eye(3)


# In[25]:


# create an uninitialised array of three integers
# the values will be whatever happens to already exist at that
# memory location
np.empty(3)


# In[27]:


np.zeros(10, dtype='int16')
np.zeros(10, dtype=np.int16)


# In[28]:


np.random.seed(0) # seed for reproducibility

x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(3,4))
x3 = np.random.randint(10, size=(3,4,5))


# In[29]:


print(f'{x3.ndim}')
print(f'{x3.shape}')
print(f'{x3.size}')


# In[30]:


print(f'{x3.dtype}')


# In[31]:


print(f'{x3.itemsize}')
print(f'{x3.nbytes}')


# In[32]:


x1


# In[33]:


x1[0]


# In[34]:


x1[4]


# In[35]:


x1[-1]


# In[36]:


x1[-2]


# In[37]:


x2


# In[38]:


x2[0,0]


# In[39]:


x2[2,0]

