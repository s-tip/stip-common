import stip.common.const as const
from stix2.properties import StringProperty, ReferenceProperty, ListProperty, DictionaryProperty
from stix2.v21.bundle import Bundle
from stix2.v21.sdo import Report, CustomObject, Vulnerability, ThreatActor, Indicator, Identity
from stix2.v21.common import GranularMarking


# S-TIP SNS 用カスタムオブジェクト
@CustomObject(const.STIP_STIX2_X_STIP_SNS_TYPE, [
    ('name', StringProperty(required=True)),
    ('description', StringProperty(required=True)),
    ('created_by_ref', ReferenceProperty(valid_types='identity')),
    ('lang', StringProperty()),
    ('granular_markings', ListProperty(GranularMarking)),
    (const.STIP_STIX2_PROP_TYPE, StringProperty(required=True)),
    (const.STIP_STIX2_PROP_AUTHOR, DictionaryProperty(required=True)),
    (const.STIP_STIX2_PROP_POST, DictionaryProperty()),
    (const.STIP_STIX2_PROP_ATTACHMENT_REFS, ListProperty(DictionaryProperty)),
    (const.STIP_STIX2_PROP_OBJECT_REF, StringProperty()),
    (const.STIP_STIX2_PROP_OBJCET_REF_VERSION, StringProperty()),
    (const.STIP_STIX2_PROP_ATTACHMENT, DictionaryProperty()),
    (const.STIP_STIX2_PROP_TAGS, ListProperty(StringProperty)),
    (const.STIP_STIX2_PROP_INDICATORS, ListProperty(StringProperty)),
    (const.STIP_STIX2_PROP_IDENTITY, StringProperty(required=True)),
    (const.STIP_STIX2_PROP_TOOL, DictionaryProperty(required=True)),
])
class StipSns(object):
    pass
