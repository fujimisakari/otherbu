# OtherBu(アザブ)
  http://otherbu.com

## 概要
  ブックマークの配置やデザインをお好みで指定できる
  カスタマイズ性の高さが特徴のWebブックマークです。


## 開発環境手順

1. 環境に合った.envファイルを準備
```
% cp .env.example .env
% vim .env
```

2. DB構築、マイグレート
```
% ./env/otherbu_init.sh develop pip
```

3. debug環境の起動
```
% cd otherbu/application
% ./manage.py runserver
```
