import requests
def sina():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    url = 'https://m.weibo.cn/comments/hotflow?id=4280123584809974&mid=4280123584809974&max_id=168241767636061&max_id_type=0'
    html = requests.get(url,headers=headers)
    print(html.text)

sina()
