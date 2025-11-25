import pyxel
class Character:
    """This class represents the player of the game: Mario and Luigi"""

    def __init__(self, x, y, img, u, v, width, height, D , max_floors, up,
                 down, floors_y):
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
        """
        self.x = x
        self.y = y
        self.img = img
        self.u = u
        self.v = v
        self.width = width
        self.height = height
        self.D = D
        self.floor = 0
        self.max_floors = max_floors
        self.up = up
        self.down = down


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

    def move_up(self):
        if self.floor < self.max_floors:
            self.y -= self.D
            self.floor += 1

    def move_down(self):
        if self.floor > 0:
            self.y += self.D
            self.floor -= 1

    def update(self):
        if pyxel.btnp(self.up):
            self.move_up()
        if pyxel.btnp(self.down):
            self.move_down()

    def draw(self):
        pyxel.blt(self.x, self.y, self.img, self.u, self.v, self.width, self.height)

