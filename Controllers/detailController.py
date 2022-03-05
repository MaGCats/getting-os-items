import time
import Models.detail as detail
from Utilities.seleniumUtil import SeleniumUtil

class DetailController:
    def __init__(self, driver):
        self.driver = driver
        return

        # 詳細情報を上限付きで取得する
    def getDetails(self, about_list = [], limit = 100000):
        count = 0
        detail_list = []
        for about in about_list:
            if count == limit:
                break
            count += 1
            print("こちらのNFTの情報を取得します:" + about.detail_url)
            detail_list.append(self.fetchDetail(about.detail_url))
            print("進捗:" + str(count) + "/" + str(len(about_list)))
        return detail_list

    # 詳細情報を取得
    def fetchDetail(self, url):
        detail_data = detail.Detail()
        self.driver.get(url)
        time.sleep(1)

        # 表示倍率を縮小
        self.driver.execute_script("document.body.style.zoom='60%'")
        # 読み込み待ち
        time.sleep(2)

        # コレクション名
        detail_data.collection_name = SeleniumUtil.assignElementValue(self.driver,\
            '//div[contains(@class,"item--collection-detail")]/div/a', 'text')

        # NFT名
        detail_data.name = SeleniumUtil.assignElementValue(self.driver, \
            '//section[@class="item--header"]/h1', 'text')

        # NFT所有者ブロック
        if (owner_itm := SeleniumUtil.findElements(self.driver, '//section[@class="item--counts"]/div/div/a')) != False:
            # NFTの所有者名（１つの場合のみ）
            detail_data.owner_name = owner_itm.text
            # 所有者URL（１つの場合のみ）
            detail_data.owner_url = owner_itm.get_attribute("href")

        if (creator_name := SeleniumUtil.findElements(self.driver, \
            '//div[contains(@id,"Body react-aria-")]/div/div/section/div/a/span')) != False:
            # 作成者の名前
            detail_data.creator_name = creator_name.text
            # 作成者のURL
            detail_data.creator_address = SeleniumUtil.assignElementValue(self.driver,\
                '//div[contains(@id,"Body react-aria-")]/div/div/section/div/a', 'href')

        # 説明
        # TODO:改行処理の実装
        # description = driver.find_element_by_xpath('//div[contains(@class,"item--description-text")]/p').text

        # Detailsを開く
        if (detail_btn := SeleniumUtil.findElements(self.driver,\
            '//button[span[contains(text(),"Details")]]')) != False:
            self.driver.execute_script("arguments[0].click();", detail_btn)
            time.sleep(0.1)

        # NFTのコントラクトアドレス
        if (scan_contract_address := SeleniumUtil.assignElementValue(self.driver,\
            '//span[contains(@class, "elqhCm cCfKUE jmAsQO")]/a', 'href')) != "":
            detail_data.contract_address = scan_contract_address.split('/')[-1]

        # トークンID
        # token_id = driver.find_element_by_xpath('//div[@class="Blockreact__Block-sc-1xf18x6-0 elqhCm")]/div/span').get_attribute("href")

        # コンテンツを選択する
        if (content_btn := SeleniumUtil.findElements(self.driver,\
                '//div[@class="item--summary"]/article/div/div/div/div/img')) != False:
            self.driver.execute_script("arguments[0].click();", content_btn)
            time.sleep(0.3)
            # コンテンツの中身のURL
            detail_data.data_url = SeleniumUtil.assignElementValue(self.driver, \
                '//div[@class="Overlayreact__Overlay-sc-1yn7g51-0 ebMEfa"]/div/div/div/div/div/img', 'src')

        return detail_data