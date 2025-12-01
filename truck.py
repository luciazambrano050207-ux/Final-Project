import pyxel
class Truck:
    """ This class represents the truck. """
    def __init__(self):
        """ This method creates a Truck object. """
        #self.x = 10
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

    def draw(self):
        if self.package < 8:
            pyxel.blt(8, 42, 0, 32, 96, 48, 32)