
# coding: utf-8

# In[ ]:


get_ipython().system('pip3 install kubernetes')


# In[ ]:


from kubernetes import client, config, watch


# In[ ]:


config.load_kube_config()


# In[ ]:


v1 = client.CoreV1Api()


# In[ ]:


ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print(f'{i.status.pod_ip} {i.metadata.namespace} {i.metadata.name}')

