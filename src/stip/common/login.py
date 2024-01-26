import pyotp
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.utils import translation
from django.utils.datastructures import MultiValueDictKeyError
from stip.common import get_text_field_value
from ctirs.models import STIPUser as User


def _get_login_authcode(request):
    return get_text_field_value(request, 'authcode', default_value='')


def login(request, redirect_to, password_modified_to='password_modified'):
    if request.user.is_authenticated:
        return redirect(redirect_to)

    replace_dict = {}
    user = None
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
    except MultiValueDictKeyError:
        return render(request, 'cover.html', replace_dict)
    if user:
        if len(user.api_key) == 0:
            api_key = user.change_api_key()
            user.api_key = api_key
            user.save()
        request.session['username'] = str(user)
        if user.totp_secret is None:
            auth_login(request, user)
            request = set_language_setting(request, user)
            if not user.is_modified_password:
                return redirect(password_modified_to)
            return redirect(redirect_to)
        else:
            return render(request, 'cover_totp.html')
    else:
        replace_dict['error_msg'] = 'Login Failed'
        return render(request, 'cover.html', replace_dict)


def login_totp(request, redirect_to, password_modified_to='password_modified'):
    if request.user.is_authenticated:
        return redirect(redirect_to)

    replace_dict = {}
    username = request.session.get('username', None)
    if not username:
        return render(request, 'cover.html', replace_dict)
    authcode = _get_login_authcode(request)
    user = User.objects.get(username=username)
    totp = pyotp.TOTP(user.totp_secret)

    if totp.verify(authcode):
        auth_login(request, user)
        request = set_language_setting(request, user)
        if not user.is_modified_password:
            return redirect(password_modified_to)
        return redirect(redirect_to)
    else:
        replace_dict['error_msg'] = 'Two-factor authentication failed.'
        return render(request, 'cover_totp.html', replace_dict)


def set_language_setting(request, stip_user):
    lang = stip_user.language
    request.session['_language'] = lang
    translation.activate(lang)
    return request
