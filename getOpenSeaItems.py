from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')

# driver = webdriver.Chrome('./chromedriver', options=options)
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(5)
# driver.get('https://opensea.io/Mag_387')
driver.get('https://opensea.io/CATHATS?tab=created')

# driver.execute_script("window.scrollTo(0,20000)")
# driver.find_element(By.CSS_SELECTOR, "div:nth-child(11) .Image--image").click()
# element = driver.find_element(By.CSS_SELECTOR, "div:nth-child(11) .Image--image")

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(1)

# 縮小ボタンを選択
small_btn = driver.find_element_by_xpath('//button[contains(@class,"bnWGYU")]')
small_btn.click()
time.sleep(0.5)
# 表示倍率を縮小
driver.execute_script("document.body.style.zoom='20%'")
time.sleep(0.5)
# ページを一番下までスクロール
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 読み込み待ち
time.sleep(5)

# 詳細ページのリンクを取得
assets_el = driver.find_elements_by_xpath('//div[contains(@class,"AssetsSearchView--assets")]/div/div/div/div/div/article/a')
assets_count = len(assets_el)

# 取得結果を表示
print([s.get_attribute("href") for s in assets_el])
print(assets_count)


