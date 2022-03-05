# Create by MaG(magcats.eth)
# Create date : 2022/02/27

# TODO 例外処理実装

from Controllers.aboutController import AboutController
from Controllers.detailController import DetailController

from selenium import webdriver
from selenium.webdriver.chrome import service as ch

from Utilities.csvUtil import CsvUtil

def main():
    targetUrl = 'https://opensea.io/mag_387'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    chrome_service = ch.Service(executable_path = "./chromedriver")
    driver = webdriver.Chrome(service = chrome_service)
    driver.implicitly_wait(5)

    # 一覧ページでNFT一覧の情報を取得
    about_ctr = AboutController(driver)
    link_list = about_ctr.fetchAbout(targetUrl)

    print("取得可能なリンク数は" + str(len(link_list)) + "です")

    detail_ctr = DetailController(driver)
    dts = detail_ctr.getDetails(link_list, 5)
    
    # 書き出し
    arr = CsvUtil.getDetailsArray(dts)
    export_title = CsvUtil.UrlToTitle(targetUrl)
    CsvUtil.writeCsv(arr, export_title)

if __name__ == "__main__":
    main()