import pyxel
class Character:
    """ This class represents the player of the game: Mario and Luigi """

    def __init__(self, x, y, D , max_floors, up,
                 down, side):
        """ This method creates the Character object
        :param x : the initial x of the character
        :param y : the initial y of the character
        :param img : the index of the image bank
        :param u :  coordinate x of the image in the image bank
        :param v : coordinate y of the image in the image bank
        :param width : the width of the character
        :param height : the height of the character
        :param D : the distance that the character can move
        :param max_floors : the maximum number of floors that the character can move
        :param up : the key to move the character up
        :param down : the key to move the character down
        :param side : the side of the character
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
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be a int")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be a int")
        self.__y = y

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, img):
        if not isinstance(img, int):
            raise TypeError("img must be a int")
        self.__img = img

    @property
    def u(self):
        return self.__u

    @u.setter
    def u(self, u):
        if not isinstance(u, int):
            raise TypeError("u must be a int")
        self.__u = u

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        if not isinstance(v, int):
            raise TypeError("v must be a int")
        self.__v = v

    @property
    def up(self):
        return self.__up

    @up.setter
    def up(self, up):
        if not isinstance(up, int):
            raise TypeError("up must be a int")
        self.__up = up

    @property
    def down(self):
        return self.__down

    @down.setter
    def down(self, down):
        if not isinstance(down, int):
            raise TypeError("down must be a int")
        self.__down = down

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side: str):
        if not isinstance(side, str):
            raise TypeError("side must be a str")
        if not side.lower() == "left" and not side.lower() == "right":
            raise ValueError("The side must be left or right")
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
        """ This method detects if the package is falling. If it falls,
        it punishes the object"""
        self.punish = True
        self.punish_frame = pyxel.frame_count

    def check_package(self, packages):
        """ This method checks if the Mario or Luigi takes the package. If
        the collision is detected, it changes the image/ sprite of the
        object depending on the floor Mario or Luigi are or the belt the
        package is"""
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
        """ This method shows that if the game is not paused, it handles the
        movement of the objects. """
        if not pause:
            self.check_package(packages)
            if pyxel.btnp(self.up):
                self.move_up()
            if pyxel.btnp(self.down):
                self.move_down()

            if self.punish and pyxel.frame_count - self.punish_frame >= 60:
                self.punish = False


    def draw(self, pause, pause_frame):
        """ This method changes the image of the objects depending on the
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