from requests_tor import RequestsTor
from bs4 import BeautifulSoup
import random
from dotenv import dotenv_values

config = dotenv_values(".env") 


useragentlist = [
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

dkforest_url = 'http://dkforestseeaaq2dqz2uflmlsybvnq2irzn4ygyvu53oazyorednviid.onion'
breach_url = "http://breachedu76kdyavc6szj6ppbplfqoz3pgrk3zw57my4vybgblpfeayd.onion/"

#got csrf
beginpage_dk = rt.get(dkforest_url)
soup = BeautifulSoup(beginpage_dk.content, "html.parser")
csrfToken_dk = soup.findAll(attrs={'name':'csrf'})[0]['value']
print(csrfToken_dk)

usernames_dk = ["singlemomof1","singlemomof2","singlemomof3","singlemomof4","singlemomof5","singlemomof6"]

print(config)

passwd_dk = config['DKFOREST_PASSWORD']

#got auth token
login_data_dk = {
    'csrf': csrfToken_dk,
    'username': random.choice(usernames_dk),
    'password': passwd_dk
}
login_cookie_dk ={
    "_csrf":csrfToken_dk
}
headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-GB,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Origin': 'http://dkforestseeaaq2dqz2uflmlsybvnq2irzn4ygyvu53oazyorednviid.onion',
        'Referer': 'http://dkforestseeaaq2dqz2uflmlsybvnq2irzn4ygyvu53oazyorednviid.onion/',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': random.choice(useragentlist)
}
loginpage_dk = rt.post(dkforest_url, data=login_data_dk, cookies=login_cookie_dk, headers=headers)

if(loginpage_dk.ok):
    print("login success")
    print(loginpage_dk.headers)
    print(loginpage_dk.cookies)
    print(loginpage_dk.request.headers)
else:
    print("login failed")
    exit()

#got auth token
auth_token_dk = loginpage_dk.request.headers['Cookie'].split('=')[2]
print(auth_token_dk)

# using cookie goto a forum
webpage_cookie_dk = {
    "_csrf":csrfToken_dk,
    "auth-token":auth_token_dk
}


#currently sending back to login page.. how do iget the auth-token??
dkforest_forums = "http://dkforestseeaaq2dqz2uflmlsybvnq2irzn4ygyvu53oazyorednviid.onion/forum"
dkforest_chat = "http://dkforestseeaaq2dqz2uflmlsybvnq2irzn4ygyvu53oazyorednviid.onion/chat"
dkforest_samplepost1 = "http://dkforestseeaaq2dqz2uflmlsybvnq2irzn4ygyvu53oazyorednviid.onion/t/2593c5d0-c638-415a-861b-8fb6210d6fdb"
dkforest_samplepost2 = "http://dkforestseeaaq2dqz2uflmlsybvnq2irzn4ygyvu53oazyorednviid.onion/t/9025994c-2880-4f63-9504-c8a9846019a2"

postlist_dk = rt.get(dkforest_samplepost1,headers=headers,cookies=webpage_cookie_dk)
print(postlist_dk.status_code)
postlist_dk = rt.get(dkforest_samplepost2,headers=headers,cookies=webpage_cookie_dk)
print(postlist_dk.status_code)

with open('sampplepost.html', 'w') as f:
    f.write(postlist_dk.text)

