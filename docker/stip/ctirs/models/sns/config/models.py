# -*- coding: utf-8 -*-
from django.db import models

####################
class SNSConfigManager(models.Manager):
    pass

class SNSConfig(models.Model):
    DEFAULT_SNS_IDENTITY_NAME = 's-tip-sns'
    DEFAULT_SNS_HEADER_TITLE = 'S-TIP'
    DEFAULT_SNS_BODY_COLOR = '#FFFFFF'
    DEFAULT_SNS_VERSION_PATH = '/opt/s-tip/sns/version'
    DEFAULT_SNS_PUBLIC_SUFFIX_LIST_FILE_PATH = '/opt/s-tip/rs/data/public_suffix_list.dat'
    DEFAULT_CIRCL_MONGO_HOST = 'mongo'
    DEFAULT_CIRCL_MONGO_PORT = 27017
    DEFAULT_CIRCL_MONGO_DATABASE = 'circl'
    DEFAULT_ATTCK_MONGO_HOST = 'mongo'
    DEFAULT_ATTCK_MONGO_PORT = 27017
    DEFAULT_ATTCK_MONGO_DATABASE = 'attck'
    DEFAULT_RS_HOST = 'https://localhost:10001/'
    DEFAULT_GV_L2_URL = ''
    DEFAULT_RS_COMMUNITY_NAME = 'Default Community'
    DEFAULT_SMTP_PORT = 25
    DEFAULT_NS_URL = 'http://fsi.fujitsu.com'
    DEFAULT_NS_NAME = 's-tip'
    DEFAULT_SLACK_BOT_CHANNEL = '#s-tip'

    SNS_VERSION = None

    common_cti_extractor_threat_actors_list = models.TextField(max_length=10240,default='')
    common_cti_extractor_white_list = models.TextField(max_length=10240,default='')
    sns_identity_name = models.TextField(max_length=32,default=DEFAULT_SNS_IDENTITY_NAME)
    sns_header_title = models.TextField(max_length=32,default=DEFAULT_SNS_HEADER_TITLE)
    sns_body_color = models.TextField(max_length=32,default=DEFAULT_SNS_BODY_COLOR)
    sns_version_path = models.TextField(max_length=1024,default=DEFAULT_SNS_VERSION_PATH)
    sns_public_suffix_list_file_path = models.TextField(max_length=1024,default=DEFAULT_SNS_PUBLIC_SUFFIX_LIST_FILE_PATH)
    circl_mongo_host = models.TextField(max_length=128,default=DEFAULT_CIRCL_MONGO_HOST)
    circl_mongo_port = models.IntegerField(default=DEFAULT_CIRCL_MONGO_PORT)
    circl_mongo_database = models.TextField(max_length=64,default=DEFAULT_CIRCL_MONGO_DATABASE)
    attck_mongo_host = models.TextField(max_length=128,default=DEFAULT_ATTCK_MONGO_HOST)
    attck_mongo_port = models.IntegerField(default=DEFAULT_ATTCK_MONGO_PORT)
    attck_mongo_database = models.TextField(max_length=64,default=DEFAULT_ATTCK_MONGO_DATABASE)
    cs_custid = models.TextField(max_length=64,default='')
    cs_custkey = models.TextField(max_length=64,default='')
    rs_host = models.TextField(max_length=128,default=DEFAULT_RS_HOST)
    rs_community_name = models.TextField(max_length=64,default=DEFAULT_RS_COMMUNITY_NAME)
    proxy_http = models.TextField(max_length=128,default='')
    proxy_https = models.TextField(max_length=128,default='')
    gv_l2_url = models.TextField(max_length=128,default=DEFAULT_GV_L2_URL)
    jira_host = models.TextField(max_length=128,default='')
    jira_username = models.TextField(max_length=64,default='')
    jira_password = models.TextField(max_length=64,default='')
    jira_project = models.TextField(max_length=64,default='')
    jira_type = models.TextField(max_length=64,default='')
    smtp_port = models.IntegerField(default=DEFAULT_SMTP_PORT)
    smtp_accept_mail_address = models.TextField(max_length=128,default='')
    stix_ns_url = models.TextField(max_length=128,default=DEFAULT_NS_URL)
    stix_ns_name = models.TextField(max_length=128,default=DEFAULT_NS_NAME)
    slack_bot_token = models.CharField(max_length=128, default='')
    slack_bot_channel = models.CharField(max_length=128,default=DEFAULT_SLACK_BOT_CHANNEL)
    
    objects = SNSConfigManager()

    @staticmethod
    def get_sns_config():
        return SNSConfig.objects.get()

    @staticmethod
    def get_value_with_null_check(v,default_value=None):
        if v is None:
            return default_value
        if len(v) is 0:
            return default_value
        return v

    @staticmethod
    def get_common_ta_list():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.common_cti_extractor_threat_actors_list,default_value='')

    @staticmethod
    def get_common_white_list():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.common_cti_extractor_white_list,default_value='')

    @staticmethod
    def get_sns_identity_name():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.sns_identity_name,default_value=SNSConfig.DEFAULT_SNS_IDENTITY_NAME)

    @staticmethod
    def get_sns_header_title():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.sns_header_title,default_value=SNSConfig.DEFAULT_SNS_HEADER_TITLE)

    @staticmethod
    def get_sns_body_color():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.sns_body_color)

    @staticmethod
    def get_sns_version():
        if SNSConfig.SNS_VERSION is not None:
            return SNSConfig.SNS_VERSION
        sns_config = SNSConfig.get_sns_config()
        sns_version_path =  SNSConfig.get_value_with_null_check(sns_config.sns_version_path)
        if sns_version_path is None:
            SNSConfig.SNS_VERSION = ''
        else:
            try:
                with open(sns_version_path,'r') as fp:
                    SNSConfig.SNS_VERSION = fp.readline().strip()
            except IOError:
                SNSConfig.SNS_VERSION = ''
        return SNSConfig.SNS_VERSION

    @staticmethod
    def get_sns_public_suffix_list_file_path():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.sns_public_suffix_list_file_path,default_value=SNSConfig.DEFAULT_SNS_PUBLIC_SUFFIX_LIST_FILE_PATH)

    @staticmethod
    def get_circl_mongo_host():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.circl_mongo_host,default_value=SNSConfig.DEFAULT_CIRCL_MONGO_HOST)

    @staticmethod
    def get_circl_mongo_port():
        sns_config = SNSConfig.get_sns_config()
        return int(sns_config.circl_mongo_port)

    @staticmethod
    def get_circl_mongo_database():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.circl_mongo_database,default_value=SNSConfig.DEFAULT_CIRCL_MONGO_DATABASE)

    @staticmethod
    def get_attck_mongo_host():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.attck_mongo_host,default_value=SNSConfig.DEFAULT_ATTCK_MONGO_HOST)

    @staticmethod
    def get_attck_mongo_port():
        sns_config = SNSConfig.get_sns_config()
        return int(sns_config.attck_mongo_port)

    @staticmethod
    def get_attck_mongo_database():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.attck_mongo_database,default_value=SNSConfig.DEFAULT_ATTCK_MONGO_DATABASE)

    @staticmethod
    def get_cs_custid():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.cs_custid)

    @staticmethod
    def get_cs_custkey():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.cs_custkey)

    @staticmethod
    def get_rs_host():
        sns_config = SNSConfig.get_sns_config()
        if sns_config.rs_host is None:
            rs_host = SNSConfig.DEFAULT_RS_HOST
        elif len(sns_config.rs_host) == 0:
            rs_host =  SNSConfig.DEFAULT_RS_HOST
        else:
            rs_host = sns_config.rs_host
        #最後が / なら除去
        if rs_host.endswith('/') == True:
            return rs_host[:-1]
        return rs_host

    @staticmethod
    def get_rs_regist_stix_url():
        return '%s%s' % (SNSConfig.get_rs_host(),'/api/v1/stix_files')

    #@staticmethod
    #def get_rs_get_stix_url():
    #    return '%s%s' % (SNSConfig.get_rs_host(),'/api/v1/stix_files')

    @staticmethod
    def get_rs_get_matching_url():
        return '%s%s' % (SNSConfig.get_rs_host(),'/api/v1/gv/matched_packages')

    @staticmethod
    def get_rs_get_feeds_url():
        return '%s%s' % (SNSConfig.get_rs_host(),'/api/v1/sns/feeds')

    @staticmethod
    def get_rs_get_content_url():
        return '%s%s' % (SNSConfig.get_rs_host(),'/api/v1/sns/content')

    @staticmethod
    def get_rs_get_related_packages_url():
        return '%s%s' % (SNSConfig.get_rs_host(),'/api/v1/sns/related_packages')

    @staticmethod
    def get_rs_get_comments_url():
        return '%s%s' % (SNSConfig.get_rs_host(),'/api/v1/sns/comments')

    @staticmethod
    def get_rs_get_likers_url():
        return '%s%s' % (SNSConfig.get_rs_host(),'/api/v1/sns/likers')

    @staticmethod
    def get_rs_query_url():
        return '%s%s' % (SNSConfig.get_rs_host(),'/api/v1/sns/query')

    @staticmethod
    def get_rs_get_share_misp_url():
        return '%s%s' % (SNSConfig.get_rs_host(),'/api/v1/sns/share_misp')
    
    @staticmethod
    def get_rs_community_name():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.rs_community_name,default_value=SNSConfig.DEFAULT_RS_COMMUNITY_NAME)

    @staticmethod
    def get_proxy_http():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.proxy_http)

    @staticmethod
    def get_proxy_https():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.proxy_https)

    @staticmethod
    def get_proxies():
        http_proxy = SNSConfig.get_proxy_http()
        https_proxy = SNSConfig.get_proxy_https()
        if http_proxy is None and https_proxy is None:
            return None
        else:
            proxies = {}
            if http_proxy is not None:
                proxies[u'http'] = http_proxy
            if https_proxy is not None:
                proxies[u'https'] = https_proxy
            return proxies

    @staticmethod
    def get_gv_l2_url():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.gv_l2_url,default_value=None)

    @staticmethod
    def get_jira_host():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.jira_host)

    @staticmethod
    def get_jira_username():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.jira_username)

    @staticmethod
    def get_jira_password():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.jira_password)

    @staticmethod
    def get_jira_project():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.jira_project)

    @staticmethod
    def get_jira_type():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.jira_type)

    @staticmethod
    def get_smtp_port():
        sns_config = SNSConfig.get_sns_config()
        return int(sns_config.smtp_port)

    @staticmethod
    def get_smtp_accept_mail_address():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.smtp_accept_mail_address)

    @staticmethod
    def get_stix_ns_url():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.stix_ns_url,default_value=SNSConfig.DEFAULT_NS_URL)

    @staticmethod
    def get_stix_ns_name():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.stix_ns_name,default_value=SNSConfig.DEFAULT_NS_NAME)

    @staticmethod
    def get_slack_bot_token():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.slack_bot_token,default_value=None)

    @staticmethod
    def get_slack_bot_chnnel():
        sns_config = SNSConfig.get_sns_config()
        return SNSConfig.get_value_with_null_check(sns_config.slack_bot_channel,default_value=SNSConfig.DEFAULT_SLACK_BOT_CHANNEL)
    
    class Meta:
        db_table = 'stip_sns_system'
