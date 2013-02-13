# -*- coding: utf-8 -*-

import re
import os
import shutil
from django.conf import settings


def uploader(path, request, upload_file):
    '''
    ファイルをアップロード
    '''
    upfile = request.FILES[upload_file]
    file_dict = get_file_property(upfile.name)
    file_name = "%s/%s.%s" % (path, settings.BK_IMAGE_NAME, file_dict['ext'])
    create_file = open(file_name, mode='w')
    for chunk in upfile.chunks():
        create_file.write(chunk)
    create_file.close()


def create_userdir(user_dir, auth_type):
    '''
    ユーザーディレクトリ作成
    '''
    user_path = "%s/%s" % (auth_type, user_dir)
    path = os.path.join(settings.USER_IMG_DIR, user_path)
    try:
        os.mkdir(path)
    except:
        shutil.rmtree(path)  # ディレクトリ内にファイルがあっても削除する
        os.mkdir(path)


def get_file_property(file_name):
    '''
    ファイル名と拡張子の情報を取得
    '''
    ret = re.search(r"(?P<file>.*)[.](?P<ext>.*)$", file_name)
    if ret:
        file_dict = {'file': ret.group("file"), 'ext': ret.group("ext")}
        return file_dict
    else:
        return None


def url_exchnge(url):
    '''
    URLにプロトコルが宣言されていなければ付与する
    '''
    r = re.compile('http')
    if not r.match(url):
        new_url = "http://%s" % url
    else:
        new_url = url
    return new_url


def guess_encoding(str):
    '''
    エンコードの判定
    '''
    encodings = ["utf-8", "shift-jis", "euc-jp", "ascii", 'iso2022-jp']
    for enc in encodings:
        try:
            unicode(str, enc)
            break
        except UnicodeDecodeError:
            enc = ""
    return enc


def encode_utf8(data, enc):
    '''
    エンコードのutf8へ変更
    '''
    data = unicode(data, enc)
    return data.encode('utf-8')
