import requests
from bs4 import BeautifulSoup

# 二次元の表形式データにするのに必要
import pandas as pd

url = 'https://scraping-for-beginner.herokuapp.com/ranking/'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')
# ここまでは03_Webページ内のデータを自動抽出(BeautifulSoup編)で練習済み


# ------------------------
## 1つの観光地情報を取得

# 観光地名取得
spots = soup.find_all('div', attrs={'class': 'u_areaListRankingBox'})
spot = spots[0]
spot_name = spot.find('div', attrs={'class', 'u_title'})

# 1観光地1の先頭の1を除去する
spot_name.find('span', attrs={'class', 'badge'}).extract()

# \nを置き換える
spot_name = spot_name.text.replace('\n', '')


# 評点の取得
eval_num = spot.find('div', attrs={'class', 'u_rankBox'})
eval_num = eval_num.text.replace('\n', '')

# 文字列から浮動小数へ
eval_num = float(eval_num)


# テーブル情報(カテゴリ)の取得
categoryItems = spot.find('div', attrs={'class': 'u_categoryTipsItem'})
categoryItems = categoryItems.find_all('dl')

# 楽しさのみ取得
categoryItem = categoryItems[0]
category = categoryItem.dt.text
rank = float(categoryItem.span.text)

# 辞書型で表示
details = {}
for categoryItem in categoryItems:                              # categoryItem = categoryItems[0]と同じ
  category = categoryItem.dt.text
  rank = float(categoryItem.span.text)
  details[category] = rank

# 観光地名、評点をdetailsに追加
datum = details
datum['観光地名'] = spot_name
datum['評点'] = eval_num


# ------------------------
# すべての観光地情報を取得

soup = BeautifulSoup(res.text, 'html.parser')

# すべての情報を格納
data = []

# 観光地名取得
spots = soup.find_all('div', attrs={'class': 'u_areaListRankingBox'})
for spot in spots:
  spot_name = spot.find('div', attrs={'class', 'u_title'})
  spot_name.find('span', attrs={'class', 'badge'}).extract()
  spot_name = spot_name.text.replace('\n', '')

  # 評点の取得
  eval_num = spot.find('div', attrs={'class', 'u_rankBox'})
  eval_num = eval_num.text.replace('\n', '')
  eval_num = float(eval_num)

  # テーブル情報(カテゴリ)の取得
  categoryItems = spot.find('div', attrs={'class': 'u_categoryTipsItem'})
  categoryItems = categoryItems.find_all('dl')
  details = {}
  for categoryItem in categoryItems:                              # categoryItem = categoryItems[0]と同じ
    category = categoryItem.dt.text
    rank = float(categoryItem.span.text)
    details[category] = rank
  datum = details
  datum['観光地名'] = spot_name
  datum['評点'] = eval_num
  data.append(datum)

df = pd.DataFrame(data)

# columsでリストを表示してコピーする
df.columns

# 順序を入れ替える
df = df[['観光地名', '評点', '楽しさ', '人混みの多さ', '景色', 'アクセス']]


# CSVで出力する
df.to_csv('観光地情報.csv', index=False)