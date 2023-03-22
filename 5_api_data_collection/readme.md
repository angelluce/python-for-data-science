# APIs and Data Collection

## Glossary

| Library, Property, or Method | Definition | Example |
| ---------------------------- | ---------- | ------- |
| Query String | A convention for appending key-value pairs to a URL. The question mark denotes separation between the URL and the string, the ampersand denotes the separation between the pairs, and the equal sign denotes the separation between the key and its value. | `https://www.ibm.com/analytics/db2?lnk=hpmps_bupr&lnk2=learn` |
| requests |  A python library that allows you to send HTTP/1.1 requests. | `import requests` |
| requests.get() |  Sends a GET request to a URL. Returns a requests.Response object. | `url=‘https://www.ibm.com’` </br> `r=requests.get(url)` |
| requests.headers | Check the server’s response headers. | `header=r.headers` |
| response.json() | Returns the response object as a Python dictionary. | `extractResp = response.json()` <br> `print(extractResp)` </br> `# output is:` </br> `# {` </br> `# "Course Live": true,` </br> `# "Course Name": "Python",` </br> `# "Paid Users": 239,` </br> `# "Total Users": 578` </br> `# }` |
| requests.post() | Posts data to a server in a request body. | `url_post='http://httpbin.org/post'` </br> `response=requests.post(url_post,data=payload)` | 
| response.status_code | Check the response status code | `r.status_code` |
| response.text | Returns the response as a string | `r.text[0:100]` |
