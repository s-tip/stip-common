
from decouple import config


class SessionConfig(object):

    @staticmethod
    def get_session_cokkie_age():
        DEFAULT_VALUE = 60 * 60 * 24
        return int(config(
            'SESSION_COOKIE_AGE',
            DEFAULT_VALUE))

    @staticmethod
    def get_session_expire_at_browser_close():
        DEFAULT_VALUE = False
        v = config('SESSION_EXPIRE_AT_BROWSER_CLOSE', '')
        return v.lower() == 'true' if v else DEFAULT_VALUE

    @staticmethod
    def get_session_cookie_path():
        v = config('SESSION_COOKIE_PATH', '')
        return v if len(v) else None
