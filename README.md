# OtherBu(アザブ)
  http://otherbu.com

## 概要
  ブックマークの配置やデザインをお好みで指定できる
  カスタマイズ性の高さが特徴のWebブックマークです。


## 開発環境手順
1. 個人設定ファイルを準備(必要があれば中身を書き換える)
% mv settings/private_config_tmpl settings/private_config

2. DB構築、マイグレート
% cd otherbu/config/
% . ./otherbu_init.sh local-init pip

3. debug環境の起動
% ./manage.py runserver localhost:8088
