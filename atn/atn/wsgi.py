"""
WSGI config for atn project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB_DIR = os.path.join(BASE_DIR, 'libs')
sys.path.append(LIB_DIR)
#import pdb; pdb.set_trace()
print('BASE: %s', BASE_DIR)
print('LIBS: %s', LIB_DIR)
print('PPATH: %s', sys.path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'atn.settings')

application = get_wsgi_application()
