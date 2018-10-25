Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:22:17) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
========= RESTART: C:\Users\Administrator\Desktop\cramb\getTrain.py =========

Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\cramb\getTrain.py", line 56, in <module>
    html=get_html(nurl)
  File "C:\Users\Administrator\Desktop\cramb\getTrain.py", line 30, in get_html
    req = requests.get(url, headers=heads)
  File "C:\Python27\lib\site-packages\requests-2.8.1-py2.7.egg\requests\api.py", line 69, in get
    return request('get', url, params=params, **kwargs)
  File "C:\Python27\lib\site-packages\requests-2.8.1-py2.7.egg\requests\api.py", line 50, in request
    response = session.request(method=method, url=url, **kwargs)
  File "C:\Python27\lib\site-packages\requests-2.8.1-py2.7.egg\requests\sessions.py", line 468, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Python27\lib\site-packages\requests-2.8.1-py2.7.egg\requests\sessions.py", line 576, in send
    r = adapter.send(request, **kwargs)
  File "C:\Python27\lib\site-packages\requests-2.8.1-py2.7.egg\requests\adapters.py", line 423, in send
    raise ConnectionError(e, request=request)
ConnectionError: HTTPConnectionPool(host='www.jt2345.com', port=80): Max retries exceeded with url: /huoche/checi/D2998.htm (Caused by NewConnectionError('<requests.packages.urllib3.connection.HTTPConnection object at 0x045F5F70>: Failed to establish a new connection: [Errno 10060] ',))
>>> 
