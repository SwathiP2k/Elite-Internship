#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json

fd = open('record.json', 'r')
txt = fd.read()
fd.close()

record = json.loads(txt)

ui_prod = input("enter the prod_id")
ui_quant = int(input("enter the quantity"))

print("products:", record[ui_prod]['name'])
print("price:", record[ui_prod]['pr'])
print("Billing amount:", record[ui_prod]['pr']*ui_quant)

record[ui_prod]['qn'] = record[ui_prod]['qn']-ui_quant


# In[2]:


js = json.dumps(record)
fd = open("record.json",'w')
fd.write(js)
fd.close()


# In[3]:


record


# # sales
# 

# In[4]:


{'prod':ui_prod,'qn':ui_quant,'amount':record[ui_prod]['pr']*ui_quant}


# In[5]:


sales = {1:{'prod':ui_prod,'qn':ui_quant,'amount':record[ui_prod]['pr']*ui_quant},
        2:{'prod':ui_prod,'qn':ui_quant,'amount':record[ui_prod]['pr']*ui_quant},
        3:{'prod':ui_prod,'qn':ui_quant,'amount':record[ui_prod]['pr']*ui_quant}
        }


# In[6]:


sale = json.dumps(sales)
fd = open("record.json",'w')
fd.write(sale)
fd.close()


# In[7]:


sale


# In[ ]:




