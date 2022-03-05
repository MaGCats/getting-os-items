# Create by MaG(magcats.eth)
# Create date : 2022/02/27

# TODO 例外処理実装

from Controllers.aboutController import AboutController
from Controllers.detailController import DetailController

from selenium import webdriver
from selenium.webdriver.chrome import service as ch

from Utilities.csvUtil import CsvUtil

#
# ＊メインメソッド＊
#
def main():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    chrome_service = ch.Service(executable_path = "./chromedriver")
    driver = webdriver.Chrome(service = chrome_service)
    driver.implicitly_wait(5)

    # 一覧ページでNFT一覧の情報を取得
    about_ctr = AboutController(driver)
    link_list = about_ctr.fetchAbout('https://opensea.io/mag_387')

    print("取得可能なリンク数は" + str(len(link_list)) + "です")

    detail_ctr = DetailController(driver)
    dts = detail_ctr.getDetails(link_list, 1)
    
    # 書き出し
    arr = CsvUtil.getDetailsArray(dts)
    CsvUtil.writeCsv(arr)

if __name__ == "__main__":
    main()