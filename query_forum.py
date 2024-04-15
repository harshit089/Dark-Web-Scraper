from requests_tor import RequestsTor
from bs4 import BeautifulSoup
import random

USERAGENT_LIST = [
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0) chromeframe/10.0.648.205',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_0) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101213 Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2',
        'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
        'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; chromeframe/11.0.696.57)',
        'Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36',
        'Opera/9.80 (X11; Linux i686; U; ja) Presto/2.7.62 Version/11.01',
        'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
        'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; ja) Opera 11.00'
        ]

rt = RequestsTor(tor_ports=(9050,9052,9054,9056,9058,9060), tor_cport=9051,autochange_id=2)

query_home = "http://ruc4i7xn5qu5uc7fu2sc34r6xl55xhgvxbcs56t4ayvbqo2fmp4pehqd.onion/"

headers = {
    'Host':'ruc4i7xn5qu5uc7fu2sc34r6xl55xhgvxbcs56t4ayvbqo2fmp4pehqd.onion',
    'User-Agent': random.choice(USERAGENT_LIST),
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language':'en-US,en;q=0.5',
    'Accept-Encoding':'gzip, deflate, br',
    'Connection':'keep-alive',
    # 'Cookie':' PHPSESSID=2tp1s3llsegotpemn96efuad7l; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-04-15%2016%3A40%3A49%7C%7C%7Cep%3Dhttp%3A%2F%2Fruc4i7xn5qu5uc7fu2sc34r6xl55xhgvxbcs56t4ayvbqo2fmp4pehqd.onion%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-04-15%2016%3A40%3A49%7C%7C%7Cep%3Dhttp%3A%2F%2Fruc4i7xn5qu5uc7fu2sc34r6xl55xhgvxbcs56t4ayvbqo2fmp4pehqd.onion%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%3B%20rv%3A109.0%29%20Gecko%2F20100101%20Firefox%2F115.0; sbjs_session=pgs%3D12%7C%7C%7Ccpg%3Dhttp%3A%2F%2Fruc4i7xn5qu5uc7fu2sc34r6xl55xhgvxbcs56t4ayvbqo2fmp4pehqd.onion%2F; ia3rfv5poAi7NdHwpqa_meta_stats1358=wpqa_meta_stats; ia3rfv5poAi7NdHwpqa_meta_stats1105=wpqa_meta_stats; ia3rfv5poAi7NdHwpqa_meta_stats1214=wpqa_meta_stats; ia3rfv5poAi7NdHwpqa_meta_stats482=wpqa_meta_stats
    'Upgrade-Insecure-Requests':'1',
    'Sec-Fetch-Dest':'document',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'cross-site'
}

home = rt.get(query_home, headers=headers)
with open("query_home.html", "w") as f:
    f.write(home.text)

post_link ="http://ruc4i7xn5qu5uc7fu2sc34r6xl55xhgvxbcs56t4ayvbqo2fmp4pehqd.onion/question/send-usdt-almost-free-with-tron-energy-marketplace/"
post = rt.get(post_link, headers=headers)
with open("post_query.html", "w") as f:
    f.write(post.text)

next_page="http://ruc4i7xn5qu5uc7fu2sc34r6xl55xhgvxbcs56t4ayvbqo2fmp4pehqd.onion/page/2/"
next = rt.get(next_page, headers=headers)
with open("next_query.html", "w") as f:
    f.write(next.text)