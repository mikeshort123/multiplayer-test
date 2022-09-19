import pygame


class Handler():


    def __init__(self):

        self.keyMap = {
            'UP' : 'w',
            'DOWN' : 's',
            'LEFT' : 'a',
            'RIGHT' : 'd'
        }

        self.keyList = {
            self.keyMap[i] : False for i in self.keyMap
        }

        self.keyChanges = []

        self.mousepos = (0,0)

    def reset(self):
        self.keyChanges = []


    def getKeyPressed(self,key):

        return self.keyList[self.keyMap[key]]

    def getKeyChanged(self,key):

        code = self.keyMap[key]
        return code in self.keyChanges



    def handleEvent(self,e):

        if e.type == pygame.KEYDOWN:
            self.setKey(e.unicode, True)

        if e.type == pygame.KEYUP:
            self.setKey(e.unicode, False)

        if e.type == pygame.MOUSEBUTTONDOWN:
            self.setKey("mb" + str(e.button), True)

        if e.type == pygame.MOUSEBUTTONUP:
            self.setKey("mb" + str(e.button), False)

        if e.type == pygame.MOUSEMOTION:
            self.mousepos = e.pos


    def setKey(self, key, mode):
        if key in self.keyList:
            self.keyList[key] = mode

            if mode: self.keyChanges.append(key)
