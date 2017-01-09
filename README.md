# OtherBu(アザブ)
  http://otherbu.com

## 概要
  ブックマークの配置やデザインをお好みで指定できる
  カスタマイズ性の高さが特徴のWebブックマークです。


## 開発環境手順
1. 個人設定ファイルの(必要があれば)中身を書き換える
```
% vim application/settings/private_config.py
```

2. DB構築、マイグレート
```
% cd otherbu/env
% ./otherbu_init.sh local-init pip
```

3. debug環境の起動
```
% cd otherbu/application
% ./manage.py runserver
```
