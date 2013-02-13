# -*- coding: utf-8 -*-

import urllib2
import socket
from sgmllib import SGMLParser
from module.misc.common_api import guess_encoding, encode_utf8


class MySGMLParser(SGMLParser):
    def __init__(self):
        socket.setdefaulttimeout(2)
        SGMLParser.__init__(self)
        self.flag = False

    def start_title(self, attribute):
        self.flag = True

    def handle_data(self, data):
        if self.flag:
            self.title = data

    def end_title(self):
        self.flag = False


def getPageTitle(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7')]
    try:
        response = opener.open(url).read()
        parser = MySGMLParser()
        parser.feed(response)
        enc = guess_encoding(parser.title)
        if enc != 'utf-8':
            return encode_utf8(parser.title, enc)
        return parser.title
    except:
        return False
