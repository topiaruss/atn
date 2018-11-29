#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    LIB_DIR = os.path.join(BASE_DIR, 'atn', 'libs')
    sys.path.append(LIB_DIR)
    #import pdb; pdb.set_trace()
    print('BASE: %s', BASE_DIR)
    print('LIBS: %s', LIB_DIR)
    print('PPATH: %s', sys.path)
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'atn.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
