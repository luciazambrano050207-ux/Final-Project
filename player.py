class Player:
    """This class represent the players of the game.
    """
    def __init__(self,name : str, image: str, start_level: int= 1, end_level:
    int= 3, x_position: int, y_position: int):
        self.name = name
        self.image = image
        self.level = start_level
        self.end_level = end_level
        self.action = "idle"
        self.box = False
        self.x_position = x_position
        self.y_position = y_position
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self.__name = name
    @property
    def image(self):
        return self.__image
    @image.setter
    def image(self, image):
        if not isinstance(image, str):
            raise TypeError("image must be a string")
        self.__image = image
    @property
    def start_level(self):
        return self.__start_level
    @start_level.setter
    def start_level(self, start_level):
        if not isinstance(start_level, int):
            raise TypeError("start_level must be a int")
        self.__start_level = start_level
    @property
    def end_level(self):
        return self.__end_level
    @end_level.setter
    def end_level(self, end_level):
        if not isinstance(end_level, int):
            raise TypeError("end_level must be a int")
        self.__end_level = end_level
    @property
    def action(self):
        return self.__action
    @action.setter
    def action(self, action):
        if not isinstance(action, str):
            raise TypeError("action must be a string")
        self.__action = action
    @property
    def box(self):
        return self.__box
    @box.setter
    def box(self, box):
        if not isinstance(box, bool):
            raise TypeError("box must be a bool")
        self.__box = box
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be a int")
        self.__x = x
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be a int")
        self.__y = y



    def move_up(self):
        if self.level < self.end_level:
            self.level += 1
            self.action = "up"
            print(self.name, "move to platform", self.level)
        else:
            print(self.name, "is at the top")
    def move_down(self):
        if self.level > 1:
            self.level -= 1
            self.action = "down"
            print(self.name, "move to platform", self.level)
        else:
            print(self.name, "is at the bottom")
    def with_box(self):
        if not self.box:
            self.box = True
            self.action = "box"
            print(self.name, "has a box in level", self.level)
   #Me falta cuando el personaje deja la caja en la plataforma