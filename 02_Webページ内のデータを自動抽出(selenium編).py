from selenium import webdriver
from time import sleep

# 二次元の表形式データにするのに必要
import pandas as pd

browser = webdriver.Chrome('chromedriver.exe')

url = "https://scraping-for-beginner.herokuapp.com/login_page"
browser.get(url)

sleep(4)
elem_username = browser.find_element_by_id('username')
elem_username.send_keys('imanishi')

elem_password = browser.find_element_by_id('password')
elem_password.send_keys('kohei')

sleep(1)
elem_login_btn = browser.find_element_by_id('login-btn')
elem_login_btn.click()
# ここまでは(01_ログインなどのブラウザ操作.py)で練習済み

# テーブル内の名前の取得
# name = browser.find_element_by_id('name')
# name = name.text

# テーブル内の所属企業の取得
# company = browser.find_element_by_id('company')
# company = company.text

# テーブル内の生年月日の取得
# birthday = browser.find_element_by_id('birthday')
# birthday = birthday.text

# テーブル内の出身の取得
# come_from = browser.find_element_by_id('come_from')
# come_from = come_from.text

# テーブル内の趣味の取得
# hobby = browser.find_element_by_id('hobby')
# hobby = hobby.text
# hobby = hobby.replace('\n', ',')                 # replace('A', 'B')でAをBに置き換える

# タグで情報を取得(1つのみ)
# elem_th = browser.find_element_by_tag_name('th')
# elem_th = elem_th.text

# タグで情報を取得(複数個)
elems_th = browser.find_elements_by_tag_name('th')
# elems_th = elems_th[0].text

keys = []
for elem_th in elems_th:
  key = elem_th.text
  keys.append(key)                               # append()は末尾に要素を追加する
# print(keys)

# タグでテーブル全体を取得
elems_td = browser.find_elements_by_tag_name('td')
values = []
for elem_td in elems_td:
  value = elem_td.text
  values.append(value)
# print(values)

# 二次元の表形式データにする
df = pd.DataFrame()
df['項目'] = keys
df['値'] = values

# CSVファイルとして出力
df.to_csv('講師情報.csv', index=False)

sleep(2)
browser.quit()