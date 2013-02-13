# -*- coding: utf-8 -*-

#==================================================
# プライベート設定
#==================================================

# シェルスクリプトからでも読め込みできるように
# 変数名と値の=間のスペースは消してます

DB_NAME='otherbu'          # DB名
DB_USER='other'            # mysqlユーザー名
DB_PASS='bookmark'         # mysqlパスワード
PUBLIC_HOSTNAME='hogehost' # 公開用サーバーネーム

DEV_DB_NAME='otherbu2'     # DB名
DEV_DB_USER='other2'       # mysqlユーザー名
DEV_DB_PASS='bookmark2'    # mysqlパスワード
DEV_DIRECTORY='otherbu2'   # 本番でのdevディレクトリ

# Djangoの秘密鍵
DJANGO_SECRET_KEY='hogehogehoge'

# =====================
#  OAuth認証key
# =====================

## 本番用
# twiiter
MY_TWITTER_CONSUMER_KEY=''
MY_TWITTER_CONSUMER_SECRET=''

# facebook
MY_FACEBOOK_APP_KEY=''
MY_FACEBOOK_APP_SECRET=''
MY_FACEBOOK_REDIRECT_URI=''

## dev用
# twiiter
DEV_MY_TWITTER_CONSUMER_KEY=''
DEV_MY_TWITTER_CONSUMER_SECRET=''

# facebook
DEV_MY_FACEBOOK_APP_KEY=''
DEV_MY_FACEBOOK_APP_SECRET=''
DEV_MY_FACEBOOK_REDIRECT_URI=''
