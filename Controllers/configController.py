import configparser
import os
import errno

class ConfigController:
    def __init__(self):
        config_path = 'config.ini'
        config_ini = configparser.ConfigParser()
        if not os.path.exists(config_path):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), config_path)

        try:
            config_ini.read(config_path, encoding='utf-8')

            self.targetUrl = config_ini['TARGET']['TargetURL']
            self.limit = int(config_ini['SETTINGS']['GetLimit'])
        except Exception as e:
            self.limit = 10000
            print("設定ファイルの読み込みに失敗しました。設定ファイルとその内容をご確認ください。")
            print(e)
        
