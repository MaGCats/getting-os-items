class UrlUtil:
    @staticmethod
    def getBlockchainTypeFromUrl(url):
        if 'matic' in url:
            return 'Polygon'
        return 'ETH'