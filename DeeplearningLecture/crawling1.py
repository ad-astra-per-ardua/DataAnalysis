from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

result = []
import urllib.request
import urllib.response

for page in range(1, 7):

    url = 'https://www.ejadam.co.kr/bbs/board.php?bo_table=store&page=%d' % page
    print(url)

    html = urllib.request.urlopen(url)
    soupJadam = BeautifulSoup(html, 'html.parser')
    tag_tbody = soupJadam.find('tbody')
    for store in tag_tbody.find_all("tr"):

        if len(store) <= 3:
            break
        store_td = store.find_all('td')
        store_name = store_td[0].text.strip()
        store_phone = store_td[1].text.strip()
        store_address = store_td[2].text.strip()
result.append([store_name, store_phone, store_address])
jadam_tbl = pd.DataFrame(result, columns=('store_name', 'store_phone', 'store_address'))
jadam_tbl.to_csv("./jadam.csv", encoding='cp949', index=True, mode="w")
