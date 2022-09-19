import socket
import sys
import pygame
import json
from player import Player
from handler import Handler

def main():

    HOST = '192.168.0.77'
    PORT = 1610

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))


    pygame.init()

    display = pygame.display.set_mode((1000, 1000))
    clock = pygame.time.Clock()

    player = Player(500,500)
    handler = Handler()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                client.close()
                sys.exit()

            handler.handleEvent(event)

        player.tick(handler)

        pygame.draw.rect(display, (0,0,0), (0,0,1000,1000))
        player.render(display)

        msg = player.prep_msg()
        client.send(msg.encode('utf-8'))
        msg = client.recv(1024).decode('utf-8')

        j = json.loads(msg)

        for p in j['players']:
            pygame.draw.circle(display, (0, 100, 255), (p['x'], p['y']), 10)



        pygame.display.update()
        clock.tick(20)


def update(client):

    while True:

        woo = client.recv(1024).decode()

        (x, y) = player_pipe.recv()

        payload = {
            'x' : x,
            'y' : y
        }

        client.send(json.dumps(payload).encode())


if __name__ == '__main__':
    main()
