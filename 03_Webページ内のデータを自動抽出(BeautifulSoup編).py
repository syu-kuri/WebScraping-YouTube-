import requests
from bs4 import BeautifulSoup

url = 'https://scraping-for-beginner.herokuapp.com/udemy'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')             # html.parserはHTMLの構造を解析する
# print(soup.prettify())                                  # prettify()はきれいにフォーマットされた形でHTMLを表示する

soup.find_all('p')                                        # find_all('A')はすべての<A>の要素をリストで返す
soup.find('p')
soup.p                                                    # soup.find('p')と同じ
soup.p.text

# 受講者数を取得する
subscribers = soup.find_all('p', attrs={'class': 'subscribers'})[0]
n_subscribers = int(subscribers.text.split('：')[1])      # text.split()は指定した文字列の前後で分割しリストで返す
# print(n_subscribers)


#レビュー数を取得する
reviews = soup.find_all('p', attrs={'class': 'reviews'})[0]
n_reviews = int(reviews.text.split('：')[1])
# print(n_reviews)


# CSSセレクタ:select()
subscribers1 = soup.select('.subscribers')                # リスト形式で返す
# print(subscribers1)

subscribers2 = soup.select_one('.subscribers')            # 最初の1つのみ返す
# print(subscribers2)