from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as ch

class SeleniumUtil:
    # 要素を取得し、指定した変数に代入する　単数の要素に限る
    #type: text, href
    @staticmethod
    def assignElementValue(driver, xpath, type="text"):
        if xpath == "":
            return ""
        element = SeleniumUtil.findElements(driver, xpath)
        if element == False:
            return ""

        if type == "text":
            return element.text
        elif type == "href":
            return element.get_attribute("href")
        elif type == "src":
            return element.get_attribute("src")
        return ""    

    # 単数または複数の要素を取得する
    @staticmethod
    def findElements(driver, xpath, multi=False):
        elements = driver.find_elements(by=By.XPATH, value=xpath)
        if len(elements) != 0:
            if multi:
                return elements
            return elements[0]
        return False