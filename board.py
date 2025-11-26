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

        self.mario = Character(x=184, y=88, D=32, max_floors=2,
                               up = pyxel.KEY_UP, down = pyxel.KEY_DOWN,
                               side= "right")
        self.luigi = Character(x=66, y=80, D=32, max_floors=2, up=pyxel.KEY_W,
                               down=pyxel.KEY_S, side="left")

        #self.belts_y = [88, 72, 56, 40, 24]
        self.belts = [Belt(88, "left", 2),
                      Belt(72, "right", 2),
                      Belt(56,"left", 2),
                      Belt(40, "right", 2),
                      Belt(24, "left", 2)]
        self.package = Package(self.belts)
        #self.mario_catch_x = 160
        #self.luigi_catch_x = 120


        pyxel.init(self.width, self.height, title="Mario")

        pyxel.load("my_resource.pyxres")

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
        self.package.update()
        self.collisions()
    def collisions(self):
        pkg = self.package

        if pkg.belt == -1 and self.collide(pkg, self.mario):
            pkg.put_belt(0, 160, 88)

        elif pkg.belt == 0 and pkg.x<= 88:
            if self.collide(pkg, self.luigi):
                pkg.advance_belt(1, 88,64)
            else:
                pkg.fall()


        elif pkg.belt == 1 and pkg.x >= 160:

            if self.collide(pkg, self.mario):
                pkg.advance_belt(2, 160, 48)

            else:

                pkg.fall()

        elif pkg.belt == 2 and pkg.x <= 88:

            if self.collide(pkg, self.luigi):

                pkg.advance_belt(3, 88, 32)
            else:

                pkg.fall()

        elif pkg.belt == 3 and pkg.x >= 160:

            if self.collide(pkg, self.mario):

                pkg.advance_belt(4, 160, 16)

            else:
                pkg.fall()
        elif pkg.belt == 4 and pkg.x <= 88:
            if self.collide(pkg, self.luigi):
                pkg.finish = True
            else:
                pkg.fall()

    def collide(self, a, b):
        return (a.x < b.x + b.width and
                a.x + a.width > b.x and
                a.y < b.y + b.height and
                a.y + a.height > b.y)

    # self.collisions()
        #self.collide()






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
        self.package.draw()

        pyxel.bltm(120,0,0,120, 0,16,128)

        # Text in screen without having to do the letters
        pyxel.text(40,5, "Easy", 15)


   # def collide(self):
        #if self.package.x == 160:
           # if (self.mario.floor == 2 * self.package.belt and
              #  self.mario.floor != 0 and self.package.belt != 0):
               # self.package.belt += 1
       # if self.package.x == 88:
           # if ((self.luigi.floor == 0 and self.package.belt == 0) or
               # (self.luigi.floor == 2 * self.package.belt + 1)):
               # self.package.belt += 1

