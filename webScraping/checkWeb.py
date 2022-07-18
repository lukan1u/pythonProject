import requests

# r = requests.get('https://www.google.com/')
# r = requests.post('https://httpbin.org/post', data={'key': 'value'})

# # page status 200 means ok
# # page status 404 means page not found or offline

# r = requests.put('https://httpbin.org/put', data={'key': 'value'})
# r = requests.delete('https://httpbin.org/delete')


payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.status_code)
print(r.url)
