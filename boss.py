import pyxel
class Boss:
    """ This class represents the boss. """
    def __init__(self):
        """ This method creates the Boss object by receiving all the
            information needed. The boss will appear on screen every time a
            package falls to punish Mario or Luigi, and after each break, to
            make them come back to work.
            :param x: int. The x coordinate of the boss
            :param y: int. The y coordinate of the boss
            :param img : The index of the image bank
            :param u :  Coordinate x of the image in the image bank
            :param v : Coordinate y of the image in the image bank
            :param width : The width of the boss
            :param height : The height of the boss
        """
        #self.x = x
        #self.y = y
        #self.img = img
        #self.u = u
        #self.v = v
        #self.width = width
        #self.height = height
        self.pkg_fall = 0
        #self.visible = False
        self.punish = False
        self.finish_break = False


    #def disappear(self):
        #if self.at_truck and Truck.package == 8:
            #self.visible = False
        #if not self.active and self.side == "left" and self.x == 50 \
                #and self.y == 0:
            #self.visible = False

    def fall_mario(self):
        self.side = "right"
        self.pkg_fall += 1
        self.punish = True

    def fall_luigi(self):
        self.side = "left"
        self.pkg_fall += 1
        self.punish = True

    def draw(self):
        if self.punish:
            if self.side == "right":
                pyxel.blt(224, 56, 0, 48, 48, 16, 16)
            else:
                pyxel.blt(8, 104, 0, 48, 16, 16, 16)
        if self.finish_break:
            pyxel.blt(224, 56, 0, 48, 48, 16, 16)
            pyxel.blt(8, 104, 0, 48, 16, 16, 16)


    #@property
    #def x(self) -> int:
        #return self.__x

    #@x.setter
    #def x(self, x: int):
        #if not isinstance(x, int):
            #raise TypeError("The x must be an int")
        #elif x < 0:
            #raise ValueError("The x must be >= 0")
         #else:
            #self.__x = x

    #@property
    #def y(self) -> int:
        #return self.__y

    #@y.setter
    #def y(self, y: int):
        #if not isinstance(y, int):
            #raise TypeError("The y must be an int")
        #elif y < 0:
            #raise ValueError("The y must be >= 0")
        #else:
            #self.__y = y

    #@property
    #def img(self):
        #return self.__img

    #@img.setter
    #def img(self, img):
        #if not isinstance(img, int):
            #raise TypeError("img must be a int")
        #self.__img = img

    #@property
    #def u(self):
        #return self.__u

    #@u.setter
    #def u(self, u):
        #if not isinstance(u, int):
            #raise TypeError("u must be a int")
        #self.__u = u

    #@property
    #def v(self):
        #return self.__v

    #@v.setter
    #def v(self, v):
        #if not isinstance(v, int):
            #raise TypeError("v must be a int")
        #self.__v = v

    #def move_right(self):
        #self.x += self.D

    #def move_left(self):
        #self.x -= self.D