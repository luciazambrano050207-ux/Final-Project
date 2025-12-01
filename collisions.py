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
            if not pkg.fall and not pkg.at_truck:
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

                elif pkg.belt == 4 and pkg.x <= 80:
                    if self.collide(pkg, luigi):
                        score.pkg_delivered()
                        pkg.at_truck = True

                        #pkg.finish = True
                        truck.add_package()
                        #if truck.package == 8:
                            #truck.visible = False

                        #pkg.go_truck = True
                        #pkg.finish = True
                    else:
                        pkg.fall_package()
                        luigi.fall_package()
                        boss.fall_luigi()