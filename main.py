# Create by MaG(magcats.eth)
# Create date : 2022/02/27

from selenium import webdriver
from selenium.webdriver.chrome import service as ch
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Controllers.aboutController import AboutController
from Models.config import Config
from Controllers.detailController import DetailController
from Utilities.csvUtil import CsvUtil

def main():
    conf = Config()

    # Linuxをお使いの方は、こちらをChromium用のコードに変更してください　※動作未確認
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)

    # 一覧ページでNFT一覧の情報を取得
    about_ctr = AboutController(driver, conf)
    link_list = about_ctr.fetchAbout()

    if link_list == False:
        print("NFTの基本情報を取得することができませんでした。URLが正しいかご確認ください。")
        print("URL:" + conf.targetUrl)
        return

    print("取得可能なリンク数は" + str(len(link_list)) + "です")

    detail_ctr = DetailController(driver)
    dts = detail_ctr.getDetails(conf, link_list, int(conf.limit),)
    
    # 書き出し
    arr = CsvUtil.getDetailsArray(dts)
    export_title = CsvUtil.UrlToTitle(conf.targetUrl)
    CsvUtil.writeCsv(arr, export_title)

if __name__ == "__main__":
    main()