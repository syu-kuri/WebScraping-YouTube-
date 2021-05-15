# YouTube(https://youtu.be/VRFfAeW30qE)を練習

from selenium import webdriver
from time import sleep

# chromedriverは同階層内に配置
browser = webdriver.Chrome('chromedriver.exe')

# 指定URLでのブラウザ起動
url = "https://scraping-for-beginner.herokuapp.com/login_page"
browser.get(url)

sleep(4)

# ユーザーの名前の入力
elem_username = browser.find_element_by_id('username')
elem_username.send_keys('imanishi')

# パスワード入力
elem_password = browser.find_element_by_id('password')
elem_password.send_keys('kohei')

# ログインボタンクリック
sleep(1)
elem_login_btn = browser.find_element_by_id('login-btn')
elem_login_btn.click()

# ブラウザ終了
sleep(2)
browser.quit()