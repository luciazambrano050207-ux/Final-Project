import pyxel
class Truck:
    """ This class represents the truck. """

    def __init__(self):
        """ This method creates a Truck object. """
        self.x = 8
        self.package = 0
        self.deliveries = 0
        self.waiting = False
        self.wait_frame = 0


    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        self.__x = x

    @property
    def package(self) -> int:
        return self.__package

    @package.setter
    def package(self, package: int):
        if not isinstance(package, int):
            raise TypeError("package must be an integer")
        elif package < 0:
            raise ValueError("package must be >= 0")
        self.__package = package

    @property
    def deliveries(self) -> int:
        return self.__deliveries

    @deliveries.setter
    def deliveries(self, deliveries: int):
        if not isinstance(deliveries, int):
            raise TypeError("deliveries must be an integer")
        elif deliveries < 0:
            raise ValueError("deliveries must be >= 0")
        self.__deliveries = deliveries

    @property
    def waiting(self) -> bool:
        return self.__waiting

    @waiting.setter
    def waiting(self, waiting: bool):
        if not isinstance(waiting, bool):
            raise TypeError("waiting must be a boolean")
        self.__waiting = waiting

    @property
    def wait_frame(self) -> int:
        return self.__wait_frame

    @wait_frame.setter
    def wait_frame(self, wait_frame: int):
        if not isinstance(wait_frame, int):
            raise TypeError("wait_frame must be an integer")
        self.__wait_frame = wait_frame


    def add_package(self):
        """ This method adds a package to the truck. """
        self.package += 1

    def move(self):
        """ This method moves the truck to the left. """
        self.x -= 0.4

    def update(self, score):
        """ This method checks the delivery cycle. It observes if the 8
        packages have been added, the movement of the truck, and the
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
                self.wait_frame = pyxel.frame_count
        else:
            if pyxel.frame_count - self.wait_frame >= 150:
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