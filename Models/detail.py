class Detail:
    @staticmethod
    def getDetailNames():
        return [
            "Blockchain type",
            "NFT name",
            "Description",
            "Creator name",
            "Creator url",
            "Owner name (One owner only)",
            "Owner url (One owner only)",
            "Collection name",
            "Content url",
            "Detail url",
            "Thumbnail url",
            "Contract address",
            "Token id (Comming soon.)"
        ]

    def __init__(self, 
            blockchain_type ='',
            name = '',
            description = '',
            creator_name = '',
            creator_address = '',
            owner_name = '',
            owner_url = '',
            collection_name = '',
            data_url = '',
            detail_url = '',
            thumbnail = '',
            contract_address = '',
            token_id = ''):
        # ブロックチェーン
        self.blockchain_type = blockchain_type
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
        # 詳細ページのURL
        self.detail_url = detail_url
        # NFTのサムネイルのURL
        self.thumbnail = thumbnail
        # NFTのコントラクトアドレス
        self.contract_address = contract_address
        # トークンID
        self.token_id = token_id
        
    def getDetail(self):
        return [
            self.blockchain_type,
            self.name,
            self.description,
            self.creator_name,
            self.creator_address,
            self.owner_name,
            self.owner_url,
            self.collection_name,
            self.data_url,
            self.detail_url,
            self.thumbnail,
            self.contract_address,
            self.token_id
        ]