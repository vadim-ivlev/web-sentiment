#%%

import requests

r = requests.get('http://docs.python-requests.org/en/master/user/quickstart/#make-a-request')

print(r.text)

r.close()




#%% this is a new cell

from requests_html import HTMLSession

session = HTMLSession()
r = session.get('http://docs.python-requests.org/en/master/user/quickstart/#make-a-request')
for link in r.html.absolute_links:
    print(link)
r.close()



#%%
