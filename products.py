#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json

fd = open('record.json', 'r')
txt = fd.read()
fd.close()

record = json.loads(txt)

prod_id = input("enter product id:")
name = input("Enter the product name:")
pr = int(input("enter the product price:"))
qn = int(input("Enter quantity:"))
record[prod_id] = {'name':name,'pr': pr,'qn':qn}


# In[2]:


record


# In[17]:


prod_id = input("enter product id:")
name = input("Enter the product name:")
pr = int(input("enter the product price:"))
qn = int(input("Enter quantity:"))
record[prod_id] = {'name':name,'pr': pr,'qn':qn}


# In[18]:


record


# In[19]:


js = json.dumps(record)
fd = open("record.json",'w')
fd.write(js)
fd.close()


# # purchase

# In[22]:


ui_prod = input("enter the prod_id")
ui_quant = int(input("enter the quantity"))

print("products:", record[ui_prod]['name'])
print("price:", record[ui_prod]['pr'])
print("Billing amount:", record[ui_prod]['pr']*ui_quant)

record[ui_prod]['qn'] = record[ui_prod]['qn']-ui_quant


# In[23]:


record


# In[ ]:




