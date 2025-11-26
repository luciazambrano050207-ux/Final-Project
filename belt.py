class Belt:
    """ This class represents the belt """
    def __init__(self, y, direction, speed):
        #(self, direction: str, level:int, speed:float, start_x:int,
        #end_x:int, y_ground: int = 200, y_step: int = -60):

        self.direction = direction
        #self.level = level
        self.speed = speed
        #self.start_x= 0
        #self.end_x = 0
        self.position()
        self.y = y

        #self.end_x = end_x
        #self.y_ground = y_ground
        #self.y_step = y_step
        #self.y = self.y_ground + (level - 1) * self.y_step


    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        if not isinstance(direction, str):
            raise TypeError('direction must be a string')
        self.__direction = direction

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        if not isinstance(level, int):
            raise TypeError('level must be a integer')
        self.__level = level

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if not isinstance(speed, int):
            raise TypeError('speed must be a integer')
        self.__speed = speed

    @property
    def start_x(self):
        return self.__start_x

    @start_x.setter
    def start_x(self, start_x):
        if not isinstance(start_x, int):
            raise TypeError('start_x must be a integer')
        self.__start_x = start_x

    @property
    def end_x(self):
        return self.__end_x

    @end_x.setter
    def end_x(self, end_x):
        if not isinstance(end_x, int):
            raise TypeError('end_x must be a integer')
        self.__end_x = end_x

    @property
    def y_ground(self):
        return self.__y_ground
    @y_ground.setter
    def y_ground(self, y_ground):
        if not isinstance(y_ground, int):
            raise TypeError('y_ground must be a integer')
        self.__y_ground = y_ground
    @property
    def y_step(self):
        return self.__y_step
    @y_step.setter
    def y_step(self, y_step):
        if not isinstance(y_step, int):
            raise TypeError('y_step must be a integer')
        self.__y_step = y_step
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError('y must be a integer')
        self.__y = y

    def position(self):
        """ This method initializes the start_x and end_x attributes
        according to the direction of the belt. """
        if self.direction == 'left':
            self.start_x = 224
            self.end_x = 70
        else:
            self.start_x = 70
            self.end_x = 224

