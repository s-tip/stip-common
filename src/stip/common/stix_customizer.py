import re
import json
from stix2 import registry
from stix2.properties import StringProperty, DictionaryProperty
from stix2.v21.sdo import CustomObject


class StixCustomizer(object):
    __instance = None
    ALLOWD_TYPE = ['string', 'list', 'dictionary']

    @staticmethod
    def get_instance():
        if StixCustomizer.__instance is None:
            StixCustomizer()
        return StixCustomizer.__instance

    def __init__(self):
        if StixCustomizer.__instance is not None:
            raise Exception('Use get_instance method.')
        else:
            StixCustomizer.__instance = self
        self.conf_json = None
        self.custom_objects = []
        self.custom_properties = []
        self.custom_objects_dict = {}
        self.conf_file_path = ''

    def update_customizer_conf(self, conf_json):
        with open(self.conf_file_path, 'w', encoding='utf-8') as fp:
            json.dump(conf_json, fp, indent=4, ensure_ascii=False)
        self.init_customizer_conf(self.conf_file_path)

    def init_customizer_conf(self, conf_file_path):
        self.conf_file_path = conf_file_path
        with open(conf_file_path, 'r', encoding='utf-8') as fp:
            j = json.load(fp)
        objects = []
        custom_objects_dict = {}
        if 'objects' in j:
            for o_ in j['objects']:
                if 'name' not in o_:
                    print('No name in an object. skip!!')
                    continue
                if not o_['name'].startswith('x-'):
                    print('Invalid name. skip!!: ' + o_['name'])
                    continue
                if 'properties' not in o_:
                    print('No properties in an object. skip!!')
                    continue
                properties = []
                co_properties = []
                for prop in o_['properties']:
                    if 'name' not in prop:
                        print('No name in a property. skip!!')
                        continue
                    if not prop['name'].startswith('x_'):
                        print('Invalid name. skip!!: ' + prop['name'])
                        continue
                    # if 'required' not in prop:
                    #    print('No required in a property. skip!!')
                    #    continue
                    if 'type' not in prop:
                        print('No type in a property. skip!!')
                        continue
                    if prop['type'] not in self.ALLOWD_TYPE:
                        print('Invalid type. skip!!: ' + prop['type'])
                        continue

                    if prop['type'] == 'dictionary':
                        co_properties.append((prop['name'], DictionaryProperty(required=False)))
                        for k in prop['dictionary']:
                            new_prop = prop.copy()
                            new_prop['name'] = '%s/%s' % (prop['name'], k)
                            custom_objects_dict = self._append_custom_object_dict(
                                custom_objects_dict, o_['name'], new_prop['name'])
                            new_prop['pattern'] = self._get_pattern(prop['dictionary'][k])
                            del(new_prop['dictionary'])
                            properties.append(new_prop)
                    elif prop['type'] == 'string':
                        co_properties.append((prop['name'], StringProperty(required=False)))
                        custom_objects_dict = self._append_custom_object_dict(
                            custom_objects_dict, o_['name'], prop['name'])
                        prop['pattern'] = self._get_pattern_type_string(prop)
                        properties.append(prop)

                co_properties.append(('name', StringProperty(required=True)))
                co_properties.append(('description', StringProperty(required=True)))
                if(o_['name'] in registry.STIX2_OBJ_MAPS['2.1']['objects']):
                    del(registry.STIX2_OBJ_MAPS['2.1']['objects'][o_['name']])
                @CustomObject(o_['name'], co_properties)
                class CutomObjectTemp:
                    pass
                o_['properties'] = properties
                o_['class'] = CutomObjectTemp
                objects.append(o_)
        self.conf_json = {
            'objects': objects
        }
        for key in custom_objects_dict:
            custom_objects_dict[key] = sorted(list(set(custom_objects_dict[key])))
        self.custom_objects_dict = custom_objects_dict

    def _get_pattern_type_string(self, prop):
        if 'regexp' in prop:
            return self._get_pattern(prop['regexp'])
        return None

    def _get_pattern(self, pattern):
        if pattern is None:
            return
        try:
            return re.compile(pattern)
        except Exception:
            print('Invalid regexp. skip!!: ' + pattern)
            return None

    def _append_custom_object_dict(self, d, obj_name, prop_name):
        if obj_name in d:
            if prop_name not in d[obj_name]:
                d[obj_name].append(prop_name)
        else:
            d[obj_name] = [prop_name]
        return d

    def get_custom_object_list(self):
        if not hasattr(self, 'custom_objects_dict'):
            return []
        return sorted(self.custom_objects_dict.keys())

    def get_custom_object_dict(self):
        if not hasattr(self, 'custom_objects_dict'):
            return {}
        return self.custom_objects_dict

    def get_custom_objects(self):
        if self.conf_json is None:
            return None
        if 'objects' not in self.conf_json:
            return None
        return self.conf_json['objects']
