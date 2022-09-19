import threading
import json

from player import Player

class World:

    def __init__(self):

        self.players = []

    def add_player(self, connection, address):

        player = Player(connection, address)
        self.players.append(player)

        thread = threading.Thread(target=self.handle_player_connection, args=(player,))
        thread.start()


    def handle_player_connection(self, player):

        while True:
            msg = player.connection.recv(1024)
            if not msg:
                self.players.remove(player)
                break

            player.update_state(msg.decode('utf-8'))

            msg = self.prep_msg()
            player.connection.send(msg.encode('utf-8'))

        player.connection.close()


    def prep_msg(self):

        payload = {'players' : [player.prep_msg() for player in self.players]}

        return json.dumps(payload)
