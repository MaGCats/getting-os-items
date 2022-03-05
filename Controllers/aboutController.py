import time
import Models.about as about
from Utilities.seleniumUtil import SeleniumUtil
from selenium.webdriver.common.by import By

class AboutController:
    def __init__(self, driver):
        self.driver = driver
        return

    # 一覧情報を取得
    # TODO Aboutを別の用語に置き換える
    def fetchAbout(self, url):
        self.driver.get(url)
        time.sleep(1)

        # 縮小ボタンを選択
        # small_btn = driver.find_element(by=By.XPATH, value='//button[contains(@class,"bnWGYU")]')
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
            about_list = []
            for s in assets_el:
                thumbnail = ""
                if len(thumbnail_block := s.find_elements(by=By.XPATH, value='//div/div/div/div/img')) > 0:
                    thumbnail = thumbnail_block[0].get_attribute("src")

                about_itm = about.About(
                    detail_url = s.get_attribute("href"),
                    thumbnail_url = thumbnail)
                about_list.append(about_itm)
            return about_list
        return False