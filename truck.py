class Truck:
    """ This class represents a truck. """
    def __init__(self):
        """ This method creates a Truck object by receiving all the
            information needed.
        """
        self.x = 10
        self.y = 30
        self.package = 0
        self.image = "truck.png"
        self.visible = True

    @property
    def package(self) -> int:
        return self.__package

    @package.setter
    def package(self, package: int):
        if not isinstance(package, int):
            raise TypeError("The package must be an int")
        else:
            self.__package = package

    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        if not isinstance(visible, bool):
            raise TypeError("visible must be a boolean")
        else:
            self.__visible = visible

    def add_package(self):
        self.package += 1

    def disappear(self):
        if self.package == 8:
            self.visible = False

    def reappear(self):
        self.visible = True
        self.package = 0