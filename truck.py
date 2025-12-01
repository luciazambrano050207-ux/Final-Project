import pyxel
class Truck:
    """ This class represents the truck. """
    def __init__(self):
        """ This method creates a Truck object. """
        self.x = 8
        #self.y = 30
        #self.package = 0
        #self.image =
        self.visible = True
        self.package = 0

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
        self.package += 1

    #pydef disappear(self):
        #if self.package == 8:
            #self.visible = False

    #def reappear(self):
        #self.visible = True
        #self.package = 0

    def move(self):
        self.x -= 1

    def update(self):
        if self.package == 8:
            self.move()

    def draw(self):
        if self.package == 0:
            pyxel.blt(self.x, 42, 0, 32, 96, 48, 32)
        elif self.package == 1:
            pyxel.blt(self.x, 42, 0, 88, 40, 48, 48)
        elif self.package == 2:
            pyxel.blt(self.x, 42, 0, 88, 96, 48, 48)
        elif self.package == 3:
            pyxel.blt(self.x, 42, 0, 88, 152, 48, 48)
        elif self.package == 4:
            pyxel.blt(self.x, 42, 0, 88, 208, 48, 48)
        elif self.package == 5:
            pyxel.blt(self.x, 42, 0, 144, 40, 48, 48)
        elif self.package == 6:
            pyxel.blt(self.x, 42, 0, 144, 96, 48, 48)
        elif self.package == 7:
            pyxel.blt(self.x, 42, 0, 144, 152, 48, 48)
        elif self.package == 8 and self.x > 0:
            pyxel.blt(self.x, 42, 0, 144, 208, 48, 48)
