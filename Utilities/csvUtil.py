import csv
import pprint

class CsvUtil:
    # データ処理系

    # csv書き込み時に使用するデータ配列を作成
    @staticmethod
    def getDetailsArray(details):
        pprint.pprint(details)
        arr = [["NFT name",
            "Description (Comming soon.)",
            "creator name",
            "creator url",
            "owner name (One owner only)",
            "owner url (One owner only)",
            "collection name",
            "content url",
            "contract_address",
            "token id (Comming soon.)"
        ]]

        for dt in details:
            arr.append(
                [   
                    dt.name,
                    dt.description,
                    dt.creator_name,
                    dt.creator_address,
                    dt.owner_name,
                    dt.owner_url,
                    dt.collection_name,
                    dt.data_url,
                    dt.contract_address,
                    dt.token_id
                ])

        return arr

    # csv書き込み
    @staticmethod
    def writeCsv(array):
        with open('./sample.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(array)

        with open('./sample.csv') as f:
            print(f.read())