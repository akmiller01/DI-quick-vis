from django.conf import settings

def num(s):
    try:
        return int(s)
    except:
        try:
            return float(s)
        except:
            return s

def notNone(s):
    if s is None or s == "None":
        return ""
    else:
        return s