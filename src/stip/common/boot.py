# -*- coding: utf-8 -*-
import os

def is_skip_sequence():
    is_skip_sequnece = False
    if os.environ.has_key('SKIP_BOOT_SEQUENCE') == True:
        if os.environ['SKIP_BOOT_SEQUENCE'] == 'True':
            is_skip_sequnece = True
    return is_skip_sequnece