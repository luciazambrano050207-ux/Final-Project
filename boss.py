import pyxel
class Boss:
    """ This class represents the boss. """

    def __init__(self):
        """ This method creates a Boss object. The boss will appear on screen
            every time a package falls to punish Mario or Luigi, and after
            each break, to make them come back to work.
        """
        self.__side = ""
        self.__lives = 3
        self.__punish = False
        self.__punish_frame = 0


    @property
    def side(self) -> str:
        return self.__side

    @property
    def lives(self) -> int:
        return self.__lives

    @property
    def punish(self) -> bool:
        return self.__punish

    @property
    def punish_frame(self) -> int:
        return self.__punish_frame


    def fall_mario(self):
        """ This method changes the boss's attributes when Mario drops a
        package. """
        self.__side = "right"
        self.__lives -= 1
        self.__punish = True
        self.__punish_frame = pyxel.frame_count

    def fall_luigi(self):
        """ This method changes the boss's attributes when Luigi drops a
        package. """
        self.__side = "left"
        self.__lives -= 1
        self.__punish = True
        self.__punish_frame = pyxel.frame_count

    def add_life(self, truck):
        """ This method adds a life when the truck has been completed 3
        times. """
        if truck.deliveries == 3:
            if self.__lives < 3:
                self.__lives += 1
            truck.deliveries = 0

    def update(self, truck):
        """ This method adds a life if 3 deliveries have been completed, by
        calling the add_life method. It also makes the boss disappear after
        60 frames when a package falls. """
        self.add_life(truck)
        if self.__punish and pyxel.frame_count - self.__punish_frame >= 60:
            self.__punish = False

    def draw(self, pause, pause_frame):
        """ This method shows the remaining lives on the screen. It also shows
        the boss when Mario or Luigi drop a package, and when he calls them
        back to work after their break. """
        if self.__lives >= 1:
            pyxel.blt(152, 0, 0, 0, 232, 16, 16)
        if self.__lives >= 2:
            pyxel.blt(168, 0, 0, 0, 232, 16, 16)
        if self.__lives == 3:
            pyxel.blt(184, 0, 0, 0, 232, 16, 16)

        if self.__punish:
            if self.__side == "right":
                pyxel.blt(224, 56, 0, 48, 48, 16, 16)
            else:
                pyxel.blt(14, 104, 0, 48, 16, 16, 16)

        if pause and pyxel.frame_count - pause_frame >= 270:
            pyxel.blt(224, 56, 0, 48, 48, 16, 16)
            pyxel.blt(12, 104, 0, 48, 16, 16, 16)