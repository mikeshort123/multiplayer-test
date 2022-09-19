import socket
import threading
import time
from world import World
from player import Player

def main():

    HOST = '192.168.0.77'
    PORT = 1610

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))

    server.listen()

    world = World()


    while True:

        connection, address = server.accept()
        world.add_player(connection, address)



if __name__ == '__main__':
    main()
