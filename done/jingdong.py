import requests
def sina():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv4277&productId=8790545&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&rid=0&fold=1'
    html = requests.get(url,headers=headers)
    print(html.text)

sina()
