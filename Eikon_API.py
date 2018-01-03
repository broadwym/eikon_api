
# coding: utf-8

# In[ ]:


#Import the eikon library (import eikon as ek) and input your unique alphanumeric Eikon app token ('your alphanumeric token').
#These are example Eikon API calls using Starbucks (SBUX.O)


# In[ ]:


import eikon as ek


# In[ ]:


ek.set_app_id('your alphanumeric token')


# In[ ]:


ek.get_timeseries("SBUX.O", fields='*')


# In[ ]:


ek.get_data("SBUX.O", fields = ["CF_HIGH", "CF_LOW"],  parameters=None)


# In[ ]:


ek.get_data("SBUX.O", ['TR.Employees', {'TR.GrossProfit':{'params':{'Scale': 6, 'Curn': 'EUR'},'sort_dir':'asc'}}])


# In[ ]:


ek.get_news_headlines("SBUX.O", date_from='2017-01-05T09:00:00', date_to='2017-04-05T18:00:00')

