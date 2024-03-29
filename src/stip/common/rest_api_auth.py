def auth_by_api_key(username, api_key):
    if ((username is None) or (api_key is None)):
        return None
    try:
        from ctirs.models.rs.models import STIPUser
        user_doc = STIPUser.objects.get(username=username)
    except Exception:
        return None
    if user_doc is None:
        return None
    return user_doc if user_doc.verify_api_key(api_key) else None
