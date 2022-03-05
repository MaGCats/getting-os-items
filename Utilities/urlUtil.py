class UrlUtil:
    @staticmethod
    def getBlockchainTypeFromUrl(url):
        if 'matic' in url:
            return 'Polygon'
        return 'ETH'
    
    # サムネイルのURL末尾に挿入されているサイズを縮小させられるプロパティを除去する
    @staticmethod
    def getUnSmallThumbnailUrl(url):
        if not '=' in url:
            return url

        # 最後に出現するイコールから後を追加しない形で除去
        result_url = ''
        url_arr = url.split('=')
        for i in range(len(url_arr)):
            if i == len(url_arr) - 1:
                break
            if i != 0:
                result_url += '='
            result_url += url_arr[i]

        return result_url

