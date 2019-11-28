import os

def is_skip_sequence():
    is_skip_sequnece = False
    if ('SKIP_BOOT_SEQUENCE' in os.environ) == True:
        if os.environ['SKIP_BOOT_SEQUENCE'] == 'True':
            is_skip_sequnece = True
    return is_skip_sequnece
