import django
import os
import sys

# DJANGO INTEGRATION

sys.path.append(os.path.dirname(os.path.abspath('.')))
# Do not forget the change iCrawler part based on your project name
os.environ['DJANGO_SETTINGS_MODULE'] = 'umbrellaFarms.settings'


# This is required only if Django Version > 1.8
django.setup()

# DJANGO INTEGRATION
