import requests
from bs4 import BeautifulSoup

# 画像保存に必要
from PIL import Image
import io

url = 'https://scraping-for-beginner.herokuapp.com/image'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')
# ここまでは03_Webページ内のデータを自動抽出(BeautifulSoup編)、04_ランキングサイト掲載情報を自動取得で練習済み


# ------------------------
# 画像を一枚のみ取得・保存

img_tag = soup.find('img')
img_tag['src']

root_url = 'https://scraping-for-beginner.herokuapp.com'

# 画像のURL取得
img_url = root_url + img_tag['src']

# 画像の保存
img = Image.open(io.BytesIO(requests.get(img_url).content))
img.save('img/sample.jpg')


# ------------------------
# 画像を複数枚取得・保存

soup = BeautifulSoup(res.text, 'html.parser')

img_tags = soup.find_all('img')
for i, img_tag in enumerate(img_tags):                          # enumerate()はリストの中の要素とIndexを取得する
  root_url = 'https://scraping-for-beginner.herokuapp.com'
  img_url = root_url + img_tag['src']

  img = Image.open(io.BytesIO(requests.get(img_url).content))
  img.save(f'img/{i}.jpg')