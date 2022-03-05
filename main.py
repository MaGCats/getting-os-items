# Create by MaG(magcats.eth)
# Create date : 2022/02/27

from selenium import webdriver
from selenium.webdriver.chrome import service as ch

from Controllers.aboutController import AboutController
from Controllers.configController import ConfigController
from Controllers.detailController import DetailController
from Utilities.csvUtil import CsvUtil

def main():
    conf = ConfigController()

    # Linuxをお使いの方は、こちらをChromium用のコードに変更してください　※動作未確認
    chrome_service = ch.Service(executable_path = "./chromedriver")
    driver = webdriver.Chrome(service = chrome_service)
    driver.implicitly_wait(8)

    # 一覧ページでNFT一覧の情報を取得
    about_ctr = AboutController(driver)
    link_list = about_ctr.fetchAbout(conf.targetUrl)

    if link_list == False:
        print("NFTの基本情報を取得することができませんでした。URLが正しいかご確認ください。")
        print("URL:" + conf.targetUrl)
        return

    print("取得可能なリンク数は" + str(len(link_list)) + "です")

    detail_ctr = DetailController(driver)
    dts = detail_ctr.getDetails(link_list, int(conf.limit))
    
    # 書き出し
    arr = CsvUtil.getDetailsArray(dts)
    export_title = CsvUtil.UrlToTitle(conf.targetUrl)
    CsvUtil.writeCsv(arr, export_title)

if __name__ == "__main__":
    main()