#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


url='https://www.flipkart.com/search?q=oneplus%20mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'


# In[3]:


r=requests.get(url)
r.status_code


# In[4]:


print(r.text)


# In[5]:


soup=BeautifulSoup(r.content,'lxml')
soup


# In[6]:


print(soup.prettify())


# In[7]:


soup.title


# In[8]:


soup.title.string


# In[9]:


soup.div


# In[10]:


soup.a


# In[11]:


soup.find_all('a')


# In[12]:


all_link=soup.find_all('a')
for r in all_link:
    print(r.get('href'))


# In[13]:


all_tables=soup.find_all('table')
print(all_tables)


# In[14]:


print(soup.prettify())


# In[15]:


model=soup.findAll('div',{'class':'_4rR01T'})


# In[16]:


model


# In[17]:


productname=[]
for i in model:
    p=i.text
    productname.append(p)
    
print(productname)


# In[18]:


prices=soup.findAll('div',{'class':'_30jeq3 _1_WHN1'})
prices


# In[19]:


r=soup.findAll('div',{'class':'_3LWZlK'})
rating=[]
for i in r:
    ra=i.text
    rating.append(ra)
    
print(rating)


# In[20]:


len(rating)


# In[21]:


len(prices)


# In[22]:


len(model)


# In[23]:


rating=rating[0:24]
rating


# In[24]:


len(productname)


# In[25]:


import pandas as pd
d={'product':productname,'price':prices,'rating':rating}
data=pd.DataFrame(d)
data


# In[ ]:




