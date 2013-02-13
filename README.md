# =========================
#   開発環境手順
# =========================

# 個人設定ファイルを準備(必要があれば中身を書き換える)
% mv settings/private_config_tmpl settings/private_config

# DB構築、マイグレート
% cd otherbu/config/
% . ./otherbu_init.sh local-init pip

# debug環境の起動
% cd ..
% ./manage.py runserver localhost:8088
