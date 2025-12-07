import pyxel
class Character:
    """ This class represents the player of the game: Mario and Luigi """

    def __init__(self, x, y, D, max_floors, up, down, side):
        """ This method creates a Character object
            :param x: int. The x position of the character
            :param y: int. The y position of the character
            :param D: int. The distance that the character can move
            :param max_floors: int. The maximum number of floors that the
            character can move
            :param up: the key to move the character up
            :param down: the key to move the character down
            :param side: str. The side of the character
        """
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.D = D
        self.floor = 0
        self.max_floors = max_floors
        self.up = up
        self.down = down
        self.side = side
        self.punish = False
        self.punish_frame = 0
        self.motion = "normal"
        self.timer = 0


    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y


    @property
    def side(self) -> str:
        return self.__side

    @side.setter
    def side(self, side: str):
        if not isinstance(side, str):
            raise TypeError("side must be a string")
        elif not side.lower() == "left" and not side.lower() == "right":
            raise ValueError("side must be left or right")
        self.__side = side


    def move_up(self):
        """ This method moves the character up, if it is not in the maximum
        floor. """
        if self.floor < self.max_floors:
            self.y -= self.D
            self.floor += 1

    def move_down(self):
        """ This method moves the character down, if it is not in the
        minimum floor. """
        if self.floor > 0:
            self.y += self.D
            self.floor -= 1

    def fall_package(self):
        """ This method changes the character's attributes when a package
        falls. """
        self.punish = True
        self.punish_frame = pyxel.frame_count

    def check_package(self, packages):
        """ This method checks if Mario or Luigi picks up the package. If
        the collision is detected, it changes the image/sprite of the
        object depending on the floor Mario or Luigi are or the belt the
        package is. """
        if pyxel.frame_count < self.timer:
            return

        if self.side == "right":
            if self.floor == 0:
                self.motion = "catch1"
                for pkg in packages:
                    if pkg.belt == 0 and abs(
                            pkg.x - self.x) < self.width and abs(
                            pkg.y - self.y) < self.height:
                        self.motion = "normal"
                        self.timer = pyxel.frame_count + 7
            else:
                self.motion = "normal"
                for pkg in packages:
                    if pkg.belt > 0 and abs(
                            pkg.x - self.x) < self.width and abs(
                            pkg.y - self.y) < self.height:
                        self.motion = "leave"
                        self.timer = pyxel.frame_count + 7
        else:
            if self.floor == 2:
                self.motion = "normal"
                for pkg in packages:
                    if pkg.belt == 4 and abs(
                            pkg.x - self.x) < self.width and abs(
                            pkg.y - self.y) < self.height:
                        self.motion = "normal"
                        self.timer = pyxel.frame_count + 7
            else:
                self.motion = "normal"
                for pkg in packages:
                    if pkg.belt < 4 and abs(
                            pkg.x - self.x) < self.width and abs(
                            pkg.y - self.y) < self.height:
                        self.motion = "leave"
                        self.timer = pyxel.frame_count + 7

    def update(self, packages, pause):
        """ This method handles the movement of the objects, if the game is
        not paused. """
        if not pause:
            self.check_package(packages)
            if pyxel.btnp(self.up):
                self.move_up()
            if pyxel.btnp(self.down):
                self.move_down()

            if self.punish and pyxel.frame_count - self.punish_frame >= 60:
                self.punish = False

    def draw(self, pause, pause_frame):
        """ This method changes the image of the characters depending on the
        situation. """
        if pause and pyxel.frame_count - pause_frame < 270:
            if self.side == "right":
                pyxel.blt(200, 56, 0, 64, 16, 16, 16)
            else:
                pyxel.blt(48, 80, 0, 64, 0, 16, 16)
        elif pause or self.punish:
            if self.side == "right":
                pyxel.blt(208, 56, 0, 32, 48, 16, 16)
            else:
                pyxel.blt(28, 104, 0, 16, 48, 16, 16)
        else:
            if self.side == "right":
                if self.motion == "normal":
                    pyxel.blt(self.x, self.y, 0, 32, 0, 16, 16)
                elif self.motion == "leave":
                    pyxel.blt(self.x, self.y, 0, 32, 16, 16, 16)
                elif self.motion == "catch1":
                    pyxel.blt(self.x, self.y, 0, 32, 32, 16, 16)
            else:
                if self.motion == "normal":
                    pyxel.blt(self.x, self.y, 0, 16, 0, 16, 16)
                elif self.motion == "leave":
                    pyxel.blt(self.x, self.y, 0, 16, 16, 16, 16)
                elif self.motion == "catch1":
                    pyxel.blt(self.x, self.y, 0, 16, 32, 16, 16)