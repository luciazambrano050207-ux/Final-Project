import pyxel

class Truck:
    """ This class represents the truck. """
    def __init__(self):
        """ This method creates a Truck object. """
        self.x = 8
        #self.y = 30
        #self.package = 0
        #self.image =
        #self.visible = True
        self.package = 0
        self.deliveries = 0
        self.waiting = False
        self.wait_start = 0

    @property
    def package(self) -> int:
        return self.__package

    @package.setter
    def package(self, package: int):
        if not isinstance(package, int):
            raise TypeError("The package must be an int")
        else:
            self.__package = package

    #@property
    #def visible(self) -> bool:
        #return self.__visible

    #@visible.setter
    #def visible(self, visible: bool):
        #if not isinstance(visible, bool):
            #raise TypeError("visible must be a boolean")
        #else:
            #self.__visible = visibles

    def add_package(self):
        """ This method represents that a package have been added to the
        truck"""
        self.package += 1

    def move(self):
        """ This method moves the truck when 8 packages are in the truck. """
        self.x -= 0.4

    def update(self, score):
        """ This method checks the delivery cycle. It observed if the 8
        packages have been added, the movement of the truck and the
        returning of the truck after 150 frames. """
        if not self.waiting:
            if self.package == 8 and self.x == 8:
                score.completed_truck()

            if self.package == 8 and self.x > -47:
                self.move()
            elif self.package == 8 and self.x <= -47:
                self.deliveries += 1
                self.package = 0
                self.waiting = True
                self.wait_start = pyxel.frame_count
        else:
            if pyxel.frame_count - self.wait_start >= 150:
                self.x = 8
                self.waiting = False

    def draw(self):
        """ This method changes the image of the truck according to the
        number of packages. """
        if not self.waiting:
            if self.package == 0:
                pyxel.blt(self.x, 40, 0, 32, 96, 48, 32)
            elif self.package == 1:
                pyxel.blt(self.x, 24, 0, 88, 40, 48, 48)
            elif self.package == 2:
                pyxel.blt(self.x, 24, 0, 88, 96, 48, 48)
            elif self.package == 3:
                pyxel.blt(self.x, 24, 0, 88, 152, 48, 48)
            elif self.package == 4:
                pyxel.blt(self.x, 24, 0, 88, 208, 48, 48)
            elif self.package == 5:
                pyxel.blt(self.x, 24, 0, 144, 40, 48, 48)
            elif self.package == 6:
                pyxel.blt(self.x, 24, 0, 144, 96, 48, 48)
            elif self.package == 7:
                pyxel.blt(self.x, 24, 0, 144, 152, 48, 48)
            elif self.package == 8:
                pyxel.blt(self.x, 24, 0, 144, 208, 48, 48)
