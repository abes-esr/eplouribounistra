# -*- coding: utf-8 -*-

from os import environ
from os.path import normpath

from .base import *

############################
# Allowed hosts & Security #
############################

ALLOWED_HOSTS = [
    '*'
]


DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
DATABASES['default']['NAME'] = normpath(join(dirname(dirname(SITE_ROOT)),'shared/eplouribousse.db'))
i, k =0, 1
while i <100 and k ==1:
    try:
        DATABASES['{:02d}'.format(i)]['ENGINE'] = 'django.db.backends.sqlite3' #ligne ajoutée suite au problème lors du déploiement en prod sur sbu-epluribousse.unistra.fr
        DATABASES['{:02d}'.format(i)]['NAME'] = normpath(join(dirname(dirname(SITE_ROOT)), 'shared/' + '{:02d}'.format(i) + '.db'))
        i +=1
    except:
        k =0

DEBUG = False #ligne ajoutée suite au problème lors du déploiement en prod sur sbu-epluribousse.unistra.fr
