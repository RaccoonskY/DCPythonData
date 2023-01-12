import functools
import json

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        not_parsed_result = func(*args, **kwargs)
        return json.dumps(not_parsed_result)
    return wrapped

