# -*- coding: utf-8 -*-

from django.utils.safestring import mark_safe


help_context = [
    {'title': 'カテゴリについて',
     'type': 'category',
     'category_list': [
         {'title': '機能について',
          'context': 'カテゴリはブックマークを分類するための機能になります'},
         {'title': '新規追加の方法',
          'context': 'Otherbuページの上部ナビバーのメモアイコンよりカテゴリ登録が行えます'},
         {'title': '編集の方法',
          'context': 'Otherbuページのカテゴリ名を長押しすることで編集画面が表示されます'},
         {'title': '削除の方法',
          'context': 'Settingページ → Category設定より、削除することができます'},
         {'title': 'カテゴリ位置の移動',
          'context': 'Otherbuページの上部ナビバーの矢印アイコンよりカテゴリ位置の移動が行えます'}]},
    {'title': 'ブックマークについて',
     'type': 'bookmark',
     'category_list': [
         {'title': '機能について',
          'context': 'ブックマークはURLに名前つけて記憶しておく機能になります'},
         {'title': '新規追加の方法',
          'context': mark_safe('Otherbuページの上部ナビバーのメモアイコンより手動でブックマーク登録が行えます<br />もしくは、虫めがねアイコンより任意ページを開きメモアイコンを押すことで自動登録することもできます')},
         {'title': '編集の方法',
          'context': 'Otherbuページのブックマーク名を長押しすることで編集画面が表示されます'},
         {'title': '削除の方法',
          'context': 'Settingページ → Bookmark設定 → 所属カテゴリを選択より、削除することができます'},
         {'title': '並び順の変更',
          'context': 'Settingページ → Bookmark設定 → 所属カテゴリを選択より、並び順を変更することができます'},
         {'title': '別カテゴリへ移動',
          'context': 'ブックマーク編集画面より任意のカテゴリを選択することで移動できます'}]},
    {'title': 'ページについて',
     'type': 'page',
     'category_list': [
         {'title': '機能について',
          'context': 'ページはカテゴリを分類してシーンに合ったカテゴリのみを表示させます'},
         {'title': '新規追加の方法',
          'context': 'Otherbuページの上部ナビバーのメモアイコンよりページ登録が行えます'},
         {'title': '編集の方法',
          'context': 'Otherbuページのページ名のタブを長押しすることで編集画面が表示されます'},
         {'title': '削除の方法',
          'context': 'Settingページ → Page設定 → Edit Pageより、削除することができます'},
         {'title': '並び順の変更',
          'context': 'Settingページ → Page設定 → Edit Pageより、並び順を変更することができます'},
         {'title': '所属カテゴリの編集',
          'context': 'Settingページ → Page設定 → Edit Page より、任意のページ選び所属させるカテゴリを編集することができます'}]},
    {'title': 'アカウントについて',
     'type': 'account',
     'category_list': [
         {'title': '機能について',
          'context': mark_safe('アカウントは、ブックマークデータを個別に保持するために利用してます<br />例えば、Facebookアカウントでログインして追加、変更したデータはFacebookアカウントでログイン時のみ表示します<br />ログアウトするとデフォルトのブックマークデータに切り替わります')}]},
    {'title': '同期について',
     'type': 'sync',
     'category_list': [
         {'title': '機能について',
          'context': 'web版OtherbuとAppで登録、編集等した内容を同期させることができます'},
         {'title': '同期させるには？',
          'context': '同期させるには、Twitter、Facebookどちらかのアカウントが必要になります'},
         {'title': 'Web版とApp版で編集が被った場合',
          'context': 'Web版とApp版のOtherbuで編集内容が被った場合は、編集した時刻の新しい方が優先して同期されます'}]}
]
