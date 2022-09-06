from stix2.v21.sdo import Identity
from stix2.properties import IDProperty


STIP_ORG_IDENTITY_CLASS = 'organization'
STIP_INDIVIDUAL_IDENTITY_CLASS = 'individual'
STIP_NAME = 'S-TIP'


def _get_stip_organiztaion_identity(stip_user=None):
    try:
        name = stip_user.affiliation
        if len(name) == 0:
            name = STIP_NAME
    except BaseException:
        name = STIP_NAME

    return Identity(
        identity_class=STIP_ORG_IDENTITY_CLASS,
        name=name)


def _get_stip_individual_identity(stip_user):
    if (len(stip_user.identity_id) == 0):
        id = IDProperty('identity').default()
        stip_user.identity_id = id
        stip_user.save()
    else:
        id = stip_user.identity_id
    return Identity(
        id=id,
        name=stip_user.username,
        identity_class='Individual',
        x_stip_sns_account=stip_user.username,
        created_by_ref=id,
        created=stip_user.date_joined,
        modified=stip_user.updated_at,
        allow_custom=True
    )
