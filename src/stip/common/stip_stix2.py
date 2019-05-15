# -*- coding: utf-8 -*-
from stix2.v21.sdo import Identity

#S-TIP オブジェクトに格納する固定値
STIP_IDENTITY_CLASS = 'organization'
STIP_NAME = 'Fujitsu System Integration Laboratories.'

#S-TIP の Identity を作成する
def _get_stip_identname(stip_user=None):
    #identity の name は stip_user の affiliation から
    try:
        name = stip_user.affiliation
        if len(name) == 0:
            name = STIP_NAME
    except:
        #affiliation が取れないもしくは空文字列の場合はデフォルト
        name = STIP_NAME

    stip_identity = Identity(
        identity_class=STIP_IDENTITY_CLASS,
        name = name)
    return stip_identity
