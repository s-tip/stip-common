import os
try:
    from django.utils.translation import ugettext_lazy as _
except ImportError:
    from django.utils.translation import gettext_lazy as _

# SNS feeds.feed_stix より
# Statement Attachement の prefix
MARKING_STRUCTURE_STIP_ATTACHEMENT_CONTENT_PREFIX = 'S-TIP attachement content'
MARKING_STRUCTURE_STIP_ATTACHEMENT_FILENAME_PREFIX = 'S-TIP attachement filename'

# SNS feeds.feed_stix_common より
STIP_SNS_USER_NAME_KEY = 'User Name'
STIP_SNS_SCREEN_NAME_KEY = 'Screen Name'
STIP_SNS_AFFILIATION_KEY = 'Affiliation'
STIP_SNS_REGION_CODE_KEY = 'Region Code'
STIP_SNS_CI_KEY = 'Critical Infrastructure'
STIP_SNS_REFERRED_URL_KEY = 'Referred URL'
STIP_SNS_STIX2_PACKAGE_ID_KEY = 'STIX2 Package ID'

STIP_STIX2_X_STIP_SNS_TYPE = 'x-stip-sns'

STIP_STIX2_PROP_TYPE = 'x_stip_sns_type'
STIP_STIX2_PROP_AUTHOR = 'x_stip_sns_author'
STIP_STIX2_PROP_POST = 'x_stip_sns_post'
STIP_STIX2_PROP_ATTACHMENT_REFS = 'x_stip_sns_attachment_refs'
STIP_STIX2_PROP_ATTACHMENTS = 'x_stip_sns_attachments'
STIP_STIX2_PROP_OBJECT_REF = 'x_stip_sns_object_ref'
STIP_STIX2_PROP_BUNDLE_ID = 'x_stip_sns_bundle_id'
STIP_STIX2_PROP_BUNDLE_VERSION = 'x_stip_sns_bundle_version'
STIP_STIX2_PROP_ATTACHMENT = 'x_stip_sns_attachment'
STIP_STIX2_PROP_TAGS = 'x_stip_sns_tags'
STIP_STIX2_PROP_INDICATORS = 'x_stip_sns_indicators'
STIP_STIX2_PROP_IDENTITY = 'x_stip_sns_identity'
STIP_STIX2_PROP_TOOL = 'x_stip_sns_tool'

STIP_STIX2_SNS_AUTHOR_USER_NAME_KEY = 'username'
STIP_STIX2_SNS_AUTHOR_SCREEN_NAME_KEY = 'screen_name'
STIP_STIX2_SNS_AUTHOR_AFFILIATION_KEY = 'affiliation'
STIP_STIX2_SNS_AUTHOR_REGION_CODE_KEY = 'region_code'
STIP_STIX2_SNS_AUTHOR_COUNTRY_CODE_KEY = 'country_code'
STIP_STIX2_SNS_AUTHOR_CI_KEY = 'critical_infrastructure'
STIP_STIX2_SNS_AUTHOR_REFERRED_URL_KEY = 'referred_url'

STIP_STIX2_SNS_POST_TITLE_KEY = 'title'
STIP_STIX2_SNS_POST_DECRIPTION_KEY = 'description'
STIP_STIX2_SNS_POST_TIMESTAMP_KEY = 'timestamp'
STIP_STIX2_SNS_POST_TLP_KEY = 'tlp'
STIP_STIX2_SNS_POST_SHARING_RANGE_KEY = 'sharing_range'
STIP_STIX2_SNS_POST_REFERRED_URL_KEY = 'referred_url'

STIP_STIX2_SNS_TOOL_NAME_KEY = 'name'
STIP_STIX2_SNS_TOOL_VENDOR_KEY = 'vendor'

STIP_STIX2_SNS_ATTACHMENT_FILENAME_KEY = 'file_name'
STIP_STIX2_SNS_ATTACHMENT_CONTENT_KEY = 'content'

STIP_STIX2_SNS_POST_TYPE_POST = 'post'
STIP_STIX2_SNS_POST_TYPE_ATTACHMENT = 'attachment'
STIP_STIX2_SNS_POST_TYPE_LIKE = 'like'
STIP_STIX2_SNS_POST_TYPE_UNLIKE = 'unlike'
STIP_STIX2_SNS_POST_TYPE_COMMENT = 'comment'

STIP_STIX2_SNS_ATTACHMENT_BUNDLE = 'bundle'
STIP_STIX2_SNS_ATTACHMENT_STIP_SNS = 'x_stip_sns'


# SNS setteings より
SNS_PROJECT_DIR = '/opt/s-tip/sns'
MEDIA_ROOT = SNS_PROJECT_DIR + os.sep + 'media'
MEDIA_URL = '/media/'
ATTACH_FILE_DIR = MEDIA_ROOT + os.sep + 'attach' + os.sep
STIX_FILE_DIR = MEDIA_ROOT + os.sep + 'stix' + os.sep
STIX_CACHE_DIR = MEDIA_ROOT + os.sep + 'cache' + os.sep

