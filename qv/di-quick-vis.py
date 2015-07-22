import webbrowser
import sys
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qv.settings")
import Cookie
import htmlentitydefs
import HTMLParser
import core
import core.views
import core.admin
import core.forms
import core.utils
import core.models

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    try:
        url = sys.argv[1]
    except:
        url = "127.0.0.1:8000"
        
    from django.conf import settings
    print(settings.BASE_DIR)
    
    fullUrl = "http://"+url
    webbrowser.open(fullUrl)
    print("Opening "+fullUrl)
    
    execute_from_command_line(['manage.py','runserver',url,'--noreload'])