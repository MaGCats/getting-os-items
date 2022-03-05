from os import name


class Detail:
    def __init__(self, 
            name = '',
            description = '',
            creator_name = '',
            creator_address = '',
            owner_name = '',
            owner_url = '',
            collection_name = '',
            data_url = '',
            contract_address = '',
            token_id = ''):
        # NFT名
        self.name = name
        # 説明
        self.description = description
        # 作成者名
        self.creator_name = creator_name
        # 作成者のURL ※ウォレットアドレスではない
        self.creator_address = creator_address
        # NFTの所有者名（１つの場合のみ）
        self.owner_name = owner_name
        # 所有者URL
        self.owner_url = owner_url
        # NFTのコレクション名
        self.collection_name = collection_name
        # コンテンツの中身のURL
        self.data_url = data_url
        # NFTのコントラクトアドレス
        self.contract_address = contract_address
        # トークンID
        self.token_id = token_id
        