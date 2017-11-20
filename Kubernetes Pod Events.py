
# coding: utf-8

# In[1]:


get_ipython().system('pip3 install kubernetes')


# In[2]:


from kubernetes import client, config, watch


# In[3]:


config.load_kube_config()


# In[4]:


v1 = client.CoreV1Api()


# In[5]:


ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print(f'{i.status.pod_ip} {i.metadata.namespace} {i.metadata.name}')


# In[8]:


count = 1
w = watch.Watch()
for event in w.stream(v1.list_pod_for_all_namespaces, _request_timeout=300):
    print(f'{event}')
    count -= 1
    if not count:
        w.stop()

