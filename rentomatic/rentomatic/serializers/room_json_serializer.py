import json

class RoomJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_seralize = {
                'code': str(o.code),
                'size': o.size,
                'price': o.price,
                'latitude': o.latitude,
                'longitude': o.longitude,
            }
            return to_seralize
        except AttributeError:
            return super().default(o)