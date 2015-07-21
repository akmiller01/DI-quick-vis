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
    
def byteify(input):
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input