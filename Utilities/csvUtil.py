import csv

from Models.detail import Detail

class CsvUtil:
    # csv書き込み時に使用するデータ配列を作成
    @staticmethod
    def getDetailsArray(details):
        arr = [Detail.getDetailNames()]
        for dt in details:
            arr.append(dt.getDetail())
        return arr

    # csv書き込み
    @staticmethod
    def writeCsv(array, title="export"):
        with open('./' + title + '.csv', 'w', newline='') as f:
            try:
                writer = csv.writer(f)
                writer.writerows(array)
            except Exception as e:
                print("CSVの書き込みに失敗しました。ファイルの書き込み権限がある場所で実行してください。")
                print(e)

    @staticmethod
    def UrlToTitle(url):
        if url == None or url == "":
            return "export"
        try:
            return url.split('/')[-1]
        except Exception as e:
            return "export" 