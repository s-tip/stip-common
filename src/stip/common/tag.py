import re
import stip.common.const as const

SHARP_UNDERBAR_REG = re.compile('^#_+$')
SHARP_UNDERBAR_NUMERIC_REG = re.compile('^#[_0-9０-９]+$')


def is_tag(word):
    if word[0] != '#':
        return False
    if len(word) == 1:
        return False
    if len(word) > const.MAX_HASHTAG_LENGTH:
        return False
    if re.match(SHARP_UNDERBAR_REG, word):
        return False
    if '#' in word[1:]:
        return False
    if re.match(SHARP_UNDERBAR_NUMERIC_REG, word):
        return False
    return True

