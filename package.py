import pyxel
class Package:
    """ This class represents a package. """
    def __init__(self, y, D):
        """ This method creates a Package object by receiving all the
        information needed. Every package will have the same values for the
        attributes when we create them."""
        self.x = 256
        self.y = y
        self.img = 0
        self.u = 16
        self.v = 160
        self.width = 8
        self.height = 4
        self.D = D
        self.direction = "left"
        self.side = "right"
        self.at_truck = False
        self.visible = True

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        if not isinstance(x, int):
            raise TypeError("The x must be an int")
        elif x < 0:
            raise ValueError("The x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        if not isinstance(y, int):
            raise TypeError("The y must be an int")
        elif y < 0:
            raise ValueError("The y must be >= 0")
        else:
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
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        if not isinstance(direction, str):
            raise TypeError("The direction must be a string")
        if not direction.lower() == "left" and not direction.lower() == "right":
            raise ValueError("The direction must be left or right")
        else:
            self.__direction = direction.lower()

    @property
    def side(self) -> str:
        return self.__side

    @side.setter
    def side(self, side: str):
        if not isinstance(side, str):
            raise TypeError("The side must be a string")
        if not side.lower() == "left" and not side.lower() == "right":
            raise ValueError("The side must be left or right")
        else:
            self.__side = side.lower()

    @property
    def at_truck(self) -> bool:
        return self.__at_truck

    @at_truck.setter
    def at_truck(self, at_truck: bool):
        if not isinstance(at_truck, bool):
            raise TypeError("The at_truck must be a boolean")
        else:
            self.__at_truck = at_truck

    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        if not isinstance(visible, bool):
            raise TypeError("visible must be a boolean")
        else:
            self.__visible = visible

    def update(self):
        self.x -=self.D
        if self.x < -self.width:
            self.x = 256
    def draw(self):
        pyxel.blt(self.x, self.y, self.img, self.u, self.v, self.width, self.height)


