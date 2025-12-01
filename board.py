import pyxel
from character import Character
from boss import Boss
from belt import Belt
from package import Package
from truck import Truck
from collisions import Collisions
from score import Score


class Board:
    """ This class represents the board of the game. """

    def __init__(self, width: int, height: int):
        """ Method that creates the board.
        :param width: The width of the board
        :param height: The height of the board
        """
        self.width = width
        self.height = height

        self.mario = Character(x=174, y=88, D=32, max_floors=2,
                               up = pyxel.KEY_UP, down = pyxel.KEY_DOWN,
                               side= "right")
        self.luigi = Character(x=66, y=80, D=32, max_floors=2, up=pyxel.KEY_W,
                               down=pyxel.KEY_S, side="left")
        self.boss = Boss()
        self.truck = Truck()
        self.packages = []
        self.score = Score()
        self.collisions = Collisions()
        self.belts = [Belt(88, "left", 2),
                      Belt(72, "right", 2),
                      Belt(56,"left", 2),
                      Belt(40, "right", 2),
                      Belt(24, "left", 2)]


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
        """ This is a pyxel method that gets executed in every iteration of
        the game (every frame). Here is all the code that has to be executed
        in every frame."""
        # To exit the game
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.mario.update()
        self.luigi.update()
        self.truck.update()
        for package in self.packages:
            package.update()
            if package.fall:
                self.packages.remove(package)

        self.collisions.collision(self.packages, self.mario, self.luigi, self.boss,
               self.truck, self.score)

        if len(self.packages) == 0: #If the list is empty, add one package
            self.packages.append(Package(self.belts))
        else:
            if len(self.packages) % 2 == 0: #If the number of package is
                # even, if number of belt is the last one and it's in the
                # middle of this belt, another package moves.
                if (self.packages[len(self.packages) - 2].belt == 4 and
                    self.packages[len(self.packages) - 2].x <= 120):
                        self.packages.append(Package(self.belts))
            else: #If the number of package is odd, after, 8 moves of the
                # first package, another package moves
                if self.packages[len(self.packages) - 1].moves >= 8:
                    self.packages.append(Package(self.belts))

    def draw(self):
        """This is a pyxel method that gets executed in every iteration of the
        game (every frame). Here is all the code to draw the sprites of the
        game. """
        if self.boss.lives == 0:
            pyxel.bltm(0, 0, 2, 0, 0, 256, 128)
        else:
            # Erasing the previous screen
            pyxel.cls(0)
            pyxel.bltm(0, 0, 0, 0, 0, 256, 128)

            # Drawing the characters and packages
            self.mario.draw()
            self.luigi.draw()
            self.boss.draw()
            self.truck.draw()
            for pkg in self.packages:
                pkg.draw()

            pyxel.bltm(120,0,0,120, 0,16,128)
            pyxel.bltm(0, 0, 0, 0, 0, 8,72)

            # Text in screen without having to do the letters
            pyxel.text(40,5, "Easy", 15)
            pyxel.text(244, 7, str(self.score), 0)qa