CONF_DIR = SNS_PROJECT_DIR + os.sep + 'conf'
CONF_FILE_PATH = CONF_DIR + os.sep + 'sns.conf'

#SNS_TOOL_NAME = 'S-TIP'
SNS_TOOL_NAME = 'Seamless Threat Intelligence Platform (S-TIP)'
SNS_TOOL_VENDOR = 'S-TIP Community'
SNS_TOOL_DESCRIPTION = 'S-TIP is a threat intelligence platform to bring down barriers among separate practices of CTI sharing.'
SNS_NA_ACCOUNT = 'na'
SNS_GV_CONCIERGE_ACCOUNT = 'gv_concierge'
SNS_FALCON_CONCIERGE_ACCOUNT = 'falcon_concierge'
SNS_SLACK_BOT_ACCOUNT = 'slack'

# SNS から移植
LANGUAGES = (
    ('en', _('English')),
    ('pt-br', _('Portuguese')),
    ('es', _('Spanish')),
    ('ja', _('Japanese')),
    ('fr', _('French')),
    ('zh-cn', _('Chinese')),
)
# TLPフィールドを追加
TLP_CHOICES = (
    ('RED', 'RED'),
    ('AMBER', 'AMBER'),
    ('GREEN', 'GREEN'),
    ('WHITE', 'WHITE'),
)

# ROLEフィールドを追加
ROLE_CHOICES = (
    ('admin', _('ROLE_CHOICE_admin')),
    ('user', _('ROLE_CHOICE_user')),
    ('machine', _('ROLE_CHOICE_machine')),
    ('machine_feed_only', _('ROLE_CHOICE_machine_feed_only')),
    ('machine_bot', _('ROLE_CHOICE_machine_bot')),
)

SECTOR_GROUP_CHOICES = (
    ('chemical', _('SECTOR_GROUP_Chemical Sector')),
    ('commercial', _('SECTOR_GROUP_Commercial Facilities Sector')),
    ('communication', _('SECTOR_GROUP_Communications Sector')),
    ('critical', _('SECTOR_GROUP_Critical Manufacturing Sector')),
    ('dams', _('SECTOR_GROUP_Dams Sector')),
    ('defense', _('SECTOR_GROUP_Defense Industrial Base Sector')),
    ('emergency', _('SECTOR_GROUP_Emergency Services Sector')),
    ('energy', _('SECTOR_GROUP_Energy Sector')),
    ('financial', _('SECTOR_GROUP_Financial Services Sector')),
    ('food', _('SECTOR_GROUP_Food and Agriculture Sector')),
    ('government', _('SECTOR_GROUP_Government Facilities Sector')),
    ('healthcare', _('SECTOR_GROUP_Healthcare and Public Health Sector')),
    ('information', _('SECTOR_GROUP_Information Technology Sector')),
    ('nuclear', _('SECTOR_GROUP_Nuclear Reactors, Materials, and Waste Sector')),
    ('other', _('SECTOR_GROUP_Other')),
    ('transport', _('SECTOR_GROUP_Transportation Systems Sector')),
    ('water', _('SECTOR_GROUP_Water and Wastewater Systems Sector')),
)

# CRITICAL_INFRASTRUCTURE
CRITICAL_INFRASTRUCTURE_CHOICES = (
    ('Information and Communication Services', _('CI_Information and Communication Services')),
    ('Financial Services', _('CI_Financial Services')),
    ('Aviation Services', _('CI_Aviation Services')),
    ('Railway Services', _('CI_Railway Services')),
    ('Electric Power Supply Services', _('CI_Electric Power Supply Services')),
    ('Gas Supply Services', _('CI_Gas Supply Services')),
    ('Government and Administrative Services (Including Municipal Government)', _('CI_Government and Administrative Services (Including Municipal Government)')),
    ('Medical Services', _('CI_Medical Services')),
    ('Water Services', _('CI_Water Services')),
    ('Logistics Services', _('CI_Logistics Services')),
    ('Chemical Industries', _('CI_Chemical Industries')),
    ('Credit Card Services', _('CI_Credit Card Services')),
    ('Petroleum Industries', _('CI_Petroleum Industries')),
    ('Other', _('CI_Other')),
)

SHARING_GROUP_CSC = 'csc'

SHARING_RANGE_TYPE_KEY_ALL = 'all'
SHARING_RANGE_TYPE_KEY_GROUP = 'group'
SHARING_RANGE_TYPE_KEY_PEOPLE = 'people'
SHARING_RANGE_CHOICES = (
    (SHARING_RANGE_TYPE_KEY_ALL, 'With all'),
    (SHARING_RANGE_TYPE_KEY_GROUP, 'With a group'),
    (SHARING_RANGE_TYPE_KEY_PEOPLE, 'With people'),
)

MAX_HASHTAG_LENGTH = 100
