import codecs


class TLD(object):
    tld_dict_ = None

    # TLD(Top Level Domain)リストを読み込む
    def __init__(self, file_path):
        if TLD.tld_dict_ is not None:
            return
        try:
            tld_dict = {}
            f = codecs.open(file_path, 'r', encoding='utf-8')
            lines = f.readlines()
            f.close()
            for line in lines:
                # 空行、コメント行以外をリストに追加
                if line[:-1] != '' and not line.startswith('//'):
                    tld_dict.update({line[:-1]: ''})

            self.set_dict(tld_dict)
        except Exception as e:
            print(e)
            raise e

    def get_dict(self):
        return TLD.tld_dict_

    def set_dict(self, param):
        TLD.tld_dict_ = param

    def get_tld(self, domain_name):
        # 要素数が長い方をTLDとして採用する
        tld = None
        if domain_name is None:
            return None
        klist = domain_name.split(".")
        for i in range(len(klist)):
            if '.'.join(klist[i:]) in TLD.tld_dict_:
                tld = '.'.join(klist[i:])
                break
        return tld

    def split_domain(self, domain_name):
        # TLDを取得し、TLDを構成する文字列数をカウント
        _tld = self.get_tld(domain_name)
        if _tld is None:
            return (domain_name, None)
        tld_word_num = len(_tld.split('.'))
        # domain名からTLD分の要素を省いた文字列を取得
        domain_list = domain_name.split('.')
        split_domain = '.'.join(domain_list[:tld_word_num * -1])
        # 分割した文字列を tuple にして返却
        return (split_domain, _tld)
