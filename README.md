# getting-os-items
OpenSeaの任意のユーザの"Collected"や"Created"の情報を取得するプログラム

## ざっくり導入手順
1. Pythonをインストール
    1. 3.9.6で動作確認済み、3.8以上必要　一応Mac OS CatalinaとWin10で動作確認済み
1. pip導入
1. pipでSeleniumをインストール
1. pipでwebdriver-managerをインストール

## 使い方
1. "main.py"をエディターで開き、29行目くらいにあるURLを自分が取得したい人のOpenSeaのCollectedタブのURLに置換えます。
1. ”python main.py”とターミナルに打ち込んでプログラムを起動させます。
1. 実行が完了すると、プログラムと同じディレクトリ上にsample.csvというファイルが生成されます。それが取得結果です。
    1. 取得できていない項目があるのはご愛敬ということで、今後修正していきます。