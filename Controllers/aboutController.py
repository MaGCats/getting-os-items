import time
import Models.about as about
from Utilities.seleniumUtil import SeleniumUtil
from selenium.webdriver.common.by import By

class AboutController:
    def __init__(self, driver, conf):
        self.driver = driver
        self.conf = conf
        return

    # 一覧情報を取得
    # TODO Aboutを別の用語に置き換える
    def fetchAbout(self):
        print("一覧画面で基本情報を取得します")
        url = self.conf.targetUrl
        self.driver.get(url)
        time.sleep(self.conf.aboutWaitTime)

        # 縮小ボタンを選択
        if (small_btn := SeleniumUtil.findElements(self.driver, '//button[contains(@class,"bnWGYU")]')) != False:
            small_btn.click()
        time.sleep(0.5)
        # 表示倍率を縮小
        self.driver.execute_script("document.body.style.zoom='20%'")
        time.sleep(0.5)
        # ページを一番下までスクロール
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # 読み込み待ち
        time.sleep(8)

        # 詳細ページのリンクを取得
        if (assets_el := SeleniumUtil.findElements(self.driver, '//div[contains(@class,"AssetsSearchView--assets")]/div/div/div/div/div/article/a', True)) != False:
            count = 0
            about_list = []
            for s in assets_el:
                count += 1
                print(str(count) + "/" + str(len(assets_el)) + "の基本情報を取得中")

                thumbnail = ""
                if len(thumbnail_block := s.find_elements(by=By.XPATH, value='./div/div/div/div/img')) > 0:
                    thumbnail = thumbnail_block[0].get_attribute("src")
                elif len(thumbnail_block := s.find_elements(by=By.XPATH, value='./div/div/div/div/div/img')) > 0:
                    thumbnail = thumbnail_block[0].get_attribute("src")

                about_itm = about.About(
                    detail_url = s.get_attribute("href"),
                    thumbnail_url = thumbnail)
                about_list.append(about_itm)
            return about_list
        return False