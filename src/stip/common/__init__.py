from django.utils.datastructures import MultiValueDictKeyError


def get_text_field_value(request, item_name, default_value=None, is_trim_end_space=False):
    if request.method == 'GET':
        list_ = request.GET
    elif request.method == 'POST':
        list_ = request.POST
    else:
        return default_value
    try:
        v = list_[item_name]
        if len(v) == 0:
            return default_value
        else:
            if(is_trim_end_space is not False):
                return v
            else:
                return v.strip()
    except MultiValueDictKeyError:
        return default_value
