import json 


def is_json(data):
    try:
        valid_json = json.loads(data)
        valid = True
    except:
        valid = False   
    return valid