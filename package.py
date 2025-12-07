import time
import pyxel
class Package:
    """ This class represents a package. """

    def __init__(self, belts):
        """ This method creates a Package object. """
        self.belts = belts
        self.belt = 0
        self.x = 224
        self.y = 82
        # self.img = 0
        # self.u = 32
        # self.v = 64
        self.width = 16
        self.height = 16
        self.D = 8
        self.direction = "left"
        self.time = time.time()
        self.side = "right"
        self.on_belt = True
        self.fall = False
        self.at_truck = False
        self.finish = False
        self.fall_frame = 0
        self.moves = 0

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        if not isinstance(x, int):
            raise TypeError("The x must be an int")
        if x < 0:
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


    def move(self):
        """ This method moves the package a distance D according to the
        direction. """
        if self.direction == "left":
            self.x -= self.D
        else:
            self.x += self.D

    def put_belt(self, belt, new_x, new_y):
        """ This method represents that the package has been transfer to the next belt"""
        self.belt = belt
        self.x = new_x
        self.y = new_y
        self.direction = self.belts[belt].direction
        self.on_belt = True

    def fall_package(self):
        """ This method changes the attribute fall of the package when it
        falls. """
        self.fall = True
        self.fall_frame = pyxel.frame_count
        #""" This method returns True if the package is at the end of the
        #belt and False otherwise. """
        #if self.belt < 0:
            #return False
        #if self.direction == "left":
            #return self.x <= self.belts[self.belt].end_x
        #else:
            #return self.x >= self.belts[self.belt].end_x

    def change_sides(self):
        """ This method changes the attribute side of the package when it
        moves from one side of the screen to the other. """
        if self.x <= 128:
            self.side = "left"
        if self.x >= 128:
            self.side = "right"

    def delete(self, board):
        """ This method deletes the package from the list"""
        if self.belt == 0:
            if 186 <= self.x <= 194 or self.x <= 88:
                board.packages.remove(self)
        elif self.belt == 1 or self.belt == 3:
            if self.x >= 154:
                board.packages.remove(self)
        elif self.belt == 2 or self.belt == 4:
            if self.x <= 88:
                board.packages.remove(self)

    def update(self):
        """ It controls the movement of the package, the speed of it and
        what happens if the package falls. """
        if not self.fall and not self.at_truck:
            if time.time() - self.time > 0.4:
                self.move()
                self.time = time.time()
                self.moves += 1
        elif self.fall:
            if pyxel.frame_count - self.fall_frame >= 30:
                self.finish = True

    def draw(self):
        """ This method shows the changes of the image of the package at
        certain points of the belts. """
        self.change_sides()
        if not self.fall and not self.at_truck:
            if self.side == "right":
                if self.belt == 0:
                    pyxel.blt(self.x, self.y, 0, 32,64,16,8)
                elif self.belt == 1 or self.belt == 2:
                    pyxel.blt(self.x, self.y, 0,32, 72,16,8)
                else:
                    pyxel.blt(self.x, self.y, 0 , 32, 80, 16, 8)
            else:
                if self.belt == 0 or self.belt == 1:
                    pyxel.blt(self.x, self.y, 0, 48,64, 16, 8)
                elif self.belt == 2 or self.belt == 3:
                    pyxel.blt(self.x, self.y, 0, 48, 72, 16, 8)
                else:
                    pyxel.blt(self.x, self.y, 0, 48, 80, 16, 8)
        elif self.fall:
            if self.side == "right":
                if self.belt == 0:
                    pyxel.blt(209,112, 0, 0, 120,16, 8)
                else:
                    pyxel.blt(160, 112, 0, 0, 120, 16, 8)
            else:
                pyxel.blt(80, 112, 0, 0, 120, 16, 8)