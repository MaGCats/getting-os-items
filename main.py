# Create by MaG(magcats.eth)
# Create date : 2022/02/27

# TODO 例外処理実装

from lib2to3.pytree import convert
import about
import detail

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome import service as ch

import time

import csv
import pprint

def main():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    chrome_service = ch.Service(executable_path = "./chromedriver")
    driver = webdriver.Chrome(service = chrome_service)
    driver.implicitly_wait(5)

    # 一覧ページでNFT一覧の情報を取得
    link_list = fetchAbout(driver, 'https://opensea.io/mag_387')
    print("取得可能なリンク数は" + str(len(link_list)) + "です")

    dts = getDetails(driver, link_list, 10000)
    
    # 書き出し
    arr = getDetailsArray(dts)
    writeCsv(arr)

def getDetailsArray(details):
    pprint.pprint(details)
    arr = [["NFT name",
        "Description (Comming soon.)",
        "creator name",
        "creator url",
        "owner name (One owner only)",
        "owner url (One owner only)",
        "collection name",
        "content url",
        "contract_address",
        "token id (Comming soon.)"
    ]]

    for dt in details:
        arr.append(
            [   
                dt.name,
                dt.description,
                dt.creator_name,
                dt.creator_address,
                dt.owner_name,
                dt.owner_url,
                dt.collection_name,
                dt.data_url,
                dt.contract_address,
                dt.token_id
            ])

    return arr

# csv書き込み
def writeCsv(array):
    with open('./sample.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(array)

    with open('./sample.csv') as f:
        print(f.read())

# 一覧情報を取得
# TODO Aboutを別の用語に置き換える
def fetchAbout(driver, url):
    driver.get(url)
    time.sleep(1)

    # 縮小ボタンを選択
    small_btn = driver.find_element(by=By.XPATH, value='//button[contains(@class,"bnWGYU")]')
    small_btn.click()
    time.sleep(0.5)
    # 表示倍率を縮小
    driver.execute_script("document.body.style.zoom='20%'")
    time.sleep(0.5)
    # ページを一番下までスクロール
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # 読み込み待ち
    time.sleep(8)

    # 詳細ページのリンクを取得
    assets_el = driver.find_elements(by=By.XPATH, value='//div[contains(@class,"AssetsSearchView--assets")]/div/div/div/div/div/article/a')
    # assets_count = len(assets_el)

    about_list = []
    for s in assets_el:
        about_itm = about.About(detail_url = s.get_attribute("href"))
        about_list.append(about_itm)

    # 取得結果を表示
    # return [s.get_attribute("href") for s in assets_el]
    return about_list

# 詳細情報を上限付きで取得する
def getDetails(driver, about_list = [], limit = 100000):
    count = 1
    detail_list = []
    for about in about_list:
        if count == limit:
            break
        count += 1
        print("こちらのNFTの情報を取得します:" + about.detail_url)
        detail_list.append(fetchDetail(driver, about.detail_url))
        print("進捗:" + str(count) + "/" + str(len(about_list)))
    return detail_list

# 詳細情報を取得
def fetchDetail(driver, url):
    detail_data = detail.Detail()

    driver.get(url)
    time.sleep(1)

    # 表示倍率を縮小
    driver.execute_script("document.body.style.zoom='60%'")
    # 読み込み待ち
    time.sleep(2)

    # コレクション名
    detail_data.collection_name = driver.find_element(by=By.XPATH, value='//div[contains(@class,"item--collection-detail")]/div/a').text
    # NFT名
    detail_data.name = driver.find_element(by=By.XPATH, value='//section[@class="item--header"]/h1').text

    # NFT所有者ブロック
    owner_itm = driver.find_elements(by=By.XPATH, value='//section[@class="item--counts"]/div/div/a')
    if len(owner_itm) > 0 :
        # NFTの所有者名（１つの場合のみ）
        detail_data.owner_name = owner_itm[0].text
        # 所有者URL（１つの場合のみ）
        detail_data.owner_url = owner_itm[0].get_attribute("href")

    creator_name = driver.find_elements(by=By.XPATH, value='//div[contains(@id,"Body react-aria-")]/div/div/section/div/a/span')
    if len(creator_name) > 0:
        # 作成者の名前
        detail_data.creator_name = creator_name[0].text
        # 作成者のURL
        detail_data.creator_address = driver.find_element(by=By.XPATH, value='//div[contains(@id,"Body react-aria-")]/div/div/section/div/a').get_attribute("href")

    # 説明
    # TODO:改行処理の実装
    # description = driver.find_element_by_xpath('//div[contains(@class,"item--description-text")]/p').text

    # Detailsを開く
    detail_btn = driver.find_element(by=By.XPATH, value='//button[span[contains(text(),"Details")]]')
    driver.execute_script("arguments[0].click();", detail_btn)
    time.sleep(0.1)

    # NFTのコントラクトアドレス
    scan_contract_address = driver.find_element(by=By.XPATH, value='//span[contains(@class, "elqhCm cCfKUE jmAsQO")]/a').get_attribute("href")
    if scan_contract_address != "":
        detail_data.contract_address = \
            scan_contract_address.split('/')[-1]
    # トークンID
    # token_id = driver.find_element_by_xpath('//div[@class="Blockreact__Block-sc-1xf18x6-0 elqhCm")]/div/span').get_attribute("href")

    # コンテンツを選択する
    content_btn = driver.find_elements(by=By.XPATH, value='//div[@class="item--summary"]/article/div/div/div/div/img')
    if len(content_btn) > 0:
        driver.execute_script("arguments[0].click();", content_btn[0])
        time.sleep(0.1)
        # コンテンツの中身のURL
        detail_data.data_url = driver.find_element(by=By.XPATH, value='//div[@class="Overlayreact__Overlay-sc-1yn7g51-0 ebMEfa"]/div/div/div/div/div/img').get_attribute("src")

    return detail_data

if __name__ == "__main__":
    main()