import csv
import pprint

class CsvUtil:
    # csv書き込み時に使用するデータ配列を作成
    @staticmethod
    def getDetailsArray(details):
        pprint.pprint(details)
        arr = [[
            "Blockchain type",
            "NFT name",
            "Description (Comming soon.)",
            "creator name",
            "creator url",
            "owner name (One owner only)",
            "owner url (One owner only)",
            "collection name",
            "content url",
            "detail url",
            "thumbnail url",
            "contract_address",
            "token id (Comming soon.)"
        ]]

        for dt in details:
            arr.append(
                [
                    dt.blockchain_type,
                    dt.name,
                    dt.description,
                    dt.creator_name,
                    dt.creator_address,
                    dt.owner_name,
                    dt.owner_url,
                    dt.collection_name,
                    dt.data_url,
                    dt.detail_url,
                    dt.thumbnail,
                    dt.contract_address,
                    dt.token_id
                ])

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