from pymongo import MongoClient
from dotenv import dotenv_values
from requests_tor import RequestsTor
from bs4 import BeautifulSoup
from datetime import datetime
import random
from texttable import Texttable
import time
import threading
import sys

config = dotenv_values(".env") 

try:
    client = MongoClient("mongodb+srv://littleBob:" + config["MONGODB_PASSWORD"] + "@cluster0.z3ehy3o.mongodb.net/")
    db = client["DarkWebDB"]
    post_headers = db["PostHeaders"]
    post_contents = db["PostContents"]
except Exception as e:
    print("Error connecting to MongoDB. Please check the connection and try again.")
    exit()

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

rt = RequestsTor(tor_ports=(9050,9052,9054,9056,9058,9060), tor_cport=9051,autochange_id=1)


dkforest_url = 'http://dkforestseeaaq2dqz2uflmlsybvnq2irzn4ygyvu53oazyorednviid.onion'
hidden_answr = "http://lp2fkbyfmiefvscyawqvssyh7rnwfjsifdhebp5me5xizte3s47yusqd.onion/"
query_home = "http://ruc4i7xn5qu5uc7fu2sc34r6xl55xhgvxbcs56t4ayvbqo2fmp4pehqd.onion/"

usernames_dk = ["singlemomof1","singlemomof2","singlemomof3","singlemomof4","singlemomof5"]

headers_dk = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-GB,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Origin': 'http://dkforestseeaaq2dqz2uflmlsybvnq2irzn4ygyvu53oazyorednviid.onion',
    'Referer': 'http://dkforestseeaaq2dqz2uflmlsybvnq2irzn4ygyvu53oazyorednviid.onion/',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': random.choice(USERAGENT_LIST)
}

headers_hiddenans = {
    'Host': 'lp2fkbyfmiefvscyawqvssyh7rnwfjsifdhebp5me5xizte3s47yusqd.onion',
    'User-Agent': random.choice(USERAGENT_LIST),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1'
}

headers_query = {
    'Host':'ruc4i7xn5qu5uc7fu2sc34r6xl55xhgvxbcs56t4ayvbqo2fmp4pehqd.onion',
    'User-Agent': random.choice(USERAGENT_LIST),
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language':'en-US,en;q=0.5',
    'Accept-Encoding':'gzip, deflate, br',
    'Connection':'keep-alive',
    'Upgrade-Insecure-Requests':'1',
    'Sec-Fetch-Dest':'document',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'cross-site'
}


def prepare_dk_users(usernames_dk):
    dk_users = []
    passwd_dk = config['DKFOREST_PASSWORD']

    for user in usernames_dk:
        beginpage_dk = rt.get(dkforest_url)
        soup = BeautifulSoup(beginpage_dk.content, "html.parser")
        csrfToken_dk = soup.findAll(attrs={'name':'csrf'})[0]['value']

        login_data_dk = {
            'csrf': csrfToken_dk,
            'username': user,
            'password': passwd_dk,
            'session_duration':"2592000"
        }
        login_cookie_dk ={
            "_csrf":csrfToken_dk
        }
        loginpage_dk = rt.post(dkforest_url, data=login_data_dk, cookies=login_cookie_dk, headers=headers_dk)
        auth_token_dk = loginpage_dk.request.headers['Cookie'].split('=')[2]

        dk_users.append({
            'username':user,
            "_csrf":csrfToken_dk,
            "auth-token":auth_token_dk
        })
        # print(f"User {user} prepared")
    
    return dk_users


def parser_darkfor_home(string):
    soup = BeautifulSoup(string, 'html.parser')
    namej, linkj, authorj, up_timej = ([] for _ in range(4))
    names = soup.findAll('td', style = 'vertical-align: middle;')
    i = 0
    for name in names:
        if(i%2 == 0):
            namej.append(name.a.get_text())
        i = i+1

    i = 0
    for link in names:
        if(i%2 == 0):
            linkj.append(link.a['href'])
        i = i+1

    persons = soup.find_all('a', {'style': True, 'href': True})
    i = 0
    for author in persons:
        if(i%2==1):
            authorj.append(author.get_text())
        i = i + 1

    times = soup.findAll('span', class_ = 'timestamp')
    i = 0
    for up_time in times:
        if(i%2 == 0):
            up_timej.append(datetime.strptime(up_time.get_text(), "%b %d, %Y %H:%M:%S"))
        i = i + 1

    data = []
    for name, link,  author, up_time in zip(namej, linkj, authorj,  up_timej):
        entry = {
            "_id": link,
            "site":"Darkforest",
            "name": name,
            "link": dkforest_url + link,
            "author": author,
            "upload_time": up_time
        }
        data.append(entry)

    return data

def parser_hidden_ans_home(string):
    soup = BeautifulSoup(string, 'html.parser')
    likej, dlikej, quesj, qlinkj, qaj, alinkj, timej, catj, personj, linkj = [[] for _ in range(10)]

    items = soup.findAll('div', class_ = "qa-q-list-item")
    for item in items:
        likej.append(int(item.find('span', class_ = "qa-upvote-count-data").text))
        dlikej.append(int(item.find('span', class_ = "qa-downvote-count-data").text))
        quesj.append(item.find('div', class_ = "qa-q-item-title").a.get_text())
        qlinkj.append(item.find('div', class_ = "qa-q-item-title").a['href'])
        tag = item.find('a', class_ = "qa-q-item-what")
        qaj.append(item.find('span', class_ = "qa-q-item-meta").get_text().split()[0])
        if(item.find('span', class_ = "qa-q-item-meta").get_text().split()[0] == 'answered'):
            alinkj.append(tag['href'])
        else:
            alinkj.append(None)
        timej.append(item.find('span', class_ = "qa-q-item-when-data").get_text())
        catj.append(item.find('a', class_ = "qa-category-link").get_text())
        personj.append(item.find('a', class_ = "qa-user-link").get_text())
        listaa = []
        lins = item.findAll('a', class_ = "qa-tag-link")
        for lin in lins:
            listaa.append(lin['href'])
        linkj.append(listaa)

    data = []
    for c1, c2, c3, c4, c5, c6, c7, c8, c9, c10 in zip(likej, dlikej, quesj, qlinkj, qaj, alinkj, timej, catj, personj, linkj):
        entry = {
            "_id":c4,
            "site":"Hidden Answers",
            "name": c3,
            "link": hidden_answr[:-2] + c4[2:],
            "author": c9,
            "upload_time": c7,
        }
        data.append(entry)

    return data


def parser_hidden_answer_post(string,post_link):
    # print(post_link)
    soup = BeautifulSoup(string, 'html.parser')
    namej, msgj, timej = ([] for _ in range(3))

    msgs = soup.findAll('div', itemprop="text")
    for msg in msgs:
        msgj.append(msg.get_text())

    names = soup.findAll('span', itemprop = "name")
    i = 0
    for name in names:
        if(i == 0):
            i = 1
            continue
        namej.append(name.get_text())

    times = soup.findAll('time', itemprop="dateCreated")
    for time in times:
        timej.append(datetime.strptime(time['title'].replace('T', ' ')[:-5], "%Y-%m-%d %H:%M:%S"))

    data = []
    for name, msg, time in zip(namej, msgj, timej):
        entry = {
            "_id": msg,
            "site":"Hidden Answers",
            "link": post_link,
            "username": name,
            "msg" : msg,
            "date&time" : time
        }
        data.append(entry)

    return data

def parser_darkfor_post(string,link):
    # print(link) 
    soup = BeautifulSoup(string, 'html.parser')
    namej, datej, msgj = ([] for _ in range(3))

    details = soup.findAll('div', style = 'flex: 1;')
    i = 0
    for detail in details:
        if(i%2==0):
            namej.append(detail.a.get_text())
        else:
            datej.append(datetime.strptime(detail.a.get_text(), "%b %d, %Y %H:%M:%S"))
        i=i+1

    msgs = soup.findAll('div', style = "padding: 5px 5px 10px 10px;")
    for msg in msgs:
        paras = msg.findAll('p')
        ms = ""
        for para in paras:
            ms = ms + para.get_text()
        msgj.append(ms)

    data = []
    for name, date, msg in zip(namej, datej, msgj):
        entry = {
            "_id": msg,
            "site": "Darkforest",
            "link": link,
            "username": name,
            "msg" : msg,
            "date&time" : date
        }
        data.append(entry)

    return data


