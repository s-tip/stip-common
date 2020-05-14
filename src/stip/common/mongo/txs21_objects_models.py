import datetime
import mongoengine as me


class StixManifest(me.Document):
    added = me.DateTimeField(default=datetime.datetime.utcnow, required=True)
    object_type = me.StringField(required=True)
    spec_version = me.StringField(default='2.1')
    object_id = me.StringField(required=True)
    versions = me.ListField(me.StringField())
    media_types = me.ListField(me.StringField())
    deleted_versions = me.ListField(me.StringField(), default=[])
    deleted = me.BooleanField(required=True, default=False)

    meta = {
        'db_alias': 'taxii21_alias'
    }

    @staticmethod
    def update_or_create(stix_object, media_types):
        try:
            manifest = StixManifest.objects.get(object_id=stix_object.object_id)
        except me.DoesNotExist:
            manifest = StixManifest()
            manifest.media_types = media_types
            manifest.object_type = stix_object.object_type
            manifest.spec_version = stix_object.spec_version
            manifest.object_id = stix_object.object_id
            manifest.deleted_versions = []
            manifest.deleted = False
        manifest.versions.append(stix_object.modified)
        manifest.save()
        return manifest


class StixObject(me.Document):
    object_value = me.DictField(required=True)
    added = me.DateTimeField(default=datetime.datetime.utcnow, required=True)
    object_type = me.StringField(requierd=True)
    spec_version = me.StringField(default='2.1')
    object_id = me.StringField(required=True)
    created = me.StringField(reqruied=True)
    modified = me.StringField(reqruied=True)
    revoked = me.BooleanField(default=False)
    object_marking_refs = me.ListField(me.StringField())
    created_by_ref = me.StringField()
    labels = me.ListField(me.StringField())
    source_ref = me.StringField()
    target_ref = me.StringField()
    relationship_type = me.StringField()
    manifest = me.ReferenceField(StixManifest)
    deleted = me.BooleanField(default=False)

    meta = {
        'db_alias': 'taxii21_alias'
    }

    @staticmethod
    def create(stix_object, media_types):
        so = StixObject()
        # object_value
        so.object_value = stix_object
        # object_type
        so.object_type = stix_object['type']
        # spec_version
        if 'spec_version' in stix_object:
            so.spec_version = stix_object['spec_version']
        else:
            so.spec_version = '2.1'
        # object_id
        so.object_id = stix_object['id']
        # created
        so.created = stix_object['created']
        # modified
        so.modified = stix_object['modified']
        # revoked
        if 'revoked' in stix_object:
            so.revoked = stix_object['revoked']
        else:
            so.revoked = False
        # object_marking_refs
        if 'object_marking_refs' in stix_object:
            so.object_marking_refs = stix_object['object_marking_refs']
        else:
            so.object_marking_refs = []
        # created_by_ref
        if 'created_by_ref' in stix_object:
            so.created_by_ref = stix_object['created_by_ref']
        else:
            so.created_by_ref = ''
        # labels
        if 'labels' in stix_object:
            so.labels = stix_object['labels']
        else:
            so.labels = []
        # source_ref
        if 'source_ref' in stix_object:
            so.source_ref = stix_object['source_ref']
        # target_ref
        if 'target_ref' in stix_object:
            so.target_ref = stix_object['target_ref']
        # relationship_type
        if 'relationship_type' in stix_object:
            so.relationship_type = stix_object['relationship_type']
        # deleted
        so.deleted = False
        so.save()
        manifest = StixManifest.update_or_create(so, media_types)
        so.manifest = manifest
        so.save()
        return so

    # filtering option
    # type
    # spec_version
    # object id
    # created
    # modified
    # revoked = False
    # ---
    # filtering option (Marlon)
    # source_ref (SRO only)
    # target_ref (SRO only)
    # relationship_type (SRO only)
    # sighting_of_ref (Sighting object only)
    # object_marking_refs (Any object)
    # TLP (object_mrarking_refs)
    # external_ids (in external_references)
    # source_names (in external_references)
    # created_by_ref (Any Object)
    # sectors (Identity only)
    # labels (Any Object)
    # object_refs (Grouoping, Observed-data, Report)
    # value (SCO only)
