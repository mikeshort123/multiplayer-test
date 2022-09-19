import json

class Player:

    def __init__(self, connection, address):

        self.connection = connection
        self.address = address

        self.x = 0
        self.y = 0

    def update_state(self, msg):

        j = json.loads(msg)
        self.x = j['x']
        self.y = j['y']

    def prep_msg(self):

        payload = {
            'x' : self.x,
            'y' : self.y
        }

        return payload
