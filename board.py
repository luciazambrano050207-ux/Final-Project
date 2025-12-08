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
        self.break_pause = False
        self.break_pause_frame = 0
        self.game_over = False

        self.mario = Character(x=174, y=88, D=32, max_floors=2,
                               up=pyxel.KEY_UP, down=pyxel.KEY_DOWN,
                               side="right")
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

        pyxel.init(self.width, self.height, title="Mario Bros Proyect")
        pyxel.load("assets/my_resource.pyxres")
        pyxel.run(self.update, self.draw)


    def update(self):
        """ This is a pyxel method that gets executed in every iteration of
        the game (every frame). Here is all the code that has to be executed
        in every frame."""
        # To exit the game
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if self.boss.lives == 0:
            self.game_over = True
        if self.game_over:
            return

        self.mario.update(self.packages, self.break_pause)
        self.luigi.update(self.packages, self.break_pause)
        self.truck.update(self.score)
        self.boss.update(self.truck)

        if self.truck.package == 8 and not self.break_pause:
            self.break_pause = True
            self.break_pause_frame = pyxel.frame_count

        if self.break_pause:
            for pkg in list(self.packages):
                pkg.delete(self)
            if pyxel.frame_count - self.break_pause_frame >= 300:
                self.break_pause = False

        if not self.boss.punish and not self.break_pause:
            for package in list(self.packages):
                package.update()
                if package.finish:
                    self.packages.remove(package)

            self.mario.check_package(self.packages)
            self.luigi.check_package(self.packages)
            self.collisions.collision(self.packages, self.mario, self.luigi,
                                  self.boss, self.truck, self.score)

            if len(self.packages) == 0: #If the list is empty, add one package
                self.packages.append(Package(self.belts))
            else:
                if len(self.packages) % 2 == 0: #If the number of packages is
                    # even, if package is in the middle of the last belt,
                    # another package moves
                    if (self.packages[len(self.packages) - 2].belt == 4 and
                        self.packages[len(self.packages) - 2].x <= 120):
                            self.packages.append(Package(self.belts))
                else: #If the number of packages is odd, after 8 moves of the
                    # first package, another package moves
                    if self.packages[len(self.packages) - 1].moves >= 8:
                        self.packages.append(Package(self.belts))


    def draw(self):
        """This is a pyxel method that gets executed in every iteration of the
        game (every frame). Here is all the code to draw the sprites of the
        game. """
        if self.game_over:
            pyxel.cls(0)
            pyxel.bltm(0, 0, 2, 0, 0, 256, 128)
            return

        # Erasing the previous screen
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 256, 128)

        self.mario.draw(self.break_pause, self.break_pause_frame)
        self.luigi.draw(self.break_pause, self.break_pause_frame)
        self.boss.draw(self.break_pause, self.break_pause_frame)
        self.truck.draw()
        for pkg in self.packages:
            pkg.draw()

        pyxel.bltm(120,0,0,120, 0,16,128)
        pyxel.bltm(0, 0, 0, 0, 0, 8,72)

        # Text in screen
        pyxel.text(240,35, "Easy", 0)
        pyxel.text(244, 7, str(self.score), 0)