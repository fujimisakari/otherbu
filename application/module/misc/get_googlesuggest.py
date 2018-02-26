import re
import urllib.request
from xml.etree.ElementTree import XML, ElementTree


class GetGoogleSuggest(object):

    def __init__(self, search_target, get_max_count=6):
        """
        XMLを読み込んでitemタグのリストを作る
        """
        r = re.compile(r'\s+')
        search_target = r.sub('%20', search_target)
        enc_search_target = urllib.parse.quote_plus(search_target)
        url = 'http://www.google.com/complete/search?hl=ja&q={}&output=toolbar'.format(enc_search_target)
        response = urllib.request.urlopen(url)
        text = response.readlines()
        text = text[0].decode('sjis')
        obj_xml = ElementTree(XML(text))
        self.items = obj_xml.findall('CompleteSuggestion')
        self.get_max_count = get_max_count
        self.target_tag_list = ['suggestion', 'num_queries']

    def get_data(self):
        """
        欲しいデータがディクショナリ形式で入ったリストを返す
        """
        elm_list = []
        for i, item in enumerate(self.items):
            elm_dic = {}
            for node in item.getiterator():
                for target_tag in self.target_tag_list:
                    if node.tag in target_tag:
                        if target_tag == 'suggestion':
                            # 検索候補名
                            elm_dic['value'] = node.get('data')
                        elif target_tag == 'num_queries':
                            # ヒット件数
                            # elm_dic['info'] = node.get('int')
                            elm_dic['info'] = ''
                    else:
                        pass
            i = i + 1
            elm_dic['id'] = i
            elm_list.append(elm_dic)
            if i == self.get_max_count:
                break
        return elm_list
