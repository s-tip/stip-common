import json


class MatchingCustomizer(object):
    __instance = None

    @staticmethod
    def get_instance():
        if MatchingCustomizer.__instance is None:
            MatchingCustomizer()
        return MatchingCustomizer.__instance

    def __init__(self):
        if MatchingCustomizer.__instance is not None:
            raise Exception('Use get_instance method.')
        else:
            MatchingCustomizer.__instance = self
        self.conf_json = None
        self.conf_file_path = ''

    def update_customizer_conf(self, conf_json):
        with open(self.conf_file_path, 'w', encoding='utf-8') as fp:
            json.dump(conf_json, fp, indent=4, ensure_ascii=False)
        self.init_customizer_conf(self.conf_file_path)

    def init_customizer_conf(self, conf_file_path):
        self.conf_file_path = conf_file_path
        try:
            with open(conf_file_path, 'r', encoding='utf-8') as fp:
                j = json.load(fp)
        except Exception:
            return
        matching_patterns = []
        if 'matching_patterns' in j:
            for pattern in j['matching_patterns']:
                matching_pattern = {}
                if 'name' not in pattern:
                    print('No name in a matching_pattern. skip!!')
                    continue
                for p in matching_patterns:
                    if p['name'] == pattern['name']:
                        print('Duplicate a name. skip!!')
                        continue
                matching_pattern['name'] = pattern['name']
                matching_pattern['type'] = pattern['type']
                if 'targets' not in pattern:
                    print('No targets in a matching_pattern. skip!!')
                    continue
                if not isinstance(pattern['targets'], list):
                    print('Invalid targets. skip!!')
                    continue
                targets = []
                for target in pattern['targets']:
                    if 'object' not in target:
                        print('No object in a target. skip!!')
                        continue
                    if 'property' not in target:
                        print('No property in a target. skip!!')
                        continue
                    l_ = target['property'].split('/')
                    prop = '--'.join(l_)
                    type_ = '%s:%s' % (target['object'], prop)
                    if type_ in targets:
                        print('Duplicate a matching elemnt. skip!!')
                        continue
                    targets.append(type_)
                if len(targets) < 2:
                    print('Too few targets in a target. skip!!')
                    continue
                matching_pattern['targets'] = targets
                matching_patterns.append(matching_pattern)

        self.conf_json = {
            'matching_patterns': matching_patterns
        }

    def get_matching_patterns(self):
        if self.conf_json is None:
            return []
        if 'matching_patterns' not in self.conf_json:
            return []
        return self.conf_json['matching_patterns']