def full_crawler():
    print("Crawling...")
    sys.stdout.flush()
    dk_users = prepare_dk_users(usernames_dk)
    # get data from darkforest,random user
    user = random.choice(dk_users)
    webpage_cookie_dk = {
        "_csrf":user['_csrf'],
        "auth-token":user['auth-token']
    }
    forum_page = rt.get(dkforest_url+"/forum", cookies=webpage_cookie_dk, headers=headers_dk)

    #parse using function
    darkfor_home_data = parser_darkfor_home(forum_page.text)
    #store in mongodb
    try:
        post_headers.insert_many(darkfor_home_data)
    except Exception as e:
        # print(e)
        pass

    #use the links in the data received to generate post links
    for entry in darkfor_home_data:
        post_link = entry["link"]
        user = random.choice(dk_users)
        post_page = rt.get(post_link, cookies={"_csrf":user['_csrf'],"auth-token":user['auth-token']}, headers=headers_dk)
        post_data = parser_darkfor_post(post_page.text, post_link)
        try:
            post_contents.insert_many(post_data)
        except Exception as e:
            # print(e)
            pass
        
    #use all the post links to get the post data,put to parser and store in mongodb

    #repeat for hidden answers
    hidden_ans_np ="http://lp2fkbyfmiefvscyawqvssyh7rnwfjsifdhebp5me5xizte3s47yusqd.onion/index.php/questions?start="
    for i in range(94):
        # print(i)
        hidden_answr_tmp = hidden_ans_np + str(i*20)
        hidden_answr_home = rt.get(hidden_answr_tmp, headers=headers_hiddenans)
        hidden_answr_home_data = parser_hidden_ans_home(hidden_answr_home.text)

        try:
            post_headers.insert_many(hidden_answr_home_data)
        except Exception as e:
            # print(e)
            pass


        for entry in hidden_answr_home_data:
            post_link = entry["link"]
            post_page = rt.get(post_link, headers=headers_hiddenans)
            post_data = parser_hidden_answer_post(post_page.text, post_link)
            try:
                post_contents.insert_many(post_data)
            except Exception as e:
                # print(e)
                pass

# full_crawler()

def SearchBarIntro():
    
    banner = '''
 ______              _             _  _  _       _         ______                                           
(______)            | |           (_)(_)(_)     | |       / _____)                                          
 _     _ _____  ____| |  _  _____  _  _  _ _____| |__    ( (____   ____  ____ _____ ____  ____  _____  ____ 
| |   | (____ |/ ___) |_/ |(_____)| || || | ___ |  _ \    \____ \ / ___)/ ___|____ |  _ \|  _ \| ___ |/ ___)
| |__/ // ___ | |   |  _ (        | || || | ____| |_) )   _____) | (___| |   / ___ | |_| | |_| | ____| |    
|_____/ \_____|_|   |_| \_)        \_____/|_____)____/   (______/ \____)_|   \_____|  __/|  __/|_____)_|    
                                                                                   |_|   |_|                                                                                                                                                   
    '''
    print(banner)
    print("Search through what's happening in the dark side of the internet...\n\n")

def SearchBar(search_option):    
    if search_option == "u":
        username = input("Enter the username to search: ")
        results = post_contents.find({"username": username}).sort("date&time", -1)
    elif search_option == "k":
        search = input("Enter the keyword(s) to search (comma separated for multiple keywords): ")
        keywords = [keyword.strip().lower() for keyword in search.split(",")]
        results = post_contents.find({"msg": {"$regex":"|".join(keywords)}})
    # elif search_option == "d":
    #     search = input("Enter the day to search (YYYY-MM-DD), lw for last week, lm for last month: ")
    #     if search == "lw":
    #         # Calculate the start and end dates for last week
    #         today = datetime.now().date()
    #         start_date = today - timedelta(days=today.weekday() + 7)
    #         end_date = today - timedelta(days=today.weekday() + 1)
    #         results = post_contents.find({"date&time": {"$gte": start_date, "$lte": end_date}})
    #     elif search == "lm":
    #         # Calculate the start and end dates for last month
    #         today = datetime.now().date()
    #         start_date = today.replace(day=1) - timedelta(days=1)
    #         end_date = start_date.replace(day=1)
    #         results = post_contents.find({"date&time": {"$gte": start_date, "$lte": end_date}})
    #     else:
    #         results = post_contents.find({"date&time": {"$regex": search}})
    else:
        print("Invalid search option")
        return


    t = Texttable()

    t.add_row([ "site", "msg", "link", "username", "date&time"])
    ff_temp=[]
    for result in results:
        t.add_row([result["site"], result["msg"], result["link"], result["username"], result["date&time"].strftime("%Y-%m-%d %H:%M:%S")])
    print(t.draw())

    # # ask for file output
    file_output = input("Do you want to save the results in a file? (y/n): ")
    if file_output == 'y':
        filename = input("Enter the filename (default data.txt): ") or "data.txt"
        with open(filename, 'w') as file:
            file.write(t.draw())
        print("File saved as", filename)
    else:
        print("Results not saved in a file")

def background_crawler():
    while True:
        try:
            full_crawler()
        except Exception as e:
            print("Network issue, retrying in 24 hours...")
        time.sleep(24 * 60 * 60)

crawler_thread = threading.Thread(target=background_crawler, daemon=True)
crawler_thread.start()

SearchBarIntro()
while True:
    search_option = input("Enter the search option (u/k/q): ")
    search_option = search_option.lower()
    if(search_option=='q'):
        break
    try:
        SearchBar(search_option)
    except Exception as e:
        print("Error in searching")
        continue
