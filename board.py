import pyxel
from character import Character
from belt import Belt
from package import Package

class Board:
    """The board of the game"""

    def __init__(self, width: int, height: int):
        """ Method that creates the board.
        :param width: The width of the board
        :param height: The height of the board
        """
        self.width = width
        self.height = height

        self.mario = Character(x=184, y=88, img=0, u=32, v=0, width=16,
                               height=16, D=32, max_floors=2,
                               up = pyxel.KEY_UP, down = pyxel.KEY_DOWN)
        self.luigi = Character(x=66, y=80, img=0, u=16, v=0, width=16,
                               height=16, D=32, max_floors=2, up=pyxel.KEY_W,
                               down=pyxel.KEY_S)
        self.floors_y = [120, 96, 72, 48, 24]
        self.belts = [Belt(120, "left", 1), Belt(96, "right", 1),Belt(72,
            "left", 1), Belt(48, "right", 1),
                      Belt(24, "left", 1)]
        start_belt = self.belts[0]
        if self.belts[0].direction == "left":
            start_x = 240
        else:
            start_x = 20
        self.package= (start_belt, start_x)
        pyxel.init(self.width, self.height, title="Mario")

        pyxel.load("assets/my_resource.pyxres")

        pyxel.run(self.update, self.draw)

    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height

    @width.setter
    def width(self, width: int):
        if not isinstance(width, int):
            raise TypeError("The width must be an integer " + str(type(width)) + "is provided")
        elif width < 1 or width > 256:
            raise ValueError("The width must be in the range 1 to 256")
        else:
            self.__width = width

    @height.setter
    def height(self, height: int):
        if not isinstance(height, int):
            raise TypeError("The height must be an integer " + str(type(height)) + "is provided")
        elif height < 1 or height > 256:
            raise ValueError("The height must be in the range 1 to 256")
        else:
            self.__height = height


    def update(self):
        """ This is a pyxel method that gets executed in every iteration of the game (every
        frame). You need to put here all the code that has to be executed in every frame. Now
        it contains only the logic to move the character if a key is pressed."""
        # To exit the game
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.mario.update()
        self.luigi.update()
        if self.package is None:
            return
        self.package.update()

        if self.package.belt.direction == "left" and self.package.x <= 20:
            self



    def draw(self):
        """This is a pyxel method that gets executed in every iteration of the game (every
        frame). You need to put here all the code to draw the sprites of the game.
        """
        # Erasing the previous screen
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 256, 128)
        # Drawing the character, parameters of pyxel.blt are (x, y, sprite tuple)

        self.mario.draw()
        self.luigi.draw()
        #self.package.draw()

        pyxel.text(40,50, "Medium", 15) #Text en pantalla sin necesidad de
    # hacer las letras0