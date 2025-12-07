class Belt:
    """ This class represents the belt. """

    def __init__(self, y, direction, speed):
        """ This method creates the Belt object.
        :param y: int. The y position of the belt
        :param direction: str. The direction of the belt
        :param speed: int. The speed of the belt
        """
        self.y = y
        self.direction = direction
        self.speed = speed


    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        if not isinstance(direction, str):
            raise TypeError("direction must be a string")
        elif direction != "right" and direction != "left":
            raise ValueError("direction must be 'right' or 'left'")
        self.__direction = direction

    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        if not isinstance(speed, int):
            raise TypeError("speed must be an integer")
        elif speed < 0:
            raise ValueError("speed must be >= 0")
        self.__speed = speed