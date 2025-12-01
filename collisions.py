class Collisions:
    """ This class represents the collisions between two objects. """
    def __init__(self):
        pass

    def collide(self, a, b):
        return (a.x < b.x + b.width and
                a.x + a.width > b.x and
                a.y < b.y + b.height and
                a.y + a.height > b.y)

    def collision(self, packages, mario, luigi, boss, truck, score):
        for pkg in packages:
            if not pkg.fall:
                if pkg.belt == 0 and 180 <= pkg.x <= 186:
                    if self.collide(pkg, mario):
                        pkg.put_belt(0, 156, 82)
                        score.pkg_delivered()

                    else:
                        pkg.fall_package()
                        mario.fall_package()
                        boss.fall_mario()

                elif pkg.belt == 0 and pkg.x <= 80:
                    if self.collide(pkg, luigi):
                        pkg.put_belt(1, 84,66)
                        score.pkg_delivered()

                    else:
                        pkg.fall_package()
                        luigi.fall_package()
                        boss.fall_luigi()

                elif pkg.belt == 1 and pkg.x >= 162:
                    if self.collide(pkg, mario):
                        pkg.put_belt(2, 156, 50)
                        score.pkg_delivered()

                    else:
                        pkg.fall_package()
                        mario.fall_package()
                        boss.fall_mario()

                elif pkg.belt == 2 and pkg.x <= 80:
                    if self.collide(pkg, luigi):
                        pkg.put_belt(3, 84, 34)
                        score.pkg_delivered()
                    else:
                        pkg.fall_package()
                        luigi.fall_package()
                        boss.fall_luigi()

                elif pkg.belt == 3 and pkg.x >= 162:
                    if self.collide(pkg, mario):
                        pkg.put_belt(4, 156, 18)
                        score.pkg_delivered()
                    else:
                        pkg.fall_package()
                        mario.fall_package()
                        boss.fall_mario()

                elif pkg.belt == 4 and pkg.x <= 80: #esto es para ver que cuando
                    # colisione con luigi en la ultima plataforma, se tiene que
                    # ir a una parte del truck, se tiene que mejorar o simplificar
                    if self.collide(pkg, luigi):
                        score.pkg_delivered()
                        if truck.package == 0:
                            pkg.x, pkg.y = 24, 56
                        elif truck.package == 1:
                            pkg.x, pkg.y = 40, 56
                        elif truck.package == 2:
                            pkg.x, pkg.y = 24, 48
                        elif truck.package == 3:
                            pkg.x, pkg.y = 40, 48
                        elif truck.package == 4:
                            pkg.x, pkg.y = 24, 40
                        elif truck.package == 5:
                            pkg.x, pkg.y = 40, 40
                        elif truck.package == 6:
                            pkg.x, pkg.y = 24, 32
                        elif truck.package == 7:
                            pkg.x, pkg.y = 40, 32
                        pkg.finish = True
                        pkg.belt = -1 #Para que cuando llegue al ultimo belt,
                        # se quede en el camnion porque sino desaparece del
                        # camnion y aparece como si se hubiese caido

                        pkg.finish = True
                        truck.add_package()
                        if truck.package == 8:
                            truck.visible = False

                        #pkg.go_truck = True
                        #pkg.finish = True
                    else:
                        pkg.fall_package()
                        luigi.fall_package()
                        boss.fall_luigi()