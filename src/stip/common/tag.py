import re
import string
import stip.common.const as const

sharp_underbar_reg = re.compile('^#_+$')
sharp_underbar_numeric_reg = re.compile('^#[_0-9０-９]+$')


def is_tag(word):
    if word[0] != '#':
        return False
    if len(word) == 1:
        return False
    if len(word) > const.MAX_HASHTAG_LENGTH:
        return False
    if re.match(sharp_underbar_reg, word):
        return False
    if '#' in word[1:]:
        return False
    if re.match(sharp_underbar_numeric_reg, word):
        return False
    return True
