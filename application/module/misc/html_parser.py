# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser


class My_parser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.is_a = False
        self.is_h3 = False
        self.category_name = None
        self.a_name = None
        self.href = None
        self.bookmark = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)  # タプルだと扱いにくいので辞書にする
        if tag == 'h3':
            self.is_h3 = True
        if tag == 'a':
            self.is_a = True
            if attrs.get('href', False):
                self.href = attrs['href']

    def handle_endtag(self, tag):
        if tag == 'h3':
            self.is_h3 = False

        if tag == 'a':
            self.is_a = False
            self.bookmark.append({
                'category_name': self.category_name,
                'url': self.href,
                'a_name': self.a_name
            })
            self.href = None
            self.val = None

    def handle_data(self, data):
        data = unicode(data, 'utf-8')
        if self.is_h3:
            self.category_name = data
        if self.is_a:
            self.a_name = data


def get_import_list(html):
    parser = My_parser()
    parser.feed(html)
    return parser.bookmark
