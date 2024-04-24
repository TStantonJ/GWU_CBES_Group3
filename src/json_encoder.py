import json
from bson import ObjectId
from datetime import datetime

class JSONEncoder(json.JSONEncoder):
    """
        Extended JSONEncoder for converting ObjectId and datetime to str.

        Use like this: json.dumps(document, cls=JSONEncoder)
    """
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        elif isinstance(o, datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")
        return json.JSONEncoder.default(self, o)

