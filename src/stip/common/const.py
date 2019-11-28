import os
from django.utils.translation import ugettext_lazy

#SNS feeds.feed_stix より
#Statement Attachement の prefix
MARKING_STRUCTURE_STIP_ATTACHEMENT_CONTENT_PREFIX = 'S-TIP attachement content'
MARKING_STRUCTURE_STIP_ATTACHEMENT_FILENAME_PREFIX = 'S-TIP attachement filename'

#SNS feeds.feed_stix_common より
STIP_SNS_USER_NAME_KEY = 'User Name'
STIP_SNS_SCREEN_NAME_KEY = 'Screen Name'
STIP_SNS_AFFILIATION_KEY = 'Affiliation'
STIP_SNS_REGION_CODE_KEY = 'Region Code'
STIP_SNS_CI_KEY = 'Critical Infrastructure'
STIP_SNS_REFERRED_URL_KEY = 'Referred URL'
STIP_SNS_STIX2_PACKAGE_ID_KEY = 'STIX2 Package ID'

#SNS setteings より
SNS_PROJECT_DIR='/opt/s-tip/sns'
MEDIA_ROOT= SNS_PROJECT_DIR + os.sep + 'media'
MEDIA_URL = '/media/'
ATTACH_FILE_DIR = MEDIA_ROOT + os.sep + 'attach' + os.sep
STIX_FILE_DIR = MEDIA_ROOT + os.sep + 'stix' + os.sep
STIX_CACHE_DIR = MEDIA_ROOT + os.sep + 'cache' + os.sep

CONF_DIR = SNS_PROJECT_DIR + os.sep + 'conf'
CONF_FILE_PATH = CONF_DIR + os.sep + 'sns.conf'

SNS_TOOL_NAME = 'S-TIP'
SNS_TOOL_VENDOR = 'S-TIP Community'
SNS_NA_ACCOUNT = 'na'
SNS_GV_CONCIERGE_ACCOUNT = 'gv_concierge'
SNS_FALCON_CONCIERGE_ACCOUNT = 'falcon_concierge'
SNS_SLACK_BOT_ACCOUNT = 'slack'

#SNS から移植
LANGUAGES = (
    ('en', ugettext_lazy('English')),
    ('pt-br', ugettext_lazy('Portuguese')),
    ('es', ugettext_lazy('Spanish')),
    ('ja', ugettext_lazy('Japanese')),
    ('fr', ugettext_lazy('French')),
    ('zh-cn', ugettext_lazy('Chinese')),
)
#TLPフィールドを追加
TLP_CHOICES = (
    ('RED','RED'),
    ('AMBER','AMBER'),
    ('GREEN','GREEN'),
    ('WHITE','WHITE'),
)

#ROLEフィールドを追加
ROLE_CHOICES = (
    ('admin',               ugettext_lazy('ROLE_CHOICE_admin')),
    ('user',                ugettext_lazy('ROLE_CHOICE_user')),
    ('machine',             ugettext_lazy('ROLE_CHOICE_machine')),
    ('machine_feed_only',   ugettext_lazy('ROLE_CHOICE_machine_feed_only')),
    ('machine_bot',         ugettext_lazy('ROLE_CHOICE_machine_bot')),
)

SECTOR_GROUP_CHOICES=  (
    ('chemical',        ugettext_lazy('SECTOR_GROUP_Chemical Sector')),
    ('commercial',      ugettext_lazy('SECTOR_GROUP_Commercial Facilities Sector')),
    ('communication',   ugettext_lazy('SECTOR_GROUP_Communications Sector')),
    ('critical',        ugettext_lazy('SECTOR_GROUP_Critical Manufacturing Sector')),
    ('dams',            ugettext_lazy('SECTOR_GROUP_Dams Sector')),
    ('defense',         ugettext_lazy('SECTOR_GROUP_Defense Industrial Base Sector')),
    ('emergency',       ugettext_lazy('SECTOR_GROUP_Emergency Services Sector')),
    ('energy',          ugettext_lazy('SECTOR_GROUP_Energy Sector')),
    ('financial',       ugettext_lazy('SECTOR_GROUP_Financial Services Sector')),
    ('food',            ugettext_lazy('SECTOR_GROUP_Food and Agriculture Sector')),
    ('government',      ugettext_lazy('SECTOR_GROUP_Government Facilities Sector')),
    ('healthcare',      ugettext_lazy('SECTOR_GROUP_Healthcare and Public Health Sector')),
    ('information',     ugettext_lazy('SECTOR_GROUP_Information Technology Sector')),
    ('nuclear',         ugettext_lazy('SECTOR_GROUP_Nuclear Reactors, Materials, and Waste Sector')),
    ('other',           ugettext_lazy('SECTOR_GROUP_Other')),
    ('transport',       ugettext_lazy('SECTOR_GROUP_Transportation Systems Sector')),
    ('water',           ugettext_lazy('SECTOR_GROUP_Water and Wastewater Systems Sector')),
)

#CRITICAL_INFRASTRUCTURE
CRITICAL_INFRASTRUCTURE_CHOICES=  (
    ('Information and Communication Services',                                      ugettext_lazy('CI_Information and Communication Services')),
    ('Financial Services',                                                          ugettext_lazy('CI_Financial Services')),
    ('Aviation Services',                                                           ugettext_lazy('CI_Aviation Services')),
    ('Railway Services',                                                            ugettext_lazy('CI_Railway Services')),
    ('Electric Power Supply Services',                                              ugettext_lazy('CI_Electric Power Supply Services')),
    ('Gas Supply Services',                                                         ugettext_lazy('CI_Gas Supply Services')),
    ('Government and Administrative Services (Including Municipal Government)',     ugettext_lazy('CI_Government and Administrative Services (Including Municipal Government)')),
    ('Medical Services',                                                            ugettext_lazy('CI_Medical Services')),
    ('Water Services',                                                              ugettext_lazy('CI_Water Services')),
    ('Logistics Services',                                                          ugettext_lazy('CI_Logistics Services')),
    ('Chemical Industries',                                                         ugettext_lazy('CI_Chemical Industries')),
    ('Credit Card Services',                                                        ugettext_lazy('CI_Credit Card Services')),
    ('Petroleum Industries',                                                        ugettext_lazy('CI_Petroleum Industries')),
    ('Other',                                                                       ugettext_lazy('CI_Other')),
)

SHARING_GROUP_CSC = 'csc'

SHARING_RANGE_TYPE_KEY_ALL = 'all'
SHARING_RANGE_TYPE_KEY_GROUP = 'group'
SHARING_RANGE_TYPE_KEY_PEOPLE = 'people'
SHARING_RANGE_CHOICES=(
    (SHARING_RANGE_TYPE_KEY_ALL, 'With the CSC Community'),
    (SHARING_RANGE_TYPE_KEY_GROUP, 'With a group'),
    (SHARING_RANGE_TYPE_KEY_PEOPLE, 'With people'),
)
