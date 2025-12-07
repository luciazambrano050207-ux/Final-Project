class Belt:
    """ This class represents the belt. """
    def __init__(self, y, direction, speed):
        self.y = y
        self.direction = direction
        self.speed = speed


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError('y must be a integer')
        self.__y = y

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        if not isinstance(direction, str):
            raise TypeError('direction must be a string')
        self.__direction = direction

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if not isinstance(speed, int):
            raise TypeError('speed must be a integer')
        self.__speed = speed